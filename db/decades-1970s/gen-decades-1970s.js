(function(){'use strict';
/* JAH The 1970s Database generator — jahdb-decades-1970s-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-D1970-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The 1970s at a Glance: Malaise and the Microchip - Foundations",
  "1970: The First Earth Day - Foundations",
  "1970: The Beatles Break Up - Foundations",
  "1971: The Intel 4004 \u2014 the First Microprocessor - Foundations",
  "1972: The Watergate Break-In - Foundations",
  "1972: Title IX - Foundations",
  "1973: Roe v. Wade - Foundations",
  "1973: The Oil Crisis - Foundations",
  "1974: Nixon Resigns - Foundations",
  "1975: The Fall of Saigon - Foundations"
 ],
 "Compounded": [
  "1970: The Kent State Shootings - Compounded",
  "1971: Email Is Invented - Compounded",
  "1972: Pong Launches Video Games - Compounded",
  "1972: The Munich Olympics Massacre - Compounded",
  "1973: Hip-Hop Is Born in the Bronx - Compounded",
  "1974: The First Barcode Scans - Compounded",
  "1975: Microsoft Is Founded - Compounded",
  "1975: Jaws Invents the Summer Blockbuster - Compounded",
  "1976: Apple Is Founded - Compounded",
  "1976: Viking Lands on Mars - Compounded",
  "1977: Star Wars Changes Everything - Compounded"
 ],
 "Advanced": [
  "1977: Voyager Launches for the Stars - Advanced",
  "1978: The First Test-Tube Baby - Advanced",
  "1978: The Camp David Accords - Advanced",
  "1979: Three Mile Island - Advanced",
  "1979: The Iran Hostage Crisis Begins - Advanced",
  "1979: The Sony Walkman - Advanced",
  "1973: The Endangered Species Act - Advanced",
  "1970: The EPA Is Founded - Advanced",
  "1972: Atari Is Founded - Advanced",
  "1977: The Apple II - Advanced",
  "1974: The Rubik's Cube Is Invented - Advanced",
  "1979: The First Commercial Cellular Network - Advanced",
  "1975: Saturday Night Live Premieres - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# 1970S — "+safe+"\n"
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
    name:topic+' — 1970s history record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A 1970s history record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"decades-1970s-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-decades-1970s-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('decades-1970s',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
