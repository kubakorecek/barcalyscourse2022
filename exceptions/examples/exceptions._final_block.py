# Simple example
def out_func():
    return in_func(0)


def in_func(divisor):
    try:
        return 1 / divisor
    except ZeroDivisionError:
        return 0
    finally:
        print("I will be always called.")
        return -1
if __name__ == '__main__':
    print(out_func())