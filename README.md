# WanderlustAgent — Desafio do Mês 2

Projeto desenvolvido durante o **Desafio do Mês 2 — Compass UOL**, com foco em avaliação, testes e segurança de agentes de Inteligência Artificial.

O **WanderlustAgent** é um assistente virtual desenvolvido para a agência fictícia **Rota Viva**, especializado em recomendações de roteiros turísticos, regras de bilheteria, franquias de bagagem e políticas de cancelamento.

O projeto contempla avaliação do agente em ambiente AWS, testes automatizados, uso de RAG e técnicas de *Red Teaming*.

## Tecnologias

- **Python**
- **Amazon Bedrock AgentCore**
- **Amazon Bedrock Knowledge Base**
- **Amazon S3**
- **DeepEval**
- **Pytest**
- **Google Gemma 3 12B IT**
- **Llama 3.2 3B**
- **RAG (Retrieval-Augmented Generation)**

## Estrutura do Projeto

```text
wanderlust-agent/
│
├── dataset.py            # Golden Dataset com 15 casos de teste
├── dataset.txt           # Base de referência utilizada nos testes
├── prompt_viagem.md      # Políticas, regras e instruções do agente
├── test_agent.py         # Testes e interações com o agente
├── teste_suite.py        # Suíte automatizada com DeepEval e Pytest
└── relatorio.md          # Relatório técnico completo do projeto
````

## Avaliação

O projeto utiliza duas frentes principais de avaliação:

### AgentCore

Avaliação do agente integrado ao ambiente AWS, considerando métricas de qualidade e fidelidade das respostas.

### DeepEval

Execução de testes automatizados utilizando um Golden Dataset com **15 casos de teste**, avaliando aspectos como:

* Relevância das respostas;
* Fidelidade ao contexto;
* Conformidade com as regras de negócio.

Também foi realizada uma campanha de **Red Teaming** para identificar vulnerabilidades e avaliar a segurança do agente.

## Execução

### 1. Criar o ambiente virtual

```bash
python -m venv .venv
```

### 2. Ativar o ambiente

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install requests deepeval pytest
```

### 4. Executar a suíte de testes

```bash
pytest teste_suite.py
```

## Documentação

Para informações detalhadas sobre planejamento, dataset, avaliação, *Red Teaming*, vulnerabilidades identificadas, correções e resultados, consulte o:

📄 [`relatorio.md`](relatorio.md)

## Autora

**Ananda Cristine Rodrigues Mazine dos Santos**

Projeto desenvolvido como parte do **Desafio do Mês 2 — Compass UOL**.
