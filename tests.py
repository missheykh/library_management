import pickle
import os
from models import BaseUser,Admin,Member,Book
import settings
# from db import QueryUsers
# admin_user2=Admin('sara','12345')
# member_user2=Member('reza','12345678910')

# admin_user2.save()
# member_user2.save()
 
# print(admin_user1.username,admin_user1.password)
# print(member_user1.username,member_user1.password)


# items=load(settings.USER_DATA_PATH/"users.db")
# print(items)
# for i in items:
#     print(i.username)
#     print(i.password)


# try:
#     f=open('salaam.txt','r')
#     print(f.read())
#     # f.write('first line\n')
#     # f.write('second line\n')
# except Exception as e:
#     print(e)

# finally:
#     f.close()
#     print("the file closed")

# try:
#     os.remove('salaam.txt')
# except Exception as e:
#     print(e)

# if os.path.exists('salam.txt'):
#     os.remove('salam.txt')
# else:
#     raise BaseException('not exist')

# def fib(limit):
#     a,b=0,1
#     return a
#     while b<limit:
#         a,b=b,a+b
#         return a

# # for elm in fib(10):
# #     print(elm)

# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)



# def fib(n):
#     return 1 if n<=2 else fib(n-1)+fib(n-2)


# print(fib(4))

# a=QueryUsers()
# items=a.loadall()
# for i in items:
#     print(i.username,i.password)


# for elm in Member.query.loadall():
#     print(elm.username)




# book_obj_1=Book(name='jang va solh',author='tolstoy')
# book_obj_2=Book(name='اما',author='جین آستین')

# book_obj_1.save()
# book_obj_2.save()

# for elm in Book.query.loadall():
#     print(elm.name)

# print(Admin.query.exist("username","mina"))