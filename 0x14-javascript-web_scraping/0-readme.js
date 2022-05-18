#!/usr/bin/node
// reads and prints readme file
const fs = require('fs');
const fileToRead = process.argv[2];

fs.readFile(fileToRead, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
