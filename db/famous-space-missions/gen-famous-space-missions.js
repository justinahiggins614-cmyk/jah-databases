(function(){'use strict';
/* JAH Famous Space Missions Database generator — "jahdb-famous-space-missions-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SMIS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["Apollo 11 (1969): First Moon Landing", "Apollo 8 (1968): First Around the Moon", "Apollo 13 (1970): The Successful Failure", "Vostok 1 (1961): First Human in Space", "STS-1 Columbia (1981): First Shuttle Flight", "Voyager Grand Tour (1977-1989)", "Hubble Servicing Mission 1 (1993)", "Cassini-Huygens (1997-2017)", "Mars Pathfinder (1997)", "ISS Expedition 1 (2000)", "Curiosity Landing (2012)"], "compounded": ["Apollo 17 (1972): Last Moonwalk", "Skylab (1973-1974)", "Salyut 1 (1971): First Space Station", "Venera Program (1961-1984)", "Viking (1976): First Mars Landers", "Galileo (1989-2003)", "NEAR Shoemaker (1996-2001)", "Deep Impact (2005)", "Rosetta and Philae (2004-2016)", "Hayabusa (2003-2010)", "Chang'e 4 (2019): Far Side Landing", "Tianwen-1 (2021): China's Mars"], "advanced": ["Apollo-Soyuz (1975): The Handshake", "STS-135 (2011): Last Shuttle Flight", "New Horizons Pluto Flyby (2015)", "Juno (2016-): Jupiter Polar Orbiter", "OSIRIS-REx (2016-2023): Asteroid Sample", "DART (2022): The Asteroid Deflection", "Artemis I (2022): The Moon Return Begins", "Inspiration4 (2021): First All-Civilian Orbit", "Polaris Dawn (2024): First Commercial Spacewalk", "Shenzhou 5 (2003): China's First Taikonaut", "The Missions That Made Us: Capstone"]};
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
var gen={version:"jahdb-famous-space-missions-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("famous-space-missions",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
