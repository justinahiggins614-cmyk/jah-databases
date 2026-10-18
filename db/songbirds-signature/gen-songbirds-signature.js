(function(){'use strict';
/* JAH Signature Songbirds Database generator — jahdb-songbirds-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SNGBS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: American Robin (Turdus migratorius)", "Signature Study: Northern Cardinal (Cardinalis cardinalis)", "Signature Study: Blue Jay (Cyanocitta cristata)", "Signature Study: Black-capped Chickadee (Poecile atricapillus)", "Signature Study: House Sparrow (Passer domesticus)", "Signature Study: European Starling (Sturnus vulgaris)", "Signature Study: Common Blackbird (Turdus merula)", "Signature Study: Eurasian Blue Tit (Cyanistes caeruleus)", "Signature Study: Barn Swallow (Hirundo rustica)", "Signature Study: Common Nightingale (Luscinia megarhynchos)", "Signature Study: European Robin (Erithacus rubecula)"], "Compounded": ["Signature Study: Northern Mockingbird (Mimus polyglottos)", "Signature Study: Gray Catbird (Dumetella carolinensis)", "Signature Study: Eastern Bluebird (Sialia sialis)", "Signature Study: Baltimore Oriole (Icterus galbula)", "Signature Study: American Goldfinch (Spinus tristis)", "Signature Study: European Goldfinch (Carduelis carduelis)", "Signature Study: Common Chaffinch (Fringilla coelebs)", "Signature Study: House Finch (Haemorhous mexicanus)", "Signature Study: Zebra Finch (Taeniopygia guttata)", "Signature Study: Atlantic Canary (Serinus canaria)", "Signature Study: European Greenfinch (Chloris chloris)", "Signature Study: Eurasian Bullfinch (Pyrrhula pyrrhula)"], "Advanced": ["Signature Study: Song Thrush (Turdus philomelos)", "Signature Study: Mistle Thrush (Turdus viscivorus)", "Signature Study: Wood Thrush (Hylocichla mustelina)", "Signature Study: Veery (Catharus fuscescens)", "Signature Study: Hermit Thrush (Catharus guttatus)", "Signature Study: Cedar Waxwing (Bombycilla cedrorum)", "Signature Study: Bohemian Waxwing (Bombycilla garrulus)", "Signature Study: Superb Lyrebird (Menura novaehollandiae)", "Signature Study: Australian Magpie (Gymnorhina tibicen)", "Signature Study: Common Raven (Corvus corax)", "Signature Study: Red-winged Blackbird (Agelaius phoeniceus)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature songbird species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-songbirds-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("songbirds-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
