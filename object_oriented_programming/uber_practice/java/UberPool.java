/**
 * UberPool is a subclass of Car class
 */

class UberPool extends Car {

    String brand;
    String model;

    // UberPool constructor should containg at least the same parameters of its
    // superclass, then use 'super' to call the superclass constructor
    public UberPool(String license, Account driver, String brand, String model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}
