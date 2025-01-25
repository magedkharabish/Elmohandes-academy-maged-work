import os

# Check if the file exists before deleting it
if os.path.exists(file_path):
    os.remove(file_path)  # Deletes the file
    print(f"File {file_path} has been deleted.")
else:
    print(f"File {file_path} does not exist.")
import warnings

warnings.simplefilter('always', UserWarning)

class Cars:
    def __init__(self, name, car_id, color, model, speed):
        self.car_name = name
        self.car_id = car_id
        self.car_color = color
        self.car_model = model
        self.car_speed = speed

    def move_forward(self, speed_now):
        print("peep peep", self.car_name)
        print('Move forward', self.car_name, speed_now)
        if speed_now >= 120:
            warnings.warn('Your speed is more than 120!', UserWarning)

    def move_back(self, location):
        print("Red line", self.car_name)
        print('Move back', self.car_name, location)

car1 = Cars('Toyota', 1, 'red', 2024, 250)
car2 = Cars('Lamborghini', 2, 'black', 2020, 1000)


car1.move_forward(120)
car1.move_back(90)
car1.move_forward(20)
car1.move_back("park")

car2.move_back('park')
car2.move_forward(30)  
car2.move_back(300)
