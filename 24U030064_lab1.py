#print( " Enter your marks: ")

while 1: # this will run infinitely till loop breaks ( to ask user to enter number repeatedly)
 marks = input(" Enter your marks: ") # it will take marks and store as string 
 
 if marks.lower() == "exit": # it ensure that exit will written in lower case only to exit the program
   print("teminated:") 
   break # to break if user enter "exit"

 elif marks.isnumeric():  # it will ensure that input value is  numerical only 
    k= int(marks)    # we convert the string to integer part to compare with numerical values 

    if k>=90 and k<=100:
                print(" grade is A ")

    elif k>=75 and k<=89:
                print(" grade is B ")

    elif k>=60 and k<=74:
                print(" grade is C ")

    elif k>=40 and k<=59:
                print(" grade is D ")

    elif k<=40:
                print(" grade is F ")

    else :
                print(" enter valid marks ") 

 else:
    print(" invalid output ")
