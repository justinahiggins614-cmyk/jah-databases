(function(){'use strict';
/* JAH The Visual Pattern Database Database generator — jahdb-db-visual-pattern-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VISPAT-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Pattern: Red circle, blue circle, red circle, blue circle,...",
  "Pattern: 1 dot, 2 dots, 3 dots, 4 dots,...",
  "Pattern: Big square, small square, big square, small square,...",
  "Pattern: Arrow up, arrow right, arrow down, arrow left,...",
  "Pattern: Triangle, square, pentagon, hexagon,...",
  "Pattern: Circle, circle with dot, circle with 2 dots,...",
  "Pattern: Black, white, black, white,...",
  "Pattern: 1 line, 2 lines, 3 lines (making angles),...",
  "Pattern: Small, medium, large, small, medium, large,...",
  "Pattern: Star, heart, star, heart,...",
  "Pattern: Up arrow, down arrow, up arrow, down arrow,..."
 ],
 "Compounded": [
  "Pattern: 1 square, 4 squares (2x2), 9 squares (3x3),...",
  "Pattern: Red, red, blue, red, red, blue,...",
  "Pattern: Circle, oval, circle, oval (rotating 90 deg each)...",
  "Pattern: 1, 11, 21, 1211, 111221 (look-and-say)...",
  "Pattern: Black dot moving clockwise around a square's corners...",
  "Pattern: Growing bar: 1, 2, 4, 8 units tall...",
  "Pattern: Alternating arrow directions AND growing length...",
  "Pattern: Nested squares: 1, 2, 3 nested...",
  "Pattern: Checkerboard 2x2, 4x4, 6x6...",
  "Pattern: Spiral with 1, 2, 3 turns...",
  "Pattern:  Dominoes: 1-2, 2-3, 3-4...",
  "Pattern: Moon phases: new, crescent, half, gibbous, full..."
 ],
 "Advanced": [
  "Pattern: Penrose impossible triangle rotating...",
  "Pattern: Fractal tree: each branch splits in two...",
  "Pattern: 1, 2, 4, 8, 16 dots in circles (powers of 2)...",
  "Pattern: Fibonacci squares: 1,1,2,3,5,8...",
  "Pattern: Rotating cube nets: which folds to a cube...",
  "Pattern: Escher-like tessellation growing...",
  "Pattern: Knight's tour partial path on chessboard...",
  "Pattern: Overlapping circles: 1, 3, 7 regions (Venn)...",
  "Pattern: Moiré patterns from overlapping grids...",
  "Pattern: Golden spiral from Fibonacci squares...",
  "Pattern: Cellular automaton row 1, 2, 4, 8 live cells..."
 ]
};
var DEMOKIND="pattern-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Visual Pattern Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — visual pattern record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A visual pattern record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-db-visual-pattern-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-visual-pattern',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
