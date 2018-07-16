
# coding: utf-8

# In[17]:


num=[]
for i in range(2000,3201):
    if(i%7==0)&(i%5!=0):
        num.append(str(i))
print(','.join(num))
        


# In[18]:


firstname=input("What is your firstname?")
lastname=input("What is your lastname?")
name=firstname + " "+lastname
print(name[::-1])


# In[19]:


d=12
r=d/2
volume=4*3.14*r**3/3
print("The volume of sphere with radius 12 cm is ",volume)


# In[20]:



numbers=input("Enter the numbers of your choice seperated by commas...").split(",")
numbers


# In[21]:


symbol='*'
for i in range(1,6):
    print(symbol*i)
for i in reversed(range(1,5)):
    print(symbol*i)


# In[22]:


word=input("Enter a word of your choice...")
print(word[::-1])

