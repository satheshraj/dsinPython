input_string = "Sathesh"
input_string_lst = list(input_string)
rev_lst = ""

while input_string_lst:
    rev_lst += input_string_lst.pop()

print(rev_lst)

print(input_string[::-1])