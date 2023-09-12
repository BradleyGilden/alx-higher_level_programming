#!/usr/bin/node

/**
 * A new list must be created with each value equal to the value of the
 * initial list, multipled by the index in the list
 */
const list = require('./100-data').list;

const nlist = list.map((index, value) => { return index * value; });
console.log(list);
console.log(nlist);
