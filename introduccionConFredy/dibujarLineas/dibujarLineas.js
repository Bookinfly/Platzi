// Obtener el elemento de entrada donde el usuario ingresa el número de líneas
var texto = document.getElementById("texto_lineas");

// Obtener el botón y asignarle un listener para detectar el clic
var boton = document.getElementById("botoncito");
boton.addEventListener("click", dibujoPorClick);

// Obtener el elemento canvas y su contexto 2D para dibujar
var d = document.getElementById("dibujito");
var ancho = d.width;
var lienzo = d.getContext("2d");

/**
 * Función para dibujar una línea en el canvas
 * @param {string} color - Color de la línea
 * @param {number} xinicial - Coordenada x inicial
 * @param {number} yinicial - Coordenada y inicial
 * @param {number} xfinal - Coordenada x final
 * @param {number} yfinal - Coordenada y final
 */
function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal) {
    lienzo.beginPath(); // Iniciar una nueva ruta
    lienzo.strokeStyle = color; // Establecer el color de la línea
    lienzo.moveTo(xinicial, yinicial); // Mover el punto de inicio
    lienzo.lineTo(xfinal, yfinal); // Dibujar una línea hasta el punto final
    lienzo.stroke(); // Renderizar la línea
    lienzo.closePath(); // Finalizar la ruta
}

/**
 * Función que se ejecuta al hacer clic en el botón
 * Toma el número de líneas ingresadas y dibuja en el canvas
 */
function dibujoPorClick() {
    // Obtener y convertir a entero el valor ingresado por el usuario
    var lineas = parseInt(texto.value);
    var l = 0; // Contador de líneas
    var yi, xf; // Variables para calcular las coordenadas
    var colorcito = "#FAA"; // Color de las líneas
    var espacio = ancho / lineas; // Espacio entre líneas

    // Bucle para dibujar las líneas según el número indicado
    for (l = 0; l < lineas; l++) {
        yi = espacio * l; // Coordenada y inicial
        xf = espacio * (l + 1); // Coordenada x final
        dibujarLinea(colorcito, 0, yi, xf, 300); // Dibujar línea desde el borde izquierdo hacia abajo
        console.log("Linea " + l); // Mostrar en consola el número de línea dibujada
    }

    // Dibujar líneas adicionales para formar un marco o estructura
    dibujarLinea(colorcito, 1, 1, 1, 299); // Línea vertical izquierda
    dibujarLinea(colorcito, 1, 299, 299, 299); // Línea horizontal inferior
}
