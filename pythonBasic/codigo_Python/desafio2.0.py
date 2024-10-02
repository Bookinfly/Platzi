name = "USS Walker" #reemplazar todo esto por una lista + adelante
nucleo_warp = 500
escudos = 80
integridad_estructural = 75
soporte_vital = 400
faser = 100

escudo_enemigo = 110
integridad_nave_enemiga = 60
disrruptor = 60
capitan = ""
variantes = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30]

import random


def run():
    salto()
    print("Eres un teniente de la flota estelar, el ultimo oficial en pie tras una emboscada klingon al " + name + "el caos reina a tu alrrededor, el equipo medico se esta llevando a los oficiales de puente, mientras que cadetes se acercan para tomar sus puestos, uno se te acerca mientras y te ayuda a incorporarte mientras apaga las llamas de tu uniforme")
    salto()
    global capitan
    capitan = input("¿Señor, cual es su nombre?    ")
    salto()
    print("Parece que has obtenido una promocion de campo, cuales son sus ordenes capitan " + capitan)
    salto()
    print("Opcion A: Maximo Warp en direccion a la federacion!!!!")
    salto()
    print("Opcion B: Pagaran por esto!... Energia a los escudos y cañones faser, fuego a mi señal")
    salto()
    print("Opcion C: Envien un saludo en todas las señales y un mensaje de alerta de largo alcance, y cadete... necesito un informe se situacion ya!!!")
    opciones_1 = input("Inique sus ordenes ingresando A, B, o C : ")#reemplazar esto por una lista de opciones
    salto()
    if opciones_1 == "A":
        salto()
        print("Motores Warp fuera de linea, moviendose a maximo impulso")
        salto()
        huida()
    elif opciones_1 == "B":
        salto()
        print("Impacto directo, pero sus escudos resisten")
        salto()
        combate(True)
    elif opciones_1 == "C":
        salto()
        print("Multiples heridos y desesos en todas las cubieras")
        salto()
        print("Cubiertas de la 5 a la 12 destruidas, escudos al 50 porciento, sistema de armas y de impulso operativos, integridad del casco 30 porciento, nucle warp operativo aunque inestable......motores warp fuera de linea")
        salto()
        print("La nave de carga que escoltabamos esta siendo abordada, y sus armas y motores fueron incapacitados")
        salto()
        estrategia()
    else:
        salto()
        print("Elija una opcion valida")
        salto()
        print("Señor recibimos otro impacto, los escudos estan no resistiran")
        global escudos
        escudos -= 30


def combate(batalla):
    while batalla == True:
        i = 1
        i += 1
        global nucleo_warp
        nucleo_warp += 10
        salto()
        if i == 1:
            salto()
            print("Escudos al 80 porciento. Fasers a toda capacidad")
            salto()
        print(" Indique A para disparo de advertencia con 10 porciento de la carga maxima")
        salto()
        print(" Indique B para disparo de normal con 20 porciento de carga maxima")
        salto()
        print(" Indique C para maxima potencia con 50 porciento de carga maxima")
        salto()
        mando = input("Responde A, B, o C : ")
        salto()
        if mando == "A" :
            if faser > 100:
                salto()
                print("los faser estan sobrecargados, estamos indefensos")
                salto()
                batalla = False
            elif faser < 10:
                salto()
                print("Energia insuficiente para realizar un disparo")
                salto()
                game_over()
            ataque(10)
            desviar_f()
        elif mando == "B" :
            if faser > 100:
                salto()
                print("los faser estan sobrecargados, estamos indefensos")
                salto()
                batalla = False
                game_over()
            elif faser < 20:
                salto()
                print("Energia insuficiente para realizar un disparo")
                salto()
                game_over()
            ataque(20)
            desviar_f()
        elif mando == "C" :
            if faser > 100:
                salto()
                print("los faser estan sobrecargados, estamos indefensos")
                salto()
                batalla = False
                game_over()
            elif faser < 50:
                salto()
                print("Energia insuficiente para realizar un disparo")
                salto()
                game_over()
            ataque(50)
            desviar_f()
        else:
            salto()
            print("escoje una opcion correcta")
            salto()
        contrataque()
        desviar_e()
        if i == 10:
            salto()
            print("Multiples señales desconocidas acercandose a velocidad Warp")
            salto()
            input("Señor si vamos a retirarnos es ahora o nunca!!")
            escape = input("Seleccione A para continuar y B para ponerse en fuga")
            salto()
            if escape == "B":
                salto()
                print("Emprendes una sabia retirada a maximo impulso, mientras los hostiles les persiguen y les disparan, logran poner en linea los motores Warp y escapan")
                exit()
        if i == 11:
            salto()
            print("Decemas de naves hostiles te rodean, ya no puedes ganar ni escapar")
            game_over()

def contrataque():
    global escudos
    global integridad_estructural
    if escudos > 0:
        escudos -= disrruptor
        salto()
        print("Nos impactaron sus disrruptores")
        salto()
        print("Escudos al " + str(escudos) + " porciento")
        salto()
    elif escudos <= 0:
        integridad_estructural -= disrruptor
        if integridad_estructural <= 0:
            salto()
            print("Escudos cayeron, el enemigo apunta a nuestro nucleo, preparanse para el impacto!")
            game_over()
        salto()
        print("integridad de casco en " + str(integridad_estructural) + " porciento")
        salto()

def ataque(a):
    global faser
    global escudo_enemigo
    global integridad_nave_enemiga
    faser -= a 
    salto()
    print("Energia de Fasers al " + str(faser) + " porciento")
    salto()
    if escudo_enemigo <= 0:
        salto()
        print("Escudos de nave desconocida fuera de linea")
        salto()
        integridad_nave_enemiga -= a
        if a <= 10:
            salto()
            print("Impacto directo, la nave hostil recibio daños menores al casco")
            salto()
        elif a <= 20:
            salto()
            print("Impacto directo, su sistema de soporte de vida esta comprometido")
            salto()
        elif a <= 50:
             salto()
             ("Imacto directo, dañamos su nucleo y sus cubiertas")
             salto()
        if integridad_nave_enemiga <= 0:
            salto()
            print("Victoria para la Federacion")
            salto()
            print("El bravo capitan " + str(capitan) + " y su valerosa tripulacion han destruido al enemigo!")
            salto()
            win()
    elif escudo_enemigo > 0:
        escudo_enemigo -= a
        print("Los escudos obsorvieron el daño")
    salto()
    print("Escudo enemigo al " + str(escudo_enemigo))
    salto()


def game_over():
        salto()
        print("Capitan " + capitan + " a sido un honor")
        salto()
        print("El enemigo te ha destuido")
        salto()
        print("GAME OVER")
        exit()
        
    
def desviar_e():
    global escudos
    global nucleo_warp
    salto()
    print("Energia del nucleo en " + str(nucleo_warp))
    salto()
    print("¿Capitan " + str(capitan) + " desea desviar energia a los sistemas de escudos?")
    salto()
    desvio = input("ingrese la cantidad de energia a desviar, no debes permitir que la energia del nuclo llegue a 0 ni la que la de las armas supere 100 : ")
    desvio = int(desvio)
    
    if desvio < nucleo_warp:
        escudos += desvio
        nucleo_warp -= desvio
        if nucleo_warp <= 0:
            print("fallas en todos los sistemas, el nucleo esta inestable")
            game_over()
    else:
        print("fallas en todos los sistemas, el nucleo esta inestable")
        game_over()


def desviar_f():
    global faser
    global nucleo_warp
    salto()
    print("Energia del nucleo en " + str(nucleo_warp))
    salto()
    print("¿Capitan " + str(capitan) + " desea desviar energia a los sistemas de armas?")
    salto()
    desvio = input("ingrese la cantidad de energia a desviar, no debes permitir que la energia del nuclo llegue a 0 ni la que la de las armas supere 100 : ")
    desvio = int(desvio)
    if desvio > 100:
        print("sistema de armas sobrecargado")
        game_over()
    elif desvio < 101:
        faser += desvio
        nucleo_warp -= desvio
        if nucleo_warp <= 0:
            game_over
        if faser > 100:
            game_over


def azar():
    random.choice(variantes)


def win():
    salto()
    print("Victoria!!!")
    exit()



def huida(escape):
    print("Ahhhhhh")


def estrategia():
    pass


def salto():
    print("")


if __name__ == "__main__":
    run() 
