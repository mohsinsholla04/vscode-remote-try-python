def main():
    time = input("What time is it? ")
    meal = convert(time)
    whatToEat = meal_time(meal)

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)


def meal_time(smth): # i cant think of a meaningful name
    if smth 

if __name__ == "__main__":
    main()
