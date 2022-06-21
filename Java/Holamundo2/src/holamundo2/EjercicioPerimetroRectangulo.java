package holamundo2;

import java.util.Scanner;

public class EjercicioPerimetroRectangulo {
    public static void main(String [] args) {
        
    
        Scanner entrada = new Scanner (System.in);           
        
            
    System.out.print(" digitel el alto del rectangulo: ");
    int alto = Integer.parseInt(entrada.nextLine());
    System.out.print(" digitel el ancho del rectangulo: ");
    int ancho = Integer.parseInt(entrada.nextLine());
    int resultado = (alto * ancho);
    int perimetro = (alto * ancho) * 2;
    System.out.println("El area del rectangulo es: = " + resultado);
    System.out.println("El perimetro del rectangulo es = " + perimetro);   
    
        
    }  
}
