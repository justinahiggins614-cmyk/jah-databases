(function(){'use strict';
/* JAH The Podcast Idea Factory Database generator — jahdb-podcast-idea-factory-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working podcast factory: every call creates a complete show concept —
   title, tagline, format, two hosts with bios, six episode ideas, target audience,
   and a ready-to-render cover-art SVG.
   Deterministic: same seed, same show. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-PCIFS-";
var FIELDS=["Talk & Interview","Story & Narrative","Comedy & Play"];
var TITLES={"Talk & Interview":[["The Long Table","conversations that run past midnight"],["Signal & Noise","finding the story in the static"],["Second Draft","creators on the work before the work"],["The Green Room","what guests say after the show"]],
 "Story & Narrative":[["The Paper Trail","mysteries told in documents"],["Low Orbit","dispatches from the edge"],["The Lantern Archive","stories kept in the dark"],["Halfway Home","journeys that changed the teller"]],
 "Comedy & Play":[["The Pun Also Rises","wordplay with ambition"],["Serious Nonsense","very silly, very smart"],["The Laugh Track","comedy, examined"],["Yes, And...","improv games with real stakes"]]};
var FORMATS={"Talk & Interview":"weekly long-form conversation, 60–90 minutes, one guest, cold open with the best moment",
 "Story & Narrative":"serialized narrative, 30–45 minutes, scored and sound-designed, season arcs of eight episodes",
 "Comedy & Play":"panel games and bits, 45 minutes, recurring segments, audience call-ins"};
var FIRST=["Mara","Jules","Theo","Priya","Dario","Wren","Kai","Lena","Otis","Suki","Rafe","Nadia"];
var LAST=["Vance","Okafor","Lindqvist","Marsh","Delacroix","Kim","Reyes","Novak"];
var BIOS=["a former radio producer who asks the question nobody asks","a comedian with a researcher\u2019s heart","a novelist who treats every guest like a character","a sound designer who hears stories in noise","a journalist who laughs at the wrong moments","an archivist of other people\u2019s best stories"];
var EPISODES={"Talk & Interview":["The guest who almost didn\u2019t come","Failure, ranked","The 3am question","Mentors and rivals","The episode with no guest","Live from the green room"],
 "Story & Narrative":["The letter that started it","Static: episode one","The map room","What the tape caught","The return","Season finale: the lantern"],
 "Comedy & Play":["Pun championship semifinals","The bit that bombed (and why)","Call-in chaos hour","Improv: the haunted studio","The roast of the hosts","Live show spectacular"]};
var AUDIENCES={"Talk & Interview":"curious commuters and late-night thinkers","Story & Narrative":"headphone people who finish every series","Comedy & Play":"anyone who laughs at wordplay in traffic"};
function coverSVG(initial,cols){
  return '<svg xmlns="http://www.w3.org/2000/svg" width="300" height="300" viewBox="0 0 300 300"><rect width="300" height="300" fill="'+cols[1]+'"/><rect x="30" y="30" width="240" height="240" rx="24" fill="'+cols[0]+'"/><text x="150" y="185" font-family="Georgia,serif" font-size="110" font-weight="bold" text-anchor="middle" fill="'+cols[1]+'">'+initial+'</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var tt=pick(TITLES[field],s);
  var hosts=[{name:pick(FIRST,s)+" "+pick(LAST,s),bio:pick(BIOS,s)},{name:pick(FIRST,s)+" "+pick(LAST,s),bio:pick(BIOS,s)}];
  var eps=pickN(EPISODES[field],s,6);
  var pal=pick([["#FF6B35","#2B2D42"],["#20BF9F","#0B4F6C"],["#8A1C7C","#F7C548"],["#005EB8","#F5F0E1"]],s);
  var svg=coverSVG(tt[0].charAt(0),pal);
  var title=tt[0]+" — podcast concept";
  var desc='GENERATED PODCAST — "'+tt[0]+'": '+tt[1]+'. A '+field.toLowerCase()+' show ('+FORMATS[field]+'), hosted by '+hosts[0].name+' and '+hosts[1].name+'. Six launch episodes planned. For '+AUDIENCES[field]+'.';
  var prog="# Podcast concept — "+tt[0]+"\n"
    +"title = \""+tt[0]+"\"\n"+"tagline = \""+tt[1]+"\"\n"+"format_ = \""+FORMATS[field]+"\"\n"
    +"hosts = "+JSON.stringify(hosts.map(function(h){return h.name;}))+"\n"
    +"episodes = "+JSON.stringify(eps)+"\n"
    +"print(\"Podcast:\", title)\n"+"print(\"Tagline:\", tagline)\n"+"print(\"Format:\", format_)\n"
    +"print(\"Hosts:\", \", \".join(hosts))\n"+"print(\"Launch episodes:\")\n"
    +"[print(\" %d. %s\" % (i+1, e)) for i, e in enumerate(episodes)]\n"
    +"print(\"Cover SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — podcast record', title:title, description:desc,
    how_it_works:'The factory picks a show title and tagline from the '+field+' pool, assigns the field\u2019s format, creates two hosts with names and bios, and plans six launch episode titles. The cover-art SVG renders the show initial in a generated palette — deterministic per seed.',
    key_points:['Show: "'+tt[0]+'" — '+tt[1],'Format: '+FORMATS[field],'Hosts: '+hosts.map(function(h){return h.name+" ("+h.bio+")";}).join('; '),'Episodes: '+eps.join('; '),'Audience: '+AUDIENCES[field]+'.','Deterministic: seed '+seed+' always rebuilds this exact show.'],
    requirements:['A seed number to regenerate this exact show','An HTML file to view the cover SVG'],
    standards:['Title and tagline are original','Two hosts with distinct bios','Six episode titles planned','Cover SVG renders the show initial'],
    citations:['Podcast craft references: format design.','Audio storytelling references: episode architecture.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{show:tt[0],tagline:tt[1],format:FORMATS[field],hosts:hosts,episodes:eps,audience:AUDIENCES[field],svg:svg},
    svg:svg,
    demo:{kind:'podcast-plan',language:'python',program:prog,note:'Prints the show concept, hosts, and six launch episodes.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.output||!r.output.hosts||r.output.hosts.length!==2)e.push('hosts');
  if(!r.output||!r.output.episodes||r.output.episodes.length!==6)e.push('episodes');
  if(!r.output||!r.output.svg||r.output.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate podcast in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-podcast-idea-factory-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('podcast-idea-factory-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();