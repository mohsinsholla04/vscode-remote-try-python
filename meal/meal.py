def main():
    time = input("What time is it? ")
    meal = convert(time)
    meal_time(meal)


def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)


def meal_time(smth): # i cant think of a meaningful name
    if 7 <= smth < 8:
        print("Breakfast time")
    elif 12 <= smth < 13:
        print("Lunch time")
    elif 18 <= smth < 19:
        print("Dinner time")



if __name__ == "__main__":
    main()
