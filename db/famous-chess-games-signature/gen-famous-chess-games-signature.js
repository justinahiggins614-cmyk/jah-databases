(function(){'use strict';
/* JAH Signature Famous Chess Games Database generator — jahdb-famous-chess-games-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSFAM-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["How to read a Signature immortal", "The Signature brilliancy blueprint", "Signature opening drama", "Signature middlegame storms", "Signature endgame poetry", "The Signature sacrifice ethic", "Signature time-trouble heroics", "Signature defensive masterpieces", "Signature miniature method", "Signature annotation style", "The Signature study habit"], "Compounded": ["Signature Immortal No. 1: The Harbor Storm (original composition)", "Signature Immortal No. 2: The Northgate Siege (original composition)", "Signature Immortal No. 3: The Lantern Hunt (original composition)", "Signature Immortal No. 4: The Tidewater Sacrifice (original composition)", "Signature Immortal No. 5: The Quarry Defense (original composition)", "Signature Immortal No. 6: The Falcon's Dive (original composition)", "Signature Immortal No. 7: The Millstone Grind (original composition)", "Signature Immortal No. 8: The Beacon's Light (original composition)", "Signature Immortal No. 9: The Cinder Rebirth (original composition)", "Signature Immortal No. 10: The Gullwing Soar (original composition)", "Signature Immortal No. 11: The Foxglove Quiet (original composition)", "Signature Immortal No. 12: The Keystone (original composition)"], "Advanced": ["Signature Masterpiece No. 1: The Meridian Game (original composition)", "Signature Masterpiece No. 2: The Tidal Game (original composition)", "Signature Masterpiece No. 3: The Forge Game (original composition)", "Signature Masterpiece No. 4: The Mirror Game (original composition)", "Signature Masterpiece No. 5: The Labyrinth Game (original composition)", "Signature Masterpiece No. 6: The Phoenix Game (original composition)", "Signature Masterpiece No. 7: The Eclipse Game (original composition)", "Signature Masterpiece No. 8: The Constellation Game (original composition)", "Signature Masterpiece No. 9: The Hourglass Game (original composition)", "Signature Masterpiece No. 10: The Tapestry Game (original composition)", "Signature Masterpiece No. 11: The Signature Game (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# famous-game-analyzer-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 famous chess game record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A famous chess game record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"famous-game-analyzer-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-famous-chess-games-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('famous-chess-games-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
