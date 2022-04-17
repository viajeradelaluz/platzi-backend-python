#!/usr/bin/node

export default class Account {
  constructor (name, document) {
    this.id;
    this.name = name;
    this.document = document;
    this.email;
    this.password;
  }

  print () {
    console.log(`Account name: ${this.name} | email: ${this.email}`);
  }
}
