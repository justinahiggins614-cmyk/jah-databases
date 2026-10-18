(function(){'use strict';
/* JAH The Owls Database generator — jahdb-owls-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OWL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Great Horned Owl (Bubo virginianus)", "Eurasian Eagle-Owl (Bubo bubo)", "Snowy Owl (Bubo scandiacus)", "Barn Owl (Tyto alba)", "Barred Owl (Strix varia)", "Great Gray Owl (Strix nebulosa)", "Tawny Owl (Strix aluco)", "Spotted Owl (Strix occidentalis)", "Long-eared Owl (Asio otus)", "Short-eared Owl (Asio flammeus)", "Eastern Screech-Owl (Megascops asio)"], "Compounded": ["Western Screech-Owl (Megascops kennicottii)", "Northern Saw-whet Owl (Aegolius acadicus)", "Boreal Owl (Aegolius funereus)", "Burrowing Owl (Athene cunicularia)", "Little Owl (Athene noctua)", "Elf Owl (Micrathene whitneyi)", "Northern Pygmy-Owl (Glaucidium gnoma)", "Eurasian Pygmy Owl (Glaucidium passerinum)", "Northern Hawk Owl (Surnia ulula)", "Spectacled Owl (Pulsatrix perspicillata)", "Mottled Owl (Strix virgata)", "Striped Owl (Asio clamator)"], "Advanced": ["Stygian Owl (Asio stygius)", "Philippine Eagle-Owl (Ketupa philippensis)", "Blakiston's Fish Owl (Ketupa blakistoni)", "Tawny Fish Owl (Ketupa flavipes)", "Brown Fish Owl (Ketupa zeylonensis)", "Verreaux's Eagle-Owl (Ketupa lactea)", "Powerful Owl (Ninox strenua)", "Southern Boobook (Ninox boobook)", "Morepork (Ninox novaeseelandiae)", "Oriental Scops Owl (Otus sunia)", "Eurasian Scops Owl (Otus scops)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A owl species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-owls-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("owls",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
