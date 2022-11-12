
package ciclos04;

import javax.swing.JOptionPane;
public class Ejercicio05JPopc  {

    public static void main(String[] args) {
        

        int numero, aleatorio, conteo = 0; //creo el aleatorio
        aleatorio = (int) (Math.random() * 100);
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero entre 1 y 100:  "));
            if (numero < aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero mayor");
            } else if (numero > aleatorio) {
                JOptionPane.showMessageDialog(null, "Digite un numero menor");
            } else {
                JOptionPane.showMessageDialog(null, "Felicidades, has acertado");
            }
            conteo++;
        } while (numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el número en " + conteo + " intentos");
    }

}
    

