# print("hello python")
flag = False

a = 1
b = 2
c = 3
if a or b + 1 != c:
    print("1")
else:
    print("2")
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
account = 'xtyghost'
password = 123456
print("please input account")
user_account = input()
print("please input password")
user_password = input()
print("user_account== %s ; user_account= %s \n" % ( user_password, user_account))
if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
