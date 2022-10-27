//Ejercicio3 leer un numero e indicar si es positivo o negativo hasta que se introduzca un 0
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio3 {

    public static void main(String[] args) {
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero != 0) {
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero ingresado  " + numero + " es PAR");
            } else {
                JOptionPane.showMessageDialog(null, "El numero ingresado  " + numero + " es IMPAR");
            }
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "El numero" + numero + "finaliza el programa");

    }

}
