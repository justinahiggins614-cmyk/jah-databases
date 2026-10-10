(function(){'use strict';
var SLUG='electricity-energy-published';
var PREFIX='JAH-electricity-energy-published-P-';
var STUDY='electricity-energy';
var FIELD='Electricity and Energy';
var CATS=["power-systems","electrical-machines","renewable-energy","wiring-codes","power-electronics","energy-management"];
var DATA={"works":[{"t":"Electric Power Distribution Engineering","a":"Turan Gonen","p":"CRC Press","y":2014,"g":"power-systems","ref":"ISBN 978-1482227004, CRC Press, 3rd edition.","ov":"Comprehensive treatment of distribution system planning, load forecasting, and voltage regulation.","f":["Load forecasting accuracy determines distribution investment quality.","Voltage regulation keeps service within standards across feeders."],"ch":["load characteristics","distribution system planning","voltage regulation","system protection"]},{"t":"Power System Analysis and Design","a":"J. Duncan Glover; Mulukutla S. Sarma; Thomas J. Overbye","p":"Cengage Learning","y":2016,"g":"power-systems","ref":"ISBN 978-1305632134, Cengage Learning, 6th edition.","ov":"Power flow, fault analysis, and stability for modern power systems with renewable integration.","f":["Power flow solutions underpin every planning and operations decision.","Transient stability limits how much can be transferred."],"ch":["power flow","fault analysis","symmetrical components","power system stability"]},{"t":"Electric Machinery Fundamentals","a":"Stephen J. Chapman","p":"McGraw-Hill","y":2011,"g":"electrical-machines","ref":"ISBN 978-0073529547, McGraw-Hill, 5th edition.","ov":"Transformers, DC machines, and AC machines explained with practical examples.","f":["The equivalent circuit predicts machine behavior under any load.","Understanding torque-speed curves prevents misapplication."],"ch":["transformers","DC motors and generators","induction motors","synchronous machines"]},{"t":"Renewable Energy: Power for a Sustainable Future","a":"Godfrey Boyle","p":"Oxford University Press","y":2012,"g":"renewable-energy","ref":"ISBN 978-0199545339, Oxford University Press, 3rd edition.","ov":"Survey of renewable technologies: solar, wind, hydro, biomass, and geothermal with resource assessment.","f":["Resource assessment comes before technology selection.","No single renewable fits every site; portfolios win."],"ch":["solar thermal","photovoltaics","wind power","integration into electricity systems"]},{"t":"Photovoltaic Systems Engineering","a":"Roger A. Messenger; Jerry Ventre","p":"CRC Press","y":2017,"g":"renewable-energy","ref":"ISBN 978-1315218398, CRC Press, 4th edition.","ov":"Engineering of PV systems from cell physics to grid-connected design and economics.","f":["Shading losses dominate underperforming arrays.","Proper inverter sizing determines system availability."],"ch":["PV cell physics","system components","stand-alone design","grid-connected systems"]},{"t":"Wind Energy Explained","a":"James F. Manwell; Jon G. McGowan; Anthony L. Rogers","p":"Wiley","y":2009,"g":"renewable-energy","ref":"ISBN 978-0470015001, Wiley, 2nd edition.","ov":"Theory and practice of wind energy: aerodynamics, siting, and grid integration.","f":["Wind resource measurement is the highest-value project expense.","Capacity factor matters more than nameplate rating."],"ch":["wind characteristics","aerodynamics","siting","electrical integration"]},{"t":"Electrical Wiring Residential","a":"Ray C. Mullin; Phil Simmons","p":"Cengage Learning","y":2017,"g":"wiring-codes","ref":"ISBN 978-1337101837, Cengage Learning, 19th edition.","ov":"Step-by-step residential wiring practice aligned to the National Electrical Code.","f":["Code-compliant wiring is a safety discipline, not paperwork.","Load calculations precede every panel and circuit design."],"ch":["blueprints and load calculations","branch circuits","service entrances","low-voltage systems"]},{"t":"NFPA 70: National Electrical Code","a":"National Fire Protection Association","p":"NFPA","y":2023,"g":"wiring-codes","ref":"NFPA 70, 2023 edition, National Fire Protection Association.","ov":"The enforceable US standard for safe electrical design, installation, and inspection.","f":["The Code's core purpose is practical safeguarding of persons and property.","Article 110 requirements apply across nearly all installations."],"ch":["general requirements","wiring and protection","wiring methods","equipment for general use"]},{"t":"Power Electronics: Converters, Applications, and Design","a":"Ned Mohan; Tore M. Undeland; William P. Robbins","p":"Wiley","y":2002,"g":"power-electronics","ref":"ISBN 978-0471226932, Wiley, 3rd edition.","ov":"Design of rectifiers, inverters, and DC-DC converters with applications.","f":["Switching waveforms determine both efficiency and EMI.","Magnetics design is the craft behind converter performance."],"ch":["power semiconductor devices","DC-DC converters","inverters","resonant converters"]},{"t":"Energy Systems Engineering","a":"Francis M. Vanek; Louis D. Albright","p":"McGraw-Hill","y":2008,"g":"energy-management","ref":"ISBN 978-0071495932, McGraw-Hill.","ov":"Quantitative evaluation of energy systems: fossil, nuclear, and renewable with economics.","f":["Levelized cost lets technologies be compared honestly.","End-use efficiency is usually the cheapest energy source."],"ch":["energy economics","fossil energy","nuclear energy","energy storage"]},{"t":"Smart Grid: Fundamentals of Design and Analysis","a":"James Momoh","p":"Wiley","y":2012,"g":"power-systems","ref":"ISBN 978-0470889398, Wiley.","ov":"Design and analysis of smart grids: sensing, communication, and control of the modern grid.","f":["Two-way communication transforms passive grids into active systems.","Distribution automation cuts outage durations dramatically."],"ch":["smart grid architecture","sensing and measurement","communication networks","distribution automation"]},{"t":"Electric Motors and Drives","a":"Austin Hughes; Bill Drury","p":"Newnes (Elsevier)","y":2013,"g":"electrical-machines","ref":"ISBN 978-0080983325, Newnes, 4th edition.","ov":"Practical guide to selecting and applying motors and variable-speed drives.","f":["Drive-motor matching determines efficiency more than either alone.","Most industrial motors are oversized; right-sizing saves energy."],"ch":["motor types","drive principles","selecting drives","efficiency and energy saving"]}],"lvl2":[{"t":"Projected vehicle-to-grid integration handbook","g":"power-systems","b":"Bidirectional EV charging is entering grid codes.","d":"Projects a handbook for V2G aggregation, battery-warranty-safe dispatch, and distribution-level coordination."},{"t":"Projected solid-state transformer design guide","g":"power-electronics","b":"Medium-voltage power electronics are displacing iron-core transformers.","d":"Projects a design guide for solid-state transformers in distribution substations, with protection and reliability methods."},{"t":"Projected agrivoltaics engineering text","g":"renewable-energy","b":"Co-locating solar with agriculture is scaling fast.","d":"Projects an engineering text for elevated PV over crops: light modeling, mounting, and dual-revenue economics."},{"t":"Projected home energy audit curriculum","g":"energy-management","b":"Electrification incentives are driving residential retrofits.","d":"Projects a technician curriculum for blower-door testing, heat-pump sizing, and panel upgrades."},{"t":"Projected high-temperature superconducting cable manual","g":"electrical-machines","b":"HTS cables are leaving the demonstration phase in dense cities.","d":"Projects an installation and maintenance manual for cryogenic cable systems in urban grids."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad7(n){var s=String(n);while(s.length<7)s='0'+s;return s;}
var ANGLES=['Abstract and scope','Chapter outline','Key findings','Curriculum notes'];
var SITE_SLUGS=['signature-math','jah-calculator','jah-dictionary','jah-wiki','jah-n-wiki-leaks','signature-llama','jah-ai-models','cyber-patent-catalog','signature-one-archive','jah-computer-systems','signature-books','signature-comics','signature-newspapers','signature-backend','signature-boundless-generators','signature-ai-mixlab','signature-ai-olypics','signature-chip-maker','signature-app-archive','signature-ai-robot-matcher','signature-experiment-solver','signature-ai-image-video-maker','signature-ai-song-maker','signature-fixit','signature-university','signature-earth','signature-flight-school','signature-game-store','signature-website-creator','signature-antivirus','signature-os-updater','signature-space-mapping','signature-cookbook','signature-spell-check','signature-image-grid-measure','signature-cyber-mega-mall','signature-3d-print'];
function angleNote(angle){
  if(angle==='Chapter outline')return 'Study angle: chapter outline. Readers work the table of contents as a syllabus, summarizing each chapter\'s method before moving on. ';
  if(angle==='Key findings')return 'Study angle: key findings. This record distills the results and recommendations a practitioner would quote on the job. ';
  if(angle==='Curriculum notes')return 'Study angle: curriculum notes. Instructors can teach the material in twelve sessions, pairing each reading with a hands-on exercise. ';
  return 'Study angle: abstract and scope. This entry states what the work covers, who it is written for, and where it sits in the field. ';
}
function buildLevel1(rnd,w,angle){
  var title=w.t+' \u2014 '+angle;
  var chs=[];for(var i=0;i<w.ch.length;i++)chs.push('Chapter '+(i+1)+': '+w.ch[i]+'.');
  var content='Published work: \u201C'+w.t+'\u201D by '+w.a.replace(/;/g,',')+' ('+w.p+', '+w.y+'). '+w.ov+
   ' Key findings: '+w.f[0]+' '+w.f[1]+
   ' Contents: '+chs.join(' ')+
   ' '+angleNote(angle)+
   ' Publication: '+w.p+'. Source: '+w.ref;
  return {title:title,content:content};
}
function buildLevel2(rnd,cat){
  var pool=DATA.lvl2.filter(function(x){return !x.g||x.g===cat;});
  if(!pool.length)pool=DATA.lvl2;
  var tp=pick(pool,rnd);
  var title='Level 2: '+tp.t;
  var content='Level 2 projection record for the '+FIELD+' published archive. Projected entry: \u201C'+tp.t+'\u201D. '+
   'Trend basis: '+tp.b+' Projected content: '+tp.d+
   ' Issued in: JAH '+FIELD+' Published Archive, projection series. '+
   'Confidence: projection, derived from the direction of the archived published works, not from a real publication. Nothing here is cited as fact; the entry models where the literature points next.';
  return {title:title,content:content};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var wl=DATA.works.filter(function(w){return w.g===cat;});
  if(!wl.length)wl=DATA.works;
  var level=rnd()<0.55?1:2;
  var id=PREFIX+pad7(seed);
  var sig='../'+STUDY+'-study/index.html?sig=JAH-'+STUDY+'-STUDY-S-'+pad7(seed);
  var rec;
  if(level===1){
    var w=pick(wl,rnd);
    var b=buildLevel1(rnd,w,pick(ANGLES,rnd));
    rec={id:id,title:b.title,authors:w.a.split(';').map(function(s){return s.trim();}).filter(Boolean),
      publication:w.p,year:w.y,full_content:b.content,source_ref:w.ref,signature_link:sig,level:1,category:cat,_seed:seed};
  }else{
    var b2=buildLevel2(rnd,cat);
    var pa=pick(DATA.projAuthors,rnd);
    rec={id:id,title:b2.title,authors:[pa],publication:'JAH '+FIELD+' Published Archive, projection series',year:2026,
      full_content:b2.content,source_ref:'Projection record; no external citation. Derived from archive trend basis.',signature_link:sig,level:2,category:cat,_seed:seed};
  }
  return rec;
}
var CHECKS=[
 ['object',function(r){return (r&&typeof r==='object')?'':'not an object';}],
 ['id-type',function(r){return typeof r.id==='string'?'':'id not string';}],
 ['id-format',function(r){return new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{7}$').test(r.id)?'':'id format';}],
 ['id-seed',function(r){return r.id.slice(-7)===pad7(r._seed)?'':'id/seed mismatch';}],
 ['title-type',function(r){return typeof r.title==='string'?'':'title not string';}],
 ['title-len',function(r){return (r.title.length>=12&&r.title.length<=220)?'':'title length';}],
 ['authors-arr',function(r){return (Array.isArray(r.authors)&&r.authors.length>=1)?'':'authors array';}],
 ['authors-items',function(r){return r.authors.every(function(a){return typeof a==='string'&&a.length>=3;})?'':'author item';}],
 ['publication-type',function(r){return (typeof r.publication==='string'&&r.publication.length>=3)?'':'publication';}],
 ['year-range',function(r){return (Number.isInteger(r.year)&&r.year>=1800&&r.year<=2026)?'':'year';}],
 ['content-type',function(r){return typeof r.full_content==='string'?'':'content not string';}],
 ['content-min',function(r){return r.full_content.length>=400?'':'content too short';}],
 ['content-max',function(r){return r.full_content.length<=4000?'':'content too long';}],
 ['content-sentences',function(r){return ((r.full_content.match(/[.!?]/g)||[]).length>=3)?'':'content sentences';}],
 ['content-clean',function(r){return !/lorem|TBD|TODO|\bxxx\b/i.test(r.full_content)?'':'content placeholder';}],
 ['content-no-stub',function(r){return !/\bstub\b/i.test(r.full_content)?'':'content stub';}],
 ['source-type',function(r){return (typeof r.source_ref==='string'&&r.source_ref.length>=8)?'':'source_ref';}],
 ['siglink-type',function(r){return typeof r.signature_link==='string'?'':'signature_link type';}],
 ['siglink-format',function(r){return new RegExp('^\\.\\./'+STUDY+'-study/index\\.html\\?sig=JAH-'+STUDY+'-STUDY-S-\\d{7}$').test(r.signature_link)?'':'signature_link format';}],
 ['siglink-seed',function(r){return r.signature_link.indexOf(pad7(r._seed))>=0?'':'signature_link seed';}],
 ['level-val',function(r){return (r.level===1||r.level===2)?'':'level value';}],
 ['level2-title',function(r){return (r.level!==2||/^Level 2/.test(r.title))?'':'level2 title';}],
 ['level1-title',function(r){return (r.level!==1||!/^Level 2/.test(r.title))?'':'level1 title';}],
 ['level2-projection',function(r){return (r.level!==2||/projection/i.test(r.full_content))?'':'level2 projection word';}],
 ['level1-authors',function(r){return (r.level!==1||!/unknown/i.test(r.authors.join(' ')))?'':'level1 authors';}],
 ['category-valid',function(r){return CATS.indexOf(r.category)>=0?'':'category';}],
 ['seed-num',function(r){return (Number.isInteger(r._seed)&&r._seed>=1)?'':'_seed';}],
 ['json-roundtrip',function(r){return JSON.parse(JSON.stringify(r)).id===r.id?'':'json roundtrip';}],
 ['no-undefined',function(r){return Object.keys(r).every(function(k){return r[k]!==undefined;})?'':'undefined value';}],
 ['content-pub',function(r){return (r.level!==1||r.full_content.indexOf(r.publication)>=0)?'':'content lacks publication';}],
 ['title-id',function(r){return r.title!==r.id?'':'title==id';}],
 ['siglink-relative',function(r){return r.signature_link.indexOf('../')===0?'':'siglink relative';}],
 ['no-site-slugs',function(r){var t=(r.title+' '+r.full_content).toLowerCase();return !SITE_SLUGS.some(function(s){return t.indexOf(s)>=0;})?'':'site slug referenced';}],
 ['no-orig-website',function(r){return !/original website/i.test(r.title+' '+r.full_content)?'':'original-website phrase';}],
 ['level2-year',function(r){return (r.level!==2||r.year===2026)?'':'level2 year';}],
 ['level1-ref',function(r){return (r.level!==1||/ISBN|doi|RFC|ISO|NFPA|FAA|Codex|Tetra|Handbook|open textbook|lulu|IPC|FDA/i.test(r.source_ref))?'':'level1 ref weak';}],
 ['category-nonempty',function(r){return (typeof r.category==='string'&&r.category.length>=2)?'':'category empty';}],
 ['title-spacing',function(r){return !/  /.test(r.title)?'':'title double space';}],
 ['content-no-html',function(r){return !/[<>]/.test(r.full_content)?'':'content has angle brackets';}],
 ['content-no-breakword',function(r){return r.full_content.indexOf('word-break')<0?'':'content css leak';}]
];
function validate(r){
  var e=[];
  for(var i=0;i<CHECKS.length;i++){var m='';try{m=CHECKS[i][1](r);}catch(x){m='threw '+x.message;}if(m)e.push(CHECKS[i][0]+': '+m);}
  return {ok:!e.length,errors:e};
}
function selfTest(){
  var fails=[];
  for(var s=1;s<=40;s++){
    var r=generate(s);
    for(var i=0;i<CHECKS.length;i++){var m='';try{m=CHECKS[i][1](r);}catch(x){m='threw '+x.message;}if(m)fails.push({seed:s,check:CHECKS[i][0],msg:m});}
  }
  return {seeds:40,checksPerSeed:CHECKS.length,total:40*CHECKS.length,failures:fails,ok:fails.length===0};
}
var gen={version:'jahdb-electricity-energy-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
