import pandas as pd

#Nested dictionary sample

Employee={
    'Sathesh':{'Id':'100','Name':'Sathesh','DOB':'1991'},
    'Raj':{'Id':'101','Name':'Raj','DOB':'1991'}
}

print(Employee)
print(type(Employee))

# Accessing elements
print(Employee['Sathesh']['Id'])

# Updating elements
Employee['Sathesh']['Id'] = 1001
print(Employee['Sathesh']['Id'])

# Deleting
# Employee['Sathesh'].pop('Id')
# Employee['Sathesh'].popitem()
del Employee['Sathesh']['Id']

print(Employee['Sathesh'])

# Convert to dataframes

df = pd.DataFrame(Employee)
print(df)




