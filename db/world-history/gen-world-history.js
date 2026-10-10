(function(){'use strict';
/* JAH World History Database generator — deterministic, every record validated.
   Signature records are ILLUSTRATIVE TIMELINE EXERCISES on fictional
   civilizations — never presented as real historical events. Compact JSON. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['ancient','medieval','modern','contemporary','cultures','timelines'];
var PREFIX='JAH-HIST-';
var ERAS=['Ancient (before 500 CE)','Medieval (500–1500)','Early Modern (1500–1800)','Modern (1800–1945)','Contemporary (1945–present)'];
var CAT_ERA={ancient:'Ancient (before 500 CE)',medieval:'Medieval (500–1500)',modern:'Modern (1800–1945)',contemporary:'Contemporary (1945–present)'};
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
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var era=CAT_ERA[cat]||pick(ERAS,rnd);
  var civ=pick(CIVS,rnd),sc=pick(SCEN,rnd);
  var id=PREFIX+String(seed).padStart(7,'0');
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
    title:'Timeline exercise: '+sc[0]+' among '+civ,
    category:cat,era:era,kind:'timeline-exercise',
    scenario:'Imagine '+civ+', where '+sc[0]+' unfolds over generations.',
    description:'Fictional timeline practice: '+sc[0]+' among '+civ+'. Order the '+n+' events, then argue which mattered most. '+NOTICE,
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
