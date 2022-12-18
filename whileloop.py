i = 1

while i <= 1000:
    if (i % 10 == 0):
        print(f"{i:03}")
    else:
        print(f"{i:03}", end=" ")
    i = i + 1

# Infinity Loop
r = 1
while True:
    if (r <= 20):
        print(r, "OK")
    else:
        break
    r = r + 1
