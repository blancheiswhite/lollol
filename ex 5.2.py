
# coding: utf-8

# In[16]:


def mental(name):
    indicated = 'idk'
    if name == 'GAD' or 'phobia' or 'panic disorder' or 'ocd' or 'ptsd' or 'asd' :
        indicated = 'anxiety disorder'
    if name == 'depressive disorder'or 'bipolar disorder' :
        indicated = 'mood disorder'
    if name =='adhd' :
        indicated = 'behavior disorder'
    return indicated
mental('adhd')


# In[12]:


def mental(name):
    indicated = 'idk'
    if name = [ 'GAD', 'phobia', 'panic disorder', 'ocd', 'ptsd', 'asd'] :
        indicated = 'anxiety disorder'
    if name == ['depressive disorder', 'bipolar disorder'] :
        indicated = 'mood disorder'
    if name == 'adhd' :
        indicated = 'behavior disorder'
    return indicated

