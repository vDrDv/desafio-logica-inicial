import random

heroi = input("Digite onome do seu HERÓI: ")

while not heroi:
    heroi = input("Por favor, digite o nome do seu HERÓI: ")

xp = random.randint(1000, 18001) 

if xp <= 1000:
    nivel = "Ferro"
elif xp >= 1001 and xp < 2001:
    nivel = "Bronze"
elif xp >= 2001 and xp < 5001:
    nivel = "Prata"
elif xp >= 5001 and xp < 6001:
    nivel = "Quase OURO"
elif xp >= 6001 and xp < 7001:
    nivel = "Ouro"
elif xp >= 7001 and xp < 8001:
    nivel = "Platina"
elif xp >= 8001 and xp < 9001:
    nivel = "Ascendente"
elif xp >= 9001 and xp < 10001:
    nivel = "Imortal"
elif xp >= 10001:
    nivel = "Radiante"

print("O Herói de nome " + heroi + " esta no nível de " + nivel + ". Com uma experiência total de: " + str(xp) + ".")


