// Obtener el elemento canvas por su ID "areaDeDibujo"
const canvasElement = document.getElementById("areaDeDibujo");

// Obtener el contexto 2D del canvas para dibujar
const contextoCanvas = canvasElement.getContext("2d");

// Variables para almacenar las coordenadas anteriores del ratón
let posicionAnteriorX = 0;
let posicionAnteriorY = 0;

// Color de la línea a dibujar
const colorLinea = "blue";

// Bandera para indicar si el ratón está presionado
let ratonPresionado = false;

// Asignar eventos al canvas para manejar las interacciones del ratón
canvasElement.addEventListener("mousedown", iniciarDibujo);
canvasElement.addEventListener("mouseup", detenerDibujo);
canvasElement.addEventListener("mousemove", dibujar);

// Función que se ejecuta cuando se presiona el botón del ratón
function iniciarDibujo(evento) {
    ratonPresionado = true;
    // Actualizar las coordenadas iniciales al presionar el ratón
    posicionAnteriorX = evento.offsetX;
    posicionAnteriorY = evento.offsetY;
}

// Función que se ejecuta cuando se suelta el botón del ratón
function detenerDibujo() {
    ratonPresionado = false;
}

// Función que se ejecuta cuando el ratón se mueve sobre el canvas
function dibujar(evento) {
    if (!ratonPresionado) return; // Si el ratón no está presionado, no hacer nada

    // Obtener las coordenadas actuales del ratón
    const posicionActualX = evento.offsetX;
    const posicionActualY = evento.offsetY;

    // Dibujar una línea desde la posición anterior hasta la posición actual
    dibujarLinea(colorLinea, posicionAnteriorX, posicionAnteriorY, posicionActualX, posicionActualY, contextoCanvas);

    // Actualizar las coordenadas anteriores para el siguiente movimiento
    posicionAnteriorX = posicionActualX;
    posicionAnteriorY = posicionActualY;
}

/**
 * Función para dibujar una línea en el canvas
 * @param {string} color - Color de la línea
 * @param {number} xInicial - Coordenada X inicial
 * @param {number} yInicial - Coordenada Y inicial
 * @param {number} xFinal - Coordenada X final
 * @param {number} yFinal - Coordenada Y final
 * @param {CanvasRenderingContext2D} contexto - Contexto del canvas donde se dibujará la línea
 */
function dibujarLinea(color, xInicial, yInicial, xFinal, yFinal, contexto) {
    contexto.beginPath(); // Iniciar una nueva ruta
    contexto.strokeStyle = color; // Establecer el color de la línea
    contexto.lineWidth = 5; // Establecer el ancho de la línea
    contexto.moveTo(xInicial, yInicial); // Mover al punto inicial
    contexto.lineTo(xFinal, yFinal); // Dibujar una línea hasta el punto final
    contexto.stroke(); // Renderizar la línea
    contexto.closePath(); // Finalizar la ruta
}
