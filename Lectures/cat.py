# print("meow")
# print("meow")
# print("meow")

                                                # For  LooP
# for _ in range(1000000):
    # print("meow")

# n = int(input("What's n? "))
# while n <= 0:
#     n = int(input("What's n? "))

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break


# for _ in range(n):
#     print("meow")

def main():
    number = get_number()
    meow(number)


def get_number():
    while True:
        n = int(input("What's n ? : "))
        if n > 0:
            break
    return n


def meow(n):
    for _ in range(n):
        print("meow")


main()
