class Account {

  // Global variables of the class.
  // They're invoked with 'this.' in the constructor.
  Integer id;
  String name;
  String document;
  String email;
  String password;

  // public is used to declare constructor methods in Java.
  // Its arguments are created locally in the Account method.
  public Account(String name, String document) {
    this.name = name;
    this.document = document;
  }
}
