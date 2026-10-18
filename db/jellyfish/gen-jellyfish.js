(function(){'use strict';
/* JAH The Jellyfish Database generator — jahdb-jellyfish-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-JEL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Moon Jellyfish (Aurelia aurita)", "Lion's Mane Jellyfish (Cyanea capillata)", "Box Jellyfish (Chironex fleckeri)", "Irukandji Jellyfish (Carukia barnesi)", "Portuguese Man o' War (Physalia physalis)", "Immortal Jellyfish (Turritopsis dohrnii)", "Upside-down Jellyfish (Cassiopea xamachana)", "Atlantic Sea Nettle (Chrysaora quinquecirrha)", "Pacific Sea Nettle (Chrysaora fuscescens)", "Compass Jellyfish (Chrysaora hysoscella)", "Blue Blubber Jellyfish (Catostylus mosaicus)"], "Compounded": ["Cannonball Jellyfish (Stomolophus meleagris)", "Fried Egg Jellyfish (Cotylorhiza tuberculata)", "Mauve Stinger (Pelagia noctiluca)", "Crystal Jellyfish (Aequorea victoria)", "Black Sea Nettle (Chrysaora achlyos)", "Crowned Jellyfish (Cephea cephea)", "Spotted Lagoon Jellyfish (Mastigias papua)", "Flame Jellyfish (Rhopilema esculentum)", "Nomura's Giant Jellyfish (Nemopilema nomurai)", "Egg-yolk Jellyfish (Phacellophora camtschatica)", "Japanese Sea Nettle (Chrysaora pacifica)", "Amakusa Jellyfish (Sanderia malayensis)"], "Advanced": ["Mushroom Cap Jellyfish (Rhopilema verrilli)", "Giant Phantom Jelly (Stygiomedusa gigantea)", "Darth Vader Jellyfish (Bathykorus bouilloni)", "Bumpy Jellyfish (Stellamedusa ventana)", "Freshwater Jellyfish (Craspedacusta sowerbii)", "By-the-wind Sailor (Velella velella)", "Blue Button (Porpita porpita)", "Sea Gooseberry (Pleurobrachia bachei)", "Venus's Girdle (Cestum veneris)", "Bloodybelly Comb Jelly (Lampocteis cruentiventer)", "Pink Meanie (Drymonema larsoni)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A jellyfish species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"public-harvest",
    sample:true,
    disclaimer:"Generated sample record \u2014 not an archive record. Seeded archive records are the authoritative entries.",
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
var gen={version:"jahdb-jellyfish-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("jellyfish",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
