/**
 * UberVan is a subclass of Car class
 */

class UberVan extends Car {
    String typeCarAccepted;
    String[] seatMaterial;

    // UberVan constructor should containg at least the same parameters of its
    // superclass, then use 'super' to call the superclass constructor
    public UberVan(String license, Account driver,
            String typeCarAccepted, String[] seatMaterial) {
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatMaterial = seatMaterial;
    }
}
