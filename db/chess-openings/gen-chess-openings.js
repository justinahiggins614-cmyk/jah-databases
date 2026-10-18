(function(){'use strict';
/* JAH Chess Openings Database generator — jahdb-chess-openings-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSOP-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["How to read this database: ECO codes A00-E99", "The five opening principles", "Italian Game: ECO C50-C59", "Ruy Lopez: ECO C60-C99", "Scotch Game: ECO C44-C45", "French Defense: ECO C00-C19", "Caro-Kann Defense: ECO B10-B19", "Sicilian Defense: ECO B20-B99", "Queen's Gambit: ECO D06-D69", "London System: ECO D02, A46", "English Opening: ECO A10-A39"], "Compounded": ["Evans Gambit: ECO C51-C52", "Vienna Game: ECO C25-C29", "Petrov's Defense: ECO C42-C43", "Pirc Defense: ECO B07-B09", "Scandinavian Defense: ECO B01", "Alekhine's Defense: ECO B02-B05", "Nimzo-Indian Defense: ECO E20-E59", "King's Indian Defense: ECO E60-E99", "Grunfeld Defense: ECO D80-D99", "Dutch Defense: ECO A80-A99", "Catalan Opening: ECO E01-E09", "Reti Opening: ECO A04-A09"], "Advanced": ["Najdorf Variation: ECO B90-B99", "Sveshnikov Variation: ECO B33", "Dragon Variation: ECO B70-B79", "Marshall Attack: ECO C89", "Berlin Defense: ECO C65-C67", "Winawer Variation: ECO C15-C19", "Semi-Slav Defense: ECO D43-D49", "Trompowsky Attack: ECO A45", "Benko Gambit: ECO A57-A59", "Building a White repertoire", "Building a Black repertoire"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# chess-opening-repertoire-demo \u2014 "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record \u2014 structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' \u2014 chess opening record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess opening record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-opening-repertoire-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-chess-openings-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chess-openings',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
