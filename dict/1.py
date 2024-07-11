car = {
        "type": "sedan",
        "color": "blue",
        "mileage": 80000,
        }

# test
print(car.get("mileage", "new car!"))
print(car.get("model", "no such car!"))
