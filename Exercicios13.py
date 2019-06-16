#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 13
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# 1 Defina a função soma_nat que recebe como argumento um número natural n e devolve a soma de todos os números naturais até n.
# 
# Ex: soma_nat(5) = 15

# In[1]:


soma_nat = lambda n : 1 if n == 1 else n + soma_nat(n-1)

soma_nat(5)


# 2- Defina a função div que recebe como argumentos dois números naturais  m   e  n  e devolve o resultado da divisão inteira de  m  por  n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira. 
#  
# Ex: div(7,2) = 3 

# In[2]:


div = lambda m, n : 0 if m < n else 1 + div(m-n,n)
div(7,2)


# 3 Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n. 
#  
# Ex: prim_alg(5649) = 5 Ex: prim_alg(7) = 7 

# In[5]:


prim_alg = lambda n : str(n)[0]

print (prim_alg(5649))
print (prim_alg(7))


# 4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e devolve o produto dos seus elementos. 
#  
# Ex: prod_lista([1,2,3,4,5,6]) = 720 

# In[1]:


prod_lista = lambda w : False if len(w)==0 else True     if w.pop(0) else contem_parQ(w)

prod_lista([1,2,3,4,5,6])


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém um número par e False em caso contrário.
# 
# Ex: contem_parQ([2,3,1,2,3,4]) = True
# Ex: contem_parQ([1,3,5,7]) = False

# In[22]:


contem_parQ = lambda w: False if len(w)==0 else True     if w.pop()%2==0 else contem_parQ(w)

print(contem_parQ([2,3,1,2,3,4]))
print(contem_parQ([1,3,5,7]))


# 6 Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros w e devolve True se w contém apenas números ímpares e False em caso contrário.
# 
# Ex: todos_imparesQ([1,3,5,7]) = True

# In[24]:


todos_imparesQ = lambda w: True if len(w)==0 else False     if w.pop()%2==0 else contem_parQ(w)

print(todos_imparesQ([1,3,5,7]))
print(todos_imparesQ([1,3,2,7]))


# 7 Defina a função pertenceQ que recebe como argumentos uma lista de números inteiros  w  e um número inteiro  n  e devolve True se  n  ocorre em  w  e False em caso contrário. 
#  
# - Ex: pertenceQ([1,2,3],1) = True 
# - Ex: pertenceQ([1,2,3],2) = True
# - Ex: pertenceQ([1,2,3],3) = True 
# - Ex: pertenceQ([1,2,3],4) = False 

# In[27]:


pertenceQ = lambda m, n : False if len(m)==0 else True     if m.pop()== n  else pertenceQ(m, n)

print (pertenceQ([1,2,3],1))
print (pertenceQ([1,2,3],2))
print (pertenceQ([1,2,3],3))
print (pertenceQ([1,2,3],4))


# 8 Defina a função junta que recebe como argumentos duas listas de números inteiros w1 e w2 e devolve a concatenação de w1 com w2 .
# 
# Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6]
# Ex: junta([],[4,5,6]) = [4, 5, 6]
# Ex: junta([1,2,3],[]) = [1, 2, 3]

# In[34]:


junta = lambda v,w: w if len(v)==0 else v if len(w)==0 else v     if len(junta_sep(v,w))== len(w) else v

print(junta([1,2,3],[4,5,6]))
print(junta([],[4,5,6]))
print(junta([1,2,3],[]))


# 9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de números inteiros w e devolve True se alguma das sublistas w tem um número primo e False em caso contrário. -Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True -Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False

# In[35]:


primo = lambda n: len([i for i in range(2,n) if n%i==0])==0 
extrai_lista = lambda w: None if len(w)==0 else w.pop()
lista_primo = lambda v: False if v == None or len(v)==0 else True if primo(v.pop()) else lista_primo(v)
temPrimoQ = lambda w: True if lista_primo(extrai_lista(w)) else False if len(w) == 0 else temPrimoQ(w)

print(temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]))
print(temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]))
print(temPrimoQ([[]]))
print(temPrimoQ([[2]]))


# 10 Defina a função inverteLista que recebe como argumento uma lista w e devolve a mesma lista mas invertida.
# 
# Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1]
# Ex: inverteLista([])

# In[36]:


inverte_lista = lambda w: w[::-1]
print(inverte_lista([1,2,3,4,5]))
print(inverte_lista([1,3,2]))
print(inverte_lista([]))


# In[ ]:




