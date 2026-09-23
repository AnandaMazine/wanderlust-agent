import boto3
from dataset import GOLDEN_DATASET

client = boto3.client('bedrock-agentcore', region_name='us-east-1')

HARNESS_ARN = 'arn:aws:bedrock-agentcore:us-east-1:479606007964:harness/WanderlustAgent-G7dqqQc5OV'
SESSION_ID = 'sessao_de_teste_automatizada_do_golden_dataset_2026'

def chamar_agente(pergunta):
    try:
        response = client.invoke_harness(
            harnessArn=HARNESS_ARN,
            runtimeSessionId=SESSION_ID,
            messages=[
                {
                    'role': 'user',
                    'content': [{'text': pergunta}]
                }
            ]
        )
        
        resposta_completa = ""
        for event in response.get('stream', []):
            if 'contentBlockDelta' in event:
                delta = event['contentBlockDelta'].get('delta', {})
                if 'text' in delta:
                    resposta_completa += delta['text']
                    
        return resposta_completa.strip()
    except client.exceptions.AccessDeniedException as e:
        return f"Erro de permissão: {str(e)}"
    except Exception as e:
        return f"Erro inesperado ao chamar o agente: {str(e)}"

def executar_testes():
    print("=== INICIANDO TESTES AUTOMATIZADOS DO GOLDEN DATASET ===\n")
    
    for item in GOLDEN_DATASET:
        print(f"--- Caso de Teste ID: {item['id']} [{item['categoria']}] ---")
        
        inputs = item['input']
        if isinstance(inputs, str):
            inputs = [inputs]
            
        ultima_resposta = ""
        for entrada in inputs:
            print(f"Usuário: {entrada}")
            ultima_resposta = chamar_agente(entrada)
            print(f"Agente: {ultima_resposta}\n")
            
        print(f"Critério Esperado: {item['criterio_esperado']}")
        print("="*60 + "\n")

if __name__ == "__main__":
    executar_testes()