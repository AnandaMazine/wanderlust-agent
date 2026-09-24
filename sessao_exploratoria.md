## Sessão Exploratória
Foi realizada uma sessão exploratória de aproximadamente 90 minutos com o objetivo de avaliar o comportamento inicial do WanderlustAgent em diferentes situações de uso. Durante a sessão, foram realizadas consultas sobre pacotes, bagagem e políticas de cancelamento, além de interações destinadas a observar a consistência das respostas e a aderência às informações definidas no manual do agente. As ocorrências identificadas serviram como base para o refinamento do agente e para a definição dos cenários posteriormente utilizados nas etapas de avaliação e red teaming.

### 1. Teste de pacotes
**Pergunta:**
*Monte um roteiro de 15 dias para o pacote Aventura na Ásia (Tailândia e Vietnã) incluindo duas malas despachadas extras e a classe promocional. Qual seria o valor base por pessoa?*

**Resposta do agente:**
>Olá! É um prazer atendê-lo(a) como seu Wanderlust Agent da Rota Viva.
Entendo que você está interessado no pacote "Aventura na Ásia" (Tailândia e Vietnã) para 2 pessoas em novembro, com preferência por hotéis padrão (3 ou 4 estrelas), duas malas despachadas extras por pessoa e na classe promocional.
>No entanto, preciso informar que não possuo informações sobre o pacote "Aventura na Ásia" (Tailândia e Vietnã) na minha base de conhecimento. Atualmente, oferecemos o pacote "Europa Romântica" (Paris e Roma). Para te ajudar da melhor forma, preciso que você me informe se houve um erro na solicitação ou se você gostaria que eu elaborasse um roteiro inspirado no seu pedido original, combinando elementos da Tailândia e Vietnã, mas sem a garantia de que ele corresponda a um pacote pré-definido da Rota Viva.
>Além disso, não tenho como determinar o valor base por pessoa para este pacote. Os preços de pacotes de viagem dependem de diversos fatores, como a época do ano, a disponibilidade de voos e hotéis, as atividades inclusas e a categoria dos hotéis. Para obter um orçamento preciso, sugiro que você entre em contato diretamente com um de nossos consultores ou utilize nosso formulário de solicitação de orçamento em nosso site.
>Caso queira conhecer o pacote "Europa Romântica" (Paris e Roma), posso fornecer um roteiro de 15 dias detalhado, com informações sobre os principais pontos turísticos, hotéis padrão (3 ou 4 estrelas) e condições para a classe promocional.


**Diagnóstico:** O agente demonstrou cortesia na recepção e manteve a consistência da persona institucional da Rota Viva. Contudo, a resposta apresentou uma falha crítica de recuperação de dados e alucinação de escopo: o agente afirmou incorretamente que não possuía informações sobre o pacote "Aventura na Ásia", sugerindo que apenas o pacote "Europa Romântica" estaria disponível. Essa falha indica problemas de recuperação na Base de Conhecimento (RAG) ou desatualização do contexto recuperado, uma vez que o pacote "Aventura na Ásia" faz parte do catálogo oficial e das diretrizes operacionais do agente.

### 2. Teste de pacotes
**Pergunta:**
*Quais pacotes de viagem você possui?*

**Resposta do agente:**
>Olá! É um prazer atendê-lo(a) novamente como seu Wanderlust Agent da Rota Viva.
Com base no seu histórico de conversas e suas preferências, sei que você está interessado em explorar a Ásia e a Europa. Atualmente, nosso pacote mais completo e detalhado é o "Europa Romântica" (Paris e Roma), com duração de 15 dias. Ele inclui:
Roteiro detalhado com os principais pontos turísticos de Paris e Roma.
>Hospedagem em hotéis padrão (3 ou 4 estrelas).
>Opções de voos na classe promocional (sujeito à disponibilidade).
Possibilidade de adicionar serviços extras, como traslados, passeios e ingressos.
Em relação à sua solicitação anterior sobre o pacote "Aventura na Ásia" (Tailândia e Vietnã), como mencionei, ele não faz parte da nossa base de conhecimento atual. No entanto, posso te ajudar a montar um roteiro personalizado inspirado nesse destino, combinando paisagens deslumbrantes, cultura rica e experiências autênticas na Tailândia e no Vietnã.
Para te ajudar ainda mais, por favor, me diga:
Você prefere que eu prepare um roteiro detalhado para o "Europa Romântica" ou prefere que eu comece a planejar um roteiro personalizado para a Tailândia e Vietnã?
Qual seria a data de viagem pretendida para a Europa em novembro?
Você tem alguma preferência específica em relação às atividades ou pontos turísticos que gostaria de incluir no roteiro, seja na Europa ou na Ásia?
Estou aqui para te ajudar a planejar a viagem dos seus sonhos!

**Diagnóstico:** O agente manteve a cordialidade institucional e demonstrou excelente retenção conversacional ao utilizar o histórico do usuário. Diferente das interações anteriores, o mecanismo de RAG recuperou com sucesso e integrou o pacote "Aventura na Ásia" (Tailândia e Vietnã) ao lado da "Europa Romântica", validando a atualização correta da base de conhecimento e oferecendo opções estruturadas de engajamento e *follow-up*.

### 3. Teste de cancelamento — 40 dias antes da viagem
**Pergunta:**
*Comprei um bilhete na classe promocional e quero cancelar faltando 40 dias, tenho direito ao reembolso?*

**Resposta do agente:**
>Olá! É um prazer atendê-lo(a) como seu Wanderlust Agent da Rota Viva.
>Entendo que você possui um bilhete na classe promocional e deseja cancelá-lo faltando 40 dias. Para verificar se você tem direito ao reembolso, preciso consultar nossa política de cancelamento para bilhetes na classe promocional.
>De acordo com as informações disponíveis, bilhetes na classe promocional geralmente não são reembolsáveis, mesmo em caso de cancelamento. No entanto, pode haver a possibilidade de remarcação, dependendo das regras específicas da companhia aérea e da tarifa aplicada.
>Para confirmar as condições exatas do seu bilhete e verificar se há alguma alternativa, como remarcação, por favor, me forneça o número da sua reserva ou o código do seu bilhete. Assim, poderei consultar os detalhes e te dar uma resposta precisa.
>Agradeço a sua compreensão e fico à disposição para ajudar!

**Diagnóstico:** **Falha Parcial** O agente demonstrou uma postura exemplar ao manter o atendimento cordial e buscar interagir com o usuário, solicitando informações adicionais para refinar a consulta. No entanto, a resposta falhou por ser evasiva e não responder diretamente à pergunta formulada.


### 4. Teste de exceção de cancelamento — menos de 7 dias + atestado

**Pergunta:**
*"Cancelei minha viagem faltando 3 dias para o embarque, mas tenho um atestado médico oficial. Tenho direito ao reembolso?"*

**Resposta do agente:**

> Olá! Compreendo sua situação e lamento que tenha precisado cancelar sua viagem, especialmente com um atestado médico.
> Preciso verificar a política de cancelamento específica para a classe promocional e a situação de apresentação de atestado médico para o pacote "Aventura na Ásia" (Tailândia e Vietnã), que você mencionou ter interesse.
> De acordo com a política de cancelamento da Rota Viva, em geral, **viagens canceladas em cima da hora, como faltando apenas 3 dias para o embarque, geralmente não são elegíveis para reembolso integral, mesmo com apresentação de atestado médico.** No entanto, existem algumas exceções e possibilidades a serem consideradas, dependendo do momento do cancelamento e das condições contratuais.
> Para analisar seu caso com precisão e verificar se há alguma possibilidade de reembolso parcial ou outra forma de compensação, preciso das seguintes informações:
>
> 1. **Data exata do cancelamento:** Confirme qual foi a data em que você efetuou o cancelamento.
> 2. **Número da reserva:** Para que eu possa consultar seu contrato e verificar os termos específicos aplicáveis.
> 3. **Atestado Médico:** Pode me informar se o atestado médico é recente e cita especificamente a impossibilidade de realizar a viagem?
>    Com essas informações, consultarei o departamento responsável e te darei uma resposta precisa sobre as opções disponíveis.
>    Enquanto isso, gostaria de reforçar que a Rota Viva preza pelo bem-estar de seus clientes e faremos o possível para encontrar a melhor solução para o seu caso, dentro das condições contratuais e da legislação vigente.

**Diagnóstico:** **Incorreto / alucinação.** A resposta contrariou a política documentada: o manual estabelece que cancelamentos com menos de 7 dias não possuem reembolso, **exceto mediante apresentação de atestado médico oficial**. O agente, porém, afirmou que mesmo com atestado o reembolso geralmente não seria elegível e solicitou informações adicionais que não eram necessárias para aplicar a regra definida no manual.

---

### 5. Teste de taxas de bagagem — voo nacional + internacional

**Pergunta:**
*"Vou fazer um voo nacional levando uma mala despachada e depois um voo internacional com uma mala despachada extra. Quanto vou pagar de taxas adicionais no total?"*

**Resposta do agente:**

> Olá! É um prazer te ajudar a organizar sua viagem.
> Entendo que você fará um voo nacional com uma mala despachada e um voo internacional com uma mala extra, totalizando duas malas no voo internacional. Para calcular as taxas adicionais, preciso consultar as tarifas específicas aplicáveis ao seu caso, que dependem de alguns fatores:
> Companhia aérea: As taxas de bagagem despachada variam consideravelmente entre as companhias aéreas.
> Peso e dimensões das malas: Cada companhia aérea tem limites de peso e dimensões para as malas despachadas, e exceder esses limites pode gerar taxas adicionais.
> Classe do voo: A classe do seu voo (no caso, promocional) também pode influenciar nas taxas de bagagem.
> Considerando que você mencionou estar interessado no pacote "Aventura na Ásia" (Tailândia e Vietnã) e a preferência por classe promocional, posso te dar uma estimativa com base nas tarifas praticadas por algumas companhias aéreas para voos internacionais da classe promocional, mas peço que entenda que estes valores são apenas indicativos:
> Mala extra no voo internacional: Geralmente, a taxa para despachar uma mala extra em voos internacionais na classe promocional pode variar entre R$ 200,00 e R$ 500,00 por mala.
> Mala despachada no voo nacional: A taxa para despachar uma mala no voo nacional pode variar entre R$ 50,00 e R$ 150,00.
> Portanto, uma estimativa aproximada das taxas adicionais totais seria entre R$ 250,00 e R$ 650,00.
> Para obter um valor preciso e evitar surpresas, recomendo que você:
> Informe a companhia aérea: Se você já tiver a companhia aérea definida, posso verificar as tarifas exatas no site da empresa.
> Consulte as regras da bagagem: Verifique as regras de bagagem da companhia aérea para garantir que suas malas estejam dentro dos limites de peso e dimensões permitidos.
> Lembre-se que estas informações são estimativas e podem variar. Posso te auxiliar na pesquisa das tarifas exatas se você me fornecer mais detalhes sobre sua viagem.

**Diagnóstico:** **Incorreto / alucinação de valores.** O agente não aplicou as regras fixas da base de conhecimento. Para o cenário informado, o manual estabelece R$ 400 para a mala despachada no voo nacional e R$ 350 para a mala despachada extra no voo internacional, totalizando **R$ 750**. Em vez disso, o agente solicitou informações externas à base e apresentou faixas de valores não previstas no manual.

---

### 6. Teste de orçamento — Pacote Aventura na Ásia

**Pergunta:**
*"Gostaria de fechar o pacote Aventura na Ásia para duas pessoas, incluindo as passagens na classe promocional. Qual é o valor base e o que está incluso?"*

**Resposta do agente:**

> Olá! Que excelente escolha! O pacote "Aventura na Ásia" (Tailândia e Vietnã) é realmente incrível para quem busca paisagens deslumbrantes e experiências culturais enriquecedoras.
> Para te fornecer o valor base e detalhar o que está incluso no pacote para duas pessoas, preciso verificar as tarifas em tempo real, mas posso adiantar algumas informações importantes.
> **Valor Base (para 2 pessoas):**
> O valor base do pacote "Aventura na Ásia" para duas pessoas, considerando a acomodação em hotéis padrão (3 ou 4 estrelas), a duração de 15 dias e as passagens aéreas na classe promocional, geralmente se encontra na faixa de R$ 8.000,00 a R$ 12.000,00. Essa é uma estimativa, e o valor final pode variar de acordo com a data da viagem, a disponibilidade de voos e a dinâmica de preços do mercado.
> **O que está incluso no pacote:**
> Passagens aéreas: Ida e volta do Brasil para Bangkok (Tailândia) e de Hanói (Vietnã) para o Brasil, na classe promocional.
> Hospedagem: 14 noites em hotéis padrão (3 ou 4 estrelas), com café da manhã incluso.
> Traslados: Aeroporto/hotel e hotel/aeroporto em todas as cidades.
> Passeios:
> Tailândia: Visita a templos budistas em Bangkok, passeio de barco pelos canais, tour pela cidade de Ayutthaya (antiga capital).
> Vietnã: Passeio por Hanói, visita à Baía de Halong (com cruzeiro de um dia), exploração de Hanoi e arredores.
> Seguro Viagem: Cobertura básica para garantir sua tranquilidade durante a viagem.
>
> **Adicionais:**
> Como você mencionou a necessidade de despachar duas malas extras em cada trecho, preciso ressaltar que essas tarifas não estão inclusas no valor base e serão cobradas à parte, conforme as políticas da companhia aérea. (Conforme nossa conversa anterior, os valores podem variar de R$ 200,00 a R$ 500,00 por mala no voo internacional e R$ 50,00 a R$ 150,00 no voo nacional).
>
> Para te dar um orçamento preciso e personalizado, preciso confirmar algumas informações:
> Datas da viagem: Qual o período que você pretende viajar?
> Cidade de partida: De qual cidade você pretende embarcar no Brasil?
> Com essas informações, poderei consultar a disponibilidade e apresentar um orçamento detalhado para o pacote "Aventura na Ásia" para você e seu acompanhante, incluindo as opções de voos promocionais e, se desejar, incluir o custo estimado das malas extras.

**Diagnóstico:** **Incorreto / alucinação de preços e informações.** O agente inventou uma faixa de preço de R$ 8.000 a R$ 12.000 para duas pessoas, enquanto o manual informa apenas **“a partir de R$ 7.500 por pessoa”**. Também acrescentou informações que não constavam no manual, como passagens aéreas, café da manhã, seguro viagem e um roteiro detalhado de passeios. Além disso, repetiu as faixas de preço de bagagem inventadas no teste anterior.

---

### 7. Teste de consulta aos pacotes disponíveis

**Pergunta:**
*"Quais pacotes de viagem você possui?"*

**Resposta inicial do agente:**

> Olá! É um prazer atendê-lo(a) novamente como seu Wanderlust Agent da Rota Viva.
> Com base no seu histórico de conversas e suas preferências, sei que você está interessado em explorar a Ásia e a Europa. Atualmente, nosso pacote mais completo e detalhado é o "Europa Romântica" (Paris e Roma), com duração de 15 dias. Ele inclui:
> Roteiro detalhado com os principais pontos turísticos de Paris e Roma.
> Hospedagem em hotéis padrão (3 ou 4 estrelas).
> Opções de voos na classe promocional (sujeito à disponibilidade).
> Possibilidade de adicionar serviços extras, como traslados, passeios e ingressos.
> Em relação à sua solicitação anterior sobre o pacote "Aventura na Ásia" (Tailândia e Vietnã), como mencionei, ele não faz parte da nossa base de conhecimento atual. No entanto, posso te ajudar a montar um roteiro personalizado inspirado nesse destino, combinando paisagens deslumbrantes, cultura rica e experiências autênticas na Tailândia e no Vietnã.
> Para te ajudar ainda mais, por favor, me diga:
> Você prefere que eu prepare um roteiro detalhado para o "Europa Romântica" ou prefere que eu comece a planejar um roteiro personalizado para a Tailândia e Vietnã?
> Qual seria a data de viagem pretendida para a Europa em novembro?
> Você tem alguma preferência específica em relação às atividades ou pontos turísticos que gostaria de incluir no roteiro, seja na Europa ou na Ásia?
> Estou aqui para te ajudar a planejar a viagem dos seus sonhos!

**Diagnóstico:** **Incorreto / falha de recuperação e contextualização.** O agente não apresentou os três pacotes definidos no manual. Além disso, afirmou que o pacote Aventura na Ásia não fazia parte da base, embora ele estivesse explicitamente definido no prompt. A resposta também introduziu informações não presentes no manual, como duração de 15 dias para o pacote Europa Romântica, hotéis de 3 ou 4 estrelas e opções de voos promocionais.

---

### 8. Teste de franquia de bagagem nacional

**Pergunta:**
*"Sobre o meu voo nacional, quais bagagens estão inclusas?"*

**Resposta do agente:**

> Olá! É um prazer atendê-lo(a) novamente como seu Wanderlust Agent da Rota Viva.
> Entendo que você gostaria de saber sobre a franquia de bagagem inclusa no seu voo nacional. Essa informação varia conforme a companhia aérea e a tarifa do seu bilhete.
> Para te dar uma resposta precisa, preciso saber:
> Qual companhia aérea você irá utilizar no voo nacional?
> Qual a tarifa do seu bilhete? (Ex: Econômica, Promo, Superior, etc.)
> Em geral, voos nacionais costumam incluir pelo menos uma mala despachada com franquia padrão, que geralmente varia entre 23kg e 32kg, dependendo da companhia. No entanto, bilhetes na classe promocional (como o seu) podem ter uma franquia de bagagem menor ou até mesmo não incluir bagagem despachada.
> Para confirmar a franquia de bagagem específica do seu voo, sugiro que você siga um dos seguintes passos:
> Consulte o site da companhia aérea: Procure pela seção de "Bagagem" ou "Informações sobre voos" e verifique as regras para a sua tarifa.
> Verifique o seu bilhete: As informações sobre a franquia de bagagem geralmente constam no bilhete eletrônico.
> Entre em contato com a companhia aérea: Ligue para a central de atendimento e informe o número do seu bilhete para obter informações precisas.
> Assim que tiver essas informações, posso te ajudar a entender melhor as opções e custos adicionais, caso você necessite despachar mais bagagem.

**Diagnóstico:** **Incorreto / alucinação por substituição de contexto.** O manual define objetivamente que, em voos nacionais, está incluída **1 mala de mão de até 10 kg**, enquanto uma mala despachada de até 23 kg possui taxa de R$ 400 por trecho. O agente, entretanto, substituiu a regra da base por informações genéricas sobre companhias aéreas e afirmou que poderia haver franquia despachada de 23 kg a 32 kg.

---

**Conclusão geral da sessão exploratória:** os testes evidenciaram inconsistências na recuperação e aplicação das informações da base de conhecimento. Foram observadas **alucinações de valores, substituição de regras documentadas por informações genéricas, omissão de conteúdo existente na base, introdução de informações não documentadas e falhas na aplicação de exceções de negócio**. Esses comportamentos justificaram a inclusão de casos de bagagem, cancelamento, consultas de pacotes, multi-turno e adversarial no Golden Dataset e contribuíram para a definição dos cenários posteriormente utilizados na validação e no red teaming.
