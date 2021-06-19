# Ejercicio de edad
edad = int(input("Proporciona tu edad: "))
etapaVida = None

if 0 <= edad < 10:
    etapaVida = "La infancia es increible..."
elif edad >= 10 and edad < 20:
    etapaVida = "Muchos cambios y mucho estudio..."
elif edad >= 20 and edad < 30:
    etapaVida = "Amor y comienza el trabajo..."
else:
    etapaVida = "Etapa de vida no reconocida"

print(f"A los {edad} años {etapaVida}")