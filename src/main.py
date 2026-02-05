import mymodule 


num1=int(input("Enter an value"))
num2=int(input("Enter an another value"))

sum_of_number=mymodule.add(num1, num2)
difference=mymodule.subtract(num1, num2)
product=mymodule.multiply(num1, num2)

print("Sum of the two number are:", sum_of_number)

print("Difference of the number:", difference)

print("Product of two numbers:", product)

numerator=int(input("Enter an value"))
denominator=int(input("Enter another value"))

divison=mymodule.divison(numerator, denominator)

print("Divison of two numbers:", divison)


