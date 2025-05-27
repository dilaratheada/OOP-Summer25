class Car:
    def __init__(self, brand, engine_status):
        self.brand = brand              
        self.__engine_status = engine_status  

    def show_engine_status(self):
        print(f"{self.brand} - Engine status: {self.__engine_status}")

    def __start_the_engine(self):
        self.__engine_status = "Running"
        print("The engine has started.")

    def start_the_car(self):
        self.__start_the_engine()

    def __stop_the_engine(self):
        self.__engine_status = "Stopped"
        print("The engine has stopped running.")

    def stop_the_car(self):
        self.__stop_the_engine()

car1 = Car("Toyota", "Stopped")
car2 = Car("BMW", "Stopped")
car3 = Car("Tesla", "Running")

car1.show_engine_status()
car1.start_the_car()
car1.show_engine_status()
car1.stop_the_car()
car1.show_engine_status()