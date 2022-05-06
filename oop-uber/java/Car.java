class Car {

    // Global variables of the class.
    // They're invoked with 'this.' in the constructor.
    private Integer id;
    private String license;
    private Account driver;
    protected Integer passenger; // protected = restricted

    // public is used to declare constructor methods in Java.
    // Its arguments are created locally in the Car method.
    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
        this.id += 1;
    }

    // Getter
    public Integer getPassenger() {
        return passenger;
    }

    // Setter
    public void setPassenger(Integer passenger) {
        if (passenger >= 4) {
            this.passenger = passenger;
        } else {
            System.out.println("Value Error: All cars should have at least 4 passengers.");
        }
    }

    void printDataCar() {
        if (passenger != null) {
            System.out.println(
                    "License: " + license + " Driver Name: " + driver.name
                            + " Passengers: " + passenger);
        }
    }
}
