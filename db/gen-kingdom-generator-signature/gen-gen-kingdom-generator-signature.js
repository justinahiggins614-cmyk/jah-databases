(function(){'use strict';
/* JAH The Kingdom Generator Database generator — jahdb-gen-kingdom-generator-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Real working client-side
   generator: every call composes a genuine original creation from the
   archive's pools — name, measures, description, practice, key points,
   and a runnable demonstration program. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function rint(r,lo,hi){return lo+Math.floor(r()*(hi-lo+1));}
var PREFIX="JAH-KGDS-";
var NOUN="kingdom";
var FIELDS=["Kingdom Foundations", "Kingdom Intrigue", "Kingdom Legends"];
var TOPICS={"Kingdom Foundations": ["The Gilded Kingdom of Valdor", "Stormhaven and the Cliff Lords", "The Quiet Kingdom of Mirell", "Emberhold, Realm of the Forge-Kings", "The Moonlit Kingdom of Selene", "Thornhollow and the Briar Throne", "The Salt Kingdom of Brine", "Cloudspire, Kingdom of the High Aeries", "The Verdant Kingdom of Greenmarch", "Frostfall and the Winter Jarls", "The Paper Kingdom of Inkwell"], "Kingdom Intrigue": ["The Twin Kingdoms of Janus and June", "The Sunken Kingdom of Pelagia", "Ironmarch and the War Colleges", "The Velvet Kingdom of Noctis", "The Clockwork Kingdom of Coghaven", "Starfall and the Comet Court", "The Ashen Kingdom of Cinder", "The Floating Kingdom of Aerilon", "The Deep Kingdom of Undertow", "The Golden Kingdom of Auria", "The Howling Kingdom of Wolfmere"], "Kingdom Legends": ["The Silent Kingdom of Vesper", "The Thorned Kingdom of Rosalind", "The Opal Kingdom of Prism", "The Desert Kingdom of Sirocco", "The Mist Kingdom of Veyl", "The Coral Kingdom of Reefhold", "The Obsidian Kingdom of Nightreach", "The Lantern Kingdom of Glowmere", "The Broken Kingdom of Shardfall", "The Dreaming Kingdom of Somnus", "The Stormcrown Dominion", "The Everlasting Kingdom of Aevum"]};
var PEOPLE=["Sarella Voss", "Tommick Anders", "Ysolde Marr", "Brannic Cole", "Odessa Quinn", "Fenwick Hale", "Marisol Dray", "Corvin Ash", "Liora Venn", "Dain Mercer", "Petra Sol", "Rurik Dane", "Isolde Fenn", "Cassian Wren", "Mirabel Koss", "Theron Pike", "Anwen Sorrel", "Jorunn Vale", "Silas Quill", "Nerissa Bloom", "Emric Thane", "Tilda Moss", "Varric Stone", "Elowen Marsh"];
var PLACES=["Karrath Vale", "the Ember Isles", "Vessalyne", "Morrowgate", "Thistledown Reach", "the Obsidian Coast", "Lantern Hollow", "Cinderfell", "the Moonlit Expanse", "Gallowmere", "Starfall Bay", "the Whispering Steppes", "Duskmere", "the Crystal Fens", "Ashenford", "the Gilded Strait", "Ravenscar", "the Sunken Library", "Thornwall", "the Velvet Dunes", "Mistral Key", "the Howling Crags", "Bellwether Downs", "the Sapphire Deep"];
var ADJS=["luminous", "weathered", "restless", "gilded", "silent", "storm-born", "ancient", "mischievous", "solemn", "radiant", "shadowed", "resolute", "whimsical", "unyielding", "tender", "fierce", "patient", "wild", "careful", "boundless"];
var ATTRS=[{"key": "territory", "label": "Territory", "unit": "thousand leagues\u00b2", "lo": 5, "hi": 400}, {"key": "population", "label": "Population", "unit": "millions", "lo": 1, "hi": 120}, {"key": "treasury", "label": "Treasury", "unit": "million crowns", "lo": 10, "hi": 900}, {"key": "age", "label": "Age", "unit": "centuries", "lo": 1, "hi": 30}];
var CATS1=["monarchy", "council", "tribal moot", "magocracy", "merchant princes", "elder circle", "elected wardens", "theocratic order"];
var CATS2=["prosperous", "war-torn", "isolated", "seafaring", "mountain-bound", "scholarly", "militant", "festive"];
function attrsFor(r){
  var o={};
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];o[a.key]=rint(r,a.lo,a.hi);}
  return o;
}
function demoProgram(title,attrs){
  var L=['# '+title+' — generated demonstration',
         '# Property of Justin Addam Higgins (JAH).','attrs = {'];
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];
    L.push('    '+JSON.stringify(a.label)+': '+attrs[a.key]+',  # '+a.unit);}
  L.push('}');
  L.push("print("+JSON.stringify("== "+title+" ==")+")");
  L.push('for label, value in attrs.items():');
  L.push("    print('  %s: %s' % (label, value))");
  L.push('total = sum(attrs.values())');
  L.push('print("  total = %.2f" % total)');
  L.push('print("  mean  = %.2f" % (total / len(attrs)))');
  L.push('for label, value in attrs.items():');
  L.push("    assert value > 0, 'attribute must be positive: ' + label");
  L.push('print("OK - generated demo passed")');
  return L.join("\n")+"\n";
}
function composeDesc(title,field,attrs,adj,person,place,c1,c2){
  var bits=[];
  for(var i=0;i<ATTRS.length;i++){var a=ATTRS[i];
    bits.push(a.label.toLowerCase()+' of '+attrs[a.key]+' '+a.unit);}
  var p1=title+' is a '+adj+' '+NOUN+' of the archive. Chronicled by '+person+' of '+place+
    ', it carries '+bits[0]+' and '+bits[1]+' — measures that set it apart from its kin.';
  var p2='In practice it shows '+bits[2]+' and '+bits[3]+', with the twin natures of '+
    c1+' and '+c2+'. Those who work with it learn quickly: respect its pattern and it repays the courtesy.';
  return p1+'\n\n'+p2;
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(rnd,FIELDS);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(rnd,pool);
  var adj=pick(rnd,ADJS), person=pick(rnd,PEOPLE), place=pick(rnd,PLACES);
  var c1=pick(rnd,CATS1), c2=pick(rnd,CATS2);
  var attrs=attrsFor(rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var desc=composeDesc(topic,field,attrs,adj,person,place,c1,c2);
  var kp=[topic+' — original '+NOUN+' of the archive.',
          'Measures: '+ATTRS.map(function(a){return a.label.toLowerCase()+' '+attrs[a.key]+' '+a.unit;}).join('; ')+'.',
          'Twin natures: '+c1+' and '+c2+'.',
          'Kept by the archive; seeded records remain authoritative.'];
  return {
    id:id,
    name:topic+' — generated '+NOUN,
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+desc,
    field:field,
    how_it_works:'Name it, place it in '+place+', test it in play, keep one secret back, and check the finished '+NOUN+' against its seed.',
    key_points:kp,
    requirements:['A fixed name','A home in the archive','The four measures recorded','One secret withheld'],
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'generated-demo',language:'python',program:demoProgram(topic,attrs),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var ok=false;
  try{ ok=new RegExp('^'+PREFIX.replace(/[-]/g,'\\-')+'\\d{6}$').test(r.id||''); }catch(x){}
  if(!ok)e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.description||String(r.description).length<120)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-kingdom-generator-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-kingdom-generator-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
