
//Ejercicio 4 con JOptionPane
package Ciclos01;

import javax.swing.JOptionPane;

public class Ejercicio5 {

    public static void main(String[] args) {

        int numero, contador = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
        while (numero >= 0) {
            JOptionPane.showMessageDialog(null, "El numero ingresado  " + numero + " es POSITIVO");
            contador++;
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero"));
        }
        JOptionPane.showMessageDialog(null, "A ingresado " + contador + "numeros positivos");

    }
}
