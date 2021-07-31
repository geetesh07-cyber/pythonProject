#build a calculator
#vanvert string to title
# def format_name(f_name,l_name):
#    f_name =  f_name.title()
#    l_name =  l_name.title()
#    result = f_name + l_name
#    return result
# print(format_name("HII ","ii"))

#i think i can make calculator by mysel

def calculator(a,b,operator):
    a = int(a)
    b = int(b)
    if operator == "add":
        return a+b
    elif operator == "subtract":
        return a-b
    elif operator == "multiply":
        return a*b
    elif operator == "divide":
        return a/b
    else:
        return a%b
condition = True
while condition ==True:
    first_number = int(input("Give first number \n"))
    second_number = int(input("Give second number \n"))
    operator = input("What do you want to do? \n")
    print(calculator(first_number,second_number,operator))
    u = input(" DO YOU WANT TO USE THE CALCULATOR AGAIN \n")
    if u == "no":
        condition = False
        print("GOOD BYE")
