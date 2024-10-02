var d = document.getElementById("dibujito");
var lienzo = d.getContext("2d");
console.log(lienzo);

function dibujarLinea(color, xinicial, yinicial, xfinal, yfinal){
    lienzo.beginPath();
    lienzo.strokeStyle = color;
    lienzo.moveTo(xinicial, yinicial);
    lienzo.lineTo(xfinal, yfinal);
    lienzo.stroke();
    lienzo.closePath();
}

dibujarLinea("black", 30, 60, 75, 250);