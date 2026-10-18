(function(){'use strict';
/* JAH The Character-to-Outfit Signature Database generator — jahdb-db-character-to-outfit-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CHOFS-";
var FIELDS=["Character Style Foundations", "Character Transformations", "Character Style Mastery"];
var TOPICS={"Character Style Foundations": ["Disneybounding Basics", "The Color Palette Decode", "Iconic Details", "Silhouette Translation", "Casual Versus Costume", "Character Research", "The Mood Board Method", "Thrifting Character Pieces", "Hair and Makeup Signals", "The Footwear Finish", "Photographing the Look"], "Character Transformations": ["Hero Transformations", "Villain Chic", "Princess Modernized", "Sci-Fi Character Style", "Fantasy Character Style", "Anime and Manga Looks", "Video Game Characters", "Book Character Style", "Historical Figure Inspired", "Musician Style Translation", "Group and Couple Themes", "Original Character Design"], "Character Style Mastery": ["The Signature Character", "Convention Mastery", "Crafting Character Pieces", "Character Makeup Artistry", "Photography and Cosplay", "Teaching Character Style", "The Business of Character", "Respectful Adaptation", "Evolving With Characters", "The Character Wardrobe", "Legacy of Play"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# minibot — "+safe+"\n"
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
    name:topic+' — character outfit record',
    title:topic,
    description:"SAMPLE RECORD (generated — structural Signature sample). A Signature-original character outfit record sample of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated Signature sample record — not an archive record. Seeded Signature records are the authoritative entries.',
    demo:{kind:"topic-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-db-character-to-outfit-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-character-to-outfit-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
