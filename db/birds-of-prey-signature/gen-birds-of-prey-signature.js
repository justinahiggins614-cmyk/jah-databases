(function(){'use strict';
/* JAH Signature Birds of Prey Database generator — jahdb-birds-of-prey-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Samples are clearly labeled structural
   samples and are never archive records. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BOPS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["Signature Study: Bald Eagle (Haliaeetus leucocephalus)", "Signature Study: Golden Eagle (Aquila chrysaetos)", "Signature Study: Peregrine Falcon (Falco peregrinus)", "Signature Study: Red-tailed Hawk (Buteo jamaicensis)", "Signature Study: Osprey (Pandion haliaetus)", "Signature Study: Harpy Eagle (Harpia harpyja)", "Signature Study: Philippine Eagle (Pithecophaga jefferyi)", "Signature Study: California Condor (Gymnogyps californianus)", "Signature Study: Andean Condor (Vultur gryphus)", "Signature Study: Secretarybird (Sagittarius serpentarius)", "Signature Study: Eurasian Sparrowhawk (Accipiter nisus)"], "Compounded": ["Signature Study: Northern Goshawk (Accipiter gentilis)", "Signature Study: Common Buzzard (Buteo buteo)", "Signature Study: White-tailed Eagle (Haliaeetus albicilla)", "Signature Study: Steller's Sea Eagle (Haliaeetus pelagicus)", "Signature Study: Martial Eagle (Polemaetus bellicosus)", "Signature Study: Crowned Eagle (Stephanoaetus coronatus)", "Signature Study: Gyrfalcon (Falco rusticolus)", "Signature Study: American Kestrel (Falco sparverius)", "Signature Study: Eurasian Kestrel (Falco tinnunculus)", "Signature Study: Merlin (Falco columbarius)", "Signature Study: Northern Harrier (Circus hudsonius)", "Signature Study: Western Marsh Harrier (Circus aeruginosus)"], "Advanced": ["Signature Study: Black Kite (Milvus migrans)", "Signature Study: Red Kite (Milvus milvus)", "Signature Study: Turkey Vulture (Cathartes aura)", "Signature Study: Black Vulture (Coragyps atratus)", "Signature Study: Griffon Vulture (Gyps fulvus)", "Signature Study: Lappet-faced Vulture (Torgos tracheliotos)", "Signature Study: Egyptian Vulture (Neophron percnopterus)", "Signature Study: Bearded Vulture (Gypaetus barbatus)", "Signature Study: Crested Caracara (Caracara plancus)", "Signature Study: Laughing Falcon (Herpetotheres cachinnans)", "Signature Study: Bat Falcon (Falco rufigularis)"]};
var DEMOKIND="species fact check";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Signature species demo\n# Topic: \""+safe+"\" | Field: "+field+"\n"
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
    description:"SAMPLE RECORD (generated \u2014 structural sample). A Signature bird of prey species record of \""+topic+"\" in "+field+". Generated samples are clearly labeled and never presented as archive records.",
    field:field,
    src:"signature-generated",
    sample:true,
    disclaimer:"Generated Signature sample record \u2014 not an archive record. Seeded Signature records are the authoritative entries.",
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
var gen={version:"jahdb-birds-of-prey-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("birds-of-prey-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
