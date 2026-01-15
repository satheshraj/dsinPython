import pandas as pd

#Nested dictionary sample

Employee={
    'Sathesh':{'Id':'100','Name':'Sathesh','DOB':'1991'},
    'Raj':{'Id':'101','Name':'Raj','DOB':'1991'}
}

print(Employee)


# Convert to dataframes

df = pd.DataFrame(Employee)
print(df)




