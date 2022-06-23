public class Main {
    public static void main(String[] args) {
        System.out.println(sumNums(2, 3, 5));
        Coche miCoche = new Coche();
        miCoche.anadirPuertas();
        System.out.println(miCoche.puertas);
    }

    public static int sumNums(int a, int b, int c) {
        return a + b + c;
    }

    static class Coche {
        public int puertas;
        public void anadirPuertas() {
            this.puertas = puertas + 1;
        }
    }
}