def count(val, i):
    if val != 0 and val > 0:
        val = val//10
        i += 1
        count(val, i)
        return i
    else:
        print(i)

def valid(val):
    if val != 0 and val > 0:
        count(val, i)
    else:
        print("не нч")
        val = int(input("введите новое нч: "))
        valid(val)
    return val

if __name__ == "__main__":
    i = 0
    val = int(input("нч: "))
    valid(val)