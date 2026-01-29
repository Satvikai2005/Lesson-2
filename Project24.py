import random
import string

all_character = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(all_character) for i in range(12))

print(password)

