import manager_prompt
import sales_prompt
import Plants_prompt
import Customers_prompt

while(True) :
  print("Welcome to  my botanic garden, the best nursery in your town next to your home. \n Please login using your id and password below.")
  print("MENU")
  id = input(' If you are a manager, enter using manager01, if you are admin, enter admin credentials and if you are employee, please enter using your employee id. enter quit to exit. \n please enter your id : ')
  password = input("Enter your password : ")
  try :
    if (id == "manager01" and password == "OnlyManage01") :
      manager_prompt.manage()
    elif (id is "quit") :
      print("Good Bye!")
      break
    elif (int(id) >= 1 and int(id) <= 10 and password == "OnlySell01") :
      while (True):  
          operation = input('If you want to maintain plants or customers, enter P or C rescpectively. If you want to sell plant, enter S, Enter Q for Quit :')
          if (operation in "P"):
            Plants_prompt.entry()
          elif (operation in "C"):
            Customers_prompt.entry()
          elif (operation in "S"):
            sales_prompt.sell(int(id))
          elif (operation in "Q"):
            print("you are reentering the login screen ")
            break
          else:
            print("Please enter valid value : P/C/S")
            continue
    else :
      print("Please enter valid option or enter correct id and password")
      continue
  except ValueError :
    continue
    
