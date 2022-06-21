package Ejercicio2;

import java.util.Scanner;

public class Ejercicio2 {
        public static void main(String[] args) {
            Scanner entrada = new Scanner(System.in);
            float   salario, totalACobrar;
            int  horas;
            
            System.out.println("Digite el valor del salario");
            salario = Float.parseFloat(entrada.nextLine());
            System.out.println("Digite la cantidad de horas trabajadas: ");
            horas = Integer.parseInt(entrada.nextLine());
            totalACobrar = (salario * horas);
            System.out.println("Total a cobrar por el trabajador:  = " + totalACobrar );
    }
            
            
    
}
