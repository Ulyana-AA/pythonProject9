def df(n):
    if n != 0 and n > 0:
        print(n % 10, end="")
        df(n // 10)
    else:
        pass

if __name__ == "__main__":
    n = int(input("введите число: "))
    df(n)