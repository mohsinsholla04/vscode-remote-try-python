def main():
    time = input("What time is it? ")
    meal = convert(time)
    whatTime= meal_time(meal)
    print(whatTime)

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)


def meal_time(smth): # i cant think of a meaningful name
    if 7 <= smth < 8:
        return "Breakfast time"
    elif 12 <= smth < 13:
        return "Lunch time"
    elif 18 <= smth < 19:
        return "Dinner time"
    else:
        


if __name__ == "__main__":
    main()
