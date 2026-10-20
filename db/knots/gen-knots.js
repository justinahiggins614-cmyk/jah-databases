(function(){'use strict';
/* JAH The Knot Database generator — jahdb-knots-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-KNOT-";
var FIELDS=["Bends", "Binding Knots", "Decorative Knots", "Fishing Knots", "Friction Hitches", "Hitches", "Lashings & Splices", "Loop Knots", "Stopper Knots"];
var TOPICS={"Loop Knots": ["Bowline", "Figure-Eight Loop", "Alpine Butterfly", "Slip Knot", "Bowline on a Bight", "Double Bowline", "Spanish Bowline", "Yosemite Bowline", "In-Line Figure Eight", "Directional Figure Eight", "Cowboy Bowline", "Eskimo Bowline", "Jury Mast Knot", "Perfection Loop", "Surgeon's Loop", "Dropper Loop", "French Bowline", "Triple Bowline", "Angler's Loop", "Figure-Eight Follow-Through", "Scaffold Knot", "Poacher's Knot", "Hangman's Noose", "Arbor Knot (climbing)", "Water Bowline", "Overhand on a Bight", "Running Bowline", "Bowstring Knot", "Honda Knot", "Lariat Loop", "Bosun's Chair Knot", "Fireman's Chair Knot", "Tom Fool's Knot", "Handcuff Knot"], "Stopper Knots": ["Figure-Eight Knot", "Overhand Knot", "Stevedore Knot", "Oysterman's Stopper", "Heaving Line Knot", "Double Overhand Knot"], "Hitches": ["Clove Hitch", "Two Half Hitches", "Timber Hitch", "Anchor Hitch", "Round Turn and Two Half Hitches", "Cow Hitch", "Cleat Hitch", "Pile Hitch", "Cat's Paw", "Trucker's Hitch", "Marlinspike Hitch", "Barrel Hitch", "Buntline Hitch", "Tensionless Hitch", "Highwayman's Hitch", "Picket-Line Hitch", "Evenk Hitch", "Lighterman's Hitch", "Jug Sling Hitch", "Slipped Buntline", "Ring Hitch", "Girth Hitch", "Basket Hitch", "Choker Hitch", "Timber Hitch and Half Hitch", "Killick Hitch", "Topmast Hitch", "Timber Hitch (climbing variant)", "Radiant Hitch", "Bale Sling Hitch", "Snug Hitch", "Ossel Hitch"], "Binding Knots": ["Reef Knot (Square Knot)", "Sheepshank", "Surgeon's Knot", "Constrictor Knot", "Strangle Knot", "Miller's Knot", "Mesh Knot"], "Bends": ["Sheet Bend", "Double Sheet Bend", "Fisherman's Knot", "Double Fisherman's Knot", "Water Knot", "Carrick Bend", "Hunter's Bend", "Zeppelin Bend", "Thief Knot", "Studding-Sail Halyard Bend", "Triple Fisherman's Knot", "Netting Sheet Bend"], "Friction Hitches": ["Taut-Line Hitch", "Rolling Hitch", "Prusik Knot", "Klemheist", "Munter Hitch", "Garda Hitch", "Adjustable Grip Hitch", "Midshipman's Hitch", "Camel Hitch", "Farrimond Friction Hitch", "Blake's Hitch", "Valdotain Tresse", "Distel Hitch", "Schwabisch Hitch", "Autoblock (French Prusik)", "Bachmann Knot", "Icicle Hitch", "Grip Hitch", "Prusik Loop (sewn)", "Munter-Mule-Overhand"], "Decorative Knots": ["Monkey's Fist", "Turk's Head", "Wall Knot", "Crown Knot", "Matthew Walker Knot", "Regatta Knot", "Good Luck Knot", "Crown Sinnet", "Wall Sinnet", "Ocean Plait Mat", "Prolong Knot", "Shamrock Knot", "Eternity Knot", "Knife Lanyard Knot", "Bosun's Call Lanyard Knot", "Monkey Chain", "Four-Strand Braid", "Eight-Strand Braid", "Friendship Knot", "Pineapple Knot", "Globe Knot", "Footrope Knot", "Star Knot", "Button Knot", "Fiador Knot", "Hackamore Knot", "Double Dragon Knot", "Mizuhiki Knot", "Celtic Heart Knot", "Trinity Knot", "Carrick Mat", "Square Knot (macrame)", "Lark's Head (macrame)", "Gathering Knot (macrame)", "Josephine Knot", "Snake Knot", "Cobra Knot", "King Cobra Knot", "Fishtail Braid", "Trilobite Knot", "Dragon Tongue Knot", "Gaucho Knot", "Fiador (braided)", "Mecate Knot", "Get-Down Rope Knot", "Hackamore (braided noseband)", "Rawhide Knot"], "Lashings & Splices": ["Square Lashing", "Diagonal Lashing", "Shear Lashing", "Tripod Lashing", "West Country Whipping", "Common Whipping", "Sailmaker's Whipping", "Back Splice", "Eye Splice", "Short Splice", "Chain Splice"], "Fishing Knots": ["Palomar Knot", "Improved Clinch Knot", "Uni Knot", "Snell Knot", "Nonslip Loop Knot", "Bimini Twist", "Albright Knot", "Nail Knot", "FG Knot", "Arbor Knot", "Duncan Loop", "Kreh Loop", "Spider Hitch", "Yucatan Knot", "Haywire Twist", "Slim Beauty", "Double Uni Knot", "Blood Knot", "J Knot", "RP Knot", "Seaguar Knot", "San Diego Jam Knot", "Trilene Knot", "Davy Knot", "Double Davy Knot", "Orvis Knot", "Pitxen Knot", "Harvey Knot", "Turle Knot", "Canoeist Knot", "Loop-to-Loop Connection", "Needle Knot", "Whip Finish (fly tying)", "Half Hitch (fly tying)", "Surgeon's End Loop", "Australian Braid", "Plaited Leader Loop", "No-Name Knot", "Red Phillips Knot", "Tony Pena Knot", "Spro Power Swivel Knot", "Knotless Knot", "Blowback Rig Knot", "DFC Knot"]};
var DEMOKIND="tying guide";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — "+field+" sample\n"
   + "record = {'topic': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "print('SAMPLE TOPIC: ' + record['topic'])\n"
   + "print('FIELD: ' + record['field'])\n"
   + "print('This is a labeled structural sample, not an archive record.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — knot tying record',
    title:topic+' — The Knot Database',
    description:'SAMPLE RECORD (generated — structural sample). A knot tying record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
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
var gen={version:'jahdb-knots-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('knots',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
