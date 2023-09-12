#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  for (const items of list) {
    occurences = items === searchElement ? occurences + 1 : occurences;
  }
  return occurences;
};
