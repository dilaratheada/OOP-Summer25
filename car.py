class Car:
    def __init__(self, brand, engine_status):
        self.brand = brand              
        self.__engine_status = engine_status  

    def show_engine_status(self):
        print(f"Engine status: {self.__engine_status}")

    def __start_the_engine(self):
        self.__engine_status = "Running"
        print("The engine has started.")

    def start_the_car(self):
        self.__start_the_engine()

    def __stop_the_engine(self):
        self.__engine_status = "Stoped"
        print("The engine has stoped running.")

    def stop_the_car(self):
        self.__stop_the_engine()