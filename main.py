print("Proporcione los siguientes datos del libro:")

nombreLibro = input("Proporciona el nombre: ")
id = int(input("Proporciona el ID: "))
precio = float(input("Proporciona el precio: "))
envio = input("Indica si el envío es gratuito (True/False): ")

if envio == "True":
    envio = True
elif envio == "False":
    envio = False
else:
    envio = "Valor incorrecto. Debe escribir True/False."

print(f'''
    Nombre: {nombreLibro}
    Id: {id}
    Precio: {precio}
    ¿Envío Gratuito?: {envio}
''')