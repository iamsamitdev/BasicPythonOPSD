for i in range(1, 1001):
    if (i % 10 == 0):
        print(f"{i:03}")
    else:
        print(f"{i:03}", end=" ")
# Infinity Loop
r = 1
while True:
    if (r <= 20):
        print(r, "OK")
    else:
        break
    r = r + 1
