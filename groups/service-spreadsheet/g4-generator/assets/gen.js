
/* Sample-sheet generator core. Deterministic: same seed -> same sheet.
   Row labels are a shopping list; values are seeded numbers; the totals
   row uses real formulas, worked out by the sheet engine. */
function mulberry32(a){a=a>>>0||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var LABELS=['Apples','Bread','Cheese','Eggs','Milk'];
function makeSheet(seed){
  var rnd=mulberry32(seed);
  var values={};
  LABELS.forEach(function(lab,i){
    var r=i+1;
    values['A'+r]=lab;
    ['B','C','D'].forEach(function(c){ values[c+r]=String(1+Math.floor(rnd()*30)); });
  });
  values['A6']='Total';
  ['B','C','D'].forEach(function(c){ values[c+'6']='=SUM('+c+'1:'+c+'5)'; });
  return {seed:seed, kind:'sample sheet', labels:LABELS, values:values};
}
if(typeof module!=='undefined'){module.exports={makeSheet:makeSheet,mulberry32:mulberry32,LABELS:LABELS};}
