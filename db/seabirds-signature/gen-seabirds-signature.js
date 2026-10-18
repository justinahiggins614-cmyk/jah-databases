(function(){'use strict';
/* JAH Signature Seabirds Database generator — jahdb-seabirds-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SBDS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Wandering Albatross (Diomedea exulans)", "Signature Study: Black-browed Albatross (Thalassarche melanophris)", "Signature Study: Laysan Albatross (Phoebastria immutabilis)", "Signature Study: Northern Fulmar (Fulmarus glacialis)", "Signature Study: Manx Shearwater (Puffinus puffinus)", "Signature Study: Sooty Shearwater (Ardenna grisea)", "Signature Study: Wilson's Storm Petrel (Oceanites oceanicus)", "Signature Study: European Storm Petrel (Hydrobates pelagicus)", "Signature Study: Northern Gannet (Morus bassanus)", "Signature Study: Brown Pelican (Pelecanus occidentalis)", "Signature Study: Great White Pelican (Pelecanus onocrotalus)"], "Compounded": ["Signature Study: Australasian Gannet (Morus serrator)", "Signature Study: Blue-footed Booby (Sula nebouxii)", "Signature Study: Masked Booby (Sula dactylatra)", "Signature Study: Red-footed Booby (Sula sula)", "Signature Study: Great Cormorant (Phalacrocorax carbo)", "Signature Study: Double-crested Cormorant (Nannopterum auritum)", "Signature Study: European Shag (Gulosus aristotelis)", "Signature Study: Atlantic Puffin (Fratercula arctica)", "Signature Study: Tufted Puffin (Fratercula cirrhata)", "Signature Study: Horned Puffin (Fratercula corniculata)", "Signature Study: Common Murre (Uria aalge)", "Signature Study: Thick-billed Murre (Uria lomvia)"], "Advanced": ["Signature Study: Razorbill (Alca torda)", "Signature Study: Black Guillemot (Cepphus grylle)", "Signature Study: Herring Gull (Larus argentatus)", "Signature Study: Great Black-backed Gull (Larus marinus)", "Signature Study: Laughing Gull (Leucophaeus atricilla)", "Signature Study: Black-legged Kittiwake (Rissa tridactyla)", "Signature Study: Arctic Tern (Sterna paradisaea)", "Signature Study: Common Tern (Sterna hirundo)", "Signature Study: Sooty Tern (Onychoprion fuscatus)", "Signature Study: Emperor Penguin (Aptenodytes forsteri)", "Signature Study: Adélie Penguin (Pygoscelis adeliae)"]};
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature seabird species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
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
var gen={version:"jahdb-seabirds-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("seabirds-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
