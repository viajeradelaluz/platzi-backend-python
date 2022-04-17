/**
 * UberX is a subclass of Car class
 */

class UberX extends Car {
  // UberX constructor should have at least the same arguments
  // of its superclass Car, then use 'super' to call them
  constructor(license, driver, brand, model) {
    super(license, driver);
    this.brand = brand;
    this.model = model;
  }
}
