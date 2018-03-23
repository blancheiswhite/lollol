
# coding: utf-8

# In[1]:


range(5)


# In[2]:


range(1,6)


# In[3]:


answer = 1
for num in range(1, 6):
    answer = answer * num
answer


# In[8]:


def factorail(n):
    answer = 1
    for num in range(1, 6):
        answer = answer * num
    return answer
factorail(4)


# In[10]:


def fact(n): 
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
fact(10)


# In[16]:


def factorial(n):
    answer = 1
    for num in range(-100,100):
        if num < 0:
            return 'nope'
        else :
            answer = answer * num
            return answer

factorial(-100)


# In[20]:


def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        return 'nope'
    else:
        return n*fact(n-1)
fact(-1)
fact(3)





def fact(n):
    return factorial(n)

fact(3)

