
# ✅ 5. Verificación de contraseña
# Enunciado:
# Crea un sistema que pida al usuario una contraseña.
# Si no la acierta, podrá intentarlo hasta 3 veces. Si falla, muestra un mensaje de acceso bloqueado.

Credencial_Corecta = "Pilas"

attempts = 3
while attempts < 0:
    password = input("Ingrese la contraseña:")
    if Credencial_Corecta == password:
        print("Acceso concedido")
        break
    else:
        attempts-=1
        print(f"Contraseña incorrecta. Te quedan {attempts} intento(s).")
    
    if attempts ==0:
        print("Acceso bloqueado.")