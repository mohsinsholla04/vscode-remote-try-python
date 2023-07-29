def main():
    time = input("What time is it? ")
    meal = convert(time)
    

def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    return hours + (minutes / 60)

# if __name__ == "__main__":
    main()
