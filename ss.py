num1 = int(input('num1: '))
num2 = int(input('num2: '))
num3 = int(input('num3: '))
li = []
li.append(num1)
li.append(num2)
li.append(num3)
if li[0] < li[1] < li[2]:
    print(f"Самое большое число: {li[1]} ")
    print(li[0])
    print(li[1])
    print(li[2])
