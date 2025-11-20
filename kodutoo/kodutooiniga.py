#4
for i in range(10, 20):
    print(i * i)

#5
result = 0
while True:
    try:
        num = input("Enter a number, if you want to stop enter Stop: ")
        if num == "stop" or num == "Stop":
            print(f"Result: {result}")
            break
        elif int(num) < 0:
            result += int(num)
        elif int(num) >= 1:
            continue
    except:
        print("Error, please enter a number")

#6
negative = 0
positive = 0
zero = 0

while True:
    try:
        number = input("Enter a number, if you want to stop enter Stop: ")
        if number == "stop" or number == "Stop":
            print("Negatives:", negative)
            print("Positives:", positive)
            print("Zeros:", zero)
            break
        elif int(number) > 0:
            positive += 1
            continue
        elif int(number) < 0:
            negative += 1
            continue
        elif int(number) == 0:
            zero += 1
            continue
    except:
        print("Error, please enter a number!")

#7

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
k = int(input("Enter the number u need it divided by: "))

if a <= b:
    for i in range(a, b + 1):
        if i % k == 0:
            print(i)
else:
    for i in range(a, b - 1, -1):
        if i % k == 0:
            print(i)
#8
cm = 1
toll = 2.5
counts = 1

while True:
    print(cm, "cm =", toll, "tolli")
    toll += 2.5
    cm+= 1
    counts += 1
    if counts == 21:
        break
    else:
        continue