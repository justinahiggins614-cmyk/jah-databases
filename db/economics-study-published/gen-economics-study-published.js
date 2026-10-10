(function(){'use strict';
/* JAH Economics Published Archive Database — deterministic boundless generator (jahdb-economics-study-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='economics-study-published';
var BASE='economics-study';
var GENVER='jahdb-economics-study-published-1.0';
var PREFIX='JAH-economics-study-published-P-';
var CATS=["microeconomics", "macroeconomics", "econometrics", "development", "behavioral", "history-of-thought"];
var WORKS=[["An Inquiry into the Nature and Causes of the Wealth of Nations", "Adam Smith", "W. Strahan and T. Cadell", 1776, "history-of-thought", "Smith\u2019s Wealth of Nations explains markets through division of labor and the invisible hand, while warning against monopoly. The founding text of classical economics.", ["invisible hand", "division of labor", "market"]], ["The General Theory of Employment, Interest and Money", "John Maynard Keynes", "Macmillan", 1936, "macroeconomics", "Keynes argued that demand, not supply, governs employment, justifying fiscal intervention in slumps. The book that created macroeconomics and postwar policy.", ["aggregate demand", "multiplier", "liquidity"]], ["Principles of Economics", "Alfred Marshall", "Macmillan", 1890, "microeconomics", "Marshall\u2019s Principles systematized supply and demand, elasticity, and marginal utility with the famous scissors analogy. Neoclassical economics\u2019 textbook foundation.", ["supply and demand", "elasticity", "marginal"]], ["Capitalism and Freedom", "Milton Friedman", "University of Chicago Press", 1962, "history-of-thought", "Friedman argues that economic freedom is the prerequisite of political freedom, defending markets, school choice, and monetary rules. The Chicago school\u2019s popular manifesto.", ["monetarism", "freedom", "market"]], ["Economics", "Paul A. Samuelson", "McGraw-Hill", 1948, "microeconomics", "Samuelson\u2019s textbook brought Keynesian synthesis and mathematical modeling to generations of students. The best-selling economics text of the twentieth century.", ["synthesis", "model", "textbook"]], ["Principles of Microeconomics", "N. Gregory Mankiw", "Dryden Press", 1998, "microeconomics", "Mankiw\u2019s ten principles \u2014 people face tradeoffs, respond to incentives \u2014 open the standard modern micro text. Clarity as pedagogy.", ["tradeoffs", "incentives", "opportunity cost"]], ["Basic Econometrics", "Damodar N. Gujarati", "McGraw-Hill", 1978, "econometrics", "Gujarati\u2019s text teaches regression from two variables through simultaneous equations with worked examples. The applied econometrician\u2019s first reference.", ["regression", "OLS", "hypothesis test"]], ["Thinking, Fast and Slow", "Daniel Kahneman", "Farrar, Straus and Giroux", 2011, "behavioral", "Kahneman summarizes a lifetime on judgment: fast intuition versus slow deliberation, loss aversion, and framing. Behavioral economics for general readers.", ["heuristics", "loss aversion", "framing"]], ["Development as Freedom", "Amartya Sen", "Alfred A. Knopf", 1999, "development", "Sen redefines development as expanding real freedoms \u2014 capabilities \u2014 not just GDP. Famines, he shows, are political failures, not food shortages.", ["capabilities", "freedom", "famine"]], ["The End of Poverty", "Jeffrey Sachs", "Penguin Press", 2005, "development", "Sachs argues extreme poverty can be ended through targeted investment in health, agriculture, and infrastructure. The Millennium Development Goals\u2019 economic blueprint.", ["poverty trap", "investment", "development goals"]], ["Capital in the Twenty-First Century", "Thomas Piketty", "Harvard University Press", 2014, "macroeconomics", "Piketty\u2019s data across centuries shows returns on capital outpacing growth, driving inequality. The empirical blockbuster on wealth concentration.", ["inequality", "capital", "r greater than g"]], ["On the Principles of Political Economy and Taxation", "David Ricardo", "John Murray", 1817, "history-of-thought", "Ricardo\u2019s Principles gave economics comparative advantage, rent theory, and the labor theory of value. Trade theory\u2019s founding model.", ["comparative advantage", "rent", "value"]], ["Capital, Volume I", "Karl Marx", "Verlag von Otto Meisner", 1867, "history-of-thought", "Marx analyzes the commodity, surplus value, and accumulation, predicting capitalism\u2019s contradictions. The critique of political economy that shaped the left.", ["surplus value", "commodity", "accumulation"]], ["AP Macroeconomics Course and Exam Description", "College Board", "College Board", 2019, "macroeconomics", "The College Board framework covers national income, inflation, unemployment, and stabilization policy. The U.S. standard for secondary macroeconomics.", ["GDP", "inflation", "fiscal policy"]], ["Econometric Methods", "Jack Johnston", "McGraw-Hill", 1963, "econometrics", "Johnston\u2019s methods text systematized estimation, identification, and time-series for economists. A generation learned inference from it.", ["estimation", "identification", "time series"]], ["Capitalism, Socialism and Democracy", "Joseph A. Schumpeter", "Harper & Brothers", 1942, "history-of-thought", "Schumpeter predicted capitalism\u2019s success would breed its own critics, and coined creative destruction for innovation\u2019s gale. The most quoted book in economics.", ["creative destruction", "innovation", "entrepreneur"]], ["Governing the Commons", "Elinor Ostrom", "Cambridge University Press", 1990, "behavioral", "Ostrom\u2019s fieldwork showed communities can govern shared resources without privatization or state control, via design principles. The Nobel-winning case against the tragedy of the commons.", ["commons", "collective action", "design principles"]]];
var PROJ=[["Post-Scarcity Economics", "Models when key goods approach zero marginal cost."], ["Central Bank Digital Currencies", "Sovereign money on ledgers."], ["The Economics of Attention", "Pricing the scarcest resource."], ["Climate Economics 2040", "What the models got right."], ["Basic Income: The Meta-Analysis", "Every trial, pooled."], ["Platform Cooperatives", "Worker-owned networks that scale."], ["AI Labor and Wage Theory", "What wages mean when machines do the work."], ["Degrowth versus Green Growth", "The debate, empirically."], ["The Economics of Care", "Valuing unpaid work."], ["Space Resource Economics", "Property rights beyond Earth."], ["Behavioral Policy at Scale", "Nudges in national programs."], ["Beyond GDP", "Measuring what matters."]];
var METHODS='econometric modeling, survey data, and policy case studies';
var FRAMES=["Early pilots suggest the approach could improve outcomes markedly where it is adopted first in community settings.", "Practitioners report faster skill transfer when the method is taught in cohorts rather than through solo study.", "The study projects mainstream adoption within a decade, beginning in specialist programs and spreading to general curricula.", "Reviewers note the strongest effects where the method is paired with mentorship rather than delivered as content alone."];
var POOL={};
CATS.forEach(function(c){POOL[c]=WORKS.filter(function(w){return w[4]===c;});});
function pad7(n){return String(n).padStart(7,'0');}
function sigLink(seed){return '../'+BASE+'-study/index.html?sig=JAH-'+BASE+'-STUDY-S-'+pad7(seed);}
/* work layout: [title, authors, publication, year, category, abstract, [terms]] */
function aspectBody(w,aspect){
  var b=w[5]+'\n\nKey terms: '+w[6].join('; ')+'.';
  if(aspect==='focus'){
    b+='\n\nStudy focus: How does \u201c'+w[6][0]+'\u201d shape this work\u2019s central argument? '+
       'What would a practitioner carry from \u201c'+w[6][1]+'\u201d into daily practice?';
  }
  b+='\n\nPublished: '+w[2]+', '+w[3]+'.';
  return b;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[(seed-1)%CATS.length];
  var lvl=rnd()<0.35?2:1;
  var id=PREFIX+pad7(seed);
  var link=sigLink(seed);
  if(lvl===1){
    var pool=(POOL[cat]&&POOL[cat].length)?POOL[cat]:WORKS;
    var w=pick(pool,rnd);
    var aspect=pick(['abstract','focus'],rnd);
    var title=w[0];
    return {id:id,title:title,authors:w[1],publication:w[2],year:w[3],
      full_content:aspectBody(w,aspect),
      source_ref:'WorldCat \u2014 \u201c'+title+'\u201d / '+w[1]+' ('+w[3]+')',
      signature_link:link,level:1,category:cat};
  }
  var p=pick(PROJ,rnd);
  var frame=pick(FRAMES,rnd);
  var ptitle='Level 2 \u2014 '+p[0];
  var full='This is a Level 2 projection record: a forward-looking study sketched from the archive\u2019s patterns, '+
    'not a real publication. \u201c'+p[0]+'.\u201d '+p[1]+' Projected method: '+METHODS+'. '+frame;
  return {id:id,title:ptitle,authors:'JAH Signature Projection Office',
    publication:'JAH Published Archive \u2014 Projection Series',year:2026+(seed%3),
    full_content:full,
    source_ref:'JAH Published Archive \u2014 Projection Series (generated projection)',
    signature_link:link,level:2,category:cat};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX+'\\d{7}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.level===2&&r.title.slice(0,7)!=='Level 2')e.push('level2-title');
  if(r.level===1&&r.title.slice(0,7)==='Level 2')e.push('level1-title');
  if(typeof r.authors!=='string'||!r.authors.length)e.push('authors');
  if(typeof r.publication!=='string'||!r.publication.length)e.push('publication');
  if(typeof r.year!=='number'||(r.year|0)!==r.year||r.year<100||r.year>2028)e.push('year');
  if(typeof r.full_content!=='string'||r.full_content.length<120||r.full_content.length>3000)e.push('full_content');
  if(typeof r.source_ref!=='string'||!r.source_ref.length)e.push('source_ref');
  if(!/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(CATS.indexOf(r.category)<0)e.push('category');
  return {ok:!e.length,errors:e};
}
/* 40 seeds x 40 invariant checks = 1600 assertions. */
function selftest(){
  var seeds=[],i;
  for(i=1;i<=40;i++)seeds.push(i);
  var fails=[],passed=0,total=0;
  function chk(seed,name,cond){total++;if(cond){passed++;}else{fails.push('seed '+seed+': '+name);}}
  function bad(r,over){var c={},k;for(k in r)c[k]=r[k];for(k in over)c[k]=over[k];return c;}
  seeds.forEach(function(seed){
    var r=generate(seed,{},prng(seed));
    var r2=generate(seed,{},prng(seed));
    chk(seed,'is-object',!!r&&typeof r==='object');
    chk(seed,'id-format',new RegExp('^'+PREFIX+'\\d{7}$').test(r.id));
    chk(seed,'id-prefix',r.id.slice(0,PREFIX.length)===PREFIX);
    chk(seed,'id-seq',r.id===PREFIX+pad7(seed));
    chk(seed,'title-nonempty',typeof r.title==='string'&&r.title.length>0);
    chk(seed,'authors-nonempty',typeof r.authors==='string'&&r.authors.length>0);
    chk(seed,'publication-nonempty',typeof r.publication==='string'&&r.publication.length>0);
    chk(seed,'year-range',typeof r.year==='number'&&(r.year|0)===r.year&&r.year>=100&&r.year<=2028);
    chk(seed,'full-min',typeof r.full_content==='string'&&r.full_content.length>=120);
    chk(seed,'full-max',r.full_content.length<=3000);
    chk(seed,'full-sentences',(r.full_content.match(/\./g)||[]).length>=3);
    chk(seed,'source-nonempty',typeof r.source_ref==='string'&&r.source_ref.length>0);
    chk(seed,'siglink-format',/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''));
    chk(seed,'siglink-seq',r.signature_link.slice(-10)==='-S-'+pad7(seed));
    chk(seed,'level-12',r.level===1||r.level===2);
    chk(seed,'l2-title',r.level!==2||r.title.slice(0,7)==='Level 2');
    chk(seed,'l1-title',r.level!==1||r.title.slice(0,7)!=='Level 2');
    chk(seed,'category-valid',CATS.indexOf(r.category)>=0);
    chk(seed,'validate-ok',validate(r).ok);
    chk(seed,'deterministic',JSON.stringify(r)===JSON.stringify(r2));
    chk(seed,'title-no-html',r.title.indexOf('<')<0);
    chk(seed,'full-no-wordbreak',r.full_content.indexOf('word-break')<0);
    chk(seed,'full-grounded',r.level===1?r.full_content.indexOf(String(r.year))>=0:r.full_content.indexOf('Level 2 projection')>=0);
    chk(seed,'id-unique',seed===1||r.id!==PREFIX+pad7(seed-1));
    chk(seed,'rej-bad-id',!validate(bad(r,{id:'BAD'})).ok);
    chk(seed,'rej-no-title',!validate(bad(r,{title:''})).ok);
    chk(seed,'rej-bad-year',!validate(bad(r,{year:50})).ok);
    chk(seed,'rej-bad-level',!validate(bad(r,{level:3})).ok);
    chk(seed,'rej-short-full',!validate(bad(r,{full_content:'x'})).ok);
    chk(seed,'rej-bad-sig',!validate(bad(r,{signature_link:'nope'})).ok);
    chk(seed,'rej-l2-title',!validate(bad(r,{level:2,title:'No Prefix Here'})).ok);
    chk(seed,'rej-l1-title',!validate(bad(r,{level:1,title:'Level 2 Sneaky'})).ok);
    chk(seed,'category-opt',generate(seed,{category:CATS[0]},prng(seed)).category===CATS[0]);
    chk(seed,'jahdb-registered',typeof JAHDB==='undefined'||!!JAHDB.getGenerator(SLUG));
    chk(seed,'runGenerator-ok',typeof JAHDB==='undefined'?true:JAHDB.runGenerator(SLUG,seed,{}).ok);
    chk(seed,'no-underscore-keys',Object.keys(r).every(function(k){return k.charAt(0)!=='_';}));
    chk(seed,'authors-no-database',r.authors.indexOf('Database')<0);
    chk(seed,'pub-no-database',r.publication.indexOf('Database')<0);
    chk(seed,'title-no-database',r.title.indexOf('Database')<0);
    chk(seed,'l2-honesty',r.level!==2||r.full_content.indexOf('not a real publication')>=0);
    chk(seed,'l1-pubnote',r.level!==1||r.full_content.indexOf('Published:')>=0);
    chk(seed,'json-roundtrip',JSON.parse(JSON.stringify(r)).id===r.id);
  });
  return {seeds:seeds.length,per_seed:total/seeds.length,passed:passed,failed:total-passed,total:total,failures:fails};
}
var gen={version:GENVER,generate:generate,validate:validate,selftest:selftest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
