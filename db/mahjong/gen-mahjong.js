(function(){'use strict';
/* JAH Mahjong Database generator — jahdb-mahjong-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MAHJONG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The 136 tiles", "Suits and honors", "The deal and the wall", "Mahjong drawing and discarding", "Chow, pung, and kong", "Winning hand structure", "Declaring riichi", "Furiten", "Dora", "Round wind and seat wind", "Basic table etiquette"], "Compounded": ["Yaku: riichi", "Yaku: tanyao", "Yaku: yakuhai", "Yaku: pinfu", "Yaku: iipeikou and sanshoku", "Yaku: honitsu and chinitsu", "Dora strategy", "Defense: suji", "Defense: kabe", "Tile efficiency basics", "Push-or-fold judgment", "Scoring: han and fu"], "Advanced": ["Yakuman hands", "Advanced tile efficiency: ukeire", "Betaori: full defense", "Damaten: concealed tenpai", "Atozuke", "Three-player sanma", "Tournament rules", "Online mahjong", "The history of mahjong", "Teaching mahjong", "Mahjong variants worldwide"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# mahjong-yaku-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 mahjong record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A mahjong record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"mahjong-yaku-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-mahjong-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mahjong',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
