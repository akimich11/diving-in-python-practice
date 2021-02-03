import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.photo_file_name = photo_file_name
        self.brand = brand
        try:
            c = float(carrying)
        except ValueError:
            c = 0.
        self.carrying = self.validate(c)

    @property
    def car_type(self):
        if isinstance(self, Car):
            return "car"
        elif isinstance(self, Truck):
            return "truck"
        elif isinstance(self, SpecMachine):
            return "spec_machine"
        return "car_base"

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]

    @classmethod
    def validate(cls, v1, v2=None, v3=None):
        if v2 is not None and v3 is not None:
            if not (v1 > 0 and v2 > 0 and v3 > 0):
                return [0., 0., 0.]
            return [v1, v2, v3]
        elif v1 < 0:
            return 0.
        return v1

    @staticmethod
    def is_valid(brand, photo, carrying, arg4=None):
        name, ext = os.path.splitext(photo)
        if brand != "":
            try:
                c = float(carrying)
                return bool(CarBase.validate(c)) and name != "" and ext != "" \
                       and len(photo.split(".")) == 2
            except (ValueError, IndexError):
                return False
        return False


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        try:
            seats = int(passenger_seats_count)
            self.passenger_seats_count = int(self.validate(seats))
        except ValueError:
            self.passenger_seats_count = 0

    @staticmethod
    def is_valid(brand, photo, carrying, seats=None):
        try:
            s = int(seats)
            return CarBase.is_valid(brand, photo, carrying) and bool(CarBase.validate(s))
        except ValueError:
            return False


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            w, h, le = [float(item) for item in body_whl.split('x')]
            self.body_length, self.body_width, self.body_height = self.validate(w, h, le)
        except ValueError:
            self.body_length = self.body_width = self.body_height = 0.

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying,
                 extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @staticmethod
    def is_valid(brand, photo, carrying, extra=None):
        return CarBase.is_valid(brand, photo, carrying) and extra != ""


def get_car_list(filename):
    car_list = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter=";")
        next(reader)
        for row in reader:
            try:
                if row[0] == "car" and Car.is_valid(row[1], row[3], row[5], row[2]):
                    car_list.append(Car(row[1], row[3], row[5], row[2]))
                elif row[0] == "truck" and CarBase.is_valid(row[1], row[3], row[5]):
                    car_list.append(Truck(row[1], row[3], row[5], row[4]))
                elif row[0] == "spec_machine" and SpecMachine.is_valid(row[1], row[3], row[5], row[6]):
                    car_list.append(SpecMachine(row[1], row[3], row[5], row[6]))
            except (ValueError, IndexError):
                continue
    return car_list
