(function(){'use strict';
/* JAH Subway Systems of the World Database generator — "jahdb-subway-systems-world-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUBW-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["What Is a Metro", "London Underground: 1863, The First", "Paris Métro: 1900", "New York Subway: 1904", "Moscow Metro: The Palaces", "Tokyo Metro: The Busiest", "Beijing Subway: The Fastest Growth", "Seoul Metro: The Digital Pioneer", "Shanghai Metro: The Longest Network", "Delhi Metro: The Developing-World Model", "Driverless Metros: The Automated Future"], "compounded": ["Berlin U-Bahn: 1902", "Madrid Metro: The Build Machine", "Singapore MRT: The Priced Road", "Hong Kong MTR: The Profitable Metro", "Mexico City Metro: 1969", "São Paulo Metro: Brazil's Artery", "Cairo Metro: Africa's First", "Istanbul Metro: Two Continents", "Toronto Subway and the TTC", "Chicago L: The Elevated", "Washington Metro: The Brutalist", "BART: The Futuristic Experiment"], "advanced": ["Elizabeth Line: London's Crossrail", "Grand Paris Express: The Mega-Project", "Riyadh Metro: The Desert Megaproject", "Doha Metro: The Gulf Showcase", "Lagos Metro: Africa's Megacity Answer", "Jakarta MRT: The Traffic Solution", "Bangkok's BTS and MRT", "Kuala Lumpur's Klang Valley", "Sydney Metro: Australia's First Driverless", "Athens Metro: Archaeology Underground", "The Underground City: Capstone"]};
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
var gen={version:"jahdb-subway-systems-world-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("subway-systems-world",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
