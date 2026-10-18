(function(){'use strict';
/* JAH The Frogs and Toads Database generator — jahdb-amphibians-frogs-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-FROG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["American Bullfrog (Lithobates catesbeianus)", "Green Frog (Lithobates clamitans)", "Northern Leopard Frog (Lithobates pipiens)", "Wood Frog (Lithobates sylvaticus)", "Spring Peeper (Pseudacris crucifer)", "Gray Treefrog (Hyla versicolor)", "American Green Tree Frog (Hyla cinerea)", "Red-eyed Tree Frog (Agalychnis callidryas)", "White's Tree Frog (Litoria caerulea)", "Pacific Chorus Frog (Pseudacris regilla)", "Cane Toad (Rhinella marina)"], "Compounded": ["American Toad (Anaxyrus americanus)", "Fowler's Toad (Anaxyrus fowleri)", "European Common Toad (Bufo bufo)", "Natterjack Toad (Epidalea calamita)", "Colorado River Toad (Incilius alvarius)", "Mexican Spadefoot Toad (Spea multiplicata)", "Oriental Fire-bellied Toad (Bombina orientalis)", "European Fire-bellied Toad (Bombina bombina)", "African Bullfrog (Pyxicephalus adspersus)", "Tomato Frog (Dyscophus antongilii)", "Goliath Frog (Conraua goliath)", "Strawberry Poison Dart Frog (Oophaga pumilio)"], "Advanced": ["Blue Poison Dart Frog (Dendrobates tinctorius)", "Golden Poison Frog (Phyllobates terribilis)", "Green and Black Poison Dart Frog (Dendrobates auratus)", "Panamanian Golden Frog (Atelopus zeteki)", "Variable Harlequin Toad (Atelopus varius)", "Surinam Toad (Pipa pipa)", "African Dwarf Frog (Hymenochirus curtipes)", "African Clawed Frog (Xenopus laevis)", "Darwin's Frog (Rhinoderma darwinii)", "Fleischmann's Glass Frog (Hyalinobatrachium fleischmanni)", "Ornate Horned Frog (Ceratophrys ornata)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A frog and toad species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-amphibians-frogs-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("amphibians-frogs",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
