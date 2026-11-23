"use strict";
const totals = [46, 243, 30, 16, 8, 57, 1506, 18, 18, 487, 9, 24, 502, 260, 969, 11, 12, 1210, 9, 33, 62, 249, 54, 494];
const grand = totals.reduce((a, b) => a + b, 0);
console.log("records: " + totals.length);
console.log("grand total of named figures: " + grand);
console.log("mean per record: " + (grand / totals.length).toFixed(1));
console.log("Result: records=" + totals.length + "|grand=" + grand);
