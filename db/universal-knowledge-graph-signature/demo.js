"use strict";
const totals = [63082, 164, 144, 24, 253, 60, 129, 150, 66, 205, 60, 366, 96, 65, 27, 132, 4, 10, 102, 22, 26, 438, 6, 192];
const grand = totals.reduce((a, b) => a + b, 0);
console.log("records: " + totals.length);
console.log("grand total of named figures: " + grand);
console.log("mean per record: " + (grand / totals.length).toFixed(1));
console.log("Result: records=" + totals.length + "|grand=" + grand);
