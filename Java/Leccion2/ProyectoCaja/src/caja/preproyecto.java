package caja;

import java.util.Scanner;

public class preproyecto {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int precio1 = 800, precio2 = 1200, precio3 = 2100;

        System.out.println("¿Desea agregar un servicio adicional?\n 1-SI\n 2-NO");
        int servicio = Integer.parseInt(entrada.nextLine());
        
        if (servicio == 1) {
            System.out.println("Digite una opcion:  \n 1-Busqueda por su alojamiento  \n 2-Vianda en destino  \n 3-Pack Souvenit");
            int opcion = Integer.parseInt(entrada.nextLine());
            if (opcion == 1) {
                System.out.println("El adicional tiene un valor de :$" + precio1);
            }
            if (opcion == 2) {
                System.out.println("El adicional tiene un valor de :$" + precio2);
            }
            if (opcion == 3) {
                System.out.println("El adicional tiene un valor  :$" + precio3);
            } //} else if (servicio == 2) {
            //    pass // return to "total payment"
            else {
                System.out.println("El digito ingresado no es valido");
            }
            
           // System.out.println("¿Desea agregar otro servicio? \n 1-SI \n 2-NO");
            //int nuevoSs = Integer.parseInt(entrada.nextLine());
            //if (nuevoSs == 1) {
           // return // linea14 and add payments
        }
    }
}

//else if  (nuevoSs == 2{
// go to total payment

