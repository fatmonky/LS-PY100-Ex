car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
print(car.get("color", "transparent?!")) #test. I use this, because it's safer handling if the key doesn't exist.
print(car["color"]) #test
