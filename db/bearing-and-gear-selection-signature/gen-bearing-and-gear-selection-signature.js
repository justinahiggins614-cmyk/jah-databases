(function(){'use strict';
/* Bearing and Gear Selection Database generator — jahdb-bearing-and-gear-selection-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BGSS-";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={"Foundations": ["Load Characterization", "L10 Life", "Bearing Types", "Lubrication Choice", "Fits and Clearance", "Sealing", "Gear Types", "Gear Rating", "Gear Lubrication", "Mounting Discipline", "Alignment"], "Compounded": ["Condition Monitoring", "Catalog Navigation", "Equivalent Loads", "Speed Limits", "Preload", "Backlash", "Noise Control", "Efficiency", "Materials", "Heat Treatment", "Surface Finish", "Contamination Control"], "Advanced": ["Failure Analysis", "Root Causes", "Spares Strategy", "Cost vs Life", "Custom vs Catalog", "Supplier Quality", "Installation Tools", "Storage", "Documentation", "Training", "Case Studies"]};
var SRC="signature";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n\"\"\""+safe+" — "+field+" demo.\nRecord demo. Property of Justin Addam Higgins (JAH).\n\"\"\"\n"
   + "TOPIC = \""+safe+"\"\n"
   + "FIELD = \""+field+"\"\n"
   + "STEPS = ['Describe the goal in one sentence','List what is known','Take the cheapest first step','Verify the result']\n"
   + "def main():\n"
   + "    print('Demo:', TOPIC, '[' + FIELD + ']')\n"
   + "    [print('  %d. %s' % (i+1, s)) for i, s in enumerate(STEPS)]\n"
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
    name:topic+' — '+"signature original",
    title:topic,
    description:'Signature original sample: '+'A '+field.toLowerCase()+' study of "'+topic+'" in the Bearing and Gear Selection Database. Generated sample records are clearly labeled and never presented as archive records.',
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"bearing-and-gear-selection-signature-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:"jahdb-bearing-and-gear-selection-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("bearing-and-gear-selection-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
