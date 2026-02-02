print("Enter A Choice (1-5)")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Exit.....:)")
ip=int(input("enter choice :"))
num1=int(input("Enter num1 :"))
num2=int(input("Enter num2 :"))


match ip:
    
    
    case 1:
        print(num1+num2)
    case 2:
        print(num1-num2)
    case 3:
        print(num1*num2)
    case 4:
        # if(num2==0|){
        #     print(Division by zero not possible)
        # }else{
            print(num1/num2)
    case 5:
        print("exiting....")
    case _:
        print("Invalid Choice")