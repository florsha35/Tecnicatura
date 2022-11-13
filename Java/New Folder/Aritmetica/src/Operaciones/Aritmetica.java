package Operaciones;

public class Aritmetica {

    //Atributos de la clase
    int a;
    int b;

    //EL CONSTRUCTOR - metodo especiall
    public Aritmetica() {
        System.out.println("Se esta ejecutando el constructor num1");
    }

    //SOBRECARGA DE CNSTRUCTORES
    public Aritmetica(int a, int b) {
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando el constructor num2");
    }

    //METODO
    public void SumarNumeros() {
        int resultado = a + b;
        System.out.println("resultado = " + resultado);
    }

    public int sumarConRetorno() { // int resultado = a+ b;
        int resultado = a +b;
        return resultado;        
        //return a + b; otra opcion        
    }
    
    public int sumarConArgumentos(int arg1, int arg2){
    this.a = arg1;
    this.b = arg2;
    return sumarConRetorno();
    }

}
