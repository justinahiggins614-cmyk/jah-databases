(function(){'use strict';
var SLUG='food-processing-published';
var PREFIX='JAH-food-processing-published-P-';
var STUDY='food-processing';
var FIELD='Food Processing';
var CATS=["food-science","food-safety","dairy-processing","meat-processing","bakery","preservation"];
var DATA={"works":[{"t":"Food Science","a":"Norman N. Potter; Joseph H. Hotchkiss","p":"Springer","y":1995,"g":"food-science","ref":"ISBN 978-0834212657, Springer, 5th edition.","ov":"The classic food science text: composition, preservation, and processing of major food groups.","f":["Food chemistry explains processing behavior.","Preservation methods all manipulate the same microbial factors."],"ch":["food constituents","food preservation","dairy products","cereal products"]},{"t":"Food Processing Technology","a":"P. J. Fellows","p":"Woodhead Publishing (Elsevier)","y":2016,"g":"food-science","ref":"ISBN 978-0081005224, Woodhead, 4th edition.","ov":"Principles and practice of food processing operations from raw material to package.","f":["Unit operations transfer directly from chemical engineering.","Process control determines product consistency."],"ch":["processing principles","thermal processing","dehydration","packaging"]},{"t":"Principles of Food Science","a":"Janet D. Ward; Larry T. Ward","p":"Goodheart-Willcox","y":2015,"g":"food-science","ref":"ISBN 978-1619604360, Goodheart-Willcox.","ov":"Introductory food science for career and technical education programs.","f":["Hands-on labs make food science concrete.","Career pathways motivate technical learning."],"ch":["food safety","nutrition","food processing","food careers"]},{"t":"Food Microbiology","a":"Martin R. Adams; Maurice O. Moss","p":"Royal Society of Chemistry","y":2008,"g":"food-safety","ref":"ISBN 978-0854042845, RSC, 3rd edition.","ov":"Microorganisms in food: spoilage, pathogens, and fermentation.","f":["Understanding pathogens is the basis of all food safety.","Fermentation harnesses microbes as processing tools."],"ch":["spoilage","foodborne pathogens","fermentation","control methods"]},{"t":"Food Safety Management","a":"Yasmine Motarjemi","p":"Academic Press","y":2013,"g":"food-safety","ref":"ISBN 978-0123815040, Academic Press.","ov":"A comprehensive guide to food safety systems: HACCP, risk assessment, and crisis management.","f":["Management commitment determines food safety culture.","Traceability turns recalls from disasters into procedures."],"ch":["food safety systems","HACCP","risk assessment","crisis management"]},{"t":"General Principles of Food Hygiene (CXC 1-1969)","a":"Codex Alimentarius Commission; FAO; WHO","p":"FAO/WHO","y":2020,"g":"food-safety","ref":"CXC 1-1969, rev. 2020, Codex Alimentarius.","ov":"The international code of hygienic practice including the HACCP system and guidelines.","f":["HACCP's seven principles are the global food safety language.","Prerequisite programs must precede HACCP."],"ch":["good hygiene practices","HACCP principles","hazard analysis","verification"]},{"t":"Dairy Processing Handbook","a":"Tetra Pak Processing Systems","p":"Tetra Pak","y":2015,"g":"dairy-processing","ref":"Tetra Pak Dairy Processing Handbook, 2nd revised edition, Tetra Pak.","ov":"The industry handbook for milk and dairy processing: pasteurization, homogenization, and cultured products.","f":["Heat treatment design balances safety and quality.","Membrane processes are reshaping dairy fractionation."],"ch":["milk reception","pasteurization","fermented products","cheese"]},{"t":"Bakery Technology and Engineering","a":"Samuel A. Matz","p":"Springer","y":1991,"g":"bakery","ref":"ISBN 978-0442308551, Springer, 3rd edition.","ov":"Engineering of bakery production: doughs, ovens, and process control.","f":["Dough rheology predicts baking performance.","Oven profiling is the key to consistent product."],"ch":["ingredients","dough mixing","baking","packaging"]},{"t":"Lawrie's Meat Science","a":"Fidel Toldra","p":"Woodhead Publishing (Elsevier)","y":2017,"g":"meat-processing","ref":"ISBN 978-0081006948, Woodhead, 8th edition.","ov":"The science of meat: muscle biology, slaughter, processing, and quality.","f":["Post-mortem biochemistry determines meat quality.","Chilling rate affects both safety and tenderness."],"ch":["muscle structure","slaughter","curing","packaging"]},{"t":"FDA Food Code","a":"U.S. Food and Drug Administration","p":"FDA","y":2022,"g":"food-safety","ref":"FDA Food Code 2022, U.S. Food and Drug Administration.","ov":"The model code for retail and food service regulation: sanitation, employee health, and HACCP.","f":["Time-temperature control prevents most foodborne illness.","Employee health policies are a frontline defense."],"ch":["foodborne illness","employee health","food protection","equipment"]},{"t":"Thermal Processing of Ready-to-Eat Meat Products","a":"C. Lynn Knipe; Robert E. Rust","p":"Wiley-Blackwell","y":2009,"g":"meat-processing","ref":"ISBN 978-0813821482, Wiley-Blackwell.","ov":"Lethality, stabilization, and process validation for cooked meat products.","f":["Validated lethality is non-negotiable for ready-to-eat meats.","Cooling deviations are the most common process failure."],"ch":["lethality","stabilization","process validation","packaging"]},{"t":"Introduction to Food Processing","a":"P. J. Fellows","p":"Pearson","y":2008,"g":"preservation","ref":"ISBN 978-0137143986, Pearson.","ov":"Accessible introduction to food preservation methods and their principles.","f":["Every preservation method targets specific spoilage factors.","Hurdle technology combines mild methods effectively."],"ch":["heat preservation","cold preservation","drying","fermentation"]}],"lvl2":[{"t":"Projected precision-fermentation facility guide","g":"food-science","b":"Fermentation-derived ingredients are scaling commercially.","d":"Projects a facility guide for precision fermentation: strain handling, downstream processing, and food-grade QA."},{"t":"Projected cultivated-meat processing text","g":"meat-processing","b":"Cultivated meat is approaching regulatory approval in more markets.","d":"Projects a processing text for cell-culture meat: bioreactor operations, scaffolding, and texture finishing."},{"t":"Projected AI vision inspection manual for food plants","g":"food-safety","b":"Machine vision is automating foreign-material detection.","d":"Projects an inspection manual for vision systems on food lines: validation, false-reject tuning, and sanitation."},{"t":"Projected novel-protein allergen assessment guide","g":"food-safety","b":"New protein sources raise allergenicity questions.","d":"Projects an assessment guide for evaluating allergen risk in insect, algal, and fungal proteins."},{"t":"Projected low-energy drying technology handbook","g":"preservation","b":"Heat-pump and microwave drying are cutting energy use.","d":"Projects a handbook for low-energy dehydration with quality retention data for fruits, vegetables, and herbs."}],"projAuthors":["JAH Archive Projection Desk","Signature Research Projection Unit","Archive Futures Working Group"]};
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
var gen={version:'jahdb-food-processing-published-1.0',generate:generate,validate:validate,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
