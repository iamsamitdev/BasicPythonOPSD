import time

num = 0
count = 1

while True:
    if num == 1:
        print(f"Round {count} = {num}")
        num = 0
    else:
        print(f"Round {count} = {num}")
        num = 1

    # เมื่อครบ 20 รอบให้หยุดทำงาน
    if count == 20:
        break

    # เพิ่มรอบ
    count = count + 1

    # ครบ 1 รอบทำการ sleep 1 วินาที
    time.sleep(1)
