import random
import os

lc = "abcdefghijklmnop"
uc = "ABCDEFGHIJKLMNOP"
pc = ",.<>;:/?][()*!@#$%^&"
nm = "1234567890"

print("How long do you want your password?")
x = int(input())
os.system('cls' if os.name == 'nt' else "printf '\033c'")

all = lc + uc + pc + nm

length = (x)
password = "".join(random.sample(all, length))

print(password)
