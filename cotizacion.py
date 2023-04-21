edad = int(input("¿Cuál es tu edad? "))
ingreso = float(input("¿Cuales son tus ingresos mensuales?"))
if edad > 16 and ingreso >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
