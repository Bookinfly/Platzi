// Definición de la clase Billete para representar cada tipo de billete disponible
class Billete {
    /**
     * Constructor de la clase Billete
     * @param {number} valor - Valor nominal del billete
     * @param {number} cantidad - Cantidad disponible de este billete
     */
    constructor(valor, cantidad) {
        this.valor = valor;
        this.cantidad = cantidad;
    }
}

/**
 * Función principal que se ejecuta al solicitar dinero
 * Calcula y distribuye los billetes necesarios para cumplir con la solicitud
 */
function entregarDinero() {
    // Obtener el monto solicitado por el usuario desde el campo de entrada
    const inputDinero = document.getElementById("dinero");
    let montoSolicitado = parseInt(inputDinero.value);
    
    // Reiniciar el arreglo de billetes entregados para cada solicitud
    const billetesEntregados = [];

    // Recorrer cada tipo de billete disponible en la caja
    for (const billete of caja) {
        if (montoSolicitado > 0) {
            // Calcular cuántos billetes de este tipo se necesitan
            const cantidadNecesaria = Math.floor(montoSolicitado / billete.valor);
            
            // Determinar la cantidad real de billetes que se pueden entregar
            const cantidadADescontar = cantidadNecesaria > billete.cantidad ? billete.cantidad : cantidadNecesaria;
            
            // Añadir los billetes entregados al arreglo de resultados
            if (cantidadADescontar > 0) {
                billetesEntregados.push(new Billete(billete.valor, cantidadADescontar));
                
                // Actualizar el monto restante a entregar
                montoSolicitado -= billete.valor * cantidadADescontar;
            }
        }
    }

    // Referencia al elemento donde se mostrará el resultado
    const elementoResultado = document.getElementById("resultado");
    elementoResultado.innerHTML = ""; // Limpiar resultados anteriores

    if (montoSolicitado > 0) {
        // Si no se pudo entregar la cantidad completa
        console.log("Cantidad no disponible");
        elementoResultado.innerHTML = "Cantidad no disponible";
    } else {
        // Mostrar los billetes entregados
        console.log(billetesEntregados);
        for (const billete of billetesEntregados) {
            if (billete.cantidad > 0) {
                elementoResultado.innerHTML += `${billete.cantidad} billete(s) de $${billete.valor}<br />`;
            }
        }
    }
}

// Inicialización de la caja de billetes disponibles
const caja = [
    new Billete(50, 10),  // 10 billetes de $50
    new Billete(20, 30),  // 30 billetes de $20
    new Billete(10, 10)   // 10 billetes de $10
];

// Referencia al botón de extracción y asignación del evento de clic
const botonExtraer = document.getElementById("extraer");
botonExtraer.addEventListener("click", entregarDinero);
