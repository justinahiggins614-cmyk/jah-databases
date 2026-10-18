(function(){'use strict';
/* JAH The Best Design Evolution Database generator — jahdb-db-best-design-evolution-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BDE-";
var FIELDS=["Tech Evolution","Transport Evolution","Home Evolution"];
var TOPICS={
 "Tech Evolution": [
  "iPhone 2007 vs iPhone Now: Phone Evolution - Tech Evolution",
  "Brick Phone vs Smartphone: Mobile - Tech Evolution",
  "CRT vs OLED: Screens - Tech Evolution",
  "Floppy vs Cloud: Storage - Tech Evolution",
  "Dial-Up vs Fiber: Internet - Tech Evolution",
  "Film vs Digital: Cameras - Tech Evolution",
  "VHS vs Streaming: Video - Tech Evolution",
  "Walkman vs Spotify: Music - Tech Evolution",
  "Game Boy vs Switch: Handhelds - Tech Evolution",
  "PDA vs Smartphone: Precursors - Tech Evolution",
  "Typewriter vs Laptop: Writing - Tech Evolution"
 ],
 "Transport Evolution": [
  "Model T vs Tesla: Cars - Transport Evolution",
  "Wright Flyer vs 747: Flight - Transport Evolution",
  "Steam Locomotive vs Bullet Train: Rail - Transport Evolution",
  "Clipper Ship vs Container Ship: Sea - Transport Evolution",
  "Horse Carriage vs Car: Streets - Transport Evolution",
  "Bicycle: Penny-Farthing vs Modern - Transport Evolution",
  "Concorde vs 787: Airliners - Transport Evolution",
  "Sail vs Steam: Ships - Transport Evolution",
  "Zeppelin vs Airplane: Air - Transport Evolution",
  "Stagecoach vs Train: Land - Transport Evolution"
 ],
 "Home Evolution": [
  "Icebox vs Fridge: Cold - Home Evolution",
  "Wood Stove vs Central Heat: Warmth - Home Evolution",
  "Candle vs LED: Light - Home Evolution",
  "Washboard vs Washer: Laundry - Home Evolution",
  "Outhouse vs Bathroom: Plumbing - Home Evolution",
  "Radio vs TV vs Phone: Living Room - Home Evolution",
  "Sewing: Hand vs Machine - Home Evolution",
  "Kitchen: Hearth vs Smart - Home Evolution",
  "Bed: Straw vs Memory Foam - Home Evolution",
  "Chair: Throne vs Ergonomic - Home Evolution",
  "Table: Trestle vs Standing Desk - Home Evolution",
  "Window: Shutter vs Glass - Home Evolution",
  "Door: Curtain vs Smart Lock - Home Evolution"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Design Evolution Study — "+safe+"\n"
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
    name:topic+' — design evolution record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design evolution record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"design-evolution-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-best-design-evolution-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-best-design-evolution',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
