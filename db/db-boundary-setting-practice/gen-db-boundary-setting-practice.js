(function(){'use strict';
/* JAH The Boundary Setting Practice Database Database generator — jahdb-db-boundary-setting-practice-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BOUSETPRA-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Boundary: A friend asks to copy your homework...",
  "Boundary: Someone keeps borrowing your pen without asking...",
  "Boundary: A friend wants you to skip class with them...",
  "Boundary: Someone teases you about your hobby...",
  "Boundary: A relative asks about your grades at dinner...",
  "Boundary: A friend texts you constantly during study time...",
  "Boundary: Someone cuts in front of you in line...",
  "Boundary: A coworker dumps their work on you...",
  "Boundary: A friend wants to read your diary...",
  "Boundary: Someone pressures you to drink at a party...",
  "Boundary: A neighbor's music is too loud at night..."
 ],
 "Compounded": [
  "Boundary: Your boss asks you to work another weekend...",
  "Boundary: A friend always vents but never listens...",
  "Boundary: Family criticizes your career choice...",
  "Boundary: A partner checks your phone without asking...",
  "Boundary: Someone guilt-trips you for saying no...",
  "Boundary: A friend shares your secrets...",
  "Boundary: Your roommate never cleans...",
  "Boundary: Someone touches you without consent...",
  "Boundary: A client demands instant replies at midnight...",
  "Boundary: Your parent reads your messages...",
  "Boundary: A friend mocks your boundaries...",
  "Boundary: Someone trauma-dumps on you constantly..."
 ],
 "Advanced": [
  "Boundary: Ending a friendship that hurts you...",
  "Boundary: Confronting a boss about credit theft...",
  "Boundary: Telling family you need space...",
  "Boundary: Refusing a loan to family...",
  "Boundary: Addressing a partner's drinking...",
  "Boundary: Setting limits with an intrusive in-law...",
  "Boundary: Quitting a toxic job respectfully...",
  "Boundary: Telling a friend their jokes hurt...",
  "Boundary: Boundaries after betrayal...",
  "Boundary: Saying no to a wedding party role...",
  "Boundary: Limiting contact with a draining relative..."
 ]
};
var DEMOKIND="script-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Boundary Study — "+safe+"\n"
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
    name:topic+' — boundary script record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A boundary script record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
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
var gen={version:'jahdb-db-boundary-setting-practice-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-boundary-setting-practice',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
