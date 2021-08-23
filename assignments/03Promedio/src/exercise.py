def main():
    #programa que calcula el promedio de 4 materias
    #autor: Regina Olvera

    Cal_1 = float(input("Calificación de la materia: "))
    Cal_2 = float(input("Calificación de la materia: "))
    Cal_3 = float(input("Calificación de la materia: "))
    Cal_4 = float(input("Calificación de la materia: "))
    promedio = (Cal_1 + Cal_2 + Cal_3 + Cal_4)/4
    print("El promedio es:", promedio)


if __name__ == '__main__':
    main()
