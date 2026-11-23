"use strict";
const totals = [50, 1539, 50, 27, 480, 14, 16, 490, 106, 70, 12412634, 30, 22, 24, 16, 8, 60, 19, 8, 14, 10, 55, 15, 17];
const grand = totals.reduce((a, b) => a + b, 0);
console.log("records: " + totals.length);
console.log("grand total of named figures: " + grand);
console.log("mean per record: " + (grand / totals.length).toFixed(1));
console.log("Result: records=" + totals.length + "|grand=" + grand);
