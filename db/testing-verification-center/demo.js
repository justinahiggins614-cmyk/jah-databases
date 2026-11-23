"use strict";
const totals = [59, 17, 34, 26, 14, 125, 648, 26, 32, 40, 800, 174, 254, 84, 26, 1848, 5006, 50, 33, 133, 84, 85, 21, 103];
const grand = totals.reduce((a, b) => a + b, 0);
console.log("records: " + totals.length);
console.log("grand total of named figures: " + grand);
console.log("mean per record: " + (grand / totals.length).toFixed(1));
console.log("Result: records=" + totals.length + "|grand=" + grand);
