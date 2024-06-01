class Vehicles: 

	Car_name1 = "Nissan"
	Car_name2 = "Ford"

	def main(self) :
		print("I have ", self.Car_name1)
		print("I have ", self.Car_name2)

Vehicle_class_object = Vehicles()

print("Your car is ", Vehicle_class_object.Car_name1)
Vehicle_class_object.main()