(function(){'use strict';
/* JAH Signature Frogs and Toads Database generator — jahdb-amphibians-frogs-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FROGS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: American Bullfrog (Lithobates catesbeianus)", "Signature Study: Green Frog (Lithobates clamitans)", "Signature Study: Northern Leopard Frog (Lithobates pipiens)", "Signature Study: Wood Frog (Lithobates sylvaticus)", "Signature Study: Spring Peeper (Pseudacris crucifer)", "Signature Study: Gray Treefrog (Hyla versicolor)", "Signature Study: American Green Tree Frog (Hyla cinerea)", "Signature Study: Red-eyed Tree Frog (Agalychnis callidryas)", "Signature Study: White's Tree Frog (Litoria caerulea)", "Signature Study: Pacific Chorus Frog (Pseudacris regilla)", "Signature Study: Cane Toad (Rhinella marina)"], "Compounded": ["Signature Study: American Toad (Anaxyrus americanus)", "Signature Study: Fowler's Toad (Anaxyrus fowleri)", "Signature Study: European Common Toad (Bufo bufo)", "Signature Study: Natterjack Toad (Epidalea calamita)", "Signature Study: Colorado River Toad (Incilius alvarius)", "Signature Study: Mexican Spadefoot Toad (Spea multiplicata)", "Signature Study: Oriental Fire-bellied Toad (Bombina orientalis)", "Signature Study: European Fire-bellied Toad (Bombina bombina)", "Signature Study: African Bullfrog (Pyxicephalus adspersus)", "Signature Study: Tomato Frog (Dyscophus antongilii)", "Signature Study: Goliath Frog (Conraua goliath)", "Signature Study: Strawberry Poison Dart Frog (Oophaga pumilio)"], "Advanced": ["Signature Study: Blue Poison Dart Frog (Dendrobates tinctorius)", "Signature Study: Golden Poison Frog (Phyllobates terribilis)", "Signature Study: Green and Black Poison Dart Frog (Dendrobates auratus)", "Signature Study: Panamanian Golden Frog (Atelopus zeteki)", "Signature Study: Variable Harlequin Toad (Atelopus varius)", "Signature Study: Surinam Toad (Pipa pipa)", "Signature Study: African Dwarf Frog (Hymenochirus curtipes)", "Signature Study: African Clawed Frog (Xenopus laevis)", "Signature Study: Darwin's Frog (Rhinoderma darwinii)", "Signature Study: Fleischmann's Glass Frog (Hyalinobatrachium fleischmanni)", "Signature Study: Ornate Horned Frog (Ceratophrys ornata)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature frog and toad species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-amphibians-frogs-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("amphibians-frogs-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
