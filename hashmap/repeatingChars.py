from ftplib import print_line


def findPrintDuplicates(inputText):

    RepeatHashMap = {}

    for iter in inputText:
        RepeatHashMap[iter] = RepeatHashMap.get(iter,0) + 1


    #for keys in RepeatHashMap:
        #print(f"{keys}:{RepeatHashMap[keys]}")

    for keys in RepeatHashMap:
        if RepeatHashMap[keys] > 1:
            #print(["{}".format(keys), RepeatHashMap[keys]], end=", ")
            print(f"\nkeys= {keys}, RepeatHashMap[keys] = {RepeatHashMap[keys]},")





if __name__ == "__main__":
    inputText=input("Enter the input string")
    findPrintDuplicates(inputText.lower())