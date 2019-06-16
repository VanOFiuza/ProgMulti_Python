#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 10
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# 1. Faça um Programa que peça dois números e imprima o maior deles.

# In[5]:



num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

if num1 > num2:
    print(f"Maior numero {num1}")
else:
    print(f"Maior numero {num2}")


# 
# 2. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

# In[8]:


vogal = ['A', 'E', 'I', 'O', 'U']

letra = input("Digite uma letra: ").upper()

if letra in vogal:
    print (f" A letra: {letra}, informada é uma vogal" )
else: 
    print (f" A letra: {letra}, informada não é uma vogal" )


# 3- Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez

# In[9]:


nota1 = 8
nota2 = 7

media = (nota1 + nota2 )/ 2

if media == 10:
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")
else:
    print("Reprovado")


# 4. Faça um Programa que leia três números e mostre-os em ordem decrescente

# In[10]:


numeros = [8, 12, 20]

numeros.sort
for n in reversed(numeros):
    print(n)


# 5 -As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# - salários até rs 280,00 (incluindo) : aumento de 20%
# - salários entre rs 280,00 e rs 700,00 : aumento de 15%
# - salários entre rs 700,00 e rs 1500,00 : aumento de 10%
# - salários de rs 1500,00 em diante : aumento de 5% Após o aumento ser realizado,
# informe na tela:
# - o salário antes do reajuste;
# - o percentual de aumento aplicado;
# - o valor do aumento;
# - o novo salário, após o aumento.

# In[11]:


salario = float(input('Insira o salário de um colaborador: '))
if salario <= 280:
    percentual = 0.20
elif salario > 280 and salario <= 700:
    percentual = 0.15
elif salario > 700 and salario <= 1500:
    percentual = 0.10
else:
    percentual = 0.05
novoSalario = salario + (salario * percentual)

print('Salário antes do reajuste:', salario)
print(f'Percentual de aumento aplicado: {percentual * 100}%')
print('Valor do aumento:', salario * percentual)
print('Novo salário:', novoSalario)


# 6. Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

# In[12]:


dias = {1:'Domingo', 2:'Segunda', 3:'Terca', 4:'Quarta', 5:'Quinta', 6:'Sexta', 7:'Sabado'}

d = int(input("Digite um numero correspondente ao dia da semana: "))

if d in dias.keys():
    print(dias[d])
else:
    print("Invalido")


# 7- Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
# Média de Aproveitamento Conceito
# - Entre 9.0 e 10.0 A
# - Entre 7.5 e 9.0 B
# - Entre 6.0 e 7.5 C
# - Entre 4.0 e 6.0 D
# - Entre 4.0 e zero E
# - O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

# In[13]:


n1 = float(input('Insira a primeira nota: '))
n2 = float(input('Insira a segunda nota: '))
media = (n1 + n2) / 2
if media >= 9 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9:
    conceito = 'B'
elif media >= 6 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
elif media < 4:
    conceito = 'E'
print(f'Nota 1: {n1}\nNota 2: {n2}\nMédia: {media}\nConceito: {conceito}')
if conceito <= "C":
    print("você foi APROVADO")
else:
    print("você foi REPROVADO")


# 8- Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno. Dicas:
# - Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# - Triângulo Equilátero: três lados iguais;
# - Triângulo Isósceles: quaisquer dois lados iguais;
# - Triângulo Escaleno: três lados diferentes;

# In[15]:


l1 = float(input('Insira o primeiro lado: '))
l2 = float(input('Insira o segundo lado: '))
l3 = float(input('Insira o terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os valores podem ser um triângulo.')
    if l1 == l2 == l3:
        print('Os valoresa formam um triângulo equilátero.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Os valores formam um triângulo isósceles.')
    else:
        print('Os valores formam um triângulo escaleno.')
else:
    print('Os valores não podem ser um triângulo.')


# 9- Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

# In[17]:


a = float(input('Insira o A: '))
if a == 0:
    print("Não é uma equação de segundo grau, programa encerrado.")
else:
    b = float(input('Insira o B: '))
    c = float(input('Insira o C: '))
    delta = b**2 - 4*a*c
    if delta < 0:
        print("A equação não possui raizes reais, programa encerrado")
    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui apenas uma raiz real:", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"A equação possui duas raiz reais: {x1} e {x2}")


# 10- Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serãofornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# - Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# - Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

# In[18]:


saque = int(input("Informe o valor a ser sacado: "))
if saque >= 10 and saque <= 600:
    n100 = saque // 100
    resto = saque % 100
    print(f'{n100} notas de 100 reais;')
    n50 = resto // 50
    resto = resto % 50
    print(f'{n50} notas de 50 reais;')
    n10 = resto // 10
    resto = resto % 10
    print(f'{n10} notas de 10 reais;')
    n5 = resto // 5
    resto = resto % 5
    print(f'{n5} notas de 5 reais;')
    print(f'{resto} notas de 1 real.')
else:
    print("Valor não permitido.")


# 11- Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".¶

# In[19]:


pontos = 0
respostas = [
    input("Telefonou para a vítima? (s/n): "),
    input("Esteve no local do crime? (s/n): "),
    input("Mora perto da vítima? (s/n): "),
    input("Devia para a vítima? (s/n): "),
    input("Já trabalhou com a vítima? (s/n): ")
]

for resposta in respostas:
    if resposta == "s":
        pontos += 1
        
if pontos == 2:
    print("Suspeita")
elif pontos >= 3 and pontos <= 4:
    print("Cúmplice")
elif pontos == 5:
    print("Assassino")
else:
    print("Inocente")


# 12- Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 25,00Reais receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

# In[20]:


preco = 0
kgMorg = float(input("Insira a quantidade em kg de morangos: "))
kgMaca = float(input("Insira a quantidade em kg de maçãs: "))

if kgMorg < 5:
    preco += kgMorg * 2.50
else:
    preco += kgMorg * 2.20
    
if kgMaca < 5:
    preco += kgMaca * 1.80
else:
    preco += kgMaca * 1.50
    
if preco > 25.00:
    preco *= 0.90

print('Valor a ser pago: ', preco)


# 13- Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

# In[22]:



num = int(input("Insira uma nota entre zero e dez: "))
while num < 0 or num > 10:
    print("Valor inválido.")
    num = int(input("Insira uma nota entre zero e dez: "))
else:
    print("Valor válido.")


# 14- Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

# In[25]:


nome = input("Insira o nome (maior que três caracteres): ")
while len(nome) <= 3:
    nome = input("Insira o nome (maior que três caracteres): ")
    
idade = int(input("Insira a idade (0 - 150): "))
while idade < 0 or idade > 150:
    idade = int(input("Insira a idade (0 - 150): "))
    
salario = int(input("Insira o salário (maior que zero): "))
while salario <= 0:
    salario = int(input("Insira o salário (maior que zero): "))
    
sexo = input("Insira o sexo (f/m): ")
while not (sexo in ['f', 'm']):
    sexo = input("Insira o sexo (f/m): ")
    
estadocivil = input("Insira o estado civil (s/c/v/d): ")
while not (estadocivil in ['s', 'c', 'v', 'd']):
    estadocivil = input("Insira o estado civil (s/c/v/d): ")


# 15 -Faça um programa que leia 5 números e informe o maior número

# In[26]:


maior = int(input("Digite o 1º número: "))
for num in range(2,6):
    x = int(input(f"Digite o {num}º número: "))
    if x > maior:
        maior = x
print("Maior:", maior)


# 16: Faça um programa que leia 5 números e informe a soma e a média dos números.

# In[28]:


soma = 0
for num in range(1,6):
    soma += int(input(f"Digite o {num}º número: "))
print("Soma:", soma)
print("Media:", soma / 5)


# 17. Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

# In[30]:


numero = list()
for num in range(1, 51):
    if num % 2 != 0:
        numero.append(num)
print(numero)


# 18. Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# In[31]:



tabuada = int(input("Insira um número inteiro entre 1 a 10: "))
for mt in range(0, 11):
    res = mt*tabuada
    print(f"{tabuada} X {mt} = {res}")


# 19. A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

# In[ ]:


a = 0
b = 1
lista = list()
limite = int(input("Até qual termo? "))
for i in range(limite):
    lista.append(a)
    aux = b
    b = a + b
    a = aux
print(lista)


# 20- Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

# In[ ]:


fatorial = int(input("Fatorial de: "))
for i in range(1, fatorial):
    fatorial = fatorial * i
print(fatorial)


# 21- O Sr. Manoel Joaquim possui uma grande loja de artigos de 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo

# In[ ]:



for num in range(1, 51):
    preco = num * 1.99
    print(f"{num} - R$ {preco}")


# 22. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo

# In[ ]:



preco = float(input("Insira o valor do pão: "))
for num in range(1, 51):
    total = num * preco
    print("%s - R$ %.2f" % (num, total))


# 23. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa eve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# In[ ]:


total = 0
preco = -1
i = 0
while preco != 0:
    preco = float(input("Insira o preço do item (Digite '0' para finalizar a compra): "))
    total += preco
    i += 1
    if preco == 0:
        print(f"Total: R$ {total}")
        pago = float(input("Insira o valor a ser pago: "))
        print("Troco: R$ ", pago - total)
    else:
        print(f"Produto {i}: R$ {preco}")


# 
# 24- Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
# - Código da cidade;
# - Número de veículos de passeio (em 1999);
# - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# - Qual a média de veículos nas cinco cidades juntas;
# - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.

# In[ ]:



cidades = {
    #cod #veiculos #acidentes
    "cidade0": [6753, 12],
    "cidade1": [7503, 23],
    "cidade2": [607, 3],
    "cidade3": [450, 2],
    "cidade4": [12045, 47]
}

menorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
maiorIndice = [cidades["cidade0"][0], cidades["cidade0"][1]]
somaVeiculos = 0
somaAcidentes = 0
contCidades = 0
for cod in cidades:
    somaVeiculos += cidades[cod][0]
    if cidades[cod][0] < 2000:
        somaAcidentes += cidades[cod][1]
        contCidades += 1
    if cidades[cod][1] > maiorIndice[0]:
        maiorIndice[0] = cidades[cod][1]
        maiorIndice[1] = cod
    if cidades[cod][1] < menorIndice[0]:
        menorIndice[0] = cidades[cod][1]
        menorIndice[1] = cod
        
    
mediaVeiculos = somaVeiculos / len(cidades.keys())
mediaAcidentes = somaAcidentes / contCidades

print(f"Maior índice e a cidade: {maiorIndice}")
print(f"Menor índice e a cidade: {menorIndice}")
print(f"Média de veículos nas cinco cidades juntas: {mediaVeiculos}" )
print(f"Média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio: {mediaAcidentes}" )


# 25. Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela. Os juros e a quantidade de parcelas seguem a tabela abaixo: Quantidade de Parcelas % de Juros sobre o valor inicial da dívida

# In[ ]:


dividaInicial = float(input("Insira o valor da dívida: "))
print("Dívida \t Valor Juros \t Qtde Parcelas \t Valor da Parcela")
for i in range(0, 5):
    if i == 0:
        juros = 0
    elif i == 1:
        juros = 10
    else:
        juros += 5
    valorJuros = dividaInicial * (juros / 100)
    divida = dividaInicial + valorJuros
    if i == 0:
        qtdeParc = 1
    else:
        qtdeParc = i * 3
    if qtdeParc != 0:
        valorParcela = divida / qtdeParc
    else:
        valorParcela = divida
    print(f"R$ {divida} \t {valorJuros} \t {qtdeParc} \t R$ %.2f"%(valorParcela))


# 
# 26. Faça um programa que mostre os n termos da Série a seguir: S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. Imprima no final a soma da série

# In[ ]:


termo = int(input('Insira a quantidade de termos desejada: '))

somaStr = "S = "
s = 0
m = 1
for n in range(1, termo + 1):
    s += n / m
    somaStr += str(n) + "/" + str(m)
    if n != termo:
        somaStr += " + "
    m += 2

print(somaStr)
print('Soma da série: %s' % s)

