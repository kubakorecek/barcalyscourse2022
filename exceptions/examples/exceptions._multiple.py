# Simple example
def out_func():
    number = input("Choose number:\n")
    return in_func(number)


def in_func(divisor):
    try:
        divisor = int(divisor)
        return 1 / divisor
    except ZeroDivisionError:
        print("Zero division!!!!!")
        return 0
    except ValueError:
        print("Not a number")
    finally:
        print("I will be always called.")
    return -1


if __name__ == '__main__':
    print(out_func())