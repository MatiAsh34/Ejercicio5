from PlanDeAhorro import *
import csv

class ManejadorPlan():
	def __init__(self):
		self.__lista = []

	def Carga_Lista(self):
		archivo = open('planes.csv')
		reader = csv.reader(archivo,delimiter=';')
		band = False

		for fila in reader:
			Plan = PlanDeAhorro(int(fila[0]),fila[1],float(fila[2]))
			self.__lista.append(Plan)

			if band == False:
				PlanDeAhorro.Cambio_Variables_Clase(int(fila[3]),int(fila[4]))
				band=True

	def Muestra(self):
		for i in range(len(self.__lista)):
			print(self.__lista[i])
			print("Valor de Cuota: ", self.__lista[i].Calcula_Valor_Cuota())

	def Item_A(self):
		for i in range(len(self.__lista)):
			print("\nCodigo de plan: ",self.__lista[i].get_CodigoPlan())
			print("Modelo y version: ",self.__lista[i].get_ModeloVersion())
			precio = float(input("Ingrese nuevo precio del vehiculo: "))
			self.__lista[i].Modifica_ValorVehichulo(precio)
			print("Nuevo precio: ",self.__lista[i].get_ValorVehiculo())

	def Item_B(self):
		Valor = float(input("\nIngrese un valor de cuota: "))
		for i in range(len(self.__lista)):
			if self.__lista[i].Calcula_Valor_Cuota() < Valor:
				print("\nCodigo de plan: ",self.__lista[i].get_CodigoPlan())
				print("Modelo y version: ",self.__lista[i].get_ModeloVersion())

	def Item_C(self):
		for i in range(len(self.__lista)):
			print("\nModelo y version: ",self.__lista[i].get_ModeloVersion())
			print("Monto total para licitar el vehiculo: ",self.__lista[i].Calcula_Monto_Licitar_Vehiculo())

	def Item_D(self):
		nueva_cant_cuotas = int(input("Ingrese nueva cantidad de cuotas para licitar: "))
		PlanDeAhorro.Modifica_Cantidad_Cuotas_Pagar(nueva_cant_cuotas)