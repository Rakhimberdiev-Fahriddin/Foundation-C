son = int(input(">>> : "))
lst = list()
while son:
    b = son % 10
    son //= 10
    lst.append(b)

for i in range(len(lst),0,-1):
    if i == 1:
        print(lst[i-1] * (10 **(i-1)))
    else :
        print(lst[i-1] * (10 **(i-1)),"+", end = " ")
