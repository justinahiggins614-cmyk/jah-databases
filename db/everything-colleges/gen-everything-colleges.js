(function(){'use strict';
/* JAH The Everything Colleges Database generator — jahdb-everything-colleges-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-EVCOL-";
var FIELDS=["US \u2014 Private Research Universities","US \u2014 Public Flagship Universities","US \u2014 Liberal Arts Colleges","US \u2014 Institutes & Specialized Universities","Europe","Asia & Pacific"];
var TOPICS={
 "US \u2014 Private Research Universities": [
  "Harvard University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Yale University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Princeton University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Stanford University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Massachusetts Institute of Technology \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Columbia University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "University of Chicago \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Cornell University \u2014 Institution Record \u2014 US \u2014 Private Research Universities",
  "Duke University \u2014 Institution Record \u2014 US \u2014 Private Research Universities"
 ],
 "US \u2014 Public Flagship Universities": [
  "University of California, Berkeley \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of California, Los Angeles \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of Michigan \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of Virginia \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "The University of Texas at Austin \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of North Carolina at Chapel Hill \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of Wisconsin\u2013Madison \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities",
  "University of Washington \u2014 Institution Record \u2014 US \u2014 Public Flagship Universities"
 ],
 "US \u2014 Liberal Arts Colleges": [
  "Williams College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Amherst College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Swarthmore College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Wellesley College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Pomona College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Oberlin College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Bowdoin College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges",
  "Smith College \u2014 Institution Record \u2014 US \u2014 Liberal Arts Colleges"
 ],
 "US \u2014 Institutes & Specialized Universities": [
  "California Institute of Technology \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Carnegie Mellon University \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Georgia Institute of Technology \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Rensselaer Polytechnic Institute \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Johns Hopkins University \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Northwestern University \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "New York University \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities",
  "Vanderbilt University \u2014 Institution Record \u2014 US \u2014 Institutes & Specialized Universities"
 ],
 "Europe": [
  "University of Oxford \u2014 Institution Record \u2014 Europe",
  "University of Cambridge \u2014 Institution Record \u2014 Europe",
  "Imperial College London \u2014 Institution Record \u2014 Europe",
  "ETH Zurich \u2014 Institution Record \u2014 Europe",
  "Sorbonne University \u2014 Institution Record \u2014 Europe",
  "University of Bologna \u2014 Institution Record \u2014 Europe",
  "Ludwig Maximilian University of Munich \u2014 Institution Record \u2014 Europe",
  "Trinity College Dublin \u2014 Institution Record \u2014 Europe",
  "University of Edinburgh \u2014 Institution Record \u2014 Europe"
 ],
 "Asia & Pacific": [
  "The University of Tokyo \u2014 Institution Record \u2014 Asia & Pacific",
  "Kyoto University \u2014 Institution Record \u2014 Asia & Pacific",
  "Peking University \u2014 Institution Record \u2014 Asia & Pacific",
  "Tsinghua University \u2014 Institution Record \u2014 Asia & Pacific",
  "National University of Singapore \u2014 Institution Record \u2014 Asia & Pacific",
  "The University of Melbourne \u2014 Institution Record \u2014 Asia & Pacific",
  "Seoul National University \u2014 Institution Record \u2014 Asia & Pacific",
  "Indian Institute of Technology Bombay \u2014 Institution Record \u2014 Asia & Pacific"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Everything Colleges — "+safe+"\n"
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
    name:topic+' — college record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A college record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-everything-colleges-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('everything-colleges',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
