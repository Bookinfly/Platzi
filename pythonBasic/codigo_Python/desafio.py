nucleo = 5000.0
energia_por_minuto = 50
energia_auxiliar = 2000
integridad_nucleo = 95.5
energia_escudos = 1500
integridad_del_casco = 85
energia_soporte_vital = 800
energia_impulsores = 100
energia_fasers = 1000
amortiguadores_de_inercia = 223
estres_nucleo = 0
warp = 0


def run():
    print("Eres el ultimo oficial de puente de un crucero estelar de la federacion unida de planetas, fuiste emboscado por un par de aves de presa klingon y estas en fuga")
    while warp <= 9.5:
        if warp == 0:
            nucleo -= 321.5
            warp += 0.5
            nucleo += energia_impulsores + energia_por_minuto
        if warp >= 2.5:
            estres_nucleo += 3
            print("Perdiendo integridad de casco")
            if estres_nucleo == integridad_nucleo:
                break
        if nucleo > energia_auxiliar:
            nucleo + energia_auxiliar
            energia_auxiliar = 0
            integridad_del_casco -= 15
            integridad_nucleo -= 150
            print("Usando energia auxiliar")
        elif energia_fasers >= nucleo:
            nucleo += energia_fasers / 2
            energia_fasers = energia_fasers / 2
            integridad_nucleo -= 113
            print("desviando energia de armas a motores warp")
        elif nucleo <= energia_escudos:
            nucleo += energia_escudos -100
            energia_escudos = 100
            integridad_nucleo -= 25
            integridad_del_casco -= 15
            ("Desviando energia de escudos, concentrando la enegia restante en escudos de popa")

        else:
            if energia_soporte_vital == 800:
                energia_soporte_vital -= 700
                nucleo + 700
                print("desviando soporte vital de las bahias: 1, 3, 5, 6 y 7 ")
        if integridad_nucleo <= 15:
            print("Enviando mensaje auxilio en todas las señales")
            break

            

        
        
            

        
        

    
        





if __name__ == "__main__":
    run() 