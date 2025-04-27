# ✅ 6. Juego: Adivina el número
# Enunciado:
# Escribe un programa que pida al usuario adivinar un número secreto entre 1 y 10. 
# El juego se repite hasta que adivine correctamente.



# Número secreto
numero_secreto = 7

# Pedimos al usuario por primera vez
adivinanza = int(input("Adivina un número entre 1 y 10: "))

# Mientras el número no sea el correcto
while adivinanza != numero_secreto:
    print("¡No adivinaste! Intenta de nuevo.")
    adivinanza = int(input("Adivina un número entre 1 y 10: "))

# Cuando adivina
print("🎉 ¡Felicidades! Adivinaste el número.")