package Ejercicio_5;

import java.util.Scanner;


public class Ejercicio_5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        float  suma;
        
        System.out.print("Digite una calificacion: ");
        float calificacion = Float.parseFloat(entrada.nextLine());
        System.out.print("Digite otra calificacion: ");
        float calificacion1 = Float.parseFloat(entrada.nextLine());
        System.out.print("Digite otra calificacion: ");
        float calificacion2 = Float.parseFloat(entrada.nextLine());
        
        suma = calificacion + calificacion1 + calificacion2;
        System.out.println("La suma  de las calificaciones es = " + suma);
        
        
        
        
    }
    
    
}
