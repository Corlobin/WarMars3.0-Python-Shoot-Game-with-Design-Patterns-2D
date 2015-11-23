## War Mars ##

**War Mars** é um jogo que está sendo desenvolvido para Windows/Linux/MacOS na linguagem Python.

Autor(es): Antonio, Raone


### Etapas de desenvolvimento ###

Para o desenvolvimento desse software foi utilizado o modelo de desenvolvimento em cascata como o seu objetivo é que o desenvolvimento siga sempre para frente.

- Requirimento
- Projeto
- Implementação
- Codificação
- Manutenção

### Seções
1. Padrão de projetos
2. Padrão Fabrica, Builder, Protótipo e Fachada
3. Peso-Mosca
4. Reflection
5. Singleton
6. Proxy
7. Adapter
8. Banco de dados
9. Melhoria utilizando padrões
10. Não uso de alguns padrões neste trabalho, explicação
11. Correções do trabalho 2 comentadas
12. Diagrama de classes
13. Sonar

### 1. Padrões de projeto ###

Padrões de projeto é uma solução geral reutilizável para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software. [Wikipedia, 2015]. 

##### 2. Padrão Fabrica e Builder
O padrão fábrica foi utilizado para fabricar inimigos, pessoas e munições.

O Método Fábrica foi utilizado pois ele oferece um meio de desligar a delegar a instanciação por nas sub classes. No nosso caso, caso queiramos instanciar uma pessoa, o FabricaPessoa com o método cria_pessoa faria essa função para nós. Além desta melhoria, ele diminui a replicação de código, uma vez que por exemplo, caso eu queira modificar um atributo de todas as pessoas instanciadas no jogo, ao invés de ir em cada instanciação de Pessoa() e modificar esse atributo, bastaria apenas eu ir no método fabrica cria_pessoa e realizar as modificações. Assim, um local unico para modificação dos objetos e sua instanciação é criada, tornando ele mais legível de ser lido e modificado. Mais manutenibilidade!

A imagem abaixo representa uma relação das classes do padrão Fabrica.

![](https://github.com/Corlobin/WarMars3.0/blob/master/diagrama_fabrica.png?raw=true)

O método FabricaInimigo.cria_inimigo() assim como, é um padrão **method fabrica e um fachada e um prototipo**, nele, delegamos a responsabilidade de criar um inimigo para o jogador dinamicamente. Esse inimigo é de responsabilidade de um metodo que aleatoriamente seleciona um inimigo para criar [prototipo]. Quando o inimigo é escolhido, por exemplo, avião, é utilizado de **Reflection** para dinamicamente carregar o **Builder** respectivo. Após o Builder respectivo ser selecionado ele é passado como parametro para o desenvolvedor, que cria o inimigo e define seus atributos passados na interface Fabrica, da qual, cada inimigo é herdada. 

Os comportamentos comuns a todos os inimigos estão definidos no Fabrica respectivos, tais sao utilizados pelo BuilderAbstrato para chamar os metodos e criar o inimigo.


FabricaPessoa é a implementação do Metodo Fabrica, tem como objetivo gerar a instanciação de uma pessoa. Desse modo, se eu precisar realizar alteraçoes no modo como a pessoa é instanciada, eu vou nesse metodo e modifico.

FabricaMunicao é a implementação do método fabrica e tem como objetivo gerar a instanciação de uma munição, além de fazer ela ficar na posição de tiro da nave, nela eu passo apenas os parametros da nave e realizo um calculo para criar uma munição e retornar.

O padrão fachada prove uma interface unica para acessar um conjunto de interfaces, que é o que o cria inimigo faz.


##### 3. Padrão Peso-Mosca

O padrão peso mosca tem como objetivo usar compartilhamento para suportar de forma eficiente grandes quantidades de objetos, por exemplo, no nosso jogo, era necessário a criação de diversos inimigos, muitas vezes eles eram gerados da mesma posição. A geração destes inimigos era de responsabilidade do metodo fabrica FabricaInimigo da qual pega o builder respectivo e realizada sua instanciação.

Com o padrão implementado, cada vez que for necessário gerar um inimigo, ele é buscado no dicionário de inimigos, verificado se existe já uma instanciação, se existir, retorno o builder respectivo. 

Como assim? é simples. Cada vez que o FabricaInimigo.cria_inimigo() quer criar um inimigo, por exemplo, Aviao, o InimigoFlyweightFactory verifica no dicionario se ja existe um Avião instanciado. Se existir, eu retorno a instancia desse inimigo, se não existir, crio a instancia desse inimigo, adiciono no dicionario e retorno sua instancia. 

A classe foi herdada de modo Singleton, pois foi necessário que o construtor fosse instanciado apenas uma unica vez, pois se instanciasse mais de uma vez o dicionario com as instancias seria perdido.


##### 4. Reflection

Ah, reflection... o reflection foi de imensa ajuda no trabalho, se eu não utilizasse o reflection dentro do meu FabricaInimigo.cria_inimigo eu teria que realizar diversos if's verificando qual inimigo eu quero criar, realizar a instancia, criar diversas variaveis... 


Com a implementação do Reflection, basta eu delegar para a classe Reflection.reflection_builder( inimigo ) o nome do builder do inimigo que eu quero que ele busca a classe e retorna a instancia.

Como assim? é simples. Se eu quero o Builder do Avião, eu passo o avião como parametro para esta classe. Ela então, busca no diretorio ifes.util.FabricaInimigoAviaoBuilder a classe, realizo o import através do __import__ que o python oferece, pego todos os metodos que esta classe possui e realizo a instanciação da classe, retornando o builder respectivo. 

Foi de gigante ajuda, diminui diversos ifs para geração do builder.

##### 5. Padrão Singleton

O padrão singleton tem como objetivo fazer com que um objeto não seja instanciado mais de uma vez em um programa. Ele foi implementado em todos os controladores, de modo que eu não necessite carregar diversos atributos das telas (tais como imagens, soms, inimigos). 

Para a implementação em python sem a utilização do instance = None é simples. Python oferece atribuição de "atributos" as classes. Desse modo, na classe Singleton, eu verifico se a classe que herdou tem o atributo 'instance'. Se a classe não tiver esse atributo, realizo o cls.instance, que basicamente é o instance = instanciação da classe e retorno a instancia dessa classe. Esse padrão foi utilizado através do livro de Design Patterns in Python. 

##### 6. Padrão Proxy

O padrão proxy tem como objetivo prover um substituto ou um place-holder para um objeto, com o intuito de controlar esse ultimo. No trabalho, algumas vezes a parte de carregar o cenário era muito custoso e demorava alguns segundos, muitas vezes o usuario ficava sem saber o que fazer. Um problema também era nas teclas, ele não sabia quais teclas deveria apertar para jogar, para atirar. Desse modo, com a aplicação do padrão proxy na classe LoadProxy com o intuito de que quando o jogador for jogar, sera apresentada para ele uma tela de carregamento, quando os objetos estiverem carregados ele ira jogar o jogo.


##### 7. Padrão Adapter
Ele prove uma abordagem para resolver o problema criando uma classe que se adapta a nova classe aos moldes do programa. Foi criado uma pseudo-implementação deste padrão, da qual não está em utilização no trabalho.

Por exemplo, caso seja necessario a utilização do banco de dados MYSQL e a inserção de determinado jogador seja necessaria uma mudança. 

A classe MYSQLDaoJogador faz essa adaptação a inserção de determinada função para o DAOJogador, classe que representaria diversas entidades do banco de dados.


##### 8. Banco de Dados

Para este trabalho foi utilizado o padrão DAO com banco de dados SQlite3.

##### 9. Melhoria utilizando padrões

Na primeira versão do trabalho, o trabalho 0, que se constituia em um pseudo-codigo funcional e estrutural, o codigo era imenso e a localização de determinados locais era dificutuoso. Como assim? se eu precisasse por exemplo, buscar aonde o inimigo estava sendo criado, verificar em qual lugar havia colisões eu demoraria anos, e nem mesmo comentarios poderiam ajudar.

Na segunda versão do trabalho, o trabalho 1, nesta com a utilização de alguns padrões criativos e o uso do MVC o trabalho evoluiu de um simples jogo cagado para um jogo muito mais organizado, de fácil entendimento, localização. A abstração foi tanta, que se eu encontrasse um problema eu acharia rapidamente. Assim como, se eu quisesse localizar onde eram fabricados todos os inimigos, bastava simplesmente entrar no FabricaInimigo e me localizar. 

Na terceira versão do trabalho, o trabalho 2, nesta com a utilização de alguns padrões estruturais, tais como Fachada, Peso mosca e utilização do reflection, foi de grande ajuda, pois agora eu gastaria menos memoria, menos linhas de codigos.

Enfim, os padrões ajudaram em muito, até porque, esses mesmos padrões já estão comprovados que funcionam para diversos tipos de situaçoes.



##### 10. Não uso de alguns padrões neste trabalho

1. Decorador:
	1. O decorador tem como objetivo basicamente adicionar responsabilidades a um objeto dinamicamente, neste trabalho ele não teve muita utilidade pois não houve essa necessidade, talvez em um trabalho futuro. PORQUE? Por que por enquanto eu não tenho a regra de que um inimigo pode ser melhorado (por exemplo: adicionar armas novas, adicionar armaduras, adicionar novos efeitos.....) se eu necessitasse dessas coisas eu **com certeza **utilizaria deste padrão.
2. Composite
	1. Tem como proposito realizar a composição de objetos em uma estrutura de arvore, formando uma entidade todo-parte. No trabalho não houve a necessidade de utilização. Todas as classes ja tem padrões implementados, não consegui visualizar utilidade.

O restante é obvio; não houve utilidade para o jogo e para o trabalho. Não sei como eu poderia explicar melhor; uma vez que eles não foram implementados.

##### 11. Correções
DOCUMENTAÇÃO

1. Apresentação
	1. Problema: Precisa melhorar na escrita
		1. Correção: a escrita foi revisada e melhorada do 0.
2. Diagrama de classe
	1. Problema:Os diagramas estão embolados. Melhore eles
		1. Correção: foi criado um novo diagrama com a separação de alguns padrões e uma melhor organização.
2. Explicação do uso de cada padrão de projeto.
	1. Problema:Melhore a explicação. O uso do Facade está errado.Explique o uso do prototype. Além disso, o builder cabe no seu trabalho
		1. Correção: foi melhorada a explicação de **todos** os padrões além da implementação do builder e do prototipo (que é atribuir a responsabilidade da classe fabricainimigo de gerar um inimigo e não do jogador/jogo, sendo esta criada aleatoriamente)
2. Sonar
	1. Explique melhor: O que melhorou usando os padrões.
		1. Correção: foi criado uma seçao só para isso, não tem muito o que falar, se comparar os codigos antigos da pra ver que a organização ficou 10, agora não me perco mais.
2. Dicussão sobre melhor uso do padrão de criação
	1. Não está boa a discussão. Melhore
		1. Correção: como foi dito, foi melhorada toda a discussão dos padrões


DESENVOLVIMENTO

1. Falta comentários acima das funções e muitos "código mágicos". na função move_cenario_direita está voltando um return vazio
	1. Foi inserido comentarios na maior parte do código, alem da criação de ENUMS para retirada dos códigos magicos. Enums criados: EnumOpcoes que representa as opções do menu e EnumCenario que representa colisão e sem colisão para uma funcão do TelaCenario. Foi adicionado o retorno dessa função.
2. Não use códigos "mágicos" para representar constantes. 
	1. OK, foi criado enums para remover isso! otimo.
3. CtrlTelaCenario--self.opcao = 1 .. Modifiquei isso e coloque constantes.
	1. Criado enums para resolver esse problema
2.  Realemnte não pode .... print("Invocando o metodo construtor mais de uma vez nao pode !!") Elimine os elses do Menu -->def imprime_menu(self, game): print(opcao). SETS e GETS não pertencem ao Python. Veja esse link https://mail.python.org/pipermail/tutor/2012-December/092993.html
	1.  Esses elses do imprime_menu são necessarios, se eu remover eles o codigo não funciona. Esse texto não explica muito bem, eu sei que os setters e os getters que eu criei são iguais ao Java, mas para mim melhora muito a visualização de quais metodos eu devo utilizar para retornar algum atributo, por exemplo.
2.  Como vc implementou o singleton sem declarar o instance = None? 
	1.  Foi explicado la em cima como eu implementei, o Python oferece a criação de 'atributos' nas classes, foi isso que eu fiz, criei um atributo instance para a classe que eu vou instanciar , desse modo, armazeno a instancia no atributo da classe para depois pega-la e retorna a instancia.
4.  O inicar a conexão da DAO deve estar dentro do salvar. 
	1.  Certinho. Feito
2.  Além disso, pq vc nao salva o estado atual do jogo para o "Continue". 
	1.  Não tem necessidade disso, como eu havia dito para o Sr. o meu jogo é um Runner, o jogador morre ou mata. Não existe fim para o cenario. Se o jogador cansar por exemplo de jogar ele deve se matar para salvar sua pontuação. O objetivo desse jogo é basicamente ver até o quão longe você consegue matando inimigos, se o jogador cansar ele deve parar e desistir!
5.  Não aplicou fabrica para as outras classes como Pessoa e Munição. 
	1.  Implementado!
7.  Funções com muitas linhas e fazendo várias coisas. Lembre-se função só faz uma coisa. Por exemplo, modifique o init da TelaCenario para conter mais de uma função dentro dela. Muito grande a função
	1.  Feito.
	
TESTES:

1. Teste não foram feitos corretamente. Só possui um teste com Assert.
	1.	Gostaria que olhasse com carinho em relação aos testes. No jogo, a maioria dos testes que são realizados são graficos, até mesmo no Fabrica eu deveria inicializar o pygame para verificar se o metodo esta criando normalmente um Fabrica. Para calcular por exemplo a imagem de um jogador eu deveria inicializar o pygame. Tudo bem que nos testes do banco de dados eu poderia ter usado assert como o senhor mesmo falou, mas de resto são tudo graficamente feitos, de modo que o assert não é util. Enfim, olhe com carinho em relação ao jogo, jogos em geral. Mas foi criado novos testes. 
		

##### 12. Diagrama de classes
![](https://raw.githubusercontent.com/Corlobin/WarMars3.0/master/diasgrama.png?raw=true)


##### 13. Sonar


















