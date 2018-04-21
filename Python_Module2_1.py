
# coding: utf-8

# In[2]:


input_string = input("Please enter a comma separated sequence of values: ")
output_list = []
for s in input_string.split(','):
    output_list.append(s)
    
print(output_list)    

