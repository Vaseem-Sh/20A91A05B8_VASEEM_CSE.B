#While loop


initial_value=int(input('Enter the start value '))
ending_value=int(input('Enter the end value '))
stepcount=int(input('Enter the stepcount value '))

while (initial_value<=ending_value):

    
 print(initial_value, end=" ")
 initial_value=initial_value+stepcount

print('After the end of loop, the value is ' , initial_value)
print('After the end of loop, the value is {}'.format(initial_value))

#output :

Enter the start value 10
Enter the end value 20
Enter the stepcount value 2
10 12 14 16 18 20 After the end of loop, the value is  22
After the end of loop, the value is 22
