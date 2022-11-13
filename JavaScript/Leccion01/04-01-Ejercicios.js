//Ampliando el uso de var y let
/* 
con var puedes readignar en cualquier momento este forma parte del ambito global
un error es que se sobreeescribe
*/

var nombre = 'Ariel';
nombre ='Osvaldo';
console.log(nombre);

function saludar(){
    var nombre3 = 'Natalia';
    console.log(nombre3);
    }
//console.log(nombre3); //Aqui no lee el dato de la funcion Osvaldo

if(true){
    var edad = 34;
    console.log(edad);
}
console.log(edad); //En la funcion funciono correctamente, en la estructura if fallo

/*
let: esta ouede ser reasignada en cualquier momento
la diferencia es que su ambito es de bloque,
solo disponible dentro de un bloque de llaves
o dentro de una funcion
*/

function saludar2(){
    let nombre2 = 'Ariel';
    console.log(nombre2);
}
//console.log(nombre2);

if(true){
    let edad2 = 33;
    console.log(edad2)
}
//console.log(edad2)
/* 
const se utiliza para vlores constantes que no pueden ser reasignados
*/

const fechaNacimiento = 2006;
console.log(fechaNacimiento);
//fechaNacimiento = 2008;
