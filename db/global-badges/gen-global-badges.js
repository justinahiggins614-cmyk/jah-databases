(function(){'use strict';
/* JAH The Global Badges Database generator — jahdb-global-badges-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GB-";
var FIELDS=["Aviation & Naval Badges", "Civic Honors", "Digital Badges", "Gaming Badges", "Professional Credentials", "Service Badges", "Sporting Honors", "US Military Decorations", "US Qualification Badges", "World Military Honors", "World Scouting"];
var TOPICS={"World Scouting": ["King's Scout Award", "Chief Scout's Gold Award", "Queen's Scout Award (Australia)", "Chief Scout's Award (Canada)", "President's Scout Award (Singapore)", "Fuji Scout (Japan)", "Tiger Scout Award (Korea)", "Scout of the World Award", "Wood Badge", "Order of the Arrow Vigil Honor"], "US Military Decorations": ["Medal of Honor", "Distinguished Service Cross", "Navy Cross", "Air Force Cross", "Silver Star", "Legion of Merit", "Distinguished Flying Cross", "Bronze Star Medal", "Purple Heart", "Air Medal", "Army Commendation Medal", "Meritorious Service Medal", "National Defense Service Medal", "Good Conduct Medal"], "US Qualification Badges": ["Combat Infantryman Badge", "Expert Infantryman Badge", "Combat Action Badge", "Parachutist Badge (Jump Wings)", "Air Assault Badge", "Ranger Tab", "Special Forces Tab", "Sapper Tab", "Pathfinder Badge", "Diver Badge", "Cyberspace Badge"], "Aviation & Naval Badges": ["Pilot Wings (USAF)", "Naval Aviator Wings", "Submarine Warfare Insignia (Dolphins)", "SEAL Trident", "EOD Badge (The Crab)", "Astronaut Badge"], "World Military Honors": ["Victoria Cross", "George Cross", "Military Cross", "Croix de Guerre", "Legion of Honour", "Iron Cross", "Order of the Rising Sun", "Hero of the Soviet Union", "Pour le Merite"], "Civic Honors": ["Presidential Medal of Freedom", "Congressional Gold Medal", "Nobel Prize Medal", "Order of the British Empire", "Order of Canada", "Bharat Ratna", "Order of Australia", "National Medal of Arts", "Legion d'honneur (Civil)"], "Professional Credentials": ["CPA License", "Professional Engineer (PE) Seal", "PMP Certification", "CISSP Certification", "Six Sigma Black Belt", "FAA Pilot Certificate", "FAA Remote Pilot Certificate"], "Service Badges": ["Police Badge (Shield)", "Firefighter Badge (Maltese Cross)", "Sheriff's Star", "Star of Life", "Lifeguard Emblem", "National Park Ranger Badge", "FBI Badge and Credentials", "U.S. Secret Service Star"], "Gaming Badges": ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge", "PlayStation Platinum Trophy", "Xbox Achievement (Gamerscore)", "World of Warcraft Feat of Strength", "Steam Badge"], "Digital Badges": ["Arctic Code Vault Badge", "Mars 2020 Contributor Badge", "Starstruck Badge", "Pair Extraordinaire Badge", "Quickdraw Badge", "Pull Shark Badge", "Galaxy Brain Badge", "Mozilla Open Badge", "Stack Overflow Legendary Badge", "Duolingo League Badge"], "Sporting Honors": ["Olympic Gold Medal", "FIFA World Cup Winner's Medal", "Super Bowl Ring", "NASA Mission Patch"]};
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
    name:topic+' — global badge record',
    title:topic+' — The Global Badges Database',
    description:'SAMPLE RECORD (generated — structural sample). A global badge record sample of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
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
var gen={version:'jahdb-global-badges-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('global-badges',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
