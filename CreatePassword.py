import secrets
import string

numero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
especiales = ['#', '[', ']', '(', ')', '@', '$', '&', '*', '!', '?', '/', ',', '.', '+', '_', '-', '^']
alfabeto = string.ascii_letters + ''.join(numero) + ''.join(especiales)

password = [
    secrets.choice(especiales),
    secrets.choice(numero),
    secrets.choice(string.ascii_uppercase),
    secrets.choice(string.ascii_lowercase)
]

for _ in range(15 - len(password)):
    password.append(secrets.choice(alfabeto))

secrets.SystemRandom().shuffle(password)
final_password = ''.join(password)
print(final_password)
