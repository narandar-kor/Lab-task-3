numbers = []

for i in range(1,11):
    number = int(input(f"Enter {i} positive number : "))
    numbers.append(number)

sum = 0
smallest = numbers[0]
largest = 0
even = 0
odd = 0

for i in numbers:
    sum += i 

    if i>0:
        largest=i

    if i < smallest:
        smallest = i

    if i%2 == 0:
        even += 1
    else:
        odd += 1


average = sum/10

print("\n <<<<<<<<<<- Calculation ->>>>>>>>>>\n")
print(f"Sum of number is : {sum}")
print(f"average of number is : {average}")
print(f"largerst number is : {largest}")
print(f"Smallest number is : {smallest}")
print(f"total even number is : {even}")
print(f"total odd number is : {odd}")

