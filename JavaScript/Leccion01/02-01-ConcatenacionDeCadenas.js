var nombre ='Jose';
var apellido = ' Montes';
var nombreCompleto = nombre+' '+apellido; //1° forma de concatenar
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Betancud'; //2° forma de concatenar
console.log(nombreCompleto2);
var juntos = nombre + 219;
console.log(juntos)
juntos = nombre + (78 + 17);
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);
juntos = nombre +=  apellido; //3° foma de concatenar
console.log(nombre)

//hoy ya no se usa var --> se usa let y const
let nombre2 = "Pedro";
console.log(nombre2);

const apellido2 = "Lepes"; // una constante no puede ser modificada
console.log(apellido2)

let x, y; // se pueden crear varias variables dentro de una misma linea
x = 17, y = 21; // se pueden hacer vs asignaciones de variables dentro de la misma línea
let z = x + y ; // se asigna el valor de la operacion
console.log(z)

//let 1num = 31; // la var no puede empezar con numero
//let rompiendo = "rompe" // no se pueden usar palabras reservadas

