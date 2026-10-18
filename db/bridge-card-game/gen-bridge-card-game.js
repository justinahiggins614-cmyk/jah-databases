(function(){'use strict';
/* JAH Bridge Card Game Database generator — jahdb-bridge-card-game-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BRIDGE-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The deal and the roles", "Trick-taking basics", "Trump", "Scoring: part score, game, and slam", "The bidding ladder", "Opening 1NT: the 15-17 range", "Opening one of a suit", "Responding to opener", "Opener's rebid", "Dummy play basics", "Bridge table etiquette"], "Compounded": ["Stayman", "Jacoby transfers", "Blackwood ace-asking", "Gerber", "Weak two-bids", "Preemptive openings", "Overcalls", "Takeout doubles", "Finesses", "Ruffing losers in dummy", "Managing entries", "Counting the hand"], "Advanced": ["Roman Key Card Blackwood", "Splinter bids", "Cue-bidding toward slam", "Negative doubles", "Lebensohl", "Endplays", "Squeezes", "Deception in defense", "Defensive signals: attitude, count, suit preference", "Duplicate strategy: matchpoints vs IMPs", "Tournament bridge and masterpoints"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# bridge-hcp-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 bridge record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A bridge record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"bridge-hcp-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-bridge-card-game-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('bridge-card-game',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
