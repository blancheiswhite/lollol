
# coding: utf-8

# In[11]:


def tautonym(wyatt):
    if len(wyatt) %2 == 0:
        for i in range(len(wyatt)):
            if wyatt[i] == wyatt[i+ len(wyatt)/2 ]:
                return 'true'
    else:
        return 'false'


# In[12]:


tautonym('hellohello')

