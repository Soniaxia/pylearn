my_list = []

for i in range(1,101):
    if i%3==0 and i%5==0:
        my_list.append("FizzBuzz")
    elif i%3==0:
        my_list.append("Fizz")
    elif i%5==0:
        my_list.append("Buzz")
    else:
        my_list.append(i)

print(my_list)

def total_fizz(my_list):
    total=0
    for i in my_list:
        if i == "Fizz":
            total=total+1
    return total

print(total_fizz(my_list))


for letter in "testup测试进阶":
    print(letter)