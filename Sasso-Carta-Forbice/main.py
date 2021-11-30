import random

## v1: solo una scelta (senza loop)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listaScelte = [paper, rock, scissors]
user_choice = int(input("Scegliere CARTA(0), SASSO(1), FORBICE(2): "))
computer_choice = random.randint(0,2)

if(user_choice == 0 or user_choice == 1 or user_choice == 2):
  if(user_choice == computer_choice):
    result = "PAREGGIO!"
  elif(user_choice == 0):
    if(computer_choice == 1):
      result = "VINTO!"
    else:
      result = "PERSO!"
  elif(user_choice == 1):
    if(computer_choice == 0):
      result = "PERSO!"
    else:
      result = "VINTO!"
  elif(user_choice == 2):
    if(computer_choice == 0):
      result = "VINTO!"
    else:
      result = "PERSO!"

  print("\n-----------"+"\nUTENTE\n"+listaScelte[user_choice]+"\n-----------"+"\nCOMPUTER\n"+listaScelte[computer_choice]+"\n-----------\n"+result+"\n-----------")
else:
  result = "PERSO!"
  print("Non hai scelto un'opzione valida tra quelle disponibili (0,1,2).\n-----------\n"+result+"\n-----------")




