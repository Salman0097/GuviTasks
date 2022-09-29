import re
usr_details = open("C:\\Users\\ibrah\\PycharmProjects\\User_Details.txt", "r")
def register():
    # User_details
    #usr_details = open("C:\\Users\\ibrah\\PycharmProjects\\User_Details.txt", "r")


    # mail id
    email = input("Enter the new mail id : ")
    specialCharacter = '~`!@#$%^&*()_+[]{}-=|\";:/><?.,'
    flag = 0
    for each in specialCharacter:
        if each == email[0]:
            flag = 1
    d = re.findall("^\d", email)
    if d != []:
        flag = 1
    a = re.findall(".+@\.[a-z]", email)
    if a != []:
        flag = 1
    if flag == 0:
        l = re.findall(".+@.+.\.[a-z]", email)
        if l != []:
            # print(l)
            print("Email Id is valid !, Please enter password")

    else:
        print("Invalid")
    # password
    pattern = re.compile(r'')
    while True:
        password = input("Enter the password : ")

        if len(password) <= 6:
            print("Password is too short, Enter again")
        elif len(password) > 16:
            print("Password too long, Enter again")
        elif re.search(r'[!@#$%&]', password) is None:
            print("Password must contain atleast one special character, Enter again")
        elif re.search(r'\d', password) is None:
            print("Password must contain atleast one digit, Enter again")
        elif re.search(r'[A-Z]', password) is None:
            print("password must have atleast one Capital letter, Enter again")
        elif re.match(r'[a-z A-Z 0-9 !@#$%&]{6,16}', password):
            pattern = re.match(r'[a-z A-Z 0-9 !@#$%&]{6,16}', password)
            pattern.re.match(password)
            print("Valid password")
            break
        else:
            print("Invalid password")
    usrnme = []
    pswrd = []
    for i in usr_details:
        a, b = i.split(",")
        b = b.strip()
        #c = a, b
        usrnme.append(a)
        pswrd.append(b)
        data = dict(zip(usrnme, pswrd))
        #print(data)
        if email in usrnme:
            print("Email already exists, Please Login")
            login()
        else:
            usr_details = open("C:\\Users\\ibrah\\PycharmProjects\\User_Details.txt", "a")
            usr_details.write(email + ', ' + password + '\n')
            print("Registration Success!!")

def login():
    email = input("Enter the mail id : ")

    usrnme = []
    pswrd = []
    for i in usr_details:
        a, b = i.split(",")
        b = b.strip()
        #c = a, b
        usrnme.append(a)
        pswrd.append(b)
        data = dict(zip(usrnme, pswrd))
        #print(data)
        if email in usrnme:
            password = input("Enter the password : ")
            if password in pswrd:
                print("Logged in successfully")
                break
            else:
                print("Enter the correct password")



def chooseOption():
    option = input("Login | Register ")
    option = option.upper()
    if option == "LOGIN":
        login()

    if option == "REGISTER":
        register()


chooseOption()
