#!/usr/bin/node

export default class Car {
  constructor (license, driver) {
    this.id;
    this.license = license;
    this.driver = driver;
    this.passenger;
  }

  print () {
    console.log(`License: ${this.license} Driver: ${this.driver}`);
  }
}
