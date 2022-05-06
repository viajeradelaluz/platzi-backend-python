/**
 * UberBlack is a subclass of Car class
 */

class UberBlack extends Car {
    String typeCarAccepted;
    String[] seatMaterial;

    // UberBlack constructor should containg at least the same parameters of its
    // superclass, then use 'super' to call the superclass constructor
    public UberBlack(String license, Account driver,
            String typeCarAccepted, String[] seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }
}
