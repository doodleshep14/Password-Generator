import random
import string

characters = string.ascii_letters + string.digits + string.punctuation

length = int(input("How long do you want your password to be? "))

password = ""

for i in range(length):
  password += random.choice(characters)

password = "".join(random.sample(password, len(password)))

print(password)