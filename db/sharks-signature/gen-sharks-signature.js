(function(){'use strict';
/* JAH Signature Sharks Database generator — jahdb-sharks-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SHKS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Great White Shark (Carcharodon carcharias)", "Signature Study: Tiger Shark (Galeocerdo cuvier)", "Signature Study: Bull Shark (Carcharhinus leucas)", "Signature Study: Whale Shark (Rhincodon typus)", "Signature Study: Basking Shark (Cetorhinus maximus)", "Signature Study: Great Hammerhead (Sphyrna mokarran)", "Signature Study: Scalloped Hammerhead (Sphyrna lewini)", "Signature Study: Shortfin Mako (Isurus oxyrinchus)", "Signature Study: Longfin Mako (Isurus paucus)", "Signature Study: Blue Shark (Prionace glauca)", "Signature Study: Oceanic Whitetip Shark (Carcharhinus longimanus)"], "Compounded": ["Signature Study: Silky Shark (Carcharhinus falciformis)", "Signature Study: Lemon Shark (Negaprion brevirostris)", "Signature Study: Nurse Shark (Ginglymostoma cirratum)", "Signature Study: Blacktip Reef Shark (Carcharhinus melanopterus)", "Signature Study: Whitetip Reef Shark (Triaenodon obesus)", "Signature Study: Caribbean Reef Shark (Carcharhinus perezi)", "Signature Study: Sand Tiger Shark (Carcharias taurus)", "Signature Study: Goblin Shark (Mitsukurina owstoni)", "Signature Study: Greenland Shark (Somniosus microcephalus)", "Signature Study: Common Thresher (Alopias vulpinus)", "Signature Study: Bigeye Thresher (Alopias superciliosus)", "Signature Study: Porbeagle (Lamna nasus)"], "Advanced": ["Signature Study: Salmon Shark (Lamna ditropis)", "Signature Study: Cookiecutter Shark (Isistius brasiliensis)", "Signature Study: Epaulette Shark (Hemiscyllium ocellatum)", "Signature Study: Spotted Wobbegong (Orectolobus maculatus)", "Signature Study: Horn Shark (Heterodontus francisci)", "Signature Study: Spiny Dogfish (Squalus acanthias)", "Signature Study: Pygmy Shark (Euprotomicrus bispinatus)", "Signature Study: Megamouth Shark (Megachasma pelagios)", "Signature Study: Frilled Shark (Chlamydoselachus anguineus)", "Signature Study: Bluntnose Sixgill Shark (Hexanchus griseus)", "Signature Study: Zebra Shark (Stegostoma tigrinum)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature shark species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-sharks-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("sharks-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
