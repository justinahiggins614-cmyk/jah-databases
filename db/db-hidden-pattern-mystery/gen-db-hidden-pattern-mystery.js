(function(){'use strict';
/* JAH The Hidden Pattern Mystery Database generator — jahdb-db-hidden-pattern-mystery-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MHPM-";
var FIELDS=["Number Patterns","Visual Patterns","Word Patterns"];
var TOPICS={
 "Number Patterns": [
  "The Fibonacci Footsteps \u2014 Number Patterns",
  "The Fibonacci Footsteps \u2014 Deep Dive \u2014 Number Patterns",
  "The Prime Number Letters \u2014 Number Patterns",
  "The Prime Number Letters \u2014 Deep Dive \u2014 Number Patterns",
  "The Magic Square Safe \u2014 Number Patterns",
  "The Magic Square Safe \u2014 Deep Dive \u2014 Number Patterns",
  "The Doubling Safe \u2014 Number Patterns",
  "The Doubling Safe \u2014 Deep Dive \u2014 Number Patterns",
  "The Triangular Numbers \u2014 Number Patterns",
  "The Triangular Numbers \u2014 Deep Dive \u2014 Number Patterns",
  "The Square Numbers \u2014 Number Patterns",
  "The Square Numbers \u2014 Deep Dive \u2014 Number Patterns",
  "The Collatz Countdown \u2014 Number Patterns",
  "The Collatz Countdown \u2014 Deep Dive \u2014 Number Patterns",
  "The Cicada Years \u2014 Number Patterns",
  "The Cicada Years \u2014 Deep Dive \u2014 Number Patterns",
  "The Master Pattern \u2014 Number Patterns",
  "The Master Pattern \u2014 Deep Dive \u2014 Number Patterns"
 ],
 "Visual Patterns": [
  "The Fractal Fern \u2014 Visual Patterns",
  "The Fractal Fern \u2014 Deep Dive \u2014 Visual Patterns",
  "The Symmetrical Garden \u2014 Visual Patterns",
  "The Symmetrical Garden \u2014 Deep Dive \u2014 Visual Patterns",
  "The Golden Ratio Room \u2014 Visual Patterns",
  "The Golden Ratio Room \u2014 Deep Dive \u2014 Visual Patterns",
  "The Tessellated Floor \u2014 Visual Patterns",
  "The Tessellated Floor \u2014 Deep Dive \u2014 Visual Patterns",
  "The Spiral Staircase \u2014 Visual Patterns",
  "The Spiral Staircase \u2014 Deep Dive \u2014 Visual Patterns"
 ],
 "Word Patterns": [
  "The Palindrome Plaque \u2014 Word Patterns",
  "The Palindrome Plaque \u2014 Deep Dive \u2014 Word Patterns",
  "The Anagram Letters \u2014 Word Patterns",
  "The Anagram Letters \u2014 Deep Dive \u2014 Word Patterns",
  "The Word Ladder \u2014 Word Patterns",
  "The Word Ladder \u2014 Deep Dive \u2014 Word Patterns"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hidden Pattern Study — "+safe+"\n"
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
    name:topic+' — hidden pattern case record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hidden pattern case record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-hidden-pattern-mystery-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-hidden-pattern-mystery',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
