// hacemos comentario

//TIPOS DE DATOS EN JAVASCRIPT

/* 
para comentario de multiples lineas
*/
var nombre ="Ariel";
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);
var numero = 3000; //Tipo numerico
console.log(numero);

var objeto  = {
    nombre : "Ariel",
    apellido : "Betancud",
    telefono : "260421215"
}
console.log(typeof objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);

//Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

//Tipo de dato symbol
var simbol = Symbol("Mi simbolo");
console.log(Symbol);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

//null: significa ausencia de valor
var y = null; // no es un tipo de dato, pero su origen es OBJECT
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Cientroen', 'Audi', 'BMW','Mercedes Benz'];
console.log(autos);
console.log(typeof autos);

var z= ''; // cadena vacía
console.log(z);
console.log(typeof z);