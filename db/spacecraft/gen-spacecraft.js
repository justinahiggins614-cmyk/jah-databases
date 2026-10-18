(function(){'use strict';
/* JAH Spacecraft Database generator — "jahdb-spacecraft-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SPCR-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["How Rockets Work: Action and Reaction", "Sputnik 1: 1957, The Beep", "Vostok 1: Gagarin, 1961", "Mercury: America's First Steps", "Gemini: Learning to Work in Space", "Saturn V: The Moon Rocket", "Apollo 11: The Moon Landing", "Space Shuttle: The Reusable Dream", "Soyuz: The Workhorse", "Mir: The First Station", "ISS: The Orbital Outpost"], "compounded": ["Falcon 9: The Reusable Revolution", "Crew Dragon: The Commercial Crew", "Starship: The Giant", "Ariane: Europe's Launcher", "Long March: China's Fleet", "PSLV and GSLV: India's Launchers", "H-II: Japan's Launcher", "Electron: The Small Launcher", "New Shepard: The Tourist Hop", "Orion and SLS: The Moon Return", "Starliner: The Second Taxi", "Shenzhou and Tiangong: China's Station"], "advanced": ["Hubble: The Eye in Orbit", "James Webb: The Infrared Giant", "Voyager 1 and 2: The Interstellar", "Mars Rovers: Sojourner to Perseverance", "Cassini: The Saturn Grand Tour", "New Horizons: The Pluto Flyby", "Parker Solar Probe: Touching the Sun", "Starlink: The Mega-Constellation", "Dream Chaser: The Spaceplane Returns", "SpaceShipTwo: The Tourist Climb", "The Spacefaring Species: Capstone"]};
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
var gen={version:"jahdb-spacecraft-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("spacecraft",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
