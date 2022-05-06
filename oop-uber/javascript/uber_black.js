/**
 * UberBlack is a subclass of Car class
 */

class UberBlack extends Car {
  // UberBlack constructor should have at least the same arguments
  // of its superclass Car, then use 'super' to call them
  constructor(license, driver, typeCarAccepted, seatMaterial) {
    super(license, driver);
    this.typeCarAccepted = typeCarAccepted;
    this.seatMaterial = seatMaterial;
  }
}
