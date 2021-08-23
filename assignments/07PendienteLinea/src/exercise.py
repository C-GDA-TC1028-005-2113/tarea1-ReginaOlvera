def main():
    #programa que calcula la pendiente de la recta
    #autor: Regina Olvera

    x1 = float(input("Dame x1: "))
    y1 = float(input("Dame y1: "))
    x2 = float(input("Dame x2: "))
    y2 = float(input("Dame y2: "))
    pendiente = (y2-y1)/(x2-x1)
    print("Pendiente:", pendiente)



if __name__ == '__main__':
    main()
