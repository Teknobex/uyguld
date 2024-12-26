import random

characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Kaç karakterlik bir şifre olsun?"))

password = ""

for i in range(length):
    password += random.choice(characters)
print(password)