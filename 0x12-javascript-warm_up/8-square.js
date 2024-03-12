#!/usr/bin/node
const argument = parseInt(process.argv[2]);
if (!isNaN(argument)) {
  for (let i = 0; i < argument; i++) {
    let line = '';
    for (let j = 0; j < argument; j++) {
      line += 'X';
    }
    console.log(line);
  }
} else {
  console.log('Missing size');
}
