# Primero tenemos que solicitar al ususario dos numeros
# Despues entre esos dos numeros vamos a realizar una operacion matematica ya sea suma resta o division
#si el usuario elige una divison y el segundo numero es 0 debera mostrarse un mensaje que ponga "error"



# el primer paso es pedirle dos numeros.

numero1 = int(input ("porfavor introduce el primer numero:"))
numero2 = int(input("porfavor introduce el segundo numero:"))

# el segundo paso es hacer una operacion ya sea suma resta multiplicacion o division

operacion = input ("Porfavor elige la operacion que deseas realizar:")
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

if operacion == "suma":
	print( "El resultado es:", suma)
elif operacion == "resta":
	print ("El resultado es:", resta)
elif operacion == "multiplicacion":
	print("El resultado es:", multiplicacion)

elif operacion == "division":
	if numero2 == 0:
		print(" Error")

	else:
		division = numero1 / numero2
		print("El resultado es:", division)

