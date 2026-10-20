(function(){'use strict';
/* JAH The Scout Badges Database generator — jahdb-scout-badges-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SB-";
var FIELDS=["BSA Merit Badges", "BSA Rank Badges", "Girl Scout Badges"];
var TOPICS={"BSA Merit Badges": ["Camping Merit Badge", "Hiking Merit Badge", "First Aid Merit Badge", "Swimming Merit Badge", "Lifesaving Merit Badge", "Cooking Merit Badge", "Personal Fitness Merit Badge", "Personal Management Merit Badge", "Family Life Merit Badge", "Communication Merit Badge", "Citizenship in the Community Merit Badge", "Citizenship in the Nation Merit Badge", "Citizenship in Society Merit Badge", "Citizenship in the World Merit Badge", "Emergency Preparedness Merit Badge", "Environmental Science Merit Badge", "Sustainability Merit Badge", "Backpacking Merit Badge", "Canoeing Merit Badge", "Kayaking Merit Badge", "Rowing Merit Badge", "Whitewater Merit Badge", "Small-Boat Sailing Merit Badge", "Motorboating Merit Badge", "Water Sports Merit Badge", "Snorkeling BSA Award", "Scuba Diving Merit Badge", "Climbing Merit Badge", "Orienteering Merit Badge", "Pioneering Merit Badge", "Search and Rescue Merit Badge", "Wilderness Survival Merit Badge", "Geocaching Merit Badge", "Astronomy Merit Badge", "Bird Study Merit Badge", "Mammal Study Merit Badge", "Reptile and Amphibian Study Merit Badge", "Insect Study Merit Badge", "Fish and Wildlife Management Merit Badge", "Forestry Merit Badge", "Geology Merit Badge", "Oceanography Merit Badge", "Weather Merit Badge", "Space Exploration Merit Badge", "Aviation Merit Badge", "Robotics Merit Badge", "Programming Merit Badge", "Digital Technology Merit Badge", "Engineering Merit Badge", "Electronics Merit Badge", "Electricity Merit Badge", "Chemistry Merit Badge", "Nuclear Science Merit Badge", "Medicine Merit Badge", "Veterinary Medicine Merit Badge", "Public Health Merit Badge", "Safety Merit Badge", "Traffic Safety Merit Badge", "Fire Safety Merit Badge", "Crime Prevention Merit Badge", "Fingerprinting Merit Badge", "Law Merit Badge", "American Heritage Merit Badge", "Genealogy Merit Badge", "American Cultures Merit Badge", "Art Merit Badge", "Music Merit Badge", "Theater Merit Badge", "Photography Merit Badge", "Moviemaking Merit Badge", "Animation Merit Badge", "Graphic Arts Merit Badge", "Drafting Merit Badge", "Architecture Merit Badge", "Landscape Architecture Merit Badge", "Home Repairs Merit Badge", "Plumbing Merit Badge", "Painting Merit Badge", "Woodwork Merit Badge", "Metalwork Merit Badge", "Welding Merit Badge", "Automotive Maintenance Merit Badge", "Farm Mechanics Merit Badge", "Dog Care Merit Badge", "Horsemanship Merit Badge", "Athletics Merit Badge", "Sports Merit Badge", "Golf Merit Badge", "Cycling Merit Badge", "Skating Merit Badge", "Snow Sports Merit Badge", "Fly-Fishing Merit Badge", "Fishing Merit Badge", "Hunting Merit Badge", "Game Design Merit Badge", "Chess Merit Badge", "Coin Collecting Merit Badge", "Stamp Collecting Merit Badge", "Radio Merit Badge", "Signs, Signals, and Codes Merit Badge", "Surveying Merit Badge", "Textile Merit Badge", "Leatherwork Merit Badge", "Basketry Merit Badge", "Pottery Merit Badge", "Sculpture Merit Badge", "Wood Carving Merit Badge", "Archaeology Merit Badge", "Entrepreneurship Merit Badge", "American Business Merit Badge", "Public Speaking Merit Badge", "Journalism Merit Badge", "Reading Merit Badge", "Scholarship Merit Badge", "Disabilities Awareness Merit Badge", "Inventing Merit Badge", "Exploration Merit Badge", "Scouting Heritage Merit Badge", "Bugling Merit Badge", "Indian Lore Merit Badge", "Salesmanship Merit Badge"], "BSA Rank Badges": ["Scout Rank", "Tenderfoot Rank", "Second Class Rank", "First Class Rank", "Star Scout Rank", "Life Scout Rank", "Eagle Scout Rank", "Eagle Palms"], "Girl Scout Badges": ["Girl Scout Gold Award", "Girl Scout Silver Award", "Girl Scout Bronze Award", "Brownie Hiker Badge", "Brownie Inventor Badge", "Junior Detective Badge", "Junior Animal Habitats Badge", "Cadette Archery Badge", "Cadette Trailblazing Badge", "Cadette Night Owl Badge", "Senior Truth Seeker Badge", "Ambassador Photographer Badge"]};
var DEMOKIND="requirement checklist";
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
    name:topic+' — scout badge record',
    title:topic+' — The Scout Badges Database',
    description:'SAMPLE RECORD (generated — structural sample). A scout badge record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-scout-badges-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('scout-badges',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
