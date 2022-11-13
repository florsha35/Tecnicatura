//Ejercicio01 : crear una caja con los atributos :alto,ancho y profundidad
package caja;

public class Caja {
   
    //atributos
    int alto;
    int ancho;
    int profundidad;
            
     public Caja(){  //contructor1
     }
    //Constructor con parametros
     public Caja(int ancho, int alto, int profundidad){
         this.ancho = ancho;
         this.alto = alto;
         this.profundidad = profundidad;         
     }
     
     public int calcularVolumen(){
         return ancho * alto * profundidad;
     }
     
    
}
