(function(){'use strict';
/* JAH The Hidden Object Database Database generator — jahdb-db-hidden-object-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-HIDOBJ-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "Hunt: A sunny park with trees, a pond, and a picnic blanket...",
  "Hunt: A cozy living room with a sofa, bookshelf, and firepla...",
  "Hunt: A beach with umbrellas, towels, and a snack stand...",
  "Hunt: A classroom with desks, a chalkboard, and a fish tank...",
  "Hunt: A kitchen with cabinets, a stove, and a fruit bowl...",
  "Hunt: A garden with flowers, a fence, and a birdbath...",
  "Hunt: A toy room with a rug, toy chest, and bunk bed...",
  "Hunt: A snowy yard with a snowman, sled, and pine trees...",
  "Hunt: A library with tall shelves, a globe, and a reading ch...",
  "Hunt: A farm with a barn, tractor, and hay bales...",
  "Hunt: A campsite with a tent, campfire, and cooler..."
 ],
 "Compounded": [
  "Hunt: A busy market street with stalls, awnings, and crowds...",
  "Hunt: A museum hall with paintings, statues, and a skylight...",
  "Hunt: A jungle clearing with vines, a waterfall, and ruins...",
  "Hunt: A train station with platforms, clocks, and luggage...",
  "Hunt: An attic with trunks, a dress form, and a round window...",
  "Hunt: A harbor with boats, ropes, and seagulls...",
  "Hunt: A bakery with ovens, display cases, and flour dust...",
  "Hunt: A construction site with cranes, scaffolds, and cones...",
  "Hunt: A aquarium tunnel with sharks, rays, and blue light...",
  "Hunt: A festival night with lanterns, stalls, and a stage...",
  "Hunt: A snowy mountain lodge with skis, a fireplace, and win...",
  "Hunt: A greenhouse with orchids, misters, and stone paths..."
 ],
 "Advanced": [
  "Hunt: A camouflaged forest floor in autumn: leaves, twigs, a...",
  "Hunt: A magician's stage mid-act: curtains, trapdoors, and m...",
  "Hunt: A coral reef at dusk: fans, sponges, and schooling fis...",
  "Hunt: A detective's evidence wall: photos, strings, and note...",
  "Hunt: A starry desert night: dunes, a telescope, and a campf...",
  "Hunt: A busy harbor in fog: masts, buoys, and gulls...",
  "Hunt: An old master painting: a banquet with 20 guests...",
  "Hunt: A space station interior: panels, cables, and viewport...",
  "Hunt: A rainy city street at night: neon, puddles, and umbre...",
  "Hunt: A library's rare books room: glass cases, ladders, and...",
  "Hunt: A glacier crevasse field: blue ice, snow bridges, and..."
 ]
};
var DEMOKIND="hunt-proof";
var SAMPLEDESC="";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Hidden Object Study — "+safe+"\n"
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
    name:topic+' — hidden object record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A hidden object record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records. '+SAMPLEDESC,
    field:field,
    src:'public-harvest',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
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
var gen={version:'jahdb-db-hidden-object-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('db-hidden-object',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
