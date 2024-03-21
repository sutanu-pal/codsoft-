import random
import string 
 

def genpass( length=12):
    characters= string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "_main_":
  password_length = 12
try:
  password_length= int(input(" enter desired password length (default is 12)"))

except ValueError:
  print(" invalid input. using password lenght as 12")

if password_length <= 0:
  print("password lenght should be greater than 0. using password length as 12")
  password_length=12

gen_pass= genpass(password_length)
print("Generated password:", gen_pass)

