#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Checking the number of characters the string has 
#This is working on name based only So full Name is taken into consideration and you could play around with that
Name = input ('Please enter your name ')

print('Number of characters in your name is:')
print(len(Name))


# In[22]:


#checking to see the upper case and lower case characters in a sentence
def upperlower(Sentence):
  
    upper = 0
    lower = 0
  
    for i in range(len(Sentence)):
        if (ord(Sentence[i]) >= 97 and
            ord(Sentence[i]) <= 122):
            lower += 1
        elif (ord(Sentence[i]) >= 65 and
              ord(Sentence[i]) <= 90):
            upper += 1
  
    print('Lower case characters = %s' %lower,
          'Upper case characters = %s' %upper)
  
Sentence= input('Check out your Capitalisations  ')
upperlower(Sentence)


# In[24]:


#Checking to see if there is a number in the within the string and displaying it 
Number_check = input(' Desired choice of words')

checking = [int(i) for i in Number_check.split() if i.isdigit()]

print("Your number in this particular sentence is:" + str(checking))


# In[35]:


#checking to see if the string entered has special characters or not 
import re 
def check_specialty(string): 
  
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
    if(regex.search(string) == None): 
        print("You do not have a special character") 
          
    else: 
        print("You have a special character") 
if __name__ == '__main__' : 
      
     
    string = input("Check for special characters ")
      
   
    check_specialty(string) 


# In[37]:


import re 
def check_specialty(string): 
  
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
    if(regex.search(string) == None): 
        print("You do not have a special character") 
          
    else: 
        print("You have a special character") 
if __name__ == '__main__' : 
      
     
    string = input("Check for special characters ")
      
   
    check_specialty(string) 


# In[ ]:





# In[69]:


#Checking to see if my password is valid or not 
def check_passWords(string):
    SCharacters = ['@', '#', '&', '*', '%', '$']
    
    if len(string) < 4:
        print('Password should atleast be more that 4 characters, please try again')
        
    if len(string) > 15:
        print('Your password should not exceed more that 14 characters, please try again ')
        
        
    if not any(char.isdigit() for char in string):
        print('Password should atleast contain one numeric digit')
        
        
    if not any(char.isupper() for char in string):
        print('Password should at least have one Uppercase character')
        
        
    if not any(char in SCharacters for char in string):
        print('Password should atleast contain one special character @,#,$,%,*,&')
        
    
def main():
    
    string = input('Enter your password ')
    
    if (check_passWords(string)):
        print('Password accepted')
        print(string)
    elif (string):
        print('Password is not accepted')
        
    

main()


# In[68]:


#Checking to see if my password is valid or not 
def check_passWords(string):
    SCharacters = ['@', '#', '&', '*', '%', '$']
    
    if len(string) < 4:
        print('Password should atleast be more that 4 characters, please try again')
        
    if len(string) > 15:
        print('Your password should not exceed more that 14 characters, please try again ')
        
        
    if not any(char.isdigit() for char in string):
        print('Password should atleast contain one numeric digit')
        
        
    if not any(char.isupper() for char in string):
        print('Password should at least have one Uppercase character')
        
        
    if not any(char in SCharacters for char in string):
        print('Password should atleast contain one special character @,#,$,%,*,&')
        
    
def main():
    
    string = input('Enter your password ')
    
    if (check_passWords(string)):
        print('Password accepted')
        print(string)
    elif (string):
        print('Password is not accepted')
        
    

main()


# In[ ]:





# In[66]:


name = input('What is your name   ')

if len(name) < 4:
    print('Wow your name is short')
else:
    print('Gotta pretty long name')
    
if len(name) > 20:
    print('your name is too long for out system SORRY')
else:
    print('Thanks for participating')


# In[67]:


name = input('What is your name   ')

if len(name) < 4:
    print('Wow your name is short')
else:
    print('Gotta pretty long name')
    
if len(name) > 20:
    print('your name is too long for out system SORRY')
else:
    print('Thanks for participating')


# In[ ]:




