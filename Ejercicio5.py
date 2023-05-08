from ManejadorPlan import *
import csv

def Menu_Opciones(Manejador):
	band = False

	while band == False:
		print("1-Actualizar el valor del vehículo de cada plan")
		print("2-Mostrar codigo de plan, modelo y versión del vehículo, segun un valor de cuota, cuyo valor sea inferior al ingresado")
		print("3-Mostrar el monto que se debe haber pagado para licitar el vehículo")
		print("4-Modificar la cantidad cuotas que debe tener pagas para licitar")
		print("5-Salir\n")
		Menu_Codigo = input("Ingrese codigo: ")

		if Menu_Codigo == '1':
			Manejador.Item_A()

		elif Menu_Codigo == '2':
			Manejador.Item_B()

		elif Menu_Codigo == '3':
			Manejador.Item_C()

		elif Menu_Codigo == '4':
			Manejador.Item_D()
			
		elif Menu_Codigo == '5':
			band = True

		else:
			print("Codigo incorrecto")

if __name__ == '__main__':
	Manejador = ManejadorPlan()
	Manejador.Carga_Lista()
	# Manejador.Muestra()
	Menu_Opciones(Manejador)
