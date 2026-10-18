(function(){'use strict';
/* JAH Chess Tactics Database generator — jahdb-chess-tactics-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSTAC-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The fork: double attack essentials", "The pin: absolute and relative", "The skewer: reverse-pin tactics", "Discovered attack and double check", "Double check: the forced-mate tool", "Back-rank mate patterns", "Deflection: luring defenders away", "Decoy sacrifices that win material", "Removing the defender", "Overloading", "Clearance: vacating squares for the attack"], "Compounded": ["Zwischenzug: the in-between move", "X-ray attack", "The windmill", "Anastasia's mate: knight and rook", "Arabian mate: the corner finish", "Boden's mate: criss-crossing bishops", "Smothered mate: the knight's embrace", "Damiano's bishop mate", "Pawn-storm tactics", "Attacking the castled king: the Greek gift", "Exchange sacrifice decisions", "Interference: breaking the defenders' coordination"], "Advanced": ["Calculation: the candidate-moves method", "Prophylactic thinking in sharp positions", "Seizing the initiative in complications", "The desperado", "Swindles and stalemate tricks", "Perpetual-check combinations", "Underpromotion tactics", "Positional sacrifices", "Opposite-side castling attacks", "Endgame tactics", "Building a tactics training routine"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# chess-tactics-motif-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 chess tactic record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess tactic record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-tactics-motif-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-chess-tactics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chess-tactics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
