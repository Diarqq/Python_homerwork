class Car:

    def __init__(self,company, model, year, speed =0):
        self.__company = company
        self.__model = model
        self.__year = year
        self.__speed = speed


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, x):
        self.__company = x

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, x):
        self.__year = x

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, x):
        self.__model = x

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, x):
        self.__speed = x



    def speed_up(self):
        self.__speed += 5

    def speed_down(self):
        self.__speed -= 5

    def stop(self):
        self.__speed = 0

    def turn_180(self):
        self.__speed *= -1

    def current_speed(self):
        print(self.__speed)

car1 = Car('Toyota','x2',2000, 30)
car1.current_speed()
car1.speed_up()
car1.current_speed()
car1.speed_down()
car1.speed_down()
car1.current_speed()
car1.turn_180()
car1.current_speed()
car1.turn_180()
car1.current_speed()
car1.stop()
car1.current_speed()

