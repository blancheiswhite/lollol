
# coding: utf-8

# In[19]:


class gravity(object):
    def __init__(self, value):
        self._earth = float(value)
    def e(self):
        return str(self._earth) + 'kg'
    def m(self):
        return str((self._earth * 1.0/6 )) + 'kg'


cool = gravity(100)
cool.e()
tool = gravity(100)
tool.m()


# In[12]:


def __init__(self, value, scale):
    if scale.lower() == 'e'
        self._earth = float(value)
    elif scale.lower() == 'f':
        self._earth = value * 1.0/6 

