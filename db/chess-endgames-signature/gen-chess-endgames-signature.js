(function(){'use strict';
/* JAH Signature Chess Endgames Database generator — jahdb-chess-endgames-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHESSEND-SIG";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The Signature endgame ladder", "Signature king-activation drills", "The Signature square-count method", "Signature endgame opposition training", "Signature mate-in-isolation practice", "Signature simplification scoring", "The Signature pawn-race calculator", "Signature fortress recognition", "Signature tempo counting", "Signature study-reading method", "Signature endgame journaling"], "Compounded": ["The Northgate endgame method", "The Harborlight conversion system", "The Keystone technique", "The Ridgeline simplification plan", "The Fairwind pawn system", "The Stonebridge rook method", "The Thornfield minor-piece system", "The Beacon queen-ending system", "The Millrace practical system", "The Cinderline endgame defense", "The Gullwing attack", "The Foxglove transition"], "Advanced": ["Signature Endgame Study No. 1: The Harbor Draw (original composition)", "Signature Endgame Study No. 2: The Northgate Win (original composition)", "Signature Endgame Study No. 3: The Lantern Mate (original composition)", "Signature Endgame Study No. 4: The Tidewater Promotion (original composition)", "Signature Endgame Study No. 5: The Quarry Zugzwang (original composition)", "Signature Endgame Study No. 6: The Falcon Perpetual (original composition)", "Signature Endgame Study No. 7: The Millstone Mate (original composition)", "Signature Endgame Study No. 8: The Beacon Rook (original composition)", "Signature Endgame Study No. 9: The Cinder Stalemate (original composition)", "Signature Endgame Study No. 10: The Gullwing Conversion (original composition)", "Signature Chess Endgame Study No. 11: The Meridian (original composition)"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# chess-endgame-technique-demo \u2014 "+safe+"\n"
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
    name:topic+' \u2014 chess endgame record',
    title:topic,
    description:'SAMPLE RECORD (generated \u2014 structural sample). A chess endgame record of \"'+topic+'\" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"chess-endgame-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-chess-endgames-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('chess-endgames-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
