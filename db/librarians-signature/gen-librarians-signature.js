(function(){'use strict';
/* JAH Signature Librarians Database generator — jahdb-librarians-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-LIBRS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "The Signature Welcome Tour",
  "Signature Scenario: The Impossible Question",
  "The Signature Book Match Quiz",
  "Signature Shelf-Reading Game",
  "Signature New-Card Celebration",
  "Signature Homework Help Hub",
  "The Signature Quiet Floor Redesign",
  "Signature Tech Petting Zoo",
  "Signature Local History Harvest",
  "Signature Bedtime Story Hotline",
  "Signature Library Card Art Contest",
 ],
 "Compounded": [
  "Signature Embedded Librarian Program",
  "Signature Digital Preservation Plan",
  "Signature Fake-News Workshop",
  "Signature Challenge Response Kit",
  "Signature ILL Speed Challenge",
  "Signature Director Bootcamp",
  "Signature Pop-Up Library",
  "Signature Teen Advisory Board",
  "Signature Recording Studio Guide",
  "Signature Grant-Writing Sprint",
  "Signature Data Storytelling Workshop",
  "Signature Succession Plan",
 ],
 "Advanced": [
  "Signature Vault Exhibit Program",
  "Signature Legal Research Clinic",
  "Signature Systematic Review Service",
  "Signature Score Library Project",
  "Signature Documents Hackathon",
  "Signature Preservation Emergency Kit",
  "Signature Open Textbook Project",
  "Signature Teen Lit Fest",
  "Signature Library of Things 2.0",
  "Signature AI Reference Pilot",
  "Signature Statewide Delivery Network",
 ],
};
var DEMOKIND="library calculation";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Library calculator — "+safe+"\n"
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
    name:topic+' — librarian profession record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A miners profession record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
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
var gen={version:'jahdb-librarians-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('librarians-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
