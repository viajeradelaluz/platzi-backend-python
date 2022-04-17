/**
 * UberX is a subclass of Car class
 */

class UberX extends Car {

    String brand;
    String model;

    // UberX constructor should containg at least the same parameters of its
    // superclass, then use 'super' to call the superclass constructor
    public UberX(String license, Account driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}