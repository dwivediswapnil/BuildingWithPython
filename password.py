# password = input("Enter the password ")
# while password!="pass123":
#     password = input("Enter the password ")
# print("password was correct ")   
# -------------------------------- 
# Create a program that prompts the user to input 
# their name once. Then, the program repeatedly 
# prints out the name with the first letter capitalized.
# name = input("Enter the input: ")
# while True:
#     print(name.capitalize())
#-----------------------------------
# name = input("What is your name? ")
# while True:
#     name = input("What is your name? ")
#     print(name.capitalize())
#-------------------------------------
# todos=[]
# while True:
#     user_action = input("Type add or show: ")

#     match user_action:
#         case 'add':
#             todo = input("Enter a todo:")
#             todos.append(todo)
#         case 'show'|'display': #OR operator
#             for item in todos:
#                 print(item.title())
#         case 'exit':
#             break   
#         case whatever: 
#             print("Hey you have entered an uknown command")

# print("Bye")            
#----------------------------------------
# meals = ['pasta','pizza','salad']
# for meal in 'meals':
#     print(meal.capitalize())
#----------------------------------------
# filenames = ["1.RawData.txt","2.Reports.txt","3.Presentations.txt"]
# for filename in filenames:
#     filename = filename.replace(".","-",1)
#     print(filename)
#--------------------------------------------
# todos=[]
# while True:
#     user_action = input("Type add ,show,edit,complete or exit: ")

#     match user_action:
#         case 'add':
#             todo = input("Enter a todo:")
#             todos.append(todo)
#         case 'show':
#             for index,item in enumerate(todos):
#                 # print(index,"-",item) #spaces are printed when we use print function
#                 print(f'{index +1}-{item}')
#             print("Hello",index,item)
#         case 'edit':
#             number = int(input("Number of the todo to edit: ")) 
#             number = number -1
#             new_todo = input("Enter new todo: ") 
#             todos[number] = new_todo    
#         case 'complete':
#             number = int(input("Number of the todo to complete: "))    
#             todos.pop(number-1)  
#         case 'exit':
#             break   
#         case whatever: 
#             print("Hey you have entered an uknown command")

# print("Bye")            
#--------------------------------------------------------------------------------------
# a=enumerate(["a","b","c"])
# # print(list(a))
# for i,item in list(a):
#     print(i,item)
#-------------------------------------------------------------------------------------
# waiting_list = ["sen","ben","john"]
# waiting_list.sort(reverse=True)
# for index, item in enumerate(waiting_list):
#     row = f"{index+1}.{item.capitalize()}"
#     print(row)
#------------------------------------------------------------------------------------
# Storing data in text files
while True:
    user_action = input("Type add ,show,edit,complete or exit: ")

    match user_action:
        case 'add':
            todo = input("Enter a todo:") + "\n"
            file = open('todos.txt','r')
            todos= file.readlines()
            file.close()
            #reading the file
            file = open("todos.txt",'r')
            todos.append(todo)
            #writing in the file 
            file = open("todos.txt",'w')
            file.writelines(todos)

        case 'show':
            for index,item in enumerate(todos):
                # print(index,"-",item) #spaces are printed when we use print function
                print(f'{index +1}-{item}')
            print("Hello",index,item)
        case 'edit':
            number = int(input("Number of the todo to edit: ")) 
            number = number -1
            new_todo = input("Enter new todo: ") 
            todos[number] = new_todo    
        case 'complete':
            number = int(input("Number of the todo to complete: "))    
            todos.pop(number-1)  
        case 'exit':
            break   
        case whatever: 
            print("Hey you have entered an uknown command")

   