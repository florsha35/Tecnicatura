package Ejercicio_6;

import java.util.Scanner;


public class Ejercicio_6 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
                
        float Guillermo, Juan, Luis, suma ;
        
        System.out.println("Digite el monto de dolares que tiene Guillermo");
        Guillermo = Float.parseFloat(entrada.nextLine());
        
        Luis = (Guillermo / 2);
        System.out.println("Luis tiene dolares = " + Luis );
                 
        Juan = (Guillermo + Luis) / 2;
        System.out.println("Juan tiene  dolares = " + Juan );
        
        suma = Guillermo + Luis + Juan;
        System.out.println("Entre Guillermo, Luis y Juan, tienen dolares = " + suma);
        
        
        
       
                
                
    }
    
}
