# ✅ 3. Tablas de multiplicar del 1 al 5
# Enunciado:
# Haz un programa que muestre las tablas de multiplicar del 1 al 5. Cada tabla debe ir del 1 al 10.

# Recorre del 1 al 5 (las tablas)
for numer in range(1, 6):
    print(f"Tabla del {numer}:")
    
    # Recorre del 1 al 10 (los multiplicadores)
    for i in range(1, 11):
        resultado = i * numer
        print(f"{numer} x {i} = {resultado}")
