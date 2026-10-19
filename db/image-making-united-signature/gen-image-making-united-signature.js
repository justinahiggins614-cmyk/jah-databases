(function(){'use strict';
/* JAH The United Image-Making Master Database generator — jahdb-image-making-united-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-IMUN-SIG-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={"Foundations": ["The 22 Ways: A Complete Map", "Choosing Your Way: The Decision Framework", "Capture vs Create: The Fundamental Divide", "The Honest Image: Truth Across Methods", "Photography into Painting: The Classic Pipeline", "AI Generation into Hand Finishing", "3D Rendering into Photomontage", "Photogrammetry into 3D Art", "Darkroom Craft into Digital Archive", "Printmaking Meets Digital Design", "Mosaic Thinking in Pixels"], "Compounded": ["Collage Logic in Compositing", "Vector Precision, Painterly Soul", "Restoration Across All Media", "Upscaling the Archive", "Style Transfer as Study Tool", "NeRFs for Every Image-Maker", "The Portrait Across 22 Ways", "The Landscape Across 22 Ways", "Speed Ranking: Fastest to Slowest", "Cost Ranking: Cheapest to Dearest", "Learning Curves Compared", "Combining Three or More Ways"], "Advanced": ["The Business of Many Ways", "Teaching the Whole Map", "The Future of Image-Making", "Your First Year: The United Curriculum", "The Master Image-Maker's Oath", "The Image-Maker's Library: Essential References", "Critique Culture: Giving and Receiving", "The 10,000-Hour Map: Deliberate Practice Design", "Health and the Image-Maker: Body, Eyes, Mind", "The Image-Maker's Finances", "Legacy: What Your Images Leave Behind"]};
var DEMOKIND="method choosing";
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# "+DEMOKIND+" — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — united image-making master record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A united image-making master record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature',
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
var gen={version:'jahdb-image-making-united-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('image-making-united-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
