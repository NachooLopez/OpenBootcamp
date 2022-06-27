public class ex1 {
  public static void main(String[] args) {
    Cliente cliente = new Cliente();
    cliente.edad = 22;
    cliente.nombre = "Ignacio";
    cliente.telefono = 1234567890;
    cliente.credito = 2.3;

    System.out.println(cliente.edad);
    System.out.println(cliente.nombre);
    System.out.println(cliente.telefono);
    System.out.println(cliente.credito);

    Trabajador trabajador = new Trabajador();
    trabajador.edad = 25;
    trabajador.nombre = "Lourdes";
    trabajador.telefono = 1234567892;
    trabajador.salario = 10.2;

    System.out.println(trabajador.edad);
    System.out.println(trabajador.nombre);
    System.out.println(trabajador.telefono);
    System.out.println(trabajador.salario);
  }
}

class Persona {
  int edad;
  String nombre;
  int telefono;
}

class Cliente extends Persona {
  double credito;
}

class Trabajador extends Persona {
  double salario;
}