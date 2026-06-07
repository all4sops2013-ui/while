# Write a program to print the numbers in reverse order beginning from the number entered by the user.

num = int(input("Enter a number: "))
for i in range(1,9,1):
    num = num - 1
    print(num)



i=1
while i<=14:
    print(i)
    i+=1
print('Done !!')



# WAP to take a number from the user and print the number of digits in that number using a while loop

num = int(input("Enter a number: "))
count = 0
while num!= 0:
    num=num//10
    count=count+1
print(count)


# task 1

#Write a program that:Takes a positive integer input from the user.
#Uses a while loop to find the sum of its digits.Displays the final sum.Example: Input: 5837 
#Calculation: 5 + 8 + 3 + 7 = 23 .Output: Sum of digits = 23 .Hint: Use % 10 and // 10.

num = int(input("Enter a number: "))
count = 0
sum = 0
t = 0
while num!= 0:
    t=num%10
    sum=sum+t
    num=num//10
    count=count+1
print(count)
print(sum)