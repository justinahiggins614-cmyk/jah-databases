(function(){'use strict';
/* JAH The Music Genres Database generator — jahdb-mystery-detective-fiction-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-MYSS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Detective Fiction (Signature edition)",
  "The Murders in the Rue Morgue (Signature edition)",
  "A Study in Scarlet (Signature edition)",
  "The Hound of the Baskervilles (Signature edition)",
  "The Maltese Falcon (Signature edition)",
  "The Big Sleep (Signature edition)",
  "Murder on the Orient Express (Signature edition)",
  "And Then There Were None (Signature edition)",
  "The Girl with the Dragon Tattoo (Signature edition)",
  "The Moonstone (Signature edition)",
  "The Thin Man (Signature edition)"
 ],
 "Compounded": [
  "Golden Age of Detective Fiction (Signature edition)",
  "Hardboiled vs Cozy (Signature edition)",
  "The Locked-Room Mystery (Signature edition)",
  "The Police Procedural (Signature edition)",
  "Noir Fiction (Signature edition)",
  "The Private Eye (Signature edition)",
  "Agatha Christie's Methods (Signature edition)",
  "Raymond Chandler (Signature edition)",
  "Dashiell Hammett (Signature edition)",
  "The Whodunit Structure (Signature edition)",
  "Red Herrings and Fair Play (Signature edition)",
  "The Reveal Scene (Signature edition)"
 ],
 "Advanced": [
  "Scandinavian Noir (Signature edition)",
  "The Anti-Detective Novel (Signature edition)",
  "True Crime vs Fiction (Signature edition)",
  "Forensic Mysteries (Signature edition)",
  "Detective Fiction Theory (Signature edition)",
  "The Detective as Outsider (Signature edition)",
  "Women Detectives (Signature edition)",
  "Postmodern Mystery (Signature edition)",
  "The Mystery Awards (Edgars) (Signature edition)",
  "Cozy Mystery Renaissance (Signature edition)",
  "The Impossible Crime (Signature edition)"
 ]
};
var DEMOKIND="suspect-grid building";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Suspect-grid builder — "+safe+"\n"
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
var gen={version:'jahdb-mystery-detective-fiction-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('mystery-detective-fiction-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
