import random

heroi = input("Digite onome do seu HERÓI: ")

while not heroi:
    heroi = input("Por favor, digite o nome do seu HERÓI: ")

xp = random.randint(1000, 18001) 

# Se a XP for menor do que 1.000 = Ferro
if xp <= 1000:
    nivel = "Ferro"

# Se a XP estiver entre 1.001 e 2.000 = Bronze
elif xp >= 1001 and xp < 2001:
    nivel = "Bronze"

# Se a XP estiver entre 2.001 e 5.000 = Prata
elif xp >= 2001 and xp < 5001:
    nivel = "Prata"

# Se a XP estiver entre 6.001 e 7.000 = Quase Ouro
elif xp >= 5001 and xp < 6001:
    nivel = "Quase OURO"

# Se a XP estiver entre 6.001 e 7.000 = Ouro
elif xp >= 6001 and xp < 7001:
    nivel = "Ouro"

# Se a XP estiver entre 7.001 e 8.000 = Platina
elif xp >= 7001 and xp < 8001:
    nivel = "Platina"

# Se a XP estiver entre 8.001 e 9.000 = Ascendente
elif xp >= 8001 and xp < 9001:
    nivel = "Ascendente"

# Se a XP estiver entre 9.001 e 10.000 = Imortal
elif xp >= 9001 and xp < 10001:
    nivel = "Imortal"
else: 
    xp >= 10001
    nivel = "Radiante"

print("O Herói de nome " + heroi + " esta no nível de " + nivel + ". Com uma experiência total de: " + str(xp) + ".")


