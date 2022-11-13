//EJERCICIO 7: PEDIR NUMEROS hasta que se ingrese uno negativo
//calcular la media
package Ciclos07;

import java.util.Scanner;

public class Ejercicio07 {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;

        System.out.println("Digite un numero");
        numero = Integer.parseInt(entrada.nextLine());

        while (numero >= 0) {
            suma += numero;
            conteo++;
            System.out.println("Digite otro numero");
            numero = Integer.parseInt(entrada.nextLine());
        }
        if (conteo == 0) {
            System.out.println("Error: LA DIVISION ENTRE 0 NO EXISTE");
        } else {
            promedio = (float) suma / conteo;
            System.out.println("\n El promedio es = " + promedio);
        }
    }

}
