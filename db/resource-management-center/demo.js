"use strict";
const totals = [36, 131, 1098, 28, 190, 484, 17, 136, 129, 1539, 158, 44, 60, 102, 1490, 1251, 108, 1008, 6, 21, 18, 250, 9, 255];
const grand = totals.reduce((a, b) => a + b, 0);
console.log("records: " + totals.length);
console.log("grand total of named figures: " + grand);
console.log("mean per record: " + (grand / totals.length).toFixed(1));
console.log("Result: records=" + totals.length + "|grand=" + grand);
