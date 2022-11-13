
package caja;

public class PruebaCaja {
    public static void main(String[] args) {
        //variables locales
        int medidaAncho = 3; // valores en cod. duro
        int medidaAlto = 2;
        int medidaProf = 6;
        
        Caja caja1 = new Caja(); // instanciamos el objeto, constructor vacío
        caja1.ancho = medidaAncho;
        caja1.alto = medidaAlto;
        caja1.profundidad = medidaProf;
        int resultado = caja1.calcularVolumen(); //llamamos al método
        
            System.out.println ("Resultado de volumen de caja 1 es: " +resultado);
            
            Caja caja2 = new Caja(2,4,6);// constructor con nuevos argumentos
            System.out.println ("Resultado de volumen de caja 2 es:  "+ caja2.calcularVolumen()); 
    }
    
}
