string_1 = input()
string_2 = input()

list_str_1 = list(string_1)
list_str_2 = list(string_2)

length = len(list_str_1)

for i in range(length):
    if list_str_1[i] != list_str_2[i]:
        temp = list_str_2[i +1]
        list_str_2[i+1] = list_str_2[i]
        list_str_2[i] = temp
        break
    
if list_str_1 == list_str_2:
    print("Yes")
else:
    print("No")
        
