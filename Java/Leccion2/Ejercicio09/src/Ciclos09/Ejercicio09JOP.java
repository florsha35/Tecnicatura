package Ciclos09;
import javax.swing.JOptionPane;

public class Ejercicio09JOP {
     public static void main(String[] args) {
       
        
        int dia; 
        dia = Integer.parseInt(JOptionPane.showInputDialog("Digite el día:  "));
        int mes; 
        mes = Integer.parseInt(JOptionPane.showInputDialog("Digite el mes:  "));
        int anio;
        anio = Integer.parseInt(JOptionPane.showInputDialog("Digite el año: "));
        if ((dia != 0) && (dia <= 30)) {
            if ((mes != 0) && (mes <= 12)) {
                if ((anio != 0) && (anio <= 2022)) {
                    JOptionPane.showMessageDialog(null,"La fecha ingresada es : " + dia + "/" + mes + "/" + anio);
                } else {
                    JOptionPane.showMessageDialog(null, "Fecha ingresada incorrecta, el año es incorrecto");
                }
            }
            else {
                JOptionPane.showMessageDialog(null, "Fecha ingresada incorrecta, mes incorrecto");
            }
        }
        else{
            JOptionPane.showMessageDialog(null, "Fecha ingresada incorrecta, día incorrecto");
        }
    }
    
}
