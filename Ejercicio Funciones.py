def es_bisiesto(year):
    # Verificar si el año es bisiesto
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def validate_date(date):
    try:
        # Separar la fecha en día, mes y año
        d, m, a = list(map(int, date.split()))

        # Verificar que el mes esté en el rango de 1 a 12
        if 1 <= m <= 12:
            # Verificar la cantidad de días en el mes
            dias_en_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            # Ajustar febrero si el año es bisiesto
            if es_bisiesto(a):
                dias_en_mes[2] = 29

            if 1 <= d <= dias_en_mes[m]:
                return "Fecha correcta"
            else:
                return "Fecha incorrecta"
        else:
            return "Fecha incorrecta"
    except ValueError:
        return "Fecha incorrecta"


test_dates = input("Ingrese una fecha (en formato DD MM AAAA): ")
resultado = validate_date(test_dates)
print(resultado)
