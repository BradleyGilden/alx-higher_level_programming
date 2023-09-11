#!/usr/bin/node

// a function that executes x times a function
exports.callMeMoby = function (x, callBack) {
  for (let i = 0; i < x; i++) {
    callBack();
  }
};
