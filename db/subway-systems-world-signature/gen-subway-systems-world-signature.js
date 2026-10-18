(function(){'use strict';
/* JAH Subway Systems of the World Database Signature Database generator — "jahdb-subway-systems-world-signature-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-SUBWS-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={"foundations": ["Signature Meridian Metro", "Signature Harbor Metro", "Signature Mountain Metro", "Signature Desert Metro", "Signature Island Metro", "Signature Museum Metro", "Signature Garden Metro", "Signature Night Metro", "Signature Express Metro", "Signature Cargo Metro", "Signature Flood Metro"], "compounded": ["Signature Quake Metro", "Signature Heritage Metro", "Signature Art Metro", "Signature Music Metro", "Signature Library Metro", "Signature Food Metro", "Signature Fitness Metro", "Signature School Metro", "Signature Senior Metro", "Signature Child Metro", "Signature Pet Metro", "Signature Green Tunnel"], "advanced": ["Signature Hyper Metro", "Signature Loop", "Signature Pod Metro", "Signature Gondola Metro", "Signature Water Metro", "Signature Bike Metro", "Signature Solar Metro", "Signature Quiet Metro", "Signature Deep Metro", "Signature Sky Metro", "Signature Legacy Metro"]};
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
var gen={version:"jahdb-subway-systems-world-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("subway-systems-world-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
