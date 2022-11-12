// EJERCICIO6 pedir numeros hasta que se teclee un cero,
//sumar todos los numeros
package ciclos04;

import java.util.Scanner;

public class Ejercicio06 {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, suma = 0;
        do {
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma += numero;
        } while (numero != 0);
        System.out.println("\n La suma de todos los numero ingresadoes es:" + suma);

    }

}
