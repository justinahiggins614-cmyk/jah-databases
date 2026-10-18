(function(){'use strict';
/* JAH The Neighborhood Signature Database generator — jahdb-neighborhood-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NBHS-";
var FIELDS=["Meeting Neighbors","Gatherings & Block Parties","Community Gardens & Shared Spaces","Neighborhood Safety","Local Groups & Civic Life","Welcoming & Belonging","Resolving Neighbor Issues"];
var TOPICS={
 "Meeting Neighbors": [
  "Introducing Yourself to Neighbors (Signature Edition) - Meeting Neighbors",
  "The Front Porch Principle (Signature Edition) - Meeting Neighbors",
  "Remembering Names and Details (Signature Edition) - Meeting Neighbors",
  "Small Favors, Big Community (Signature Edition) - Meeting Neighbors",
  "Neighborhood Communication Channels (Signature Edition) - Meeting Neighbors"
 ],
 "Gatherings & Block Parties": [
  "Planning a Block Party (Signature Edition) - Gatherings & Block Parties",
  "Potlucks and Progressive Dinners (Signature Edition) - Gatherings & Block Parties",
  "Holiday Events on the Block (Signature Edition) - Gatherings & Block Parties",
  "Game Nights and Movie Nights (Signature Edition) - Gatherings & Block Parties",
  "Welcoming New Neighbors as a Block (Signature Edition) - Gatherings & Block Parties"
 ],
 "Community Gardens & Shared Spaces": [
  "Starting a Community Garden (Signature Edition) - Community Gardens & Shared Spaces",
  "Shared Spaces: Parks, Playgrounds, and Trails (Signature Edition) - Community Gardens & Shared Spaces",
  "Little Free Libraries and Sharing Boxes (Signature Edition) - Community Gardens & Shared Spaces",
  "Beautification Projects That Unite (Signature Edition) - Community Gardens & Shared Spaces"
 ],
 "Neighborhood Safety": [
  "Neighborhood Watch That Works (Signature Edition) - Neighborhood Safety",
  "Lighting, Visibility, and CPTED Basics (Signature Edition) - Neighborhood Safety",
  "Knowing Your Neighbors Is Safety (Signature Edition) - Neighborhood Safety",
  "Emergency Preparedness as a Block (Signature Edition) - Neighborhood Safety",
  "Traffic Calming and Safe Streets (Signature Edition) - Neighborhood Safety"
 ],
 "Local Groups & Civic Life": [
  "Joining and Starting Local Clubs (Signature Edition) - Local Groups & Civic Life",
  "The Neighborhood Association (Signature Edition) - Local Groups & Civic Life",
  "Attending City Council and Local Meetings (Signature Edition) - Local Groups & Civic Life",
  "Voting Local: Why It Matters Most (Signature Edition) - Local Groups & Civic Life",
  "Volunteering for Local Campaigns and Causes (Signature Edition) - Local Groups & Civic Life"
 ],
 "Welcoming & Belonging": [
  "Making Newcomers Feel They Belong (Signature Edition) - Welcoming & Belonging",
  "Inclusive Neighborhoods: Everyone Belongs (Signature Edition) - Welcoming & Belonging",
  "Intergenerational Community (Signature Edition) - Welcoming & Belonging",
  "Block Identity: Name, Pride, and Story (Signature Edition) - Welcoming & Belonging"
 ],
 "Resolving Neighbor Issues": [
  "Talking to Neighbors About Problems (Signature Edition) - Resolving Neighbor Issues",
  "Noise: The Classic Neighbor Issue (Signature Edition) - Resolving Neighbor Issues",
  "Property Lines, Fences, and Trees (Signature Edition) - Resolving Neighbor Issues",
  "Mediation for Neighbor Disputes (Signature Edition) - Resolving Neighbor Issues",
  "When Neighbors Won't Resolve: Next Steps (Signature Edition) - Resolving Neighbor Issues",
  "Being the Neighbor Everyone Wants (Signature Edition) - Resolving Neighbor Issues"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Neighborhood Study — "+safe+"\n"
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
    name:topic+' — neighborhood guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A neighborhood guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"neighborhood-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-neighborhood-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('neighborhood-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
