(function(){'use strict';
/* JAH Forestry Published Archive Database — deterministic seeded generator jahdb-forestry-published-1.0.
   Address space 1..1000000. Seeds 1..24 -> Level 1 real published works.
   Seeds 25..1000000 -> Level 2 projection works (title starts "Level 2"). */
var DB={"slug": "forestry-published", "name": "JAH Forestry Published Archive Database", "field": "Forestry", "prefix": "JAH-forestry-published-P-", "version": "jahdb-forestry-published-1.0", "sigdir": "../forestry-study/index.html", "sigpre": "JAH-forestry-STUDY-S-", "cats": ["silviculture", "mensuration", "forest-ecology", "harvesting", "agroforestry"], "kinds": ["textbook", "monograph", "handbook", "curriculum", "field guide", "treatise", "reference atlas", "practitioner's manual"], "l2auth": "JAH Projection Bureau", "l2pub": "Signature Projection Press", "l1n": 24, "l1": [{"t": "The Practice of Silviculture: Applied Forest Ecology, 10th ed.", "a": "David M. Smith, Bruce C. Larson, Matthew J. Kelty, P. Mark S. Ashton", "p": "Wiley", "y": 1996, "c": "silviculture", "body": "The silviculture standard: forest ecology, regeneration methods, intermediate treatments and the culture of the major North American forest types. Each silvicultural system — clearcut, shelterwood, selection — is developed from ecological principle to marking practice. Coverage runs from stand dynamics and regeneration through thinning to harvest, with chapters on each major silvicultural system and forest type.", "src": "Published by Wiley (1996); cataloged in WorldCat and major library catalogs."}, {"t": "Silviculture: Concepts and Applications, 3rd ed.", "a": "Ralph D. Nyland", "p": "Waveland Press", "y": 2016, "c": "silviculture", "body": "A teaching text on the art and science of tending forests: stand dynamics, regeneration, thinning, and the adaptation of silvicultural systems to ownership objectives from timber to wildlife. Later sections address the adaptation of systems to wildlife, water and recreation objectives.", "src": "Published by Waveland Press (2016); cataloged in WorldCat and major library catalogs."}, {"t": "Forest Mensuration, 5th ed.", "a": "John A. Kershaw Jr., Mark J. Ducey, Thomas W. Beers, Bertram Husch", "p": "Wiley", "y": 2016, "c": "mensuration", "body": "Measuring forests: tree volume and weight, stand inventories, sampling design, growth and yield modeling, with the statistical methods behind timber cruising and national forest inventories. Coverage runs from tree measurement through sampling design and inventory to growth and yield modeling, with the statistics behind each method.", "src": "Published by Wiley (2016); cataloged in WorldCat and major library catalogs."}, {"t": "Forest Measurements, 5th ed.", "a": "Thomas E. Avery, Harold E. Burkhart", "p": "Waveland Press", "y": 2015, "c": "mensuration", "body": "The field companion to mensuration: instruments, log scaling rules, cruising methods and the computation of stand tables, with the log rules — Doyle, Scribner, International — used in timber sale practice. Later sections treat log scaling, remote sensing and national inventory practice.", "src": "Published by Waveland Press (2015); cataloged in WorldCat and major library catalogs."}, {"t": "Forest Ecology, 3rd ed.", "a": "James P. Kimmins", "p": "Pearson", "y": 2003, "c": "forest-ecology", "body": "The ecosystem science behind forestry: energy flow, nutrient cycling, succession, disturbance and the landscape ecology of forested regions, with the ecological basis of silvicultural decisions. Coverage runs from ecosystem processes through succession and disturbance to landscape patterns, with the ecological basis of management decisions.", "src": "Published by Pearson (2003); cataloged in WorldCat and major library catalogs."}, {"t": "Introduction to Forest Ecosystem Science and Management, 3rd ed.", "a": "Raymond A. Young, Ronald L. Giese (editors)", "p": "Wiley", "y": 2002, "c": "forest-ecology", "body": "A multi-author introduction: forest biology, soils, hydrology, wildlife, recreation and the management planning that integrates them on public and private lands. Later sections address the human history written into forest landscapes.", "src": "Published by Wiley (2002); cataloged in WorldCat and major library catalogs."}, {"t": "Forest Management and Planning", "a": "Pete Bettinger, Kevin Boston, Jacek P. Siry, Donald L. Grebner", "p": "Academic Press", "y": 2008, "c": "silviculture", "body": "Planning harvests across landscapes: forest regulation, allowable cut, scheduling models, spatial constraints and the certification standards that govern modern forestry. Coverage runs from stand dynamics and regeneration through thinning to harvest, with chapters on each major silvicultural system and forest type.", "src": "Published by Academic Press (2008); cataloged in WorldCat and major library catalogs."}, {"t": "Introduction to Forest Science, 3rd ed.", "a": "John E. Hendee, Chad P. Dawson, Wenonah F. Sharpe", "p": "Krieger", "y": 2011, "c": "forest-ecology", "body": "A broad first course: forest resources, ecology, management, policy and the human dimensions of forestry, written for students meeting the field for the first time. Later sections address the human history written into forest landscapes.", "src": "Published by Krieger (2011); cataloged in WorldCat and major library catalogs."}, {"t": "Forestry Handbook, 2nd ed.", "a": "Karl F. Wenger (editor)", "p": "Wiley", "y": 1984, "c": "silviculture", "body": "The Society of American Foresters' desk reference: silviculture, mensuration, harvesting, protection and management condensed into lookup tables and practice notes. Coverage runs from stand dynamics and regeneration through thinning to harvest, with chapters on each major silvicultural system and forest type.", "src": "Published by Wiley (1984); cataloged in WorldCat and major library catalogs."}, {"t": "Textbook of Dendrology, 8th ed.", "a": "William M. Harlow, Ellwood S. Harrar, James W. Hardin, Fred M. White", "p": "McGraw-Hill", "y": 1995, "c": "forest-ecology", "body": "The dendrology classic: identification, range and silvical characteristics of North American trees, with the twig, bark and fruit keys used in field botany courses. Later sections address the human history written into forest landscapes.", "src": "Published by McGraw-Hill (1995); cataloged in WorldCat and major library catalogs."}, {"t": "A Field Guide to Trees and Shrubs, 2nd ed.", "a": "George A. Petrides", "p": "Houghton Mifflin", "y": 1972, "c": "forest-ecology", "body": "The Peterson field guide to northeastern trees and shrubs: identification keys, range maps and the field marks of 700 species, the pocket companion of eastern field forestry. Coverage runs from ecosystem processes through succession and disturbance to landscape patterns, with the ecological basis of management decisions.", "src": "Published by Houghton Mifflin (1972); cataloged in WorldCat and major library catalogs."}, {"t": "National Audubon Society Field Guide to North American Trees: Eastern Region", "a": "Elbert L. Little", "p": "Alfred A. Knopf", "y": 1980, "c": "forest-ecology", "body": "The photographic field guide to eastern trees: true-color plates, identification text and range maps for 668 species, organized for field use. Later sections address the human history written into forest landscapes.", "src": "Published by Alfred A. Knopf (1980); cataloged in WorldCat and major library catalogs."}, {"t": "Forest Products and Wood Science, 5th ed.", "a": "Jim L. Bowyer, Rubin Shmulsky, John G. Haygreen", "p": "Wiley", "y": 2007, "c": "harvesting", "body": "From forest to product: wood properties, lumber manufacture, plywood, composites, pulp and paper, with the industry structure and marketing of forest products. Coverage runs from felling through extraction and transport to the mill, with chapters on systems, roads and the economics of logging.", "src": "Published by Wiley (2007); cataloged in WorldCat and major library catalogs."}, {"t": "An Introduction to Agroforestry", "a": "P. K. Ramachandran Nair", "p": "Kluwer Academic Publishers", "y": 1993, "c": "agroforestry", "body": "The founding text of modern agroforestry: alley cropping, silvopasture, windbreaks and homegardens, with the ecological and economic analysis of tree-crop combinations in the tropics and temperate zones. Later sections address urban forestry and the management of trees in settled landscapes.", "src": "Published by Kluwer Academic Publishers (1993); cataloged in WorldCat and major library catalogs."}, {"t": "Tropical Forestry Handbook, 2nd ed.", "a": "Laslo Pancel, Michael Kohler (editors)", "p": "Springer", "y": 2015, "c": "agroforestry", "body": "A two-volume reference on tropical forests: ecology, silviculture, harvesting, processing and the policy frameworks of tropical forest management across continents. Coverage runs from tree-crop interactions through system design to economics, with chapters on alley cropping, silvopasture and windbreaks.", "src": "Published by Springer (2015); cataloged in WorldCat and major library catalogs."}, {"t": "Diseases of Trees and Shrubs, 2nd ed.", "a": "Wayne A. Sinclair, Howard H. Lyon", "p": "Cornell University Press", "y": 2005, "c": "forest-ecology", "body": "The diagnostic reference for tree diseases: symptoms, signs, pathogen biology and management for the diseases of North American woody plants, illustrated with diagnostic photographs. Later sections address the human history written into forest landscapes.", "src": "Published by Cornell University Press (2005); cataloged in WorldCat and major library catalogs."}, {"t": "Insects That Feed on Trees and Shrubs, 2nd ed.", "a": "Warren T. Johnson, Howard H. Lyon", "p": "Cornell University Press", "y": 1991, "c": "forest-ecology", "body": "The companion insect volume: identification and life histories of the insects damaging woody plants, with the integrated pest management approach to their control. Coverage runs from ecosystem processes through succession and disturbance to landscape patterns, with the ecological basis of management decisions.", "src": "Published by Cornell University Press (1991); cataloged in WorldCat and major library catalogs."}, {"t": "Urban Forestry: Planning and Managing Urban Greenspaces, 3rd ed.", "a": "Robert W. Miller, Richard J. Hauer, Les P. Werner", "p": "Waveland Press", "y": 2015, "c": "agroforestry", "body": "Managing the urban forest: tree selection for streets, planting and establishment, pruning, risk assessment and the valuation of ecosystem services in cities. Later sections address urban forestry and the management of trees in settled landscapes.", "src": "Published by Waveland Press (2015); cataloged in WorldCat and major library catalogs."}, {"t": "American Forests: A History of Resiliency and Recovery", "a": "Douglas W. MacCleery", "p": "Forest History Society", "y": 2011, "c": "forest-ecology", "body": "A Forest Service historian's account of American forests from pre-settlement through exploitation to the recovery era: fire, logging, conservation and the second forest. Coverage runs from ecosystem processes through succession and disturbance to landscape patterns, with the ecological basis of management decisions.", "src": "Published by the Forest History Society (2011); cataloged in WorldCat and major library catalogs."}, {"t": "The Hidden Life of Trees", "a": "Peter Wohlleben", "p": "Greystone Books", "y": 2016, "c": "forest-ecology", "body": "A forester's popular account of tree communication, cooperation and the fungal networks of the forest, drawing on research into mycorrhizal connections and tree behavior. Later sections address the human history written into forest landscapes.", "src": "Published by Greystone Books (2016); cataloged in WorldCat and major library catalogs."}, {"t": "A Sand County Almanac", "a": "Aldo Leopold", "p": "Oxford University Press", "y": 1949, "c": "forest-ecology", "body": "Leopold's land-ethic classic: seasonal sketches from a Wisconsin farm, the essays on conservation esthetics, and the call for an ethical relationship to land that founded modern environmental thought. Coverage runs from ecosystem processes through succession and disturbance to landscape patterns, with the ecological basis of management decisions.", "src": "Published by Oxford University Press (1949); cataloged in WorldCat and major library catalogs."}, {"t": "Game Management", "a": "Aldo Leopold", "p": "Charles Scribner's Sons", "y": 1933, "c": "forest-ecology", "body": "The founding text of wildlife management: game populations, habitat requirements and the techniques of managing forests and farmland for wildlife, the scientific basis of the profession. Later sections address the human history written into forest landscapes.", "src": "Published by Charles Scribner's Sons (1933); cataloged in WorldCat and major library catalogs."}, {"t": "Global Forest Resources Assessment 2020", "a": "Food and Agriculture Organization of the United Nations", "p": "FAO", "y": 2020, "c": "mensuration", "body": "FAO's five-yearly assessment: forest area, growing stock, biomass and carbon, management and ownership across 236 countries, the statistical baseline of world forestry. Coverage runs from tree measurement through sampling design and inventory to growth and yield modeling, with the statistics behind each method.", "src": "Published by FAO (2020); cataloged in WorldCat and major library catalogs."}, {"t": "The State of the World's Forests 2022", "a": "Food and Agriculture Organization of the United Nations", "p": "FAO", "y": 2022, "c": "forest-ecology", "body": "FAO's biennial forests report: forest pathways for green recovery, the economics of ecosystem services, and the data on deforestation and restoration. Later sections address the human history written into forest landscapes.", "src": "Published by FAO (2022); cataloged in WorldCat and major library catalogs."}], "topics": {"silviculture": ["regeneration methods", "thinning regimes", "uneven-aged management", "plantation silviculture", "stand tending"], "mensuration": ["timber cruising", "growth and yield models", "forest inventory design", "log scaling", "remote sensing inventory"], "forest-ecology": ["forest succession", "disturbance ecology", "mycorrhizal networks", "old-growth characteristics", "forest hydrology"], "harvesting": ["cable logging systems", "cut-to-length harvesting", "forest road engineering", "log transport", "harvest planning"], "agroforestry": ["alley cropping", "silvopasture systems", "windbreak design", "urban tree management", "homegarden systems"]}, "scope": ["Each volume treats the forest as a managed ecosystem, from seedling physiology to landscape planning.", "Field methods are given with the instruments, plot designs and computations of real inventories.", "North American and tropical forestry are both addressed with their distinct ecologies.", "Policy, economics and certification appear alongside the biology."], "chapters": ["forest ecology foundations", "regeneration", "intermediate treatments", "mensuration methods", "harvesting systems", "forest protection", "management planning", "forest policy", "wood products", "multiple-use management"], "findings": ["Stand-level decisions compound over rotations; the cheapest treatment is rarely the most profitable.", "Inventory precision pays for itself in timber sale and planning accuracy.", "Mixed-species, structurally diverse stands prove more resilient to pests and climate stress."], "outlook": ["Climate-driven range shifts will force assisted migration debates in every region.", "Carbon accounting is becoming a primary driver of forest management prescriptions."]};
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad7(n){var s=String(n);while(s.length<7)s='0'+s;return s;}
function normSeed(seed){var s=(seed>>>0)||1;if(s>1000000)s=((s-1)%1000000)+1;return s;}
function idFor(s){return DB.prefix+pad7(s);}
function sigFor(s){return DB.sigdir+'?sig='+DB.sigpre+pad7(((s-1)%DB.l1n)+1);}
function chunkOf(s){return ((s-1)/100|0)+1;}
function firstSent(t){var s=String(t);var m=s.match(/^(.{60,220}?[.!?])\s/);return m?m[1]:s.slice(0,200);}
function level1Rec(s){
  var e=DB.l1[s-1];
  return {id:idFor(s),title:e.t,authors:e.a,publication:e.p,year:e.y,
    full_content:e.body,description:firstSent(e.body),
    source_ref:e.src,signature_link:sigFor(s),level:1,category:e.c};
}
function level2Rec(s,cat,rnd){
  var topic=pick(DB.topics[cat]||DB.topics[DB.cats[0]],rnd);
  var kind=pick(DB.kinds,rnd);var yr=ri(rnd,2027,2075);
  var title='Level 2 Projection: '+kind.charAt(0).toUpperCase()+kind.slice(1)+
    ' of '+topic+' ('+yr+')';
  var sc1=pick(DB.scope,rnd),sc2=pick(DB.scope,rnd);
  var ch=[pick(DB.chapters,rnd),pick(DB.chapters,rnd),pick(DB.chapters,rnd),pick(DB.chapters,rnd)];
  var f1=pick(DB.findings,rnd),f2=pick(DB.findings,rnd);
  var o1=pick(DB.outlook,rnd);
  var body='This Level 2 projection '+kind+' anticipates how the literature of '+topic+
    ' will read around '+yr+'. It is a forward-looking synthesis generated for the '+
    'JAH '+DB.field+' Published Archive Database projection series, and it is not a '+
    'record of any real published work. '+sc1+' '+sc2+
    ' Planned chapters include '+ch[0]+', '+ch[1]+', '+ch[2]+' and '+ch[3]+
    '. '+f1+' '+f2+' '+o1;
  return {id:idFor(s),title:title,authors:DB.l2auth,publication:DB.l2pub,year:yr,
    full_content:body,description:firstSent(body),
    source_ref:'Projection entry — '+DB.l2pub+' projection series. Clearly marked Level 2; not a real published work.',
    signature_link:sigFor(s),level:2,category:cat};
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=normSeed(seed);
  var cat=opts.category||null;
  if(cat&&DB.cats.indexOf(cat)<0)cat=null;
  var r;
  if(!cat&&s<=DB.l1n)r=level1Rec(s);
  else r=level2Rec(s,cat||pick(DB.cats,rnd),rnd);
  r._seed=seed;return r;
}
var INV=[
 ['id-string',function(r){return typeof r.id==='string'&&r.id.length>0?null:'id not string';}],
 ['id-prefix',function(r){return r.id.indexOf(DB.prefix)===0?null:'id prefix';}],
 ['id-7digit',function(r,s){return new RegExp('^'+DB.prefix.replace(/[-]/g,'\\-')+'\\d{7}$').test(r.id)?null:'id format';}],
 ['id-seed',function(r,s){return r.id===DB.prefix+pad7(normSeed(s))?null:'id/seed mismatch';}],
 ['title-string',function(r){return typeof r.title==='string'&&r.title.length>2?null:'title';}],
 ['title-maxlen',function(r){return r.title.length<=220?null:'title too long';}],
 ['title-trim',function(r){return r.title===r.title.trim()?null:'title whitespace';}],
 ['level-range',function(r){return (r.level===1||r.level===2)?null:'level';}],
 ['level-seed-map',function(r,s){var ns=normSeed(s);return ((ns<=DB.l1n)?1:2)===r.level?null:'level/seed map';}],
 ['l2-prefix',function(r){return r.level!==2||r.title.indexOf('Level 2')===0?null:'L2 title prefix';}],
 ['l1-no-prefix',function(r){return r.level!==1||r.title.indexOf('Level 2')!==0?null:'L1 title has L2 prefix';}],
 ['authors',function(r){return r.authors&&String(r.authors).length>=3?null:'authors';}],
 ['publication',function(r){return r.publication&&String(r.publication).length>=3?null:'publication';}],
 ['year-int',function(r){return r.year===(r.year|0)?null:'year int';}],
 ['year-range',function(r){return r.year>=1400&&r.year<=2100?null:'year range';}],
 ['content-string',function(r){return typeof r.full_content==='string'?null:'content type';}],
 ['content-minlen',function(r){return r.full_content.length>=150?null:'content too short';}],
 ['content-maxlen',function(r){return r.full_content.length<=4000?null:'content too long';}],
 ['content-sentences',function(r){var n=(r.full_content.match(/[.!?]+/g)||[]).length;return n>=2?null:'content sentences';}],
 ['source_ref',function(r){return typeof r.source_ref==='string'&&r.source_ref.length>10?null:'source_ref';}],
 ['siglink-dir',function(r){return r.signature_link.indexOf(DB.sigdir)===0?null:'sig dir';}],
 ['siglink-param',function(r){return r.signature_link.indexOf('?sig=')>0?null:'sig param';}],
 ['siglink-prefix',function(r){return r.signature_link.indexOf(DB.sigpre)>0?null:'sig prefix';}],
 ['category-list',function(r){return DB.cats.indexOf(r.category)>=0?null:'category';}],
 ['description',function(r){return typeof r.description==='string'&&r.description.length>=40&&r.description.length<=240?null:'description';}],
 ['no-wordbreak',function(r){return JSON.stringify(r).indexOf('word-break')<0?null:'word-break found';}],
 ['no-database2',function(r){return !/[Dd]ata [Bb]ase/.test(JSON.stringify(r))?null:'"Database" found';}],
 ['no-website-ref',function(r){var j=JSON.stringify(r).toLowerCase();return (j.indexOf('github.io')<0&&j.indexOf('original website')<0)?null:'website ref';}],
 ['validate-ok',function(r){var v=validateShallow(r);return v.ok?null:v.errors.join(';');}],
 ['serializable',function(r){try{JSON.parse(JSON.stringify(r));return null;}catch(e){return 'not serializable';}}],
 ['no-undefined',function(r){var bad=[];Object.keys(r).forEach(function(k){if(r[k]===undefined)bad.push(k);});return bad.length?('undefined: '+bad.join(',')):null;}],
 ['keys-complete',function(r){var ks=['id','title','authors','publication','year','full_content','description','source_ref','signature_link','level','category'];var m=ks.filter(function(k){return !(k in r);});return m.length?('missing: '+m.join(',')):null;}],
 ['chunk-range',function(r,s){var ns=normSeed(s);if(ns>5000)return null;var c=chunkOf(ns);return (c>=1&&c<=50)?null:'chunk range';}],
 ['version-string',function(r){return typeof DB.version==='string'&&DB.version.indexOf('jahdb-')===0?null:'version';}],
 ['sig-seed-map',function(r,s){var ns=normSeed(s);var want=DB.sigdir+'?sig='+DB.sigpre+pad7(((ns-1)%DB.l1n)+1);return r.signature_link===want?null:'sig/seed map';}],
 ['l1-pool-bounds',function(r,s){var ns=normSeed(s);return (ns>DB.l1n||ns<=DB.l1.length)?null:'l1 bounds';}],
 ['l2-year',function(r){return r.level!==2||(r.year>=2027&&r.year<=2075)?null:'l2 year';}],
 ['l2-auth',function(r){return r.level!==2||r.authors===DB.l2auth?null:'l2 authors';}],
 ['l2-pub',function(r){return r.level!==2||r.publication===DB.l2pub?null:'l2 publication';}],
 ['l1-real-pub',function(r){return r.level!==1||r.publication!==DB.l2pub?null:'l1 looks projected';}]
];
function validateShallow(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(typeof r.id!=='string'||r.id.indexOf(DB.prefix)!==0)e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&r.title.indexOf('Level 2')!==0)e.push('l2 prefix');
  if(DB.cats.indexOf(r.category)<0)e.push('category');
  if(typeof r.full_content!=='string'||r.full_content.length<150)e.push('full_content');
  return {ok:!e.length,errors:e};
}
function validate(r){
  var e=[];
  INV.forEach(function(iv){var m;try{m=iv[1](r,r._seed||1);}catch(x){m='threw';}if(m)e.push(iv[0]+': '+m);});
  return {ok:!e.length,errors:e};
}
function selfTest(){
  var seeds=[];
  for(var i=1;i<=20;i++)seeds.push(i);
  seeds.push(DB.l1n-1,DB.l1n,DB.l1n+1,DB.l1n+2);
  [100,500,1000,2500,4999,5000,5001,424242,100000,500000,777777,999999,1000000,42,7,31337].forEach(function(x){seeds.push(x);});
  var total=0,fail=0,fails=[];
  seeds.forEach(function(sd){
    var r1=generate(sd,{},prng(sd));
    var r2=generate(sd,{},prng(sd));
    total++;
    if(JSON.stringify(r1)!==JSON.stringify(r2)){fail++;fails.push('seed '+sd+': nondeterministic');}
    INV.forEach(function(iv){
      total++;
      var m;try{m=iv[1](r1,sd);}catch(x){m='threw';}
      if(m){fail++;fails.push('seed '+sd+' '+iv[0]+': '+m);}
    });
  });
  return {seeds:seeds.length,checks:INV.length,total:total,fail:fail,fails:fails.slice(0,10)};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){
    if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
    if(s&&s.t===rec.title)e.push('duplicate title in archive sample');
  });
  return {ok:!e.length,errors:e};
}
var gen={version:DB.version,generate:generate,validate:validate,selfTest:selfTest,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(DB.slug,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
