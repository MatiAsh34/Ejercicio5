from ManejadorPlan import *

class PlanDeAhorro():
	__Cantidad_Cuotas_Plan = 0
	__Cantidad_Cuotas_Pagar = 0
	def __init__(self,codigo_plan,modelo_version,valor_vehiculo):
		self.__CodigoPlan = codigo_plan
		self.__Modelo_Version = modelo_version
		self.__ValorVehiculo = valor_vehiculo
	
	def __str__(self):
		return "%s %s %s %s %s" % (self.__CodigoPlan,self.__Modelo_Version,self.__ValorVehiculo,self.__Cantidad_Cuotas_Plan,self.__Cantidad_Cuotas_Pagar)	

	def Calcula_Valor_Cuota(self):
		return ((self.__ValorVehiculo/self.__Cantidad_Cuotas_Pagar) + self.__ValorVehiculo * 0.10)

	def Calcula_Monto_Licitar_Vehiculo(self):
		return self.__Cantidad_Cuotas_Pagar * self.Calcula_Valor_Cuota()

	def Modifica_ValorVehichulo(self,nuevo_precio):
		self.__ValorVehiculo = nuevo_precio

	def get_CodigoPlan(self):
		return self.__CodigoPlan

	def get_ModeloVersion(self):
		return self.__Modelo_Version

	def get_ValorVehiculo(self):
		return self.__ValorVehiculo

	@classmethod
	def Cambio_Variables_Clase(cls,Cantidad_Cuotas_Plan,Cantidad_Cuotas_Pagar):
		cls.__Cantidad_Cuotas_Plan = Cantidad_Cuotas_Plan
		cls.__Cantidad_Cuotas_Pagar = Cantidad_Cuotas_Pagar

	@classmethod
	def Modifica_Cantidad_Cuotas_Pagar(cls,nueva_cant_cuotas):
		cls.__Cantidad_Cuotas_Pagar = nueva_cant_cuotas