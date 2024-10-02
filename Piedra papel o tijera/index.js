///FUNCIONES

//Genera num aleatorio
function aleatorio(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min)
}

//ELECCION entra por parametro la selección del player como numero y la decuelve como string con la info
function eleccion(jugada) {
    let resultado = ""
    if(jugada == 1) {
        resultado = "Piedra 🪨"
    } else if (jugada == 2) {
        resultado = "Papel 📃"
    } else if (jugada == 3) {
        resultado = "Tijera ✂️"
    } else {
        resultado = "MAL ELEGIDO"
    }
    return resultado
}

//COMBATE función que tomá las elecciónes de pc y jugador (numero) y las compara, retorna contadores de victoria actualizados
function combate(pc, jugador) {
    // COMBATE
    if (pc == jugador) {
        alert("EMPATE")
    } else if (jugador == 1 && pc == 3) {
        alert("GANASTE")
    } else if (jugador == 2 && pc == 1) {
        alert("GANASTE")
        playerWins = playerWins + 1
    } else if (jugador == 3 && pc == 2) {
        alert("GANASTE")
        playerWins = playerWins + 1
    } else {
        alert("PERDISTE")
        pcWins = pcWins + 1
    }
    return [pcWins,playerWins]
}

///VARIABLES
// 1 es piedra, 2 es papel, 3 es tijera
let jugador = 0
let pcWins = 0
let playerWins = 0
let round


while(pcWins < 3 && playerWins < 3 ) {
    let pc = aleatorio(1,3)
    jugador = prompt("Elige: 1 para piedra, 2 para papel, 3 para tijera")
    // alert("Elegiste " + jugador)
    alert("PC elige " + eleccion(pc))
    alert("Tú eliges " + eleccion(jugador))
    round = combate(pc,jugador)
    pcWins = round[0]
    playerWins = round[1]
    alert("Tu vas " + playerWins + " partidas ganadas," + " contra " + pcWins + " partidas perdidas")
if(playerWins === 3) {
    alert("Ganaste al mejor de 3")
} else if(pcWins === 3) {
    alert("Perdiste al mejor de 3")
}
} 