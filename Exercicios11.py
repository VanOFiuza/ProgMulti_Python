#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 11
#   
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# 1- Menor de dois pares: Escreva uma função que retorne o menor de dois números dados se ambos os números forem pares, mas retorna o maior se um dos dois for ímpar.
# - Exemplo: menor_de_dois_pares(2,4) --> 2 menor_de_dois_pares (2,5) --> 5 
# 

# In[8]:


def menor_de_dois_pares(n1,n2):
    if n1% 2 == 0 and n2%2 == 0 :
        if n1>n2 :
            print(n2)
        else :
            print(n1)
    else :
        if n1>n2 :
            print(n1)
        else :
            print(n2)
            
            
menor_de_dois_pares(4,8)
menor_de_dois_pares(7,5)


# 2 Mesma letra: Escreva uma função que receba uma string com duas palavras e retorne True se ambas palavras começarem com a mesma letra. Exemplo: 
# - mesma_letra('Cão covarde') -> True
# - mesma_letra('Vira Lata') -> False 
#  

# In[14]:


def mesma_letra(str):
    palavras = list(str.split(' '))
    if palavras[0][0].upper() == palavras[1][0].upper():
        return True
    else :
        return False

print(mesma_letra('Cão covarde'))
print(mesma_letra('Vira Lata'))


# In[21]:


def mesma_letra(str):
    return list(str.split())[0][0].upper() == list(str.split())[1][0].upper()

print(mesma_letra('Cão covarde'))
print(mesma_letra('Vira Lata'))


# 3 Mestre Yoda: Dada uma sentença, a função deve retornar a sentença com as palavras na ordem reversa. 
# - Exemplo: 
# - mestre_yoda('Eu estou em casa') --> 'casa em estou Eu'
# - mestre_yoda('Estamos prontos') --> 'prontos Estamos' 

# In[1]:


def mestre_yoda(s):
    lista = s.split()[::-1]
    s = ''
    for i in lista:
        s += ' ' + i
    return s


print(mestre_yoda('Eu estou em casa'))
print(mestre_yoda('Estamos prontos'))


# 4 Tem 33: Faça uma função que retorne True se, dada uma lista de inteiros, houver em alguma posição da lista um 3 do lado de outro 3. Exemplo:
# - tem_33([1,3,3]) --> True
# - tem_33([1,3,1,3]) --> False
# - tem_33([3,1,3]) --> False

# In[2]:


def tem_33(lista):
    for i in range(0, len(lista)):
        if lista[i] == 3 and i + 1 < len(lista) and lista[i+1] == 3:
            return True
    return False

print(tem_33([1,3,3]))
print(tem_33([3,1,3]))


# 5 Blackjack: Faça uma função que receba 3 inteiros entre 1 e 11. Se a soma deles for menor que 21, retorne o valor da soma. Se for mair do que 21 e houver um 11, subtraia 10 da soma antes de apresentar o resultado. Se o valor da soma passar de 21, retorne ‘ESTOUROU’. Exemplo:¶
# - blackjack(5,6,7) --> 18
# - blackjack(9,9,9) --> 'ESTOUROU'
# - blackjack(9,9,11) --> 19

# In[3]:


def blackjack(n1, n2, n3):
    somatoria = n1 + n2 + n3
    if somatoria <= 21:
        if somatoria > 21 and n1 == 11 or n2 == 11 or n3 == 11:
            return somatoria - 10
        else: 
            return somatoria
        
    elif somatoria > 21 and n1 == 11 or n2 == 11 or n3 == 11:
        somatoria -= 10
        if somatoria <= 21:
            return somatoria 
        else:
            return f"ESTOUROU: {somatoria}"
    else:
        return f"ESTOUROU: {somatoria}"


print(blackjack(10, 10, 11)) 
print(blackjack(5, 6, 5)) 
print(blackjack(11, 11, 11)) 
print(blackjack(10, 10, 10))


# 6 Espião: Escreva uma função que receba uma lista de inteiros e retorne True se contém um 007 em ordem, mesmo que não contínuo. Exemplo:
# 
# - espiao([1,2,4,0,0,7,5]) --> True
# - espiao([1,0,2,4,0,5,7]) --> True
# - espiao([1,7,2,4,0,5,0]) --> False

# In[4]:


def espiao(lista):
    chave = [0,0,7]
    ret = [False, False, False]
    k = 0
    for i in lista:
        if i == chave[k]:
            ret[k] = True
            k += 1
            if k >= len(chave):
                break
    return ret[0] and ret[1] and ret[2]

print(espiao([1,2,4,0,0,7,5]))
print(espiao([1,0,2,4,0,5,7]))
print(espiao([1,7,2,4,0,5,0]))


# 
# 7 Linha: Crie a classe Linha que tem dois atributos, coordenada1 e coordenada2. Cada coordenada é uma tupla que carrega duas coordenadas cartesianas (x,y) que denotam pontos do segmento de reta. Faça métodos que calculem o comprimento do segmento de reta e sua inclinação.

# In[5]:


import math
class Linha:
    
    def __init__(self, c1, c2):
        self.coordenada1 = c1
        self.coordenada2 = c2
        
    def calcularComprimento(self):
        return math.sqrt((self.coordenada2[0] - self.coordenada1[0])**2 + (self.coordenada2[1] - self.coordenada1[1])**2)
    
    def calcularInclinacao(self):
        return (self.coordenada2[1] - self.coordenada1[1]) / (self.coordenada2[0] - self.coordenada1[0])
    
linha = Linha((3, 2), (7, 8))
print(linha.calcularComprimento())
print(linha.calcularInclinacao())


# 8 Figuras: Crie a seguinte hierarquia de classes de figuras geométricas. Veja na figura as fórmulas:
# 
# - A classe abstrata Figura deve ter o método abstrato area.
# - A classe concreta Circulo é subclasse de Figura.
# - A classe abstrata Poligono é subclasse de Figura e deve ter os atributos base e altura .
# - As classes concretas Triangulo, Losango, Retangulo e Quadrado são subclasses de Poligono. Tente criar mais uma generalização aqui olhando as fórmulas da área.
# - Os polígonos Retangulo e Quadrado devem implementar a interface Diagonal, que deve ter um método que calcula a diagonal.
# - Crie uma classe Geometria com uma lista de Figuras com pelo menos uma figura de cada e imprima suas áreas, perímetros e diagonais.

# In[6]:


class Figura:
    def area(self):
        raise NotImplementedError(
            "A subclasse deve implementar o método abstrato")
    def perimetro(self):
        raise NotImplementedError(
            "A subclasse deve implementar o método abstrato")


# In[7]:


from math import pi
class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return self.raio**2 * pi
    
    def perimetro(self):
        return 2*pi*self.raio
    
    
circulo = Circulo(3)
print(circulo.area())
print(circulo.perimetro())


# 9 Jogo de Blacjack: Faça um joguinho simples em Python.
# 
# Aqui estão os requisitos:
# 
# - Você precisa criar um jogo de BlackJack (21) baseado em texto simples 
# - O jogo precisa ter um jogador contra um croupier automatizado.
# - O jogador pode desistir ou bater. 
# - O jogador deve ser capaz de escolher o seu valor de aposta. 
# - Você precisa acompanhar o dinheiro total do jogador. 
# - Você precisa alertar o jogador de vitórias, derrotas ou estouros, etc ... 
# 
# E o mais importante:
# 
# Você deve usar OOP e classes em alguma parte do seu jogo. Você não pode simplesmente usar funções no seu jogo. Use classes para ajudá-lo a definir o deck e a mão do jogador. Há muitas maneiras certas de fazer isso, então explore bem!

# In[1]:



class Carta(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
    def __repr__(self):
        return '<%s de %s>' % (self.valor, self.naipe)


# In[2]:



class Baralho(object):
    naipes = 'paus copas espadas ouros'.split()
    valores = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()
    
    def __init__(self):
        self.cartas = [Carta(v, n)
                      for n in self.naipes
                      for v in self.valores]
    def __len__(self):
        return len(self.cartas)
    def __getitem__(self, pos):
        return self.cartas[pos]
    def __setitem__(self, pos, item):
        self.cartas[pos] = item
    def __getone__(self):
        return self.cartas.pop()


# In[3]:


from random import shuffle

b = Baralho()
#embaralha cartas
shuffle(b)
mapa = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}
cartasUsuario = []
cartasNPC = []
apostaUsuario = 0
menuInicial = int(input('1) Jogar\n2) Sair: '))
jogando = False
if menuInicial == 1:
    jogando = True
    print('Você recebeu duas cartas iniciais')
    cartasUsuario.append(b.__getone__())
    cartasUsuario.append(b.__getone__())
    print(cartasUsuario)
    apostaUsuario = float(input('Digite sua aposta inicial em Reais (R$):'))
    print('A CPU recebeu duas cartas inicais')
    cartasNPC.append(b.__getone__())
    cartasNPC.append(b.__getone__())
    print(cartasNPC)
while jogando:
    print('\n')
    print('Sua aposta: R$'+str(apostaUsuario))
    print('Suas cartas: '+str(cartasUsuario))
    print('Cartas da CPU: '+str(cartasNPC))
    menu = int(input('1) Sacar uma carta\n2) Desistir\n3) Bater\n4) Aumentar aposta\n5) Sair: '))
    if menu == 1:
        print('\n')
        cartasUsuario.append(b.__getone__())
        print('Você sacou um '+ str(cartasUsuario[len(cartasUsuario)-1]))
        soma = 0
        lista = list(map(str, cartasUsuario))
        for i in lista:
            soma+=mapa.get(i[1])
        if soma == 21:
            print('VOCÊ GANHOU!!')
            jogando = False
        elif soma > 21:
            print('ESTOUROU, você perdeu!!!')
            jogando = False
    elif menu == 2:
        print('Você desistiu da partida!!')
        jogando = False
    elif menu == 3:
        somaUsuario = 0
        listaUsuario = list(map(str, cartasUsuario))
        for i in listaUsuario:
            somaUsuario+=int(mapa.get(i[1]))
            
        somaNPC = 0
        listaNPC = list(map(str, cartasNPC))
        for i in listaNPC:
            somaNPC+=int(mapa.get(i[1]))
        
        resultUsuario = 21-int(somaUsuario)
        resultNPC = 21-int(somaNPC)
        
        if resultUsuario < resultNPC:
            print('VOCÊ GANHOU!!')
            jogando = False
        elif resultUsuario > resultNPC:
            print('VOCÊ PERDEU!!')
            jogando = False
        else:
            print('EMPATE!!')
            jogando = False
    elif menu == 4:
        apostaUsuario += float(input('Aumente a aposta em Reais (R$):'))
    elif menu == 5:
        jogando = False


# 
