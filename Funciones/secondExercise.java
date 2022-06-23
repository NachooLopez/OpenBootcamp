public class secondExercise {
  public static void main(String[] args) {
    Coche miCoche = new Coche();
    miCoche.anadirPuertas();
    System.out.println(miCoche.puertas);
  }

}

class Coche {
  public int puertas;

  public void anadirPuertas() {
    this.puertas = puertas + 1;
  }
}