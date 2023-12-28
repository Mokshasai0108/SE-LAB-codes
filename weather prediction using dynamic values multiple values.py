num_sets = int(input("Enter the number of sets of values: "))

for i in range(num_sets):
    print("set :",i)
    temperature = int(input("Enter Temperature: "))
    humidity = int(input("Enter Humidity: "))
    wind_speed = int(input("Enter Wind speed: "))

    weather = 0.5 * temperature**2 - 0.2 * humidity + 0.1 * wind_speed
    if weather > 300:
        print("Weather is Sunny")
    elif 200 < weather <= 300:
        print("Weather is Cloudy")
    elif 100 < weather <= 200:
        print("Weather is Rainy")
    else:
        print("Weather is Stormy")

