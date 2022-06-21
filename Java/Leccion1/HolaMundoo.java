
import java.util.Scanner;

// Nuestro Primer Programa Hola Mundo
public class HolaMundoo {

    public static void main(String[] args) {
        /*System.out.println("Hola Mundo desde Java");
        
        int miVariable = 10;
        System.out.println(miVariable);
        miVariable = 5;
        System.out.println(miVariable);
        //Tipo String
        String miVariablecadena = "Bienvenidos";
        System.out.println(miVariablecadena);
        miVariablecadena = "sigamos creciendo en progrmacion";
        System.out.println(miVariablecadena);
         */

 /*/ Var - inferencia de tipos de Java
        var miVariableEntera2 = 10;
        var miVariableCadena2 = "seguimos estudiando";
        System.out.println("miVariableEntera2 = " + miVariableEntera2);
        System.out.println("miVariableCadena2 = " + miVariableCadena2);
        //soutv + tecla tab
        //Reglas para definir una variable en Java */
 /*var usuario = "Flor";
        var titulo = "Abogada";
        var union = titulo + "  " + usuario;
        System.out.println("union = " + union);

        var a = 8;
        var b = 4;
        System.out.println(usuario + "  " + (a + b));
        // ejercicio caracteres especiales
        var nombre = "Florencia";
        System.out.println("\n nueva linea: \n" + nombre); // con diagonal inversa n = salto de linea
        System.out.println("tabulador: \t" + nombre); //TABULADOR
        System.out.println("\t \t :MENU:"); // espacios para centrar
        System.out.println("retroseso: \b" + nombre); // caracter de retroseso --> borra un lugar hacia atras
        System.out.println("Comillas simples: \' "+ nombre + "\'");
        System.out.println("Comillas dobles:  \"" + nombre + "\""); */
 /*/Clase Scanner
        Scanner entrada  = new Scanner(System.in);
        System.out.println("Digite su nombre:  ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo:  ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: " + titulo2 + " " + usuario2); */
 /*/Scanner actividad del libro
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite el titulo del libro: ");
        var titulo = entrada.nextLine();
        System.out.println("Digitte el autor del libro: ");
        var autor = entrada.nextLine();
        System.out.println(titulo +"  "+ "fue escrito por" +"  "+ autor);
         */
 /* byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte"+ Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte"+ Byte.MAX_VALUE);
                
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroint = " + numEnteroInt);
        System.out.println("Valor minimo del int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del long: " + Long.MIN_VALUE);
        System.out.println("Valor maximo del long: " + Long.MAX_VALUE); */
 /*float numFloat = 3.4028235E38F;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: " + Float.MAX_VALUE); 
        
        double numDouble = 10;
        System.out.println("numDouble = " + numDouble);
        System.out.println("Valor minimo del double: " + Double.MIN_VALUE);
        System.out.println("Valor maximo del double: " + Double.MAX_VALUE);*/
 /*/Inferencia de tipos var y tipos primitivos
       var numEntero = 20; // Las literales sin punto automaticamnte son de tipo entero
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0; // automaticamente con el punto se transfortma en float
        System.out.println("numFloat = " + numFloat);
        var numDouble =10.0F;
        System.out.println("numDouble = " + numDouble); */
 /*/Tipos primitivos Char
       char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter ='\u0024'; //indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; // valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; // un caracter especial, podemos copiar y oegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter1 ='\u0024'; //indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracte1r = " + varCaracter1);
        var varCaracterDecimal1 = (char)36; // valor decimal entonces tengo q ponerle char
        System.out.println("varCaracterDecimal1 = " + varCaracterDecimal1);
        var varCaracterSimbolo1 = '$'; // un caracter especial, podemos copiar y oegar desde unicode
        System.out.println("varCaracterSimbolo1 = " + varCaracterSimbolo1);
        
        int varEnteroChar ='$'; // nos muestra el valor decimea del simbolo utilizado
        System.out.println("varEnteroChar = " + varEnteroChar);
        int EnteroChar = 'b';
        System.out.println("EnteroChar = " + EnteroChar); */
 /*/Tipos primitivos tipos booleanos
       boolean varBool = false;
        System.out.println("varBool = " + varBool);
        
        if(varBool){
            System.out.println("La bandera es verde");
        }
        else{
            System.out.println("La bandera es roja");
            
       // Es mayor de edad
       var edad = 12 ; // Literal tener presente la inferencia de tipos
       var adulto = edad >= 18; //esta es una expresion booleanna
       if(adulto){
           System.out.println("Eres mayor de edad");           
       }
       else{
           System.out.println("Eres menor de edad");
       } 
       
      
            
        } */
 /*/Conversion de tipos primitivos
       var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad + 1));

        var valorPi = Double.parseDouble("3.1416");
        System.out.println("valorPi = " + valorPi);*/
        //Pedir un valor
//        var entrada = new Scanner(System.in);
//        System.out.println("Digite su edad");
//        edad = Integer.parseInt(entrada.nextLine());
//        System.out.println("edad = " + edad); */
//        //Conversion de tipos primitivos en Java Parte 2
//        var edadTexto = String.valueOf(10);
//        System.out.println("edadTexto = " + edadTexto);
//        var fraseChar = "programadores".charAt(11);
//        System.out.println("fraseChar = " + fraseChar);
//        
//        System.out.println("Digite un caracter: ");
//        fraseChar = entrada.nextLine().charAt(0);
//        System.out.println("fraseChar = " + fraseChar);
//           int num1 =5, num2 = 4;
//           var solucion = num1 + num2; // aca no concatena porque la variable es INT , es una operacion aritmetica
//           System.out.println("solucion de la suma = " + solucion);
//           
//           solucion = num1 - num2;
//           System.out.println(" solucion de la resta = " +  solucion);
//           
//           solucion = num1 * num2;
//           System.out.println("solucion de la multiplicacion = " + solucion);
//           
//           solucion = num1 / num2;
//           System.out.println("solucion de la division = " + solucion);
//           
//           var solucion2= 3.4 / num2;
//           System.out.println("solucion2el resultado de la division = " + solucion2 );   // al usar un numero con coma.. ya lo considera float solo, no hace falta indicarlos
//                   
//           solucion = num1 % num2; // guarda el residuo entero de la division
//           System.out.println("solucion = " + solucion);
//           
//           if (num2 % 2 == 0)
//               System.out.println("Es un numero par");
//           else
//               System.out.println("El numero es impar");
//              int varNum1 = 4, varNum2 = 4;
//              int varNum3 = varNum1 + 6 - varNum2;
//              System.out.println("varNum3 = " + varNum3 );
//              
//              varNum1 +=1; //
//              System.out.println("varNum1 = " + varNum1);
//              
//              varNum1 -= 2;
//              System.out.println("varNum1 = " + varNum1);
//              
//              varNum1 *= 2;
//              System.out.println("varNum1 = " + varNum1);
//                      
//               varNum1 /= 2;
//               System.out.println("varNum1 = " + varNum1);
//               
//               varNum1 %= 3;
//               System.out.println("varNum1 = " + varNum1);
// Operadores unarios: Cambio de Signo
//        var varA = 7;
//        var varB = -varA;
//        System.out.println("varA = " + varA);
//        System.out.println("varB = " + varB); // mismo rdo con el cambio de signo
        
//        //Operador de negacion
//        var varC = true; //tipo boolean
//        var varD = !varC;
//        System.out.println("varC = " + varC);
//        System.out.println("varD = " + varD);
        
        //operadores unarios de inremento : preincremento
        var varE = 9; // se va a modificar su valor
        var varF = ++varE; //el simbolo antes de la variable
       // priumero se incrementa la varibale y desp se une su valor
        System.out.println("varE = " + varE); // se incrementa en la unidad
        System.out.println("varF = " + varF);// va a sumar uno

    }

}
