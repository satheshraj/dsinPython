#Approach explanation

# Get the input string and convert it to set ( as set removes duplicates)
# then comparing the string length with set length.
# If set length is not same as input text length , then it has duplicate chars 

inputtedText = input("Enter the string to be checked")

input_to_set = set(inputtedText)

if len(inputtedText) == len(input_to_set):
    print(f"String '{inputtedText}' has all unique characters")
else:
    print(f"String '{inputtedText}' has duplicate chars")




