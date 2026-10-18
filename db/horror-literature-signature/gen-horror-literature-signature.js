(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-horror-literature-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HORS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Horror Fiction (Signature edition)",
  "Frankenstein (Signature edition)",
  "Dracula (Signature edition)",
  "The Strange Case of Dr Jekyll and Mr Hyde (Signature edition)",
  "The Turn of the Screw (Signature edition)",
  "The Haunting of Hill House (Signature edition)",
  "The Shining (Signature edition)",
  "The Exorcist (Signature edition)",
  "It (Signature edition)",
  "The Picture of Dorian Gray (Signature edition)",
  "Rosemary's Baby (Signature edition)"
 ],
 "Compounded": [
  "Gothic Horror Origins (Signature edition)",
  "Cosmic Horror and H.P. Lovecraft (Signature edition)",
  "The Haunted House Tradition (Signature edition)",
  "Vampire Fiction Beyond Dracula (Signature edition)",
  "Ghost Stories Tradition (Signature edition)",
  "Folk Horror (Signature edition)",
  "Body Horror (Signature edition)",
  "Psychological Horror (Signature edition)",
  "Shirley Jackson's Legacy (Signature edition)",
  "Clive Barker (Signature edition)",
  "Splatterpunk (Signature edition)",
  "Zombie Fiction Roots (Signature edition)"
 ],
 "Advanced": [
  "Horror Theory: Noel Carroll (Signature edition)",
  "The Final Girl Trope (Signature edition)",
  "Horror and Social Anxiety (Signature edition)",
  "Weird Fiction vs Horror (Signature edition)",
  "Quiet Horror (Signature edition)",
  "Extreme Horror Debates (Signature edition)",
  "Horror Literary Awards (Signature edition)",
  "Female Horror Writers (Signature edition)",
  "Hauntology in Horror (Signature edition)",
  "Horror Comedy (Signature edition)",
  "The Horror Renaissance (Signature edition)"
 ]
};
var DEMOKIND="tension-curve charting";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Tension-curve chart — "+safe+"\n"
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
    name:topic+' — music genre record',
    title:topic,
    description:'SIGNATURE SAMPLE (generated — structural sample). A music genre record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'signature',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:DEMOKIND,language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-horror-literature-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('horror-literature-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
