(function(){'use strict';
/* JAH Famous Space Missions Database Signature Database generator — "jahdb-famous-space-missions-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMISS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["Signature Aurora: First Signature Crew", "Signature Meridian: Station Assembly", "Signature Perilune: Lunar Flyby", "Signature Touchdown: Lunar Landing", "Signature Base Camp: Lunar Outpost", "Signature Red Transit: Mars Cruise", "Signature First Step: Mars Landing", "Signature Ares Base: Mars Settlement", "Signature Europa Touch: Ocean World", "Signature Titan Splash: Methane Seas", "Signature Comet Catch: Sample Return"], "compounded": ["Signature Venus Dive: Atmosphere Probe", "Signature Mercury Map: Innermost Orbiter", "Signature Asteroid Tour: Five Rocks", "Signature Kuiper Run: Far Flyby", "Signature Sun Grazer: Perihelion Probe", "Signature Interstellar Scout: 200 AU", "Signature Gravity Lens: Solar Telescope", "Signature Exoplanet Direct: Imager", "Signature SETI Sweep: Listening Mission", "Signature Lunar Rescue: Standby Mission", "Signature Station Rescue: Lifeboat Fleet", "Signature Debris Rescue: Stranded Crew"], "advanced": ["Signature Mars Rescue: Ares Standby", "Signature Venus Crew: Cloud Mission", "Signature Jupiter Crew: Flyby Study", "Signature Saturn Rings: Diver Mission", "Signature Neptune Orbiter: Ice Giant", "Signature Uranus Probe: Sideways World", "Signature Pluto Orbiter: Heart Mapper", "Signature Centaur Tour: Hybrid Worlds", "Signature Trojan Camp: Jupiter's Greeks", "Signature Hilda Tour: Outer Belt", "Signature Legacy Mission"]};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+safe+" — structural sample demo\n"
    + "RECORD = "+JSON.stringify({topic:safe,field:field})+"\n"
    + "def main():\n"
    + "    print('Record:', RECORD['topic'])\n"
    + "    print('Field:', RECORD['field'])\n"
    + "    vals = [3, 7, 11]\n"
    + "    print('Sample values:', vals)\n"
    + "    print('Total:', sum(vals))\n"
    + "    print('Demo complete.')\n"
    + "if __name__ == '__main__':\n"
    + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — structural sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A '+field+' sample on "'+topic+'". Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"sample-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-famous-space-missions-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-space-missions-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
