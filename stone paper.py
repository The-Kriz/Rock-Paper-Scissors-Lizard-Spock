def rock():
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
\n""")

def paper():
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
\n""")

def scissors():
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
\n""")

def lizard():
    print("""
    .----------,
   /   .-----, _\ 
  /    `-----'  /
 /     .-------'
/    .'
    /
\n""")
def spock():
    print("""
  _
 (>\       _
(>\ \     /<)
 \ \ \   / /
  \ \ \ / /<)
   \_\_V_/ /
  / )    `-|
 | | `--   |
 |     ||  |
 \     '   /
  |       |
  |       | \n""")

def victory():
    print("""   
██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗
██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝
╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚████╔╝░
░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░
░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")

def over():
    print("""   
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
""")

import random
print("1 : stone \n2 : paper\n3 : scissors\n4 : lizard\n5 : spock\n")
j=0
k=0
n=0
while n!=100: 
  a=random.randint(1, 5)
  b=int(input("Enter your move "))
  if b==1:
      print("stone")
      rock()
  elif b==2:
      print("paper")
      paper()
  elif b==3:
      print("scissors")
      scissors()
  elif b==4:
      print("lizard")
      lizard()
  elif b==5:
      print("spock")
      spock()
  else :
      print("wrong entry")

    
  if(a==b):
    if a==1:
      print("stone")
      rock()
    elif a==2:
      print("paper")
      paper()
    elif a==3:
      print("scissors")
      scissors()
    elif a==4:
      print("lizard")
      lizard()
    elif a==5:
      print("spock")
      spock()
    else :
      print("wrong entry")
    print("draw\n")
    
  elif((a==1 and b==2 ) or (a==2 and b==3 ) or (a==3 and b==1 ) or (a==1 and b==5 ) or (a==2 and b==5 ) or (a==3 and b==5 )or (a==4 and b==1 ) or (a==4 and b==3 ) or (a==5 and b==2 )or (a==5 and b==4 )):
    j=j+1
    if a==1:
      print("stone")
      rock()
    elif a==2:
      print("paper")
      paper()
    elif a==3:
      print("scissors")
      scissors()
    elif a==4:
      print("lizard")
      lizard()
    else:
      print("spock")
      spock()
    print("you won\n")
  elif ((a==2 and b==1 ) or (a==3 and b==2 ) or (a==1 and b==3 )or (a==1 and b==4 ) or (a==2 and b==4 ) or (a==3 and b==4 )or (a==4 and b==2 ) or (a==4 and b==5 ) or (a==5 and b==1 )or (a==5 and b==3 )):
    k=k+1
    if a==1:
      print("stone")
      rock()
    elif a==2:
      print("paper")
      paper()
    elif a==3:
      print("scissors")
      scissors()
    elif a==4:
      print("lizard")
      lizard()
    else:
      print("spock")
      spock()
    print("you lost\n")
  else:
    
    print("wrong input\n") 
  if j==3 :
    n=100
    print("\n\n\nyou won the game!!")
    victory()

  elif k==3 : 
    n=100
    print("\n\n\nyou lost the game!!!")
    over()
