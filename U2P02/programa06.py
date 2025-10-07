"""programa06
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta"""

print("TODOS LAS FECHAS DEBEN DE HABER PASADO YA.")

dia = int(input("Dime un dia del mes en numero: "))
mes = int(input("Dime un mes del año en numero: "))
año = int(input("Dime un año: "))

match mes:
    case 1|3|5|7|8|10|12:
        while (dia < 0) or (dia > 31):
            dia = int(input("ESE DIA DEL AÑO NO EXISTE DI UNO VALIDO: "))
        else:
            print("El ",dia,"/",mes,"/",año," es una fecha correcta")
    case 4|6|9|11:
        while (dia < 0) or (dia > 30):
            dia = int(input("ESE DIA DEL AÑO NO EXISTE DI UNO VALIDO: "))
        else:
            print("El ",dia,"/",mes,"/",año," es una fecha correcta")
    case 2:
        while (dia < 0) or (dia > 28):
            dia = int(input("ESE DIA DEL AÑO NO EXISTE DI UNO VALIDO: "))
        else:
            print("El ",dia,"/",mes,"/",año," es una fecha correcta")