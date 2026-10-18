(function(){'use strict';
/* JAH The Retro-Futurism Database generator — jahdb-db-retro-futurism-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Real working client-side
   generator: every call composes a genuine original creation from the
   archive's pools — name, measures, description, practice, key points,
   and a runnable demonstration program. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function rint(r,lo,hi){return lo+Math.floor(r()*(hi-lo+1));}
var PREFIX="JAH-RF-";
var NOUN="retro-future vision";
var FIELDS=["Retro Basics", "Future Past", "Tomorrow's Yesterdays"];
var TOPICS={"Retro Basics": ["Tomorrow, As Promised in 1952", "The Tide-Powered Future", "Chrome Diners on the Moon", "The Galewind Rocketport", "Shadow of the Atomic Age", "Breakfast on Mars, 1975", "The Iron Robot Butler", "Frost-Free Futures", "Star Charts for Commuters", "The Thunderbird Express", "Victory Gardens on Venus"], "Future Past": ["The Mist-Clearing Ray", "The Bone-Conduction Radio", "Light-Speed Luggage", "The Storm-Proof Suburb", "The Dream Recorder", "The Echo-Locator Wristwatch", "The Gravity-Defying Living Room", "The Time-Saving Kitchen", "The Ember-Glow Dashboard", "Tide Tables for Spacefarers", "The Flame-Broiled Automat"], "Tomorrow's Yesterdays": ["The Stone-Age Kitchen of Tomorrow", "Wind-Powered Skyscrapers", "The Shadowless City", "The Starlit Drive-In", "Moon Mail Delivery", "The Sun-Powered Lawn", "The Night-Owl Commuter", "Dawn Patrol Rockets", "The River of Tomorrow", "The Mountain Observatory", "Cloud-Nine Airlines", "The World of Tomorrow, Today"]};
var PEOPLE=["Sarella Voss", "Tommick Anders", "Ysolde Marr", "Brannic Cole", "Odessa Quinn", "Fenwick Hale", "Marisol Dray", "Corvin Ash", "Liora Venn", "Dain Mercer", "Petra Sol", "Rurik Dane", "Isolde Fenn", "Cassian Wren", "Mirabel Koss", "Theron Pike", "Anwen Sorrel", "Jorunn Vale", "Silas Quill", "Nerissa Bloom", "Emric Thane", "Tilda Moss", "Varric Stone", "Elowen Marsh"];
var PLACES=["Karrath Vale", "the Ember Isles", "Vessalyne", "Morrowgate", "Thistledown Reach", "the Obsidian Coast", "Lantern Hollow", "Cinderfell", "the Moonlit Expanse", "Gallowmere", "Starfall Bay", "the Whispering Steppes", "Duskmere", "the Crystal Fens", "Ashenford", "the Gilded Strait", "Ravenscar", "the Sunken Library", "Thornwall", "the Velvet Dunes", "Mistral Key", "the Howling Crags", "Bellwether Downs", "the Sapphire Deep"];
var ADJS=["luminous", "weathered", "restless", "gilded", "silent", "storm-born", "ancient", "mischievous", "solemn", "radiant", "shadowed", "resolute", "whimsical", "unyielding", "tender", "fierce", "patient", "wild", "careful", "boundless"];
var ATTRS=[{"key": "decades", "label": "Decades", "unit": "count", "lo": 1, "hi": 12}, {"key": "gadgets", "label": "Gadgets", "unit": "count", "lo": 10, "hi": 300}, {"key": "rockets", "label": "Rockets", "unit": "count", "lo": 1, "hi": 80}, {"key": "optimism", "label": "Optimism", "unit": "scale 1-100", "lo": 1, "hi": 100}];
var CATS1=["optimistic", "sleek", "whimsical", "earnest", "gleaming", "daring", "cozy", "boundless"];
var CATS2=["diner", "rocketport", "suburb", "fairground", "observatory", "automat", "drive-in", "spaceport"];
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
var gen={version:"jahdb-db-retro-futurism-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("db-retro-futurism",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
