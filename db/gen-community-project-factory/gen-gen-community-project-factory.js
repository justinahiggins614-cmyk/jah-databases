(function(){'use strict';
/* The The Community Project Factory generator — jahdb-gen-community-project-factory-pub-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}

var PREFIX="JAH-FUN-COMMUNITY-PROJECT-FACTORY-PUB-";
var GENVER="jahdb-gen-community-project-factory-pub-1.0";
var FIELDS=["Foundations", "Compounded", "Advanced"];
var TOPICS={
 "Foundations": [
  "The Mural",
  "The Playlist",
  "The Photo Pool",
  "The Story Chain",
  "The Recipe Book",
  "The Map",
  "The Playlist Swap",
  "The Quote Wall",
  "The Time Capsule",
  "The Garden",
  "The Cleanup",
  "The Welcome Kit"
 ],
 "Compounded": [
  "The Zine",
  "The Film",
  "The Album",
  "The Game",
  "The Wiki",
  "The Festival",
  "The Charity Build",
  "The Oral History",
  "The Art Show",
  "The Cookbook",
  "The Podcast",
  "The Makerspace"
 ],
 "Advanced": [
  "The Institution",
  "The Movement",
  "The Festival Annual",
  "The Landmark",
  "The Scholarship",
  "The Archive",
  "The Network",
  "The Legacy Project",
  "Teaching Project Leadership",
  "Masterclass: Collective Creation"
 ]
};
var BLURBS={
 "The Mural": "One theme, many hands: the collective canvas.",
 "The Playlist": "Everyone adds tracks: the soundtrack.",
 "The Photo Pool": "One theme, many lenses: the gallery.",
 "The Story Chain": "Paragraph by paragraph: the novel.",
 "The Recipe Book": "Everyone\u2019s best dish: the delicious.",
 "The Map": "Favorite spots, pinned: the atlas.",
 "The Playlist Swap": "Musical exchange: the discovery.",
 "The Quote Wall": "Words that matter: the inspiration.",
 "The Time Capsule": "Today\u2019s treasures: the future gift.",
 "The Garden": "Planted together: the growing.",
 "The Cleanup": "The place, improved: the generous.",
 "The Welcome Kit": "For newcomers: the hospitality.",
 "The Zine": "The community magazine: the published.",
 "The Film": "Shot together: the cinematic.",
 "The Album": "Recorded together: the musical.",
 "The Game": "Designed together: the playable.",
 "The Wiki": "Knowledge, compiled: the resource.",
 "The Festival": "Organized together: the event.",
 "The Charity Build": "For a cause: the meaningful.",
 "The Oral History": "Stories recorded: the archive.",
 "The Art Show": "Exhibited together: the gallery.",
 "The Cookbook": "Tested and true: the delicious tome.",
 "The Podcast": "Voices together: the broadcast.",
 "The Makerspace": "The shared workshop: the tools.",
 "The Institution": "The permanent project: the legacy.",
 "The Movement": "Beyond the group: the cause.",
 "The Festival Annual": "The yearly gathering: the tradition.",
 "The Landmark": "The physical legacy: the monument.",
 "The Scholarship": "Funded futures: the generous.",
 "The Archive": "The complete history: the museum.",
 "The Network": "Groups united: the federation.",
 "The Legacy Project": "The enduring gift: the forever.",
 "Teaching Project Leadership": "Show others: the organizer mentor.",
 "Masterclass: Collective Creation": "How groups make things: the collaboration science."
};

function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}

function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — community project record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}

var BUILD_PROJECT_FACTORY=(function(){
return function(inp){
  var r=prng(inp.seed||37);
  var interest=inp.interest||'art';
  var size=parseInt(inp.size,10)||10;
  var formats=['Collaborative mural: one canvas per person, one theme','Community map: everyone pins a favorite spot with a story','Exquisite-corpse story: each person writes one paragraph','Sound collage: everyone records 10 seconds','Resource wiki: everyone adds their best tip'];
  return {title:'Community project: '+interest,intro:'Turn '+size+' interested people into one shared creation around '+interest+'.',
    sections:[{h:'Pick a format',items:[pick(formats,r)]},{h:'Run it in 4 phases',items:['Week 1: pitch + sign-ups (low barrier, one-click join)','Week 2: contributions roll in (daily prompts keep momentum)','Week 3: assembly + credits for everyone','Week 4: showcase + retrospective']},{h:'Roles (volunteer, rotate)',items:['Wrangler: keeps the timeline','Greeter: welcomes newcomers','Archivist: saves everything twice']}]};
};})();

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
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
gen.builderId="project-factory";
gen.builderFields=[["interest", "Shared interest", "text", "art"], ["size", "Group size", "number", "10"], ["seed", "Seed (optional)", "number", "37"]];
gen.build=BUILD_PROJECT_FACTORY;

if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-community-project-factory',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();