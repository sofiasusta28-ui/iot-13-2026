from enum import Enum


class Brand(Enum):
    BMW = "BMW"
    AUDI = "Audi"
    TOYOTA = "Toyota"


class Car:
    def __init__(self, brand: Brand, age: int, max_speed: int, horse_power: int, park_duration: float):
        self.brand = brand
        self.age = age
        self.max_speed = max_speed
        self.horse_power = horse_power
        self.park_duration = park_duration


    def get_brand(self):
        return self.brand

    def get_park_duration(self):
        return self.park_duration

    def __del__(self):
        print(f"{self.brand.value} видалено")


    def __str__(self):
        return (f"Марка: {self.brand.value}  Вік: {self.age} р. "
                f"Швидкість: {self.max_speed} км/год  Потужність: {self.horse_power} к.с.  "
                f"Час: {self.park_duration} год.")


class Parking:
    def __init__(self, capacity: int, price_per_hour: float):
        self.capacity = capacity
        self.price_per_hour = price_per_hour
        self.cars = []

    def park_car(self, car):
        if len(self.cars) >= self.capacity:
            print(f"Немає місця для {car.brand.value}")
            return
        self.cars.append(car)
        print(f"Автомобіль {car.brand.value} припарковано")

    def leave_parking(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f"Автомобіль {car.brand.value} покидає парковку")
        else:
            print(f"Автомобіля {car.brand.value} немає на парковці")

    def sort_cars(self):
        self.cars.sort(key=lambda car: car.park_duration, reverse=True)
        print("Машини посортовано за тривалістю стоянки.")

    def calculate_price(self):
        for car in self.cars:
            price = self.price_per_hour * car.park_duration
            print(f"Автомобіль {car.brand.value} час на стоянці {car.park_duration} год до сплати {price} грн")


if __name__ == "__main__":
    parking = Parking(capacity=2, price_per_hour=50.0)

    car1 = Car(Brand.BMW, age=3, max_speed=240, horse_power=190, park_duration=5.0)
    car2 = Car(Brand.AUDI, age=2, max_speed=220, horse_power=150, park_duration=2.0)
    car3 = Car(Brand.TOYOTA, age=5, max_speed=200, horse_power=130, park_duration=8.0)
    print(car1)
    print(car2)
    print(car3)

    parking.park_car(car1)
    parking.park_car(car2)
    parking.park_car(car3)

    parking.sort_cars()
    parking.calculate_price()

    parking.leave_parking(car1)
