"""
* Facilita o reúso do código

* Herança é um princípio da programação
orientada a objetos (POO) que permite
criar uma nova classe a partir de uma já
existente

* Chama-se "herança" porque a nova classe
herda os métodos e atributos de uma classe
já existente

* A principal vantagem de usar herança
é a reutilização do código.

* Esse reaproveitamento pode ser acionado
quando se identifica que o atributo ou
método de uma classe será igual para as
outras

Hierarquia de Classes

* A herança permite criar uma estrutura
hierárquica de classes

* A hierarquia de classes começa por
uma classe geral chamada superclasse
(ou classe mãe ou classe base ).

* Em seguida, as subclasses
(ou classe filha ou classe derivada)
tornam-se cada vez mais específicas.

* Para saber se estamos aplicando
a herança corretamente, realiza-se
o teste “É UM”.

Esse teste simples ajuda a detectar
se a subclasse pode herdar da superclasse.

A classe Gerente herda da classe Funcionário,
porque Gerente É UM tipo de funcionário

O OBJETIVO DA HERANÇA SEMPRE É O REAPROVEITAMENTO
DE CÓDIGO, POR ISSO, É RECOMENDADO USAR O super()

O método implementado na classe filha com o mesmo
nome do método da classe mãe vai primeiro procurar
se este método existe na classe filha,
portanto, a prioridade é da filha

"""