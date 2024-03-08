i = 0
my_list = []
while i<5:
    my_list.append(int(input("ingrese un valor: ")))
    i+=1
my_list.sort(reverse=True)
print(my_list)