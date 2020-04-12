def add(num):
    return num * num


l = (1, 2, 3, 4, 5)

if __name__ == "__main__":
    temp = map(add, l)
    print(list(temp))