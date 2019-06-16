#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 14
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# In[10]:


def maybe(fnc):
    
    def inner(*args):
        
        for a in args:
            if isinstance(a, Exception):
                return a
        try:
            return fnc(*args)
        except Exception as e:
            return e
    return inner


# 1 Defina a função soma_nat que recebe como argumento um número natural n e devolve a soma de todos os números naturais até n.
# 
# Ex: soma_nat(5) = 15

# In[18]:


soma_nat = maybe(lambda n: n + soma_nat(n - 1) if n > 0 else 0)

soma_nat("teste erro")
print(soma_nat(3) == 6)
print(soma_nat(5) == 15)


# 2 Defina a função div que recebe como argumentos dois números naturais m e n e devolve o resultado da divisão inteira de m por n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira.
# 
# Ex: div(7,2) = 3

# In[20]:


div = maybe(lambda m,n: 1 + div(m - n, n) if m >= n else 0)
div("teste erro")

print(div(7,2))
                


# 3 Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de n.
# 
# Ex: prim_alg(5649) = 5 Ex: prim_alg(7) = 7

# In[23]:


prim_alg = lambda n: str(n)[0]

safe_prim_alg = maybe(prim_alg)
prim_alg("teste erro")
print (prim_alg(5649))
print (prim_alg(7))


# 4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e devolve o produto dos seus elementos. 
#  
# Ex: prod_lista([1,2,3,4,5,6]) = 720 

# In[51]:


prod_lista = maybe(lambda lista: lista[len(lista) - 1] * prod_lista(lista[:-1]) if len(lista) > 0 else 1)
prod_lista([1,2,3,4,5,6]
prod_lista("teste erro")


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.
# 
# Ex: contem_parQ([2,3,1,2,3,4]) = True Ex: contem_parQ([1,3,5,7]) = False

# In[24]:


contem_parQ = maybe(lambda w: False if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and not contem_parQ(w[:-1])) else True)
contem_parQ("teste erro")
print(contem_parQ([2,3,1,2,3,4]))
print(contem_parQ([1,3,5,7]))


# 6 Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém apenas números ímpares e False em caso contrário.
# 
# Ex: todos_imparesQ([1,3,5,7]) = True Ex: todos_imparesQ([]) = True Ex: todos_imparesQ([1,2,3,4,5]) = False

# In[ ]:



todos_imparesQ = maybe(lambda w: True if len(w) == 0 or (w[len(w) - 1] % 2 != 0 and todos_imparesQ(w[:-1])) else False)
todos_imparesQ("teste erro")

assert(todos_imparesQ([1,3,5,7]) == True)
assert(todos_imparesQ([1,2,3,4,5]) == False)


# 7 - Defina a função pertenceQ que recebe como argumentos uma lista de números inteiros w e um número inteiro n e devolve True se n ocorre em w e False em caso contrário.

# In[25]:


pertenceQ = maybe(lambda w,n : False if len(w)==0 else True if w.pop()== n else pertenceQ(w,n))
pertenceQ("teste erro")
print (pertenceQ([1,2,3],1))
print (pertenceQ([1,2,3],2))
print (pertenceQ([1,2,3],3))
print (pertenceQ([1,2,3],4))


# 8 Defina a função junta que recebe como argumentos duas listas de números inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
# 
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6] Ex: junta([],[4,5,6]) = [4, 5, 6] Ex: junta([1,2,3],[]) = [1, 2, 3]

# In[27]:


junta = maybe(lambda v,w: w if len(v)==0 else v if len(w)== 0 else v if len(junta_sep(v,w)) == len(w) else v)
junta_sep = maybe(lambda v,w: [v.append(q) for q in w])

print(junta([1,2,3],[4,5,6]))
print(junta([1,2,3],[]))
print(junta([],[4,5,6]))


# In[28]:


junta("teste",1)


# 9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de números inteiros w e devolve True se alguma das sublistas w tem um número primo e False em caso contrário. 
# - Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True 
# - Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

# In[30]:


primo = maybe(lambda n: len([ i for i in range(2,n) if n%1 ==0])==0)
extrai_lista = maybe(lambda w: None if len(w)==0 else w.pop())
lista_primo = maybe(lambda v: False if v ==None or len(v)==0 else True if primo(v.pop()) else lista_primo(v))
temPrimoQ = maybe(lambda w: True if lista_primo(extrai_lista(w)) else False if len(w)==0 else temPrimoQ(w))

temPrimoQ([[4,4,4],[5,4,6,7],[2,3,4]])


# In[31]:


temPrimoQ()


# 10 - Defina a funcao inverte lista que recebe como argumento uma lista w e devolve a mesma lista mas invertida
# 
# Ex: InverteLista([1,2,3,4,5]) = ([5,4,3,2,1])
# 

# In[32]:


inverteLista = maybe(lambda w: w[::-1] )

inverteLista(1)


# In[33]:



inverteLista([1,2,3,4,5])

