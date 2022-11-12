
package ciclos04;
import javax.swing.JOptionPane;

public class Ejercicio06JPO {
    public static void main(String[] args) {
        int numero, suma = 0;
        do {
                        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            suma += numero;
        } while (numero != 0);
        JOptionPane.showMessageDialog(null, " La suma de todos los numero ingresadoes es:" + suma);
    }
    
}
