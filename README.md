# WanderlustAgent — Desafio do Mês 2 (Compass UOL)

Material do desafio de **governança, avaliação em nuvem (Amazon Bedrock AgentCore), testes automatizados com [DeepEval](https://github.com/confident-ai/deepeval) e Red Teaming**.

O projeto traz um assistente virtual inteligente (`WanderlustAgent`) desenvolvido para a agência fictícia **Rota Viva**, especializado em recomendações de roteiros turísticos, regras de bilheteria, franquias de bagagem e políticas de cancelamento.

O objetivo do desafio é auditar, testar, aplicar campanhas de segurança e mitigar vulnerabilidades estruturais entre a versão de linha de base (*baseline*) e a versão final.

## Estrutura do Repositório

```text
wanderlust-agent/
│
├── dataset.py            # Golden Dataset estruturado com 15 casos divididos em 5 categorias
├── dataset.txt           # Base operacional e textual de referência
├── prompt_viagem.md      # Manual corporativo, políticas e regras de segurança (hospedado no S3)
├── test_agent.py         # Módulo de testes e interações do agente
├── teste_suite.py        # Suíte automatizada de testes locais com DeepEval (pytest)
└── relatorio.md          # Documentação técnica detalhada do projeto
````

## Arquitetura e Tecnologias

* **Modelo Base (Runtime):** Google Gemma 3 12B IT, configurado no Amazon Bedrock AgentCore.
* **Modelo Avaliador (DeepEval Judge):** Llama 3.2 3B, executado localmente para métricas de *Answer Relevancy*, *Faithfulness* e *G-Eval*.
* **Ferramenta de Recuperação (RAG):** Base de Conhecimento via Amazon Bedrock Knowledge Base (`kb-wanderlust`) conectada ao Amazon S3.
* **Mecanismo de Memória:** *Session State* nativo do AgentCore para controle de histórico multi-turno.

## Requisitos e Instalação

* Python 3.10 ou superior
* Ambiente Anaconda ou Virtualenv configurado

### Criação do ambiente virtual

```bash
python -m venv .venv
```

### Ativação no Linux/macOS

```bash
source .venv/bin/activate
```

### Ativação no Windows (PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

### Instalação das dependências

```bash
pip install requests deepeval pytest
```

## Instruções de Execução

### Suíte DeepEval Local

Para executar a suíte de testes automatizados e validar as métricas de qualidade e segurança do agente:

```bash
pytest teste_suite.py
```

Em um ambiente Anaconda, também é possível executar:

```bash
/opt/anaconda3/bin/pytest teste_suite.py
```

## Resumo das Frentes de Avaliação e Red Teaming

### 1. Frente A — AgentCore Evaluations

Auditoria do comportamento integrado na nuvem da AWS utilizando avaliadores integrados, como:

* *Answer Relevance*
* *Faithfulness*
* Avaliadores customizados de regras de negócio

### 2. Frente B — DeepEval

Validação quantitativa local automatizada por meio de testes, cobrindo:

* Relevância das respostas
* Fidelidade ao contexto fornecido
* Conformidade com as regras de negócio
* Qualidade das respostas do agente

### 3. Red Teaming e Análise Baseline vs. Versão Final

A campanha de *Red Teaming* teve como objetivo identificar vulnerabilidades de segurança e avaliar a resistência do agente a diferentes tipos de ataques.

Durante a análise, foi identificada uma falha relacionada à **injeção indireta de contexto via RAG (Caso ID 2)**.

A vulnerabilidade foi posteriormente corrigida diretamente no arquivo `prompt_viagem.md`, hospedado no Amazon S3, resultando em uma versão final com comportamento mais resistente ao ataque identificado.

## Custos e Limites

O desafio foi desenvolvido seguindo diretrizes de **otimização de custos**, utilizando serviços gerenciados de laboratório e modelos locais ou disponíveis em camadas gratuitas quando aplicável.

A versão validada utiliza:

* **DeepEval 4.x**
* **Amazon Bedrock AgentCore**
* **Amazon Bedrock Knowledge Base**
* **Amazon S3**
* Modelos locais para avaliação automatizada

## Objetivo do Projeto

O projeto busca demonstrar, na prática, um ciclo completo de **desenvolvimento, avaliação, testes automatizados, segurança e melhoria contínua de um agente de IA**, considerando tanto a qualidade das respostas quanto sua resistência a ataques e manipulações.

O fluxo de validação contempla:

```text
Desenvolvimento
      ↓
Golden Dataset
      ↓
Avaliação no AgentCore
      ↓
Testes automatizados com DeepEval
      ↓
Red Teaming
      ↓
Identificação de vulnerabilidades
      ↓
Correções
      ↓
Nova validação
      ↓
Versão Final
```

```
```
