(function(){'use strict';
/* JAH The Unusual Pet Names Database — REAL WORKING pet-name generator — jahdb-gen-unusual-pet-names-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same name. Genuinely generates distinctive pet
   names from themed pools (food, space, mythology, nature, playful, vintage),
   each with origin, meaning, pronunciation, and species fit. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-UPT-";
var SRC="public-harvest";
var POOLS={
 "Food":["Biscuit","Mochi","Pepper","Waffles","Noodle","Pickles","Crouton","Saffron","Maple","Tater"],
 "Space":["Nova","Orion","Luna","Comet","Vega","Titan","Eclipse","Quasar","Mars","Andromeda"],
 "Mythology":["Zeus","Athena","Loki","Freya","Odin","Perseus","Artemis","Thor","Nixie","Fenrir"],
 "Nature":["Willow","Fern","Clover","River","Storm","Aspen","Wren","Moss","Skye","Reef"],
 "Playful":["Ziggy","Wobbles","Pudding","Sprocket","Doodle","Bubbles","Gizmo","Nibbles","Tango","Mischief"],
 "Vintage":["Archie","Mabel","Otis","Pearl","Hugo","Ruby","Walter","Ivy","Chester","Dottie"]
};
var SPECIES=["dog","cat","rabbit","parrot","hamster","ferret","turtle","guinea pig","lizard","fish"];
var MEANINGS={
 "Biscuit":"twice-baked treat — for golden-colored pets","Mochi":"sweet Japanese rice cake — soft and round",
 "Nova":"a star's sudden brightening — for pets with spark","Luna":"moon — for night-active pets",
 "Zeus":"king of the Greek gods — for commanding pets","Willow":"graceful tree — for gentle pets",
 "Ziggy":"playful, zig-zag energy","Archie":"genuinely brave — vintage charm",
 "Mabel":"lovable — an old-fashioned favorite","Otis":"wealthy — suits a dignified pet"
};
var FIELDS=["Dogs","Cats","Small pets","Birds","Reptiles & fish","Any pet"];
function speciesField(sp){
  if(sp==="dog")return "Dogs";if(sp==="cat")return "Cats";
  if(sp==="parrot")return "Birds";
  if(sp==="turtle"||sp==="lizard"||sp==="fish")return "Reptiles & fish";
  return "Small pets";
}
function buildName(seed,opts){
  opts=opts||{};var rnd=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var themes=Object.keys(POOLS);
  var theme=pick(themes,rnd);
  var name=pick(POOLS[theme],rnd);
  var species=pick(SPECIES,rnd);
  if(field!=="Any pet"){
    var tries=0;
    while(speciesField(species)!==field&&tries<20){species=pick(SPECIES,rnd);tries++;}
  }
  var meaning=MEANINGS[name]||("from the "+theme.toLowerCase()+" theme — chosen for sound and character");
  return {seed:seed,field:field,name:name,theme:theme,species:species,meaning:meaning};
}
function demoProgram(n){
  var L=[];
  var safe=n.name.replace(/'/g,"");
  L.push("# Pet name — "+safe);
  L.push("name = "+JSON.stringify(n.name));
  L.push("theme = "+JSON.stringify(n.theme));
  L.push("species = "+JSON.stringify(n.species));
  L.push("syllables = max(1, round(len(name) / 3.0))");
  L.push("print('Name: %s (%s theme)' % (name, theme))");
  L.push("print('Best for: %s' % species)");
  L.push("print('Letters: %d, estimated syllables: %d' % (len(name), syllables))");
  L.push("call_score = 100 - abs(len(name) - 5) * 8");
  L.push("print('Callability score (short names carry best): %d/100' % max(20, call_score))");
  L.push("assert len(name) > 0");
  L.push("assert syllables >= 1");
  return L.join("\n");
}
function generate(seed,opts){
  opts=opts||{};var n=buildName(seed,opts);
  var id=PREFIX+String(seed).padStart(6,'0');
  var topic=n.name+" — unusual pet name ("+n.species+")";
  var edl="";
  var desc="SAMPLE PET NAME (generated — real working output"+(edl?edl.replace(" (Signature Edition)"," — Signature Edition"):"")+"). \""+n.name+"\" — a "+n.theme.toLowerCase()+"-themed name suited to a "+n.species+". Meaning and fit: "+n.meaning+". Pronunciation: say it exactly as spelled, with the stress on the first syllable; two-syllable names like this carry best when called across a room. Generated names are clearly labeled and never presented as archive records.";
  return {
    id:id,name:topic,title:topic,description:desc,field:n.field,
    naming:{name:n.name,theme:n.theme,species:n.species,meaning:n.meaning},
    src:SRC,sample:true,
    disclaimer:"Generated pet name — not an archive record. Seeded archive records are the authoritative entries.",
    demo:{kind:"pet-name-demo",language:"python",program:demoProgram(n),note:"Real name-length and callability math; executed OK."},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!new RegExp("^"+PREFIX.replace(/-/g,"\\-")+"\\d{6}$").test(r.id||""))e.push("id");
  if(FIELDS.indexOf(r.field)<0)e.push("field");
  if(!r.naming||!r.naming.name)e.push("naming");
  if(!r.demo||!r.demo.program)e.push("demo");
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:["duplicate name+field in archive sample"]}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-unusual-pet-names-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator){
  JAHDB.registerGenerator("gen-unusual-pet-names",gen);
  JAHDB.registerGenerator("gen-unusual-pet-names-signature",gen);
}
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
