(function(){'use strict';
/* JAH The World's Most Unusual Buildings Database generator — jahdb-db-world-s-most-unusual-buildings-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WSMUB-";
var FIELDS=["Twisted & Dancing","Impossible Shapes","Playful Wonders"];
var TOPICS={
 "Twisted & Dancing": [
  "Dancing House vs Twisting Tower: Curves - Twisted & Dancing",
  "Gherkin vs Walkie-Talkie: London Icons - Twisted & Dancing",
  "Burj vs Shanghai Tower: Twisted Giants - Twisted & Dancing",
  "Absolute Towers vs Piano Building: Whimsy - Twisted & Dancing",
  "CCTV vs Linked Hybrid: Beijing Bold - Twisted & Dancing",
  "Sagrada Familia vs Gaudi Houses: Organic - Twisted & Dancing",
  "Guggenheim vs Disney Hall: Curves - Twisted & Dancing",
  "Marina Bay vs Interlace: Singapore Stacks - Twisted & Dancing",
  "Vessel vs Big Duck: Sculptural - Twisted & Dancing",
  "Torre Agbar vs Gherkin: Ovoids - Twisted & Dancing",
  "Eden Project vs Biosphere: Geodesic Wonders - Twisted & Dancing"
 ],
 "Impossible Shapes": [
  "Basket Building vs Duck: Mimetic - Impossible Shapes",
  "Atomium vs Eiffel: Expo Icons - Impossible Shapes",
  "Habitat 67 vs Nakagin: Modular Dreams - Impossible Shapes",
  "Ryugyong vs Torre David: Unfinished - Impossible Shapes",
  "Lotus Temple vs Opera House: Sacred Curves - Impossible Shapes",
  "Krzywy Domek vs Kunsthaus: Blobs - Impossible Shapes",
  "Cactus Tower vs Bosco Verticale: Green - Impossible Shapes",
  "Bibliotheca vs Seattle Library: Bookish - Impossible Shapes"
 ],
 "Playful Wonders": [
  "Upside-Down House vs Crooked House: Playful - Playful Wonders",
  "Gardens by the Bay vs Supertrees: Future Nature - Playful Wonders",
  "Lego House vs Real: Toy Scale - Playful Wonders",
  "Ice Hotel vs Igloo Village: Frozen - Playful Wonders",
  "Treehouse Hotel vs Cabin: Treetops - Playful Wonders",
  "Capsule Hotel vs Pod: Tiny Sleep - Playful Wonders",
  "Underwater Hotel vs Overwater: Water Sleep - Playful Wonders",
  "Cave Hotel vs Cliff Hotel: Rock Sleep - Playful Wonders",
  "Revolving Restaurant vs Rooftop: Views - Playful Wonders",
  "Library of Congress vs Trinity: Book Halls - Playful Wonders",
  "Grand Central vs St Pancras: Stations - Playful Wonders",
  "Fallingwater vs Villa Savoye: Modern Icons - Playful Wonders",
  "Sydney vs Guggenheim: Harbor vs River - Playful Wonders",
  "Pantheon vs Parthenon: Ancient Perfect - Playful Wonders",
  "Blue Mosque vs Hagia Sophia: Istanbul - Playful Wonders"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Unusual Buildings Study — "+safe+"\n"
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
    name:topic+' — architecture comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A architecture comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"unusual-buildings-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-world-s-most-unusual-buildings-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-world-s-most-unusual-buildings',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
