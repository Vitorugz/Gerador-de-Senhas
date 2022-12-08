import random

minusculas = 'abcdefghijklmnopqrstuvwxyz'
maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '@#$%*/\?'

Use_for = minusculas + maiusculas + numeros + simbolos
tamanha_da_senha = 8

password = "".join(random.sample(Use_for, tamanha_da_senha))

print("Sua senha gerada é: ", password) 
