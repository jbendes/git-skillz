import time;

i = 0
while i < 5:
    print("Churning....")
    i = i + 1
    time.sleep(0.5)
i = 0
while i < 1000:
    print(".", end="")
    i = i + 1
print("Churned!")
