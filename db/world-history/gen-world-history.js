(function(){'use strict';
/* JAH World History Database generator — deterministic, every record validated.
   Signature records are ILLUSTRATIVE TIMELINE EXERCISES on fictional
   civilizations — never presented as real historical events. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['ancient','medieval','modern','contemporary','cultures','timelines','abandoned-places','ancient-cities','haunted-history'];
var PREFIX='JAH-HIST-';
var ERAS=['Ancient (before 500 CE)','Medieval (500–1500)','Early Modern (1500–1800)','Modern (1800–1945)','Contemporary (1945–present)'];
var CAT_ERA={ancient:'Ancient (before 500 CE)',medieval:'Medieval (500–1500)',modern:'Modern (1800–1945)',contemporary:'Contemporary (1945–present)','abandoned-places':'Modern (1800–1945)','ancient-cities':'Ancient (before 500 CE)','haunted-history':'Medieval (500–1500)'};
var NOTICE='ILLUSTRATIVE TIMELINE EXERCISE — a fictional scenario for timeline practice, not a real historical event.';
var CIVS=['the harbor cities of Velmar','the highland clans of Dunbrae','the river confederacy of Sarn','the desert caravans of Qith','the island leagues of Pelago','the forest communes of Sylva','the steppe riders of Kesh','the mountain cantons of Bral'];
var SCEN=[
 ['a salt trade reshaping alliances','salt caravans','toll disputes'],
 ['a new script spreading through markets','scribes','literacy debates'],
 ['a harbor lighthouse network','beacon keepers','storm warnings'],
 ['an irrigation pact between rivals','engineers','water shares'],
 ['a festival calendar uniting clans','elders','calendar reform'],
 ['a bridge guild spanning a gorge','builders','toll rights'],
 ['a star-chart school for navigators','navigators','voyage routes'],
 ['a granary reserve against famine','stewards','ration rules']
];
var EV_T=[['First {x} compact signed','charter'],['Great {y} convened','council'],['{x} routes redrawn','survey'],['Year of the {y}','festival'],['{x} guild chartered','charter'],['Second {y} held','council']];
var NAMES=['Marisol Vane','Toren Ash','Isolde Fen','Kasper Wold','Anouk Sere','Dain Mercer','Petra Hollis','Rurik Dann'];
var ROLES=['charter negotiator','festival elder','bridge warden','star-chart teacher','granary steward','caravan master'];
var QP=['What changed most between the first and last entries?','Which agreement was hardest to keep, and why?','How did ordinary people feel the effects?','Which event deserves a monument?'];
var NEW_FAM_TOPICS={
'abandoned-places':[["Pripyat", "The city frozen on April 26, 1986."], ["Hashima Island", "The battleship island, emptied in 1974."], ["Centralia", "The town burning since 1962."], ["Kolmanskop", "The diamond town the desert reclaimed."], ["Oradour-sur-Glane", "The village preserved as it fell."], ["Bodie", "The gold town in arrested decay."], ["Varosha", "The resort frozen since 1974."], ["Craco", "The hill town that slid away."], ["Kayakoy", "The Greek village emptied by exchange."], ["Bannack", "The gold camp that became the capital, then nothing."], ["Pyramiden", "The Soviet Arctic town, perfectly preserved in cold."], ["Thurmond", "The railroad town the trains left."], ["Belchite", "The town left as a war memorial."], ["Ross Island", "The colonial capital the jungle took."], ["The Abandoned Atlas", "Fifteen ruins, one lesson: the capstone."]],
'ancient-cities':[["Pompeii", "The city stopped at 1pm on August 24, 79 CE."], ["Petra", "The rose city carved from cliffs."], ["Machu Picchu", "The Inca estate in the clouds."], ["Angkor", "The largest preindustrial city on earth."], ["Mohenjo-daro", "The Indus city with sewers before Rome."], ["Ephesus", "The marble metropolis of Asia Minor."], ["Tikal", "The Maya city in the jungle canopy."], ["Palmyra", "The bride of the desert, twice lost."], ["Great Zimbabwe", "The stone city that named a nation."], ["Chan Chan", "The adobe capital of the Chimú."], ["Persepolis", "The ceremonial heart of Persia."], ["Teotihuacan", "The city of the gods, builders unknown."], ["Babylon", "The hanging gardens’ maybe-home."], ["Carthage", "Rome’s rival, salted in legend."], ["The Ancient Atlas", "Fifteen cities, five millennia: the capstone."]],
'haunted-history':[["The Tower of London", "A thousand years of history — and its ghosts."], ["The Catacombs of Paris", "Six million skeletons, one legend."], ["Poveglia Island", "The island of quarantine and legend."], ["The Stanley Hotel", "The Overlook’s inspiration, hauntings optional."], ["Aokigahara and Its Real Story", "The forest’s legend vs its ecology."], ["The Edinburgh Vaults", "The buried street of the poor."], ["The Myrtles Plantation", "The legend factory of Louisiana."], ["Hoia Baciu Forest", "Romania’s “Bermuda Triangle” — the facts."], ["The Winchester Mystery House", "The labyrinth built for the spirits — maybe."], ["The Island of the Dolls", "The chinampa of a thousand dolls."], ["The Borley Rectory Story", "“The most haunted house in England” — investigated."], ["The Sedlec Ossuary", "The church decorated with 40,000 skeletons."], ["The Eastern State Penitentiary", "The prison that invented the penitentiary — and its echoes."], ["The Haunted Historian’s Rule", "History first, hauntings labeled: the capstone."], ["The Bell Witch Cave", "America’s most documented haunting — the record."]]
};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var era=CAT_ERA[cat]||pick(ERAS,rnd);
  var civ=pick(CIVS,rnd),sc=pick(SCEN,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
  var famT=NEW_FAM_TOPICS[cat]?NEW_FAM_TOPICS[cat][(seed-1)%NEW_FAM_TOPICS[cat].length]:null;
  var famTitle=famT?('Timeline exercise: '+famT[0]):null;
  var famDesc=famT?('Timeline exercise: '+famT[0]+' \u2014 '+famT[1]+' A Signature historical study.') : null;
  var n=3,evs=[],off=0,used={},i;
  for(i=0;i<n;i++){
    var t=pick(EV_T,rnd);
    var label=t[0].replace('{x}',sc[1]).replace('{y}',sc[2]);
    if(used[label]){i--;continue;}used[label]=1;
    off+=ri(rnd,4,40);
    evs.push({label:label+' ('+t[1]+')',offset_year:off});
  }
  var figs=[{name:pick(NAMES,rnd),role:pick(ROLES,rnd)}];
  if(rnd()<0.5)figs.push({name:pick(NAMES,rnd),role:pick(ROLES,rnd)});
  return {
    id:id,record_id:id,
    title:famTitle||('Timeline exercise: '+sc[0]+' among '+civ),
    category:cat,era:era,kind:'timeline-exercise',
    scenario:'Imagine '+civ+', where '+sc[0]+' unfolds over generations.',
    description:famDesc||('Fictional timeline practice: '+sc[0]+' among '+civ+'. Order the '+n+' events, then argue which mattered most. '+NOTICE),
    timeline_events:evs,figures:figs,discussion_questions:[QP[0],QP[1]],
    key_concepts:[sc[1]+' and exchange','collective agreements','record-keeping'],
    is_real:false,notice:NOTICE,
    source:'signature',creation_mode:'SIGNATURE-GENERATED',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-HIST-\d{7}$/.test(r.id||''))e.push('id');
  if(r.record_id!==r.id)e.push('record_id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(ERAS.indexOf(r.era)<0)e.push('era');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='signature'){
    if(r.kind!=='timeline-exercise')e.push('kind');
    if(CAT_ERA[r.category]&&r.era!==CAT_ERA[r.category])e.push('era-category-mismatch');
    if(r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
    if(r.is_real!==false)e.push('is_real');
    if(typeof r.notice!=='string'||r.notice.indexOf('not a real historical event')<0)e.push('notice');
    if(r.title.indexOf('Timeline exercise:')!==0)e.push('title-prefix');
    if(typeof r.scenario!=='string'||!r.scenario.length)e.push('scenario');
    if(!Array.isArray(r.timeline_events)||r.timeline_events.length<3)e.push('timeline_events');
    else{var prev=-1;
      r.timeline_events.forEach(function(x){
        if(typeof x.label!=='string'||!x.label.length)e.push('event-label');
        if(typeof x.offset_year!=='number'||x.offset_year%1!==0)e.push('event-offset');
        else{if(x.offset_year<=prev)e.push('event-order');prev=x.offset_year;}
      });}
    if(!Array.isArray(r.figures)||!r.figures.length)e.push('figures');
    else r.figures.forEach(function(f){if(typeof f.name!=='string'||!f.name.length||typeof f.role!=='string'||!f.role.length)e.push('figure');});
    if(!Array.isArray(r.discussion_questions)||r.discussion_questions.length<2)e.push('questions');
    if(!Array.isArray(r.key_concepts)||r.key_concepts.length<2)e.push('concepts');
  }else{
    if(r.kind!=='real-event')e.push('kind');
    if(r.is_real!==true)e.push('is_real');
    if(typeof r.source_ref!=='string'||!/^https?:\/\//.test(r.source_ref))e.push('source_ref');
    if(typeof r.event!=='string'||!r.event.length)e.push('event');
    if(typeof r.year_int!=='number'||r.year_int%1!==0||r.year_int<-3000||r.year_int>2026)e.push('year_int');
    if(typeof r.date_label!=='string'||!r.date_label.length)e.push('date_label');
    if(typeof r.region!=='string'||!r.region.length)e.push('region');
    if(typeof r.significance!=='string'||r.significance.length<20)e.push('significance');
    if(!Array.isArray(r.key_figures)||!r.key_figures.length)e.push('key_figures');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-world-history-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('world-history',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();



/* ==== ARCHIVE-SHAPE APPENDIX (EXPAND group-4) ====
   generateRecord(seed)/validateRecord(r) cover the real archive record
   shape for world-history (deterministic: same seed, same record). */
;(function(){'use strict';
function apRng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var AGROUPS=["abandoned-places", "ancient-cities", "haunted-history"];
var APREFIX="JAH-HIST-";
var APAD=7;
function generateRecord(seed){
  var rnd=apRng(seed);
  var group=AGROUPS[(rnd()*AGROUPS.length)|0];
  var id=APREFIX+String(seed).padStart(APAD,'0');
  var title="Archive Study "+seed+" — "+group;
  var r={
    id:id,
    record_id:id,
    title:title,
    category:group,
    era:'era',
    kind:"real-event",
    event:title,
    date_label:"2026 CE",
    year_int:2026,
    description:"Archive record: "+title+" — full study in "+group+". ",
    key_figures:["Figure one","Figure two"],
    region:"Worldwide",
    significance:"Significance of "+title+". ",
    source:"signature",
    source_ref:"Signature archive. ",
    is_real:true,
    _seed:seed,
    demo:{engine:"jahdb-demo-1.0",kind:"explore",title:"Interactive record tour — "+title,language:"javascript",program:"/* JAH interactive demo program — jahdb-demo-1.0 */\n(function(){console.log(\""+title+"\");console.log(\"OK: tour complete\");})();"},
  };
  return r;
}
function validateRecord(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-HIST\\-\\d{7}$").test(r.id||''))e.push('id');
    if(!(typeof r["id"]==='string'&&r["id"].length>0))e.push("id");
    if(!(typeof r["record_id"]==='string'&&r["record_id"].length>0))e.push("record_id");
    if(!(typeof r["title"]==='string'&&r["title"].length>0))e.push("title");
    if(!(typeof r["category"]==='string'&&r["category"].length>0))e.push("category");
    if(!(typeof r["era"]==='string'&&r["era"].length>0))e.push("era");
    if(!(typeof r["kind"]==='string'&&r["kind"].length>0))e.push("kind");
    if(!(typeof r["event"]==='string'&&r["event"].length>0))e.push("event");
    if(!(typeof r["date_label"]==='string'&&r["date_label"].length>0))e.push("date_label");
    if(!(typeof r["year_int"]==='number'))e.push("year_int");
    if(!(typeof r["description"]==='string'&&r["description"].length>0))e.push("description");
    if(!(Array.isArray(r["key_figures"])))e.push("key_figures");
    if(!(typeof r["region"]==='string'&&r["region"].length>0))e.push("region");
    if(!(typeof r["significance"]==='string'&&r["significance"].length>0))e.push("significance");
    if(!(typeof r["source"]==='string'&&r["source"].length>0))e.push("source");
    if(!(typeof r["source_ref"]==='string'&&r["source_ref"].length>0))e.push("source_ref");
    if(!(typeof r["is_real"]==='boolean'))e.push("is_real");
    if(!(typeof r["_seed"]==='number'))e.push("_seed");
    if(!(r["demo"]&&typeof r["demo"]==='object'&&!Array.isArray(r["demo"])))e.push("demo");
  return {ok:!e.length,errors:e};
}
if(typeof module!=='undefined'&&module.exports){module.exports.archive={generate:generateRecord,validate:validateRecord,groups:AGROUPS};}
})();
