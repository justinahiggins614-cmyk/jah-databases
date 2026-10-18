(function(){'use strict';
/* JAH Private Jets Database generator — "jahdb-private-jets-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PJET-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["What Is a Private Jet: Business Aviation Basics", "Learjet 23: The Original Bizjet", "Lockheed JetStar: First Business Jet", "Cabin Classes: VLJ to Ultra-Long-Range", "Owning vs Chartering vs Fractional", "FBOs: The Private Terminal", "Cessna Citation I: The Efficient Pioneer", "Dassault Falcon 20: French Business Jet", "Gulfstream II: Long-Range Luxury", "How Pressurization Works in Business Jets", "Business Jet Avionics Basics"], "compounded": ["Learjet 24 and 25: The Classic Learjets", "Hawker 800: The British Business Jet", "Beechjet 400: The Military Trainer Jet", "Cessna Citation X: Fastest Civilian Jet", "Gulfstream IV: The 1980s Flagship", "Gulfstream V: Ultra-Long-Range Pioneer", "Bombardier Global Express: Canadian Challenger", "Eclipse 500: The Very Light Jet Pioneer", "Embraer Phenom 100 and 300: Brazilian Challengers", "HondaJet: Overwing Engines", "Pilatus PC-24: The Super Versatile Jet", "Cirrus Vision Jet SF50: Single-Engine VLJ"], "advanced": ["Gulfstream G650: Range King", "Gulfstream G700 and G800", "Bombardier Global 7500", "Dassault Falcon 10X", "Cessna Citation Longitude", "Embraer Praetor 500 and 600", "Sustainable Aviation Fuel in Business Aviation", "Business Jet Operating Costs Explained", "Supersonic Business Jets: The Next Race", "The Future: Electric and Autonomous Bizjets", "Business Aviation's Role: Time as the Product"]};
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
var gen={version:"jahdb-private-jets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("private-jets",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
