# การสร้างตัวแปรใน python ไม่ต้องระบุชนิดข้อมูล
a = 3
b = 4.958
c = "Python Programming"

# print(a)
# print(b+20)
# print(c)

print(a, b+20, c)

x = y = z = 10

print(x, y, z)

j, k, m = 5, 10, 15

print(j, k, m)

# Boolean
status = True  # 1
msg = False  # 0

print(status, msg)

print(status == 1)
print(msg == 0)

# การแสดงข้อความร่วมกับตัวแปร
print("Product price", "{:.2f}".format(b), "baht")
print("Product price %.2f baht" % b)
print(f"Product price {b:.2f} baht")
