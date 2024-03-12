#!/usr/bin/node
const numArguments = process.argv.length - 2;
if (numArguments === 0) {
  console.log('No argument');
}
if (numArguments === 1) {
  console.log('Argument found');
}
if (numArguments > 1) {
  console.log('Arguments found');
}
