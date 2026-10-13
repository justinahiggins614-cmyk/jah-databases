(function(){'use strict';
/* JAH Public Dream Record Catalog generator — jahdb-public-dream-records-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-DREC-';
var FIELDS=["scientific-dreams", "creative-dreams", "biblical-dreams", "ancient-dreams", "psychological-dreams", "prophetic-dreams", "modern-dreams"];
var TOPICS={
 "ancient-dreams":["Gilgamesh's Dreams: The Coming of Enkidu","Penelope's Geese","Hecuba's Torch","Calpurnia's Dream: Caesar's Murder","Socrates' Dream: 'Make Music'","Xerxes' Dream: The Invasion of Greece","Croesus' Dream: Atys and the Spear","Cicero's Dream of Marius"],
 "biblical-dreams":["Joseph's Sheaves and Stars","Pharaoh's Cows and Ears","Jacob's Ladder","Solomon's Dream at Gibeon","Nebuchadnezzar's Statue","Daniel's Four Beasts","Pilate's Wife's Dream","Joseph's Flight to Egypt"],
 "creative-dreams":["Mary Shelley's Waking Dream: Frankenstein","Stevenson's Brownies: Jekyll and Hyde","Coleridge's Kubla Khan: The Opium Dream","Bram Stoker's Dracula Nightmare","Lovecraft's Dreamlands","Stephenie Meyer's Meadow: Twilight","Stephen King's Plane Dream: Misery","McCartney's Yesterday: The Morning Melody","Keith Richards' Satisfaction Riff","Tartini's Devil Sonata","Mark Twain's Premonition: Henry's Death"],
 "modern-dreams":["Jack Nicklaus's Golf Swing","Larry Page's PageRank Dream","Edgar Cayce's Sleeping Readings","Upton Sinclair's Mental Radio","The Maimonides Dream Telepathy Experiments","Rosalind Cartwright's Divorce Dreams"],
 "prophetic-dreams":["Lincoln's Assassination Dream","Harriet Tubman's Visions","Madame C.J. Walker's Dream Formula","Constantine's Chi-Rho","Joan of Arc's Voices","Descartes' Three Dreams"],
 "psychological-dreams":["Freud's Irma Dream: The Specimen Dream","Jung's House Dream","Jung's Blood Visions: Foreseeing the War","Maury's Guillotine Dream","Dunne's Precognitive Dreams","Swedenborg's Dream Journal","William Blake's Visions","Dali's Slumber with a Key","Edison's Steel Balls","Tesla's Visions"],
 "scientific-dreams":["Kekule's Ouroboros: The Benzene Ring","Loewi's Easter Dream: Chemical Neurotransmission","Howe's Savages: The Sewing Machine Needle","Mendeleev's Table: The Periodic Dream","Banting's 2 A.M. Idea: Insulin","Agassiz's Fossil Fish","Hilprecht's Babylonian Priest","Bohr's Atom: The Solar Dream","Ramanujan's Goddess Namagiri","Watson's Spiral Staircase: DNA","Poincare's Omnibus: Fuchsian Functions"]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/"/g,"'");
  return "# Dream Lab — "+safe+"\n"
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
    name:topic+' — dream study',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A dream study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'dream-timeline-explorer',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-dream-records-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-dream-records',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
