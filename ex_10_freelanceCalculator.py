# Un Freelancer desea saber cuánto puede cobrar por su trabajo semanal y mensualmente, para ello solo necesita establecer el precio de su trabajo por hora.
# Se estiman 40 horas de trabajo a la semana.
# Las Fórmulas para calcular el pago Semanal y Mensual son:
# 1) Pago_Semanal = (DolaresPorHora x 40)
# 2) Pago_Mensual = (DolaresPorHora x 160)
# ► Variables:
# Dolares_Por_Hora: Cantidad de Dólares que gana el Freelancer por hora.
# Pago_Semanal: Almacena el resultado del pago semanal.
# Pago_Mensual: Almacena el resultado del pago mensual.
# ► Salida:
# ----------------------------------------
#       CALCULADORA FREELANCER (USD)      
# ----------------------------------------
# >>> Precio en dolares por Hora: 20
# ----------------------------------------
# >>> PAGO SEMANAL: 800.00
# >>> PAGO MENSUAL: 3200.00
# ----------------------------------------


Ancho=40
relleno1="-"
relleno2=" "
cadena_vacia=""

mensaje_inicial="CALCULADORA FREELANCER (USD)"

pago_semanal=0
pago_mensual=0

pago_hora=input("Ingresa tu salario por hora: ")

try: 
    float(pago_hora) 
    si= True
except ValueError:
    si= False

if si == True:
    print(cadena_vacia.center(Ancho,relleno1))
    print(mensaje_inicial.center(Ancho,relleno2))
    print(cadena_vacia.center(Ancho,relleno1))

    print(">>> Salario por hora: ",pago_hora)
    print(cadena_vacia.center(Ancho,relleno1))
    pago_hora=float(pago_hora)
    pago_semanal=round((pago_hora*40),2)
    pago_mensual=round((pago_hora*160),2)
    print(">>>PAGO SEMANAL: ", pago_semanal)
    print(">>>PAGO MENSUAL: ", pago_mensual)
    print(cadena_vacia.center(Ancho,relleno1))
else:
    print("ERROR! Ingrese numeros.")

