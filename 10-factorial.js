#!/usr/bin/node
function factorial (nbr) {
  if (nbr === 1 || isNaN(nbr)) {
    return 1;
  }
  return nbr * factorial(nbr - 1);
}

const args = process.argv;
console.log(factorial(parseInt(args[2])));
