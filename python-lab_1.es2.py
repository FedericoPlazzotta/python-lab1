print("Please insert the string you want to process: ")
string=input()
if (len(string)<4):
    print("ERROR. the string must be at least 4 characters long. Please digit another string.")
else:
    new_string=string[0]+string[1]+string[len(string)-2:]
    print("the new string is ", new_string)