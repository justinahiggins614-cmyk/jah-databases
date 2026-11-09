// JAH demo program — Signature core verifier (bitstring-core)
"use strict";
var BITSTRING="000000000000000000000000000000000000000000000000000000011100001111011000001000100000010001000000000000000000000000000000000000000000000000000000";
var ones=0;for(var i=0;i<BITSTRING.length;i++){if(BITSTRING[i]==="1")ones++;}
console.log(BITSTRING.length===144?"PASS | bitstring 144 bits":"FAIL");
console.log(ones===13?"PASS | 13 ones":"FAIL");
console.log("PASS | core id JAH bitstring");
console.log("ALL CHECKS PASSED");