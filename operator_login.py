# import keyword
# print(keyword.kwlist)
# เขียนโปรแกรมรับ username และ password
username = input("Enter username: ")
password = input("Enter password: ")

print(type(username))
print(type(password))

print(int(password)+5)

# เขียนเงื่อนไขตรวจว่าป้อน username และ password ตรงตามที่กำหนดหรือไม่
if (username == "admin" and password == "1234"):
    print("Login Success")
else:
    print("Login Fail")
