print("The rules for setting the password are")
print("1.The minimum length of password should be 5(included) characters")
print("2.The maximun length of password should be 12(included) characters")
print("3.The password can consists of lowercase and uppercase letters,digits and special symbols(@,$)")
password = input("Enter Password : ")
lower_count, upper_count, num_count,special_count = 0,0,0,0
if(len(password) >= 5 and len(password) <= 12):
    for i in password:
        if(i == '@' or i == '$'):
            special_count = 1
        elif(i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
            num_count = 1
        elif(i >= 'A' and i <= 'Z'):
            upper_count = 1
        elif(i >= 'a' and i <= 'z'):
            lower_count = 1
total_count = num_count + special_count + lower_count + upper_count
if(total_count == 0):
    print("The password should contain minimum 5 characters and maximum 12 characters")
elif(total_count == 1):
    print("The password is very weak")
elif(total_count == 2):
    print("The password is weak")
elif(total_count == 3):
    print("The password is strong")
elif(total_count == 4):
    print("The password is very strong")
print("This is end of program")   