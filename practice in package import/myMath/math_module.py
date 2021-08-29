#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Math():
    def __init__(self, a, b):
        self.a = a 
        self.b = b
        self.answer = 0
        
    def add(self):
        self.answer = self.a + self.b
        #return self.answer
    
    def sub(self):
        self.answer = self.a-self.b
        #return self.answer
    
    def __str__(self): # 回傳屬性 answer 的字串形式
        return 'Answer: {0}'.format(self.answer) 

