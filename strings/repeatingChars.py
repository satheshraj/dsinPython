from collections import Counter
import sys

inputText = input("Enter input string:")

cnter = Counter(inputText)

#print(f"cnter ={cnter}")
#print(f"type of cnter is {type(cnter)}")

for char, cnt in cnter.items():
    if(cnt > 1):
        print(f"Repeating chars are {char}")
        #sys.exit(0)





