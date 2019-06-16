#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 09
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# 1- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# In[3]:


raio = float(input('Digite o valor do raio: '))

area = 3.14 * (raio**2)

print("Área : ",(area)) 


# 2- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 

# In[3]:


lado = float(input('Insira o valor do lado do quadrado: '))
area = (lado*lado)

print("Área : ",(area*2))


# 3- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário no referido mês. 

# In[6]:


salario = float(input('Insira o valor do seu salario: '))
horas   = int(input('Insira a quantidade de horas p/ dia: '))

print ("Seu salário no referido mês é", (salario*horas))


# 4- Faça um Programa que peça a temperatura em graus Farenheit, transforme 
# e mostre a temperatura em graus Celsius.
# C = (5 * (F-32) / 9).

# In[7]:


f = float(input('Insira a temperatura em graus  Farenheit: '))
print ("Em Graus Celsius: ", (5*(f-32)/9))


# 5- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit. 

# In[ ]:


c = float(input('Insira a temperatura em graus Celsius: '))
print ("Em Graus Farenheit: ", ((c-32) * 5/9 ))


# 6-Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre: 
#     - o produto do dobro do primeiro com metade do segundo . 
#     - a soma do triplo do primeiro com o terceiro. 
#     - o terceiro elevado ao cubo. 

# In[3]:


n1 = int(input('Insira o primeiro numero: '))
n2 = int(input('Insira o segundo numero: '))
n3 = int(input('Insira o terceiro numero: '))

print ("O produto do dobro do primeiro com metade do segundo: ", ((n1*2) * n2/2 ))
print(n1)
print ("A soma do triplo do primeiro com o terceiro: ", ((n1*3) + n3 ))
print ("O terceiro elevado ao cubo: ", ((n3**3)))


# 7 João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com o conteúdo ZERO

# In[11]:


kg = float(input('Insira o valor(kg): '))
excesso =0
multa = 0
if kg<50 :
    print("Excesso de ",excesso,"a multa será de ",multa)
else:
    excesso = (kg-50)
    multa = excesso *4
    print("Excesso de ",excesso,"a multa será de R$",multa)


# 8 Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: 
# - salário bruto. - quanto pagou ao INSS. 
# - quanto pagou ao sindicato. 
# - o salário líquido. 
# - calcule os descontos e o salário líquido, conforme a tabela abaixo:            
#     + Salário Bruto : R$            
#     - IR (11%) : R$          
#     - INSS (8%) : R$         
#     - Sindicato ( 5%) : R$      
#     = Salário Liquido : R$ 
#     
#     Obs.: Salário Bruto 
#     - Descontos = Salário Líquido. 

# In[2]:


salario = float(input('Insira o valor do seu salario: '))
horas   = int(input('Insira a quantidade de horas p/mes: '))

salario *=horas
salarioBruto = salario
impostoRenda = salario*11/100
inss= (salario*8/100)
sindicato = (salario*5/100)
salario -= impostoRenda + inss + sindicato
print('quanto pagou ao INSS: ',inss )
print('quanto pagou ao sindicato: ', sindicato )
print('quanto pagou de imposto de renda: ', impostoRenda )
print('salario liquido: ', salario )
print('salario bruto: ', salarioBruto )


# 9- Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo. 
# Exemplo: 
# -  String 1: Brasil Hexa 2018 
# -  String 2: Brasil! Hexa 2018! Tamanho de "Brasil Hexa 2018": 16 caracteres 
# -  Tamanho de "Brasil! Hexa 2018!": 18 caracteres 
# -  As duas strings são de tamanhos diferentes. 
# -  As duas strings possuem conteúdo diferente. 

# In[10]:


str1 = input('Insira a primeira frase: ')
str2 = input('Insira a segunda frase : ')

print('O tamanho de ', str1, ': ', len(str1))
print('O tamanho de ', str2, ': ', len(str2))

if len(str2) == len(str1):
    print('As duas strings são de tamanhos iguais.')
    cont=0 
    for i in range(len(str1)):
        if str1[cont]!=str2[cont] :
            print('As duas strings possuem conteúdo diferente.')
            break
        
        cont+=1
        if cont==len(str1):  
            print('As duas strings possuem conteúdo igual.')    
    
else :
    print('As duas strings são de tamanhos diferentes.')
    print('As duas strings possuem conteúdo diferente.')



# 10 Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. 
# - Observação: não use loops.

# In[17]:


nome = input('Digite seu nome ')
print(nome[::-1].upper())


# 11- Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Data de Nascimento: 29/10/1973 Você nasceu em  29 de Outubro de 1973. 
# - Obs.: Não use desvio condicional nem loops. 
#  

# In[26]:


data = input('Insira sua data de nascimento: EX:((dd/mm/aaaa)') 
meses = ['Janeiro' ,'Fevereiro' ,'Março' ,'Abril' ,'Maio' ,'Junho' ,'Julho' ,'Agosto' ,'Setembro' ,'Novembro' ,'Dezembro'] 
listData = list(data.split('/'))
mes = meses[int(listData[1])-1]

print('Você nasceu em ',listData[0],' de ',mes,' de ',listData[2])


# 12 Leet é uma forma de se escrever o alfabeto latino usando outros símbolos em lugar das letras, como números por exemplo. A própria palavra leet admite muitas variações, como l33t ou 1337. O uso do leet reflete uma subcultura relacionada ao mundo dos jogos de computador e internet, sendo muito usada para confundir os iniciantes e afirmar-se como parte de um grupo. Pesquise sobre as principais formas de traduzir as letras. Depois, faça um programa que peça uma texto e transforme-o para a grafia leet speak. 
# 
# -Desafio: não use loops nem desvios condicionais.

# In[4]:


entrada = 'abcdefghijklmnopqrstuvxwyz'.upper()
saida = '48¢d3f6#1jklmn0pqr57uvxwy2'.upper()
leet = str.maketrans(entrada, saida)
texto = input('insira um texto:')
print(texto.upper().translate(leet))


# Listas 
#  
# 13 Crie um programa que recebe uma lista de números e 
# - retorne o maior elemento 
# - retorne a soma dos elementos 
# - retorne o número de ocorrências do primeiro elemento da lista 
# - retorne a média dos elementos 
# - retorne o valor mais próximo da média dos elementos 
# - retorne a soma dos elementos com valor negativo 
# - retorne a quantidade de vizinhos iguais 

# In[7]:


lista = [1,2,3,12,20,8]




def maiorElemento(lista):
    if len(lista) == 0:
        return None
    else:
        ini = lista[0]
        for i in lista:
            if i > ini:
                ini = i
        return 'maior elemento -> '+str(ini)
        
def somaElementos(lista):
    if len(lista) == 0:
        return None
    else:
        result = 0
        for i in lista:
            result += i
        return 'soma dos elementos -> '+str(result)

def numeroOcorrenciasPrimeiroElemento(lista):
    if len(lista) == 0:
        return None
    else:
        ini = lista[0]
        count = 0
        for i in lista:
            if i == ini:
                count += 1
        return 'número de ocorrências do primeiro elemento da lista -> '+str(count)

def mediaElementos(lista):
    if len(lista) == 0:
        return None
    else:
        soma = 0
        for i in lista:
            soma += i
        return 'média dos elementos -> '+str(soma/2)
        
def valorMaisProximoMedia(lista):
        if len(lista) == 0:
            return None
        else:
            soma = 0
            media = 0
            for i in lista:
                soma += i
            media = soma/len(lista)
            diferenca = media / lista[0]
            valorMaisProx = lista[0]
            for i in lista:
                if (media - i) < diferenca:
                    diferenca = media - i
                    valorMaisProx = i
            return 'valor mais próximo da média dos elementos -> '+str(valorMaisProx)

def somaElementosNegativo(lista):
    if len(lista) == 0:
        return None
    else:
        soma = 0
        for i in lista:
            soma += i
        result = soma - (soma*2)
        return 'soma dos elementos com valor negativo -> '+str(result)
        
def quantidadeVizinhosIguais(lista):
    if len(lista) == 0:
        return None
    elif len(lista) == 1:
        return 0
    else:
        count = 0
        for i,v in enumerate(lista):
            if i+1 != len(lista):
                if lista[i] == lista[i+1]:
                    count += 1
            else:
                return 'quantidade de vizinhos iguais -> '+str(count)
                

    print(maiorElemento(lista))
    print(somaElementos(lista))
    print(numeroOcorrenciasPrimeiroElemento(lista))
    print(mediaElementos(lista))
    print(valorMaisProximoMedia(lista))
    print(somaElementosNegativo(lista))
    print(quantidadeVizinhosIguais(lista))
  



# 14 Faça um programa que receba duas listas e retorne True se são iguais ou False caso contrario. Duas listas são iguais se possuem os mesmos valores e na mesma ordem. 

# In[8]:


lista1 = [1,2,3,6,7,8,4,9]
lista2 = [1,2,3,6,7,8,4,9]

if lista1 ==lista2 :
    print (True)
else :
    print(False)


# 15 Faça um programa que receba duas listas e retorne True se têm os mesmos elementos ou False caso contrário Duas listas possuem os mesmos elementos quando são compostas pelos mesmos valores, mas não obrigatoriamente na mesma ordem. 

# In[36]:


lista1 = [1,2,3,5,7,8,4,9]
lista2 = [1,2,3,5,7,8,4,9]

listaBool = list(set(lista1) - set(lista2))


if len(listaBool) == 0:
    print(True)
else:
    print(False)
        


# 16 Faça um programa que percorre uma lista com o seguinte formato: [['Brasil', 'Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]. 
#  Essa lista indica o número de faltas que cada time fez em cada jogo. Na lista acima, no jogo entre Brasil e Itália, o Brasil fez 10 faltas e a Itália fez 9. O programa deve imprimir na tela: 
#     - o total de faltas do campeonato  
#     - o time que fez mais faltas
#     - o time que fez menos faltas 
#  

# In[43]:


lista_jogos = [['Brasil','Italia', [10, 9]], ['Brasil', 'Espanha', [5, 7]], ['Italia', 'Espanha', [7,8]]]
total_faltas = 0
dict_times = {}

menos_faltas = ""
mais_faltas = ""

for jogos in lista_jogos:
    total_faltas = total_faltas + int(jogos[2][0]) + int(jogos[2][1])
    for times, faltas in zip(jogos, jogos[2]):
        if(dict_times.get(times)):
            dict_times[times] = dict_times.get(times) + faltas
        else:
            dict_times[times] = faltas
mais_faltas = []
menos_faltas = []

for k, v in dict_times.items():
    if v == max(list(dict_times.values())):
        mais_faltas.append(k)
    if v == min(list(dict_times.values())):
        menos_faltas.append(k)


print(" Total de falta = ", dict_times, " \n Maior quantidade de faltas = ",mais_faltas," \n Menor quantidade de faltas = ",menos_faltas)


# 17 Escreva um programa que conta a quantidade de vogais em uma string e armazena tal quantidade em um dicionário, onde a chave é a vogal considerada. 

# In[44]:


texto = "Abacaxi"
vogais = ["a", "e", "i", "o", "u"]

vog = {}
for v in vogais:
    if v in texto:
        vog[v] = list(texto.lower()).count(v)
print(vog)


# 18 Escreva um programa que lê̂ duas notas de vários alunos e armazena tais notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve terminar quando for lida uma string vazia como nome. Escreva uma função que retorna a média do aluno, dado seu nome. 

# In[ ]:


nome = input('Digite o nome do aluno')
pergunta = False
boletim = {}
while len(nome) != 0: 
    if pergunta:
        nome = input('Digite o nome do aluno')
        if len(nome) == 0:
            break
    n1 = int(input('insira a primera nota'))
    n2 = int(input('insira a segunda nota'))
    boletim[nome]=[n1,n2]
    if not pergunta:
        pergunta = True
        
nome = input('insira o nome do aluno para saber a média')

def mediaPorNome(arg):
    notas = boletim.get(arg)
    print('A média do aluno '+arg+' é '+str(sum(notas)/len(notas)))
    
mediaPorNome(nome)


# 19 Uma pista de Kart permite 10 voltas para cada um de 6 corredores. Escreva um programa que leia todos os tempos em segundos e os guarde em um dicionário, onde a chave é o nome do corredor. Ao final diga de quem foi a melhor volta da prova e em que volta; e ainda a classificação final em ordem (1o o campeão). O campeão é o que tem a menor média de tempos

# In[ ]:


corrida = {}
melhoresVoltas = {}
for i in range(6):
    tempos = []
    nome = input('nome do '+str(i+1)+'º corredor:')
    for j in range(6):
        tempos.append(float(input('digite o '+str(j+1)+'º tempo do corredor '+nome+' em segundos:')))
    corrida[nome]=tempos
    
for i,k in enumerate(corrida.keys()):
    melhoresVoltas[k]=[min(corrida.get(k)), corrida.get(k).index(min(corrida.get(k)))+1]

melhoresVoltarSemIndex = {}
lista = []
for k,v in melhoresVoltas.items():
    melhoresVoltarSemIndex[v[0]]=k
    lista.append(v[0])

lista.sort()
print('Melhor volta da prova foi de '+melhoresVoltarSemIndex.get(lista[0])+      ', tempo de '+str(melhoresVoltas.get(melhoresVoltarSemIndex.get(lista[0]))[0])+' na volta '+      str(melhoresVoltas.get(melhoresVoltarSemIndex.get(lista[0]))[1]))

classificacaoLista = []
classificacaoMap = {}
for k,v in corrida.items():
    media = sum(v)/len(v)
    classificacaoLista.append(media)
    classificacaoMap[media]=k
    
classificacaoLista.sort()
    
print('Classificação: ')
for i, v in enumerate(classificacaoLista):
    print(str(i+1)+ 'º colocado -> '+classificacaoMap.get(v)+' com média de '+str(v))


# 20 Escreva um programa para armazenar uma agenda de telefones em um dicionário. Cada pessoa pode ter um ou mais telefones e a chave do dicionário é o nome da pessoa. Seu programa deve ter as seguintes funções:
# 
# incluirNovoNome – essa função acrescenta um novo nome na agenda, com um ou mais telefones. Ela deve receber como argumentos o nome e os telefones.
# incluirTelefone – essa função acrescenta um telefone em um nome existente na agenda. Caso o nome não exista na agenda, você̂ deve perguntar se a pessoa deseja inclui-lo. Caso a resposta seja afirmativa, use a função anterior para incluir o novo nome.
# excluirTelefone – essa função exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver apenas um telefone, ela deve ser excluída da agenda.
# excluirNome – essa função exclui uma pessoa da agenda.
# consultarTelefone – essa função retorna os telefones de uma pessoa na agenda.

# In[ ]:


agenda = {}

def incluirNovoNome(nome, listaTel):
    agenda[nome]=list(listaTel.split(','))
    
def incluirTelefone(nome, tel):
    if agenda.get(nome) != None:
        lista = agenda.get(nome)
        lista.append(tel)
        agenda[nome]=lista
        return True
    else:
        return False
    
def excluirTelefone(nome, tel):
    if len(agenda.get(nome)) > 1:
        lista = []
        listaAgenda = agenda.get(nome)
        for i in listaAgenda:
            if i != tel:
                lista.append(i)
        agenda[nome]=lista
    elif len(agenda.get(nome)) == 1:
        agenda.pop(nome)
        
def excluirNome(nome):
    agenda.pop(nome)
    
def consultarTelefone(nome):
    return agenda.get(nome)

menu = int(input('1) incluirNovoNome\n2) incluirTelefone\n3) excluirTelefone\n4) excluirNome\n5) consultarTelefone\n6) Sair'))
pergunta = False
while menu != 6:
    if pergunta:
        menu = int(input('1) incluirNovoNome\n2) incluirTelefone\n3) excluirTelefone\n4) excluirNome        \n5) consultarTelefone\n6) Sair'))
    else:
        pergunta = True
    
    if menu == 1:
        nome = input('Digite o nome')
        tel = input('Insira telefone, ou N telefones separados por virgula (11111,22222,33333)')
        incluirNovoNome(nome, tel)
       # print(agenda)
    elif menu == 2:
        nome = input('Digite o nome')
        tel = input('Insira 1 (um) telefone novo')
        if incluirTelefone(nome, tel):
            print(agenda)
        else:
            resp = input('deseja incluir este novo nome na agenda? S/N')
            if resp.upper() == 'S':
                incluirNovoNome(nome, tel)
        #        print(agenda)
    elif menu == 3:
        nome = input('Digite o nome')
        tel = input('Digite o telefone que deseja excluir')
        excluirTelefone(nome, tel)
       # print(agenda)
    elif menu == 4:
        nome = input('Digite o nome')
        excluirNome(nome) 
        #print(agenda)
    elif menu == 5:
        nome = input('Digite o nome')
        print(consultarTelefone(nome))
        #print(agenda)
    elif menu == 6:
        #print(agenda)
        print('Tchau =)')


# 21 Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato:
# 
# - 200.135.80.9
# - 192.168.1.1
# - 8.35.67.74
# - 257.32.4.5
# - 85.345.1.2
# - 1.2.3.4
# - 9.8.234.5
# - 192.168.0.256 
#  
# O arquivo de saída possui o seguinte formato: 
# 
# [Endereços válidos:]
# - 200.135.80.9
# - 192.168.1.1
# - 8.35.67.74
# - 1.2.3.4 
# 
# [Endereços inválidos:]
# - 257.32.4.5
# - 85.345.1.2
# - 9.8.234.5
# - 192.168.0.256

# In[ ]:


valido = list()
invalido = list()
for ip in open('arquivo.txt', 'r'):
    l_ip = ip.split('.')
    l_ip = list(map(int, l_ip))
    if len(l_ip) != 4:
        invalido.append(l_ip)
    else:
        for i in l_ip:
            if i < 0 or i > 255:
                invalido.append(l_ip)
                break
        else:
            valido.append(l_ip)
print('Validos:')
for i in valido:
    print(f'{i[0]}.{i[1]}.{i[2]}.{i[3]}')
print('\nInvalidos:')
for i in invalido:
    print(f'{i[0]}.{i[1]}.{i[2]}.{i[3]}')


# 22 A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
# 
# - alexandre 456123789
# - anderson 1245698456
# - antonio 123456456
# - carlos 91257581
# - cesar 987458
# - rosemary 789456125
# Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
# 
# ACME Inc. Uso do espaço em disco pelos usuários ----------------------------------------------------------------------- Nr. Usuário Espaço utilizado % do uso
# 
# - 1 alexandre 434,99 MB 16,85%
# - 2 anderson 1187,99 MB 46,02%
# - 3 antonio 117,73 MB 4,56%
# - 4 carlos 87,03 MB 3,37%
# - 5 cesar 0,94 MB 0,04%
# - 6 rosemary 752,88 MB 29,16%
# 
# Espaço total ocupado: 2581,57 MB Espaço médio ocupado: 430,26 MB
# 
# O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.

# In[ ]:


def format_bytes(size):
    # 2**10 = 1024
    potencia = 2**10
    n = 0
    while n < 2:
        size /= potencia
        n += 1
    return size

def percentual_uso(usoTotal, usoPessoa):
    return (100 * usoPessoa) / usoTotal

lista = []
for i in open('usuarios.txt', 'r'):
    lista.append(i.split())

usoTotal = 0
for i in lista:
    usoTotal += format_bytes(int(i[1]))
usoTotal = '%.2f' %usoTotal

espacoMedio = float(usoTotal)/len(lista)    
espacoMedio = '%.2f' %espacoMedio

relatorio = open('relatorio.txt','w+')
for i,v in enumerate(lista):
    relatorio.write(str(i+1)+' ')
    relatorio.write(v[0])
    relatorio.write(' ')
    mb = format_bytes(int(v[1]))
    relatorio.write('%.2f' %mb)
    relatorio.write(' MB ')
    percentual = percentual_uso(float(usoTotal), mb)
    relatorio.write('%.2f' %percentual)
    relatorio.write('%')
    relatorio.write('\n')
relatorio.write('Espaço total ocupado: '+str(usoTotal)+' MB Espaço médio ocupado: '+str(espacoMedio)+' MB')
relatorio.close()

for i in open('relatorio.txt','r'):
    print(i)


# In[ ]:




