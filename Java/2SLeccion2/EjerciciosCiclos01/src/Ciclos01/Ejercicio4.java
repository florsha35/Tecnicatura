//Ejercicio4 : Pedir numeros hasta que teclee uno engtivo
//Mostrar cuántos numeros ha introducido
package Ciclos01;

import java.util.Scanner;

public class Ejercicio4 {

    public static void main(String[] args) {
                         
         Scanner entrada = new Scanner(System.in);
          int numero, contador = 0;
         System.out.println("Digite un numero");
         numero = Integer.parseInt(entrada.nextLine());
         while (numero >= 0){
             System.out.println("El numero " +numero + " es positivo");
             contador ++;
             System.out.println("Digite otro numero");
             numero = Integer.parseInt(entrada.nextLine());
         }
         System.out.println("A ingresado" + contador+ " numeros positivos");
         
         
                

    }

}
