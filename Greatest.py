a = int(input('Enter the first number :'))
b = int(input('Enter the second number :'))
c = int(input('Enter the third number :')) 

largest = 0

if a>b and a>c :
    largest = a

    if b>a and b>c :
     largest = b 

     if c>a and c>b :
      largest = c

      print(largest,"is the largest of three numbers.")

