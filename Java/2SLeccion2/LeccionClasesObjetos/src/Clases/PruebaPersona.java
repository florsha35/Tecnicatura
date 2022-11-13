package Clases;


public class PruebaPersona {

    public static void main(String[] args) {

        Persona persona1;
        persona1 = new Persona(); //llamamos la constructor q nos permite crear valores
        persona1.nombre = "Florencia"; // el valor hexadecimal generalmete comienza con0x
        persona1.apellido = "Shapasnikoff";
        persona1.obtenerInformacion();

        Persona persona2 = new Persona();
        System.out.println("persona2 = " + persona2); //el da un valor en la memoria porq no tiene valor asignado
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre = "Federico";
        persona2.apellido = "Suter";
        persona2.obtenerInformacion();

    }

}
