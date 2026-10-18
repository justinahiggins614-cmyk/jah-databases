(function(){'use strict';
/* JAH The Community Vote Signature Database generator — jahdb-db-community-vote-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CMVS-";
var FIELDS=["Movies & Shows","Music & Books","Food & Places"];
var TOPICS={
 "Movies & Shows": [
  "Blockbuster vs Oscar: Film (Signature Edition) - Movies & Shows",
  "Sitcom vs Drama: TV (Signature Edition) - Movies & Shows",
  "Reality vs Scripted: TV (Signature Edition) - Movies & Shows",
  "Superhero vs Indie: Cinema (Signature Edition) - Movies & Shows",
  "Animated vs Live: Film (Signature Edition) - Movies & Shows",
  "Sequel vs Original: Hollywood (Signature Edition) - Movies & Shows",
  "Binge vs Weekly: Watching (Signature Edition) - Movies & Shows",
  "Theater vs Streaming: Viewing (Signature Edition) - Movies & Shows",
  "Dub vs Sub: Anime (Signature Edition) - Movies & Shows",
  "Remake vs Original: Stories (Signature Edition) - Movies & Shows"
 ],
 "Music & Books": [
  "Pop vs Critical: Music (Signature Edition) - Music & Books",
  "Bestseller vs Literary: Books (Signature Edition) - Music & Books",
  "Fiction vs Nonfiction: Reading (Signature Edition) - Music & Books",
  "Vinyl vs Streaming: Music (Signature Edition) - Music & Books",
  "Concert vs Album: Music (Signature Edition) - Music & Books",
  "Podcast vs Radio: Audio (Signature Edition) - Music & Books",
  "Audiobook vs Print: Books (Signature Edition) - Music & Books",
  "Fanfic vs Canon: Stories (Signature Edition) - Music & Books",
  "Meme vs Art: Internet (Signature Edition) - Music & Books",
  "Short vs Long: Video (Signature Edition) - Music & Books"
 ],
 "Food & Places": [
  "Chain vs Local: Food (Signature Edition) - Food & Places",
  "Fast vs Slow: Food (Signature Edition) - Food & Places",
  "Tourist vs Hidden: Travel (Signature Edition) - Food & Places",
  "Beach vs Mountain: Vacation (Signature Edition) - Food & Places",
  "City Break vs Resort: Trip (Signature Edition) - Food & Places",
  "Museum vs Park: Day Out (Signature Edition) - Food & Places",
  "Stadium vs Couch: Sports (Signature Edition) - Food & Places",
  "Coffee Shop vs Home: Coffee (Signature Edition) - Food & Places",
  "Bar vs Home: Drinks (Signature Edition) - Food & Places",
  "Zoo vs Safari: Animals (Signature Edition) - Food & Places",
  "Theme Park vs Nature: Fun (Signature Edition) - Food & Places",
  "Downtown vs Suburb: Live (Signature Edition) - Food & Places",
  "Festival vs Small Gig: Music Live (Signature Edition) - Food & Places",
  "All-Inclusive vs DIY: Travel (Signature Edition) - Food & Places"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Community Vote Study — "+safe+"\n"
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
    name:topic+' — community verdict record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A community verdict record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"community-vote-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-community-vote-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-community-vote-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
