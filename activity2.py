#Input a word or sentence
string = input("Please enter your own String : ")

string2 = ('')
#loop for printing in reverse 
for i in string:
    string2 = i + string2
string2 = string2.capitalize()
print("\nThe original string = ", string)
print("The Reversed String = ", string2)