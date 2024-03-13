#!/usr/bin/node

exports.converter = function (base) {
  return function of (num) {
    return num.toString(base);
  };
};
