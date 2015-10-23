## War Mars ##

**War Mars** é um jogo que está sendo desenvolvido para Windows/Linux/MacOS na línguagem Python.

## História ##

Em **Wars Mars**, o planeta terra fica completamente sem água e a vida na Terra está acabando rapidamente, após alguns meses de agonia e mortes um grupo de pesquisadores da NASA descobre que em Marte possui água que pode ser utilizada pelo ser humano, além disso, é um planeta possível para o ser humano viver. A NASA então rapidamente cria uma missão para enviar astronautas a Marte para captar essa água e tornar Marte um novo planeta habitável, mas, o que eles não esperavam é que existe já existe vida em marte e que esses alienígenas lutarão pela sua preciosa água. 

Apresentado o cenário pré-apocaliptico da Terra passando então para a luta por água em Marte, agora é a parte do jogador lutar pela sua sobrevivência e pela sobrevivência da raça humana. Deixamos o jogador com helicóptero armado para combater diversos outros helicópteros de alienígenas que vem em sua direção para mata-lo e defender seu planeta.


### Etapas de desenvolvimento ###

Para o desenvolvimento desse software foi utilizado o modelo de desenvolvimento em cascata como o seu objetivo é que o desenvolvimento siga sempre para frente.

- Requirimento
- Projeto
- Implementação
- Codificação
- Manutenção

### Padrões de projeto ###

Assim como estudado na disciplina de Programação Orientada a Objetos 2 no Instituto Federal do Espirito Santo, sendo esta, ministrada pelo Msc. Paulo Sérgio Santos, foi implementada diversos padrões de projetos para melhorar o desenvolvimento do software, facilitando uma manutenção. 
Os padrões de projetos implementados em PYTHON foram os seguintes:

**Fachada**: Foi implementado como o objetivo de compor funções, deixando o código mais limpo, legível e de fácil manutenção. A seguir um techo de código que utiliza o padrão fachada.

https://raw.githubusercontent.com/Corlobin/WarMars2.0/master/fachada.png

**Adapter**: Não houve a necessidade de integrar uma interface com a outra. 

**Singleton**: Foi implementada em todos os controladores, porque não haveria a necessidade de carregar os botões, imagens de menu, background diversas vezes das telas. Nos controles, temos as instanciações das Telas respectivas no Init(), desse modo, as telas seriam carregadas uma vez, poupando memória e melhorando o desempenho do game. Para a implementação do Padrão de Projetos Singleton foi utilizado o livro Design Patters in Python **(Community experience distilled) Gennadiy Zlobin-Learning Python design patterns _ a practical and fast-paced guide exploring Python design patterns-Packt Pub (2013)**


**Fábrica** Foi implementado o padrão de projeto Fábrica para a criação de Inimigos no jogo. A implementação desse *método fábrica* carece de amadurecimento, uma vez que todos os tutoriais de implementação desse padrão na línguagem python não traziam as informações necessárias para a implementação concisa. **http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Factory.html**

**Builder**: Não foi possível implementar este padrão de projetos pois houve uma necessidade de carência de informações de como implementa-lo na línguagem Python.

**Decorator**: Nessa versão do jogo não houve necessidade de implementar esse padrão de projetos, pois ainda não há um modo de "Level", mas em futuras versões terão "Ups" nos nívels das naves com mudanças de armas/cores, nesse caso, essa implementação será bastante útil. 


### O padrão MVC ###
O padrão MVC foi utilizado para abstrair a interação das telas das demais tornando o modelo mais restritivo e não trazendo ao usuário falhas de banco de dados por exemplo. Para a aplicação do modelo MVC, foram criadas as pastas:

1. Application
	1. **Application**
2. CCI
	1. **CtrlTelaCadastro**
	2. **CtrlTelaCenario**
	3. **CtrlTelaJogo**
	4. **CtrlTelaLogin**
	5. **CtrlTelaMenu**
	6. **CtrlTelaRanking**
3. CDP
	1. **Balas**
	2. **Fragmento**
	3. **Fumaca**
	4. **Helicoptero**
	5. **Inimigo**
	6. **Municao**
	7. **Pessoa**
4. CGD
	1. **DAOJogador**
	2. **Error**
	3. **Imagem**
	4. **Som**
5. CGT
	1. **AplGerenciarJogador**
6. CIH
	1. **TelaCadastro**
	2. **TelaCenario**
	3. **TelaCreditos**
	4. **TelaJogo**
	5. **TelaLogin**
	6. **TelaMenu**
	7. **TelaRanking**
7. DADOS
8. TESTS
9. UTIL
	1. **GameFactory**
	2. **GameInimigo**
	3. **Singleton**

### Diagrama de classes + Diagrama de padrões ###

https://raw.githubusercontent.com/Corlobin/WarMars2.0/master/diagrama%20padr%C3%B5es.png

### Soonar ##

avaliação

