#!/usr/bin/node
const square2 = require('./5-square');

class Square extends square2 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width;) {
        x += c;
      }
      console.log(x);
    }
  }
}

module.exports = Square;
