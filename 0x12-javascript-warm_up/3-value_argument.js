#!/usr/bin/node
const argv = process.argv;
if (argv[2] == undefined) {
  console.log('No Argument');
} else {
  console.log(argv[2]);
}
