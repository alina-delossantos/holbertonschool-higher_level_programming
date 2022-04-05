#!/usr/bin/node
const Xchar = parseInt(process.argv[2]);
let reps;

if (!Xchar) {
  console.log('Missing size');
} else {
  for (reps = 0; reps < Xchar; reps++) {
    console.log('X'.repeat(Xchar));
  }
}
