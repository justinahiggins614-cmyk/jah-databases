(function(){'use strict';
/* JAH The Which Design Wins Database generator — jahdb-db-which-design-wins-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WDW-";
var FIELDS=["Structural Designs","Everyday Designs","Digital Designs"];
var TOPICS={
 "Structural Designs": [
  "Suspension vs Arch Bridge: Span Designs - Structural Designs",
  "Dome vs Flat Roof: Shelter Designs - Structural Designs",
  "Skyscraper vs Courtyard Block: City Designs - Structural Designs",
  "Dam vs Levee Revisited: Water Designs - Structural Designs",
  "Truss vs Beam: Bridge Skeletons - Structural Designs",
  "Igloo vs Tent: Cold Shelters - Structural Designs",
  "Pyramid vs Ziggurat Revisited: Monument Designs - Structural Designs",
  "Cathedral vs Mosque: Sacred Designs - Structural Designs",
  "Stadium Bowl vs Arena: Crowd Designs - Structural Designs",
  "Lighthouse vs Buoy: Sea Marks - Structural Designs",
  "Windmill vs Wind Turbine: Wind Designs - Structural Designs",
  "Castle vs Fort: Defense Designs - Structural Designs"
 ],
 "Everyday Designs": [
  "QWERTY vs Dvorak: Keyboard Designs - Everyday Designs",
  "Eames Lounge vs IKEA Poang: Chair Designs - Everyday Designs",
  "Faucet: Single vs Double Handle - Everyday Designs",
  "Zipper vs Buttons: Closure Designs - Everyday Designs",
  "Mug vs Tumbler: Drink Designs - Everyday Designs",
  "Notebook: Spiral vs Bound - Everyday Designs",
  "Umbrella vs Raincoat: Rain Designs - Everyday Designs",
  "Backpack vs Suitcase: Carry Designs - Everyday Designs",
  "Knife Block vs Magnetic Strip: Kitchen Designs - Everyday Designs",
  "Shower vs Bath: Wash Designs - Everyday Designs"
 ],
 "Digital Designs": [
  "iOS vs Android: Phone Designs - Digital Designs",
  "Light vs Dark Mode: Interface Designs - Digital Designs",
  "Tabs vs Spaces: Code Designs - Digital Designs",
  "Feed vs Chronological: Social Designs - Digital Designs",
  "App vs Website: Software Designs - Digital Designs",
  "Search vs Browse: Discovery Designs - Digital Designs",
  "Password vs Passkey: Login Designs - Digital Designs",
  "Cloud vs Local: Storage Designs - Digital Designs",
  "Subscription vs Purchase: Ownership Designs - Digital Designs",
  "Notification vs Silence: Attention Designs - Digital Designs",
  "Map (Paper) vs GPS: Navigation Designs - Digital Designs",
  "E-book vs Audiobook: Reading Designs - Digital Designs"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Which Design Wins Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — design comparison record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A design comparison record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"which-design-wins-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-db-which-design-wins-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-which-design-wins',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
