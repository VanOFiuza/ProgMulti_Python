#!/usr/bin/env python
# coding: utf-8

#   ### Exercício 12
#   
#    **Nome**: Vanessa de Oliveira Fiuza <br>
#    **RA**: 817116855

# 1 Defina a função soma_nat que recebe como argumento um número natural  n   e devolve a soma de todos os números naturais até  n. 
#  
# Ex: soma_nat(5) = 15

# In[18]:


def soma_nat(n):
               if n == 1:
                   return 1
               else:
                return n + soma_nat(n-1)         
            
n = int(input('Insira o número desejado: '))        
print(soma_nat(n))
    


# 2- Defina a função div que recebe como argumentos dois números naturais  m   e  n  e devolve o resultado da divisão inteira de  m  por  n. Neste exercício você não pode recorrer às operações aritméticas de multiplicação, divisão e resto da divisão inteira. 
#  
# - Ex: div(7,2) = 3 

# In[30]:


def div(m,n):
    if m<n:
        return 0
    else:
        print(n, m)
        return 1 + div(m-n,n)
            
print(div(7,2))
                    
    


# 3 Defina a função prim_alg que recebe como argumento um número natural e devolve o primeiro algarismo (o mais significativo) na representação decimal de  n. 
#  
# Ex: prim_alg(5649) = 5 Ex: prim_alg(7) = 7 

# In[39]:


def prim_alg(n):
     return str(n)[0]

print (prim_alg(5649))
print (prim_alg(7))


# 4 Defina a função prod_lista que recebe como argumento uma lista de inteiros e devolve o produto dos seus elementos. 
#  
# Ex: prod_lista([1,2,3,4,5,6]) = 720

# In[44]:


def prod_lista(w):
    if len(w)==1 :
        return w[0]
    else :
        w[0]= w[0]*w[1] 
        w.pop(1)
        print(w)
        return prod_lista(w)

prod_lista([1,2,3,4,5,6])


# 5 Defina a função contem_parQ que recebe como argumento uma lista de números inteiros  w e devolve True se w contém um número par e False em caso contrário. 
#  
# - Ex: contem_parQ([2,3,1,2,3,4]) = True 
# - Ex: contem_parQ([1,3,5,7]) = False 

# In[66]:


def contem_parQ(w) :
    if len(w)==0:
        return False
    else :
        n = w.pop()
        if n%2 == 0 :
            return True
        else :
            return contem_parQ(w)
            

    
print (contem_parQ([1,3,5,7]))
print (contem_parQ([2,3,1,2,3,4]))


# 6 Defina a função todos_imparesQ que recebe como argumento uma lista de números inteiros w e devolve True se  w contém apenas números ímpares e False em caso contrário. 
#  
# Ex: todos_imparesQ([1,3,5,7]) = True 

# In[73]:


def todos_imparesQ(w) :
    if len(w)==0 :
        return True
    else:
        n = w.pop()
        if n % 2 == 0:
            return False
        else :
            return todos_imparesQ(w)
            
print (todos_imparesQ([1,3,5,7]))
print (todos_imparesQ([1,3,2,7]))


# 7 Defina a função pertenceQ que recebe como argumentos uma lista de números inteiros  w  e um número inteiro  n  e devolve True se  n  ocorre em  w  e False em caso contrário. 
#  
# - Ex: pertenceQ([1,2,3],1) = True 
# - Ex: pertenceQ([1,2,3],2) = True
# - Ex: pertenceQ([1,2,3],3) = True 
# - Ex: pertenceQ([1,2,3],4) = False 

# In[76]:


def pertenceQ(w, n):
    if len(w)==0 :
        return False
    else :
        m = w.pop()
        if m == n :
            return True
        else :
            return pertenceQ(w, n)
            
print (pertenceQ([1,2,3],1))
print (pertenceQ([1,2,3],2))
print (pertenceQ([1,2,3],3))
print (pertenceQ([1,2,3],4))


# 8 Defina a função junta que recebe como argumentos duas listas de números inteiros  w1  e  w2  e devolve a concatenação de  w1  com  w2 . 
#  
# - Ex: junta([1,2,3],[4,5,6]) = [1, 2, 3, 4, 5, 6] 
# - Ex: junta([],[4,5,6]) = [4, 5, 6] 
# - Ex: junta([1,2,3],[]) = [1, 2, 3] 

# In[101]:


def junta(w1, w2) :
    if len(w2)==0 :
        return w1
    else :
        n = w2.pop(0)
        w1.append(n)
        return junta(w1, w2)
    
print (junta([1,2,3],[4,5,6]))
print (junta([],[4,5,6]) )
print (junta([1,2,3],[]))


# 9 Defina a função temPrimoQ que recebe como argumento uma lista de listas de números inteiros  w  e devolve True se alguma das sublistas  w  tem um número primo e False em caso contrário. 
#  
# - Ex: temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) = True 
# - Ex: temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) = False 

# In[99]:


def primo(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True

def extraiLista(w):
    if len(w)==0:
        return None
    else:
        return w.pop()
    
def temPrimoQ(w):
    v = extraiLista(w)
    if v == None:
        return False
    else:
        if len(v) > 0:
            p = v.pop()
            if primo(p):
                return True
            else:
                w.append(v)
                return temPrimoQ(w)
        else:
            return temPrimoQ(w)
    
print (temPrimoQ([[4,4,4,4],[5,4,6,7],[2,4,3]]) )
print (temPrimoQ([[4,4,4,4],[4,4,4],[],[4]]) )


# 10 Defina a função inverteLista que recebe como argumento uma lista  w e devolve a mesma lista mas invertida. 
#  
# - Ex: inverteLista([1,2,3,4,5]) = [5, 4, 3, 2, 1] 
# - Ex: inverteLista([])

# In[95]:


def inverteLista(w) :
    return w[::-1]
print (inverteLista([1,2,3,4,5]))
    


# In[ ]:




