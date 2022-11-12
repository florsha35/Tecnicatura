//Ejercicio5:  Realizar un juego para adivinar un numero aleatorio entre 0-100 e ir
//indicando si es mayor o menor. El juego termina cuando acierta
//mostrar cuanto intentos ha hecho
package ciclos04;

import java.util.Scanner;

public class Ejercicio5 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        int numero, aleatorio, conteo = 0; //creo el aleatorio
        aleatorio = (int) (Math.random() * 100);
        do {
            System.out.println("Digite un numero entre 1 y 100:  ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero < aleatorio) {
                System.out.println("Digite un numero mayor");
            } else if (numero > aleatorio) {
                System.out.println("Digite un numero menor");
            } else {
                System.out.println("Felicidades, has acertado");
            }
            conteo++;
        } while (numero != aleatorio);
        System.out.println("Adivinaste el número en " + conteo + " intentos");
    }

}
