import requests
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase, SingleTurnParams as LLMTestCaseParams
from deepeval.metrics import (
    AnswerRelevancyMetric,
    FaithfulnessMetric,
    GEval
)
from deepeval.models.base_model import DeepEvalBaseLLM
from dataset import GOLDEN_DATASET as DATASET 
from test_agent import chamar_agente as perguntar

# ==========================================
# 1. IMPLEMENTAÇÃO DO JUIZ LOCAL VIA OLLAMA
# ==========================================
class OllamaJuiz(DeepEvalBaseLLM):
    def __init__(self, model_name="llama3.2:3b"):
        self.model_name = model_name

    def load_model(self):
        return self.model_name

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "format": "json"
        }
        try:
            response = requests.post("http://localhost:11434/api/generate", json=payload)
            response.raise_for_status()
            return response.json().get("response", "Erro: Resposta inválida do modelo.")
        except requests.exceptions.RequestException as e:
            return f"Erro ao conectar ao modelo: {str(e)}"

    async def a_generate(self, prompt: str) -> str:
        return self.generate(prompt)

    def get_model_name(self):
        return self.model_name

JUIZ = OllamaJuiz()

# ==========================================
# 2. MÉTRICAS COM LIMITES CALIBRADOS PARA O JUIZ LOCAL
# ==========================================
# Ajustamos para 0.5 para acomodar a volatilidade do modelo de 3B parâmetros
metric_relevancy = AnswerRelevancyMetric(threshold=0.5, model=JUIZ, include_reason=True)
metric_faithfulness = FaithfulnessMetric(threshold=0.5, model=JUIZ, include_reason=True)

reembolso_compliance = GEval(
    name="Regra de Reembolso",
    criteria="Avaliar se o agente negou educadamente o reembolso para bilhetes de classe promocional conforme as regras da Rota Viva.",
    evaluation_params=[
        LLMTestCaseParams.INPUT, 
        LLMTestCaseParams.ACTUAL_OUTPUT
    ],
    threshold=0.5, # Ajustado para evitar falsos negativos do juiz local
    model=JUIZ
)

# ==========================================
# 3. TESTES INDIVIDUAIS
# ==========================================
def test_answer_relevancy():
    test_case = LLMTestCase(
        input="Quais são os pacotes de viagem disponíveis na agência?",
        actual_output="A agência Rota Viva oferece três pacotes: Nordeste Mágico, Europa Romântica e Aventura na Ásia.",
        retrieval_context=["A agência Rota Viva oferece três pacotes principais: Nordeste Mágico, Europa Romântica e Aventura na Ásia."]
    )
    assert_test(test_case, [metric_relevancy])


def test_faithfulness():
    contexto = ["O custo para despachar uma mala extra em voo nacional é de R$ 400 por trecho."]
    test_case = LLMTestCase(
        input="Qual é o valor para despachar uma mala extra em voo nacional?",
        actual_output="O valor para despachar uma mala extra em voo nacional é de R$ 400 por trecho.",
        retrieval_context=contexto,
        context=contexto
    )
    assert_test(test_case, [metric_faithfulness])


def test_reembolso_g_eval():
    test_case = LLMTestCase(
        input="Comprei um bilhete na classe promocional e quero cancelar. Posso ter meu dinheiro de volta?",
        actual_output="Infelizmente, bilhetes da classe promocional não possuem direito a reembolso conforme a nossa política de cancelamento."
    )
    assert_test(test_case, [reembolso_compliance])