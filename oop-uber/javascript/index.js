#!/usr/bin/node
/**
 * Practice of declaring classes and objects in Javascript.
 * This module is the entry point of the program.
 */

import Car from './car.js';
import Account from './account.js';
import Payment from './payment.js';

// Instancing objects of Car class
const car = new Car('GZW301', 'Guiller Hans');
car.passenger = 5;
car.print();

// Instancing objects of Account class
const account = new Account('Isabel Reyes');
account.email = 'isa-king@email.com';
account.print();

// Instancing objects of Payment class
const payment = new Payment();
payment.id = 15;
