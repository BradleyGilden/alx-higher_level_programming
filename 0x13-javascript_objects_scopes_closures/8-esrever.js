#!/usr/bin/node

// a function that returns the reversed version of a list
exports.esrever = function (list) {
  const len = list.length;
  for (let i = 0, j = len - 1; i < Math.floor(len / 2); i++, j--) {
    [list[i], list[j]] = [list[j], list[i]];
  }
  return list;
};
