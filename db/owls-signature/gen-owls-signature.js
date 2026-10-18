(function(){'use strict';
/* JAH Signature Owls Database generator — jahdb-owls-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OWLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Great Horned Owl (Bubo virginianus)", "Signature Study: Eurasian Eagle-Owl (Bubo bubo)", "Signature Study: Snowy Owl (Bubo scandiacus)", "Signature Study: Barn Owl (Tyto alba)", "Signature Study: Barred Owl (Strix varia)", "Signature Study: Great Gray Owl (Strix nebulosa)", "Signature Study: Tawny Owl (Strix aluco)", "Signature Study: Spotted Owl (Strix occidentalis)", "Signature Study: Long-eared Owl (Asio otus)", "Signature Study: Short-eared Owl (Asio flammeus)", "Signature Study: Eastern Screech-Owl (Megascops asio)"], "Compounded": ["Signature Study: Western Screech-Owl (Megascops kennicottii)", "Signature Study: Northern Saw-whet Owl (Aegolius acadicus)", "Signature Study: Boreal Owl (Aegolius funereus)", "Signature Study: Burrowing Owl (Athene cunicularia)", "Signature Study: Little Owl (Athene noctua)", "Signature Study: Elf Owl (Micrathene whitneyi)", "Signature Study: Northern Pygmy-Owl (Glaucidium gnoma)", "Signature Study: Eurasian Pygmy Owl (Glaucidium passerinum)", "Signature Study: Northern Hawk Owl (Surnia ulula)", "Signature Study: Spectacled Owl (Pulsatrix perspicillata)", "Signature Study: Mottled Owl (Strix virgata)", "Signature Study: Striped Owl (Asio clamator)"], "Advanced": ["Signature Study: Stygian Owl (Asio stygius)", "Signature Study: Philippine Eagle-Owl (Ketupa philippensis)", "Signature Study: Blakiston's Fish Owl (Ketupa blakistoni)", "Signature Study: Tawny Fish Owl (Ketupa flavipes)", "Signature Study: Brown Fish Owl (Ketupa zeylonensis)", "Signature Study: Verreaux's Eagle-Owl (Ketupa lactea)", "Signature Study: Powerful Owl (Ninox strenua)", "Signature Study: Southern Boobook (Ninox boobook)", "Signature Study: Morepork (Ninox novaeseelandiae)", "Signature Study: Oriental Scops Owl (Otus sunia)", "Signature Study: Eurasian Scops Owl (Otus scops)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('Sample record — structural sample, not an archive entry.')\n"
   + "print(record['topic'] + ' [' + record['field'] + ']')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic,
    title:topic,
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature owl species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated",
    sample:true,
    disclaimer:"Generated Signature sample record \u2014 not an archive record. Seeded Signature records are the authoritative entries.",
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
var gen={version:"jahdb-owls-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("owls-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
