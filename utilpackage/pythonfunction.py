# สร้างฟังก์ชันแบบไม่มี return และไม่ีมีการรับค่าเข้าไป
def hello():
    print("Hello Python")


# เรียกใช้งานฟังก์ชันที่สร้างไว้
hello()


# สร้างฟังก์ชันแบบมีการรับค่า
def info(msg):
    print("Welcome to", msg)


# เรียกใช้งานฟังก์ชัน info(msg)
info("ITGenius")


# สร้างฟังก์ชันแบบมีการรับค่าและมี return ค่าออกไปใช้งาน
def area(width, height):
    return width * height


# เรียกใช้งานฟังก์ชัน area
print("Area of room is", area(10, 20), "sqm.")


# สร้างฟังก์ชันที่มีการกำหนดค่าเริ่มต้นให้ argument
def show_info(name="", salary=0, lang=""):
    print("Name:", name)
    print("Salary:", salary)
    print("Language:", lang)


# เรียกใช้งานฟังก์ชัน show_info
show_info()
print("-----------------")
show_info("Samit")
print("-----------------")
show_info("Samit", 100000, "C++")
