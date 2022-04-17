/**
 * Practice of declaring classes and objects in Java.
 * Class Main is the entry point of the program.
 */

class Main {

    public static void main(String[] args) {
        // Instancing an object 'car' of Car class
        Car car = new Car("AMQ123", new Account("Juan Herrea", "1026"));
        car.setPassenger(2);
        car.printDataCar();

        // Instancing an object UberX (subclass of Car)
        UberX uberX = new UberX("KJL890", new Account("Laura Bello", "1032"), "Volvo", "2021");
        uberX.setPassenger(4);
        uberX.printDataCar();
    }
}
