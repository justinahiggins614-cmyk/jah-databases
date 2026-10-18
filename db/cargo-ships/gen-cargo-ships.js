(function(){'use strict';
/* JAH Cargo Ships Database generator — "jahdb-cargo-ships-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CGSH-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["What Is a Cargo Ship: Moving the World's Goods", "How Ships Float: Buoyancy and Load Lines", "Bulk Carriers: The Tramps of the Sea", "Containerization: Malcom McLean's Revolution", "The TEU: How Containers Are Counted", "Tankers: Moving Liquid Cargo", "General Cargo Ships", "RoRo Ships: Roll On, Roll Off", "Liberty Ships: WWII Mass Production", "Ports and Terminals: Where Cargo Meets Land", "The Plimsoll Mark: Load Lines Explained"], "compounded": ["Ideal X: First Container Ship", "Emma Maersk: The E-Class Giant", "MSC Irina and Ever Alot: 24,000-TEU Giants", "TI-Class Supertankers: Largest Ships Ever", "Valemax: Giant Ore Carriers", "LNG Carriers: Floating Gas Pipelines", "Car Carriers: Pure Car and Truck Carriers", "Refrigerated Ships: Reefers", "Heavy-Lift Ships", "Panama Canal and Panamax", "Suez Canal and Suezmax", "Flags of Convenience"], "advanced": ["Slow Steaming: Saving Fuel", "Green Shipping: Ammonia and Methanol", "Autonomous Ships: The Crewless Future", "IMO and SOLAS: Rules of the Sea", "Container Terminal Automation", "The Ever Given: Suez Blockage 2021", "Breakbulk and Project Cargo", "Chemical Tankers", "Livestock Carriers", "Wind-Assisted Propulsion: Sails Return", "Ninety Percent of World Trade: The Capstone"]};
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
var gen={version:"jahdb-cargo-ships-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("cargo-ships",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
