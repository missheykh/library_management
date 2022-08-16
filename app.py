from controllers import SignUp

print("""

**************************
  Welcome To Library ...
**************************

""")
while True:
  try:
    y_n_que=input("do you already registerd?(y/n)")
    if y_n_que=="n":
        print("Ok! we will do together just now!")
        username=input("please enter an username:")
        password=input("and enter your password:")
        p=SignUp(_username=username,_password=password)
        print(f"p:{p}")
  except Exception as error:
    print(error)

