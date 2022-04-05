#!/usr/bin/node
const args = process.argv;
let reps = args[2];

if (!args[2]) {
  console.log('Missing number of occurrences');
} else {
  for (reps; reps > 0; reps--) {
    console.log('C is fun');
  }
}
