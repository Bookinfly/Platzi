contador_externo = 0
contador_interno = 1


while contador_externo < 5:
    while contador_interno < 5:
        print(contador_interno)
        contador_interno += 1

        if contador_interno >= 3:
            break
    contador_externo += 1
    contador_interno = 0