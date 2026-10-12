/* JAH Public Newspapers Database generator — jahdb-public-newspapers-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Generates COMPLETE original front pages (period-style, clearly labeled
   src:"signature-generated-sample" — never presented as genuine historic scans). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-NWS-';
var GENRES=['front page'];

var PAPERS=['The Meridian Gazette','The Harbor Chronicle','The Daily Clarion','The Evening Standard-Bearer','The Commonwealth Times'];
var EVENTS=[['GREAT EXPOSITION OPENS','A world\'s fair opens its gates; a hundred thousand pass through on the first day.'],
 ['RAIL LINE COMPLETED','The last spike is driven; two coasts are joined by iron.'],
 ['HARVEST BREAKS RECORDS','The wheat harvest exceeds all previous years; prices fall and bakers rejoice.'],
 ['NEW BRIDGE DEDICATED','A span of steel unites the river towns; thousands walk it on opening day.'],
 ['CITY LIGHTS ELECTRIFIED','The gas lamps go dark as electric light floods the avenues.'],
 ['EXPEDITION RETURNS','The explorers return with maps, specimens, and tales of the far interior.'],
 ['MARKET SOARS','Stocks climb to new heights; the ticker runs late into the evening.'],
 ['STORM BATTERS COAST','A great gale strikes the seaboard; ships shelter and the lifesavers stand ready.'],
 ['TREATY SIGNED','After long negotiation, the treaty is signed amid cannon salutes.'],
 ['CHAMPION CROWNED','Before a roaring crowd, the championship is decided in the final round.']];
var KICKERS=['CITY DESK','FOREIGN WIRE','BUSINESS','SPORTING','EDITORIAL'];
function buildPage(s,topic){
  var paper=pick(s,PAPERS);
  var ev=pick(s,EVENTS);
  var headline=topic?topic.toUpperCase():ev[0];
  var year=ri(s,1850,1929), month=pick(s,['January','March','June','September','November']), day=ri(s,1,28);
  var date=month+' '+day+', '+year;
  var articles=[
   {head:KICKERS[0]+' \u2014 '+headline,body:ev[1]+' Our correspondent wires that the scenes beggar description, and the whole city has turned out to witness the event.'},
   {head:'WHAT IT MEANS',body:'In an editorial, this paper holds that the event marks a turning point. The full implications will be felt for years; the present generation is fortunate to witness it.'},
   {head:'THE WIRES',body:'Brief dispatches from every quarter confirm the news. Further particulars will appear in our later editions as they arrive by telegraph.'}
  ];
  return {paper:paper,date:date,headline:headline,articles:articles,
    title:headline+' ('+paper+')',
    desc:headline+' \u2014 '+paper+', '+date+'. Complete imagined front page: 3 period articles in full, clearly labeled as a Signature-generated sample.'};
}
function demoProgram(rid,title,paper,date,headline,arts){
  var j=function(x){return JSON.stringify(x);};
  return '/* JAH newspaper demo program \u2014 jahdb-demo-1.0\n'+
   ' * Database: public-newspapers \u00b7 Record: '+rid+' \u00b7 '+title+'\n'+
   ' * Front-page reading walkthrough.\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js\n'+
   ' * RUN IN BROWSER: press F12, paste into the console, press Enter. */\n'+
   '(function(){var H='+j(headline)+',A='+j(arts.map(function(a){return a.head;}))+';\n'+
   'console.log("'+paper+' \u00b7 "+'+j(date)+');\n'+
   'console.log("HEADLINE: "+H);\n'+
   'A.forEach(function(h,i){console.log("["+(i+1)+"] "+h);});\n'+
   'console.log("Sample front page \u2014 imagined, not a historic scan.");})();';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120)||null;
  var s=rnd, b=buildPage(s,topic);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {
   id:id,title:b.title,paper:b.paper,date:b.date,headline:b.headline,articles:b.articles,
   description:b.desc,genre:'front page',type:'historic newspaper',
   image:'',image_full:'',image_credit:'',
   demo:{engine:'jahdb-demo-1.0',kind:'front-page',title:'Front-page reading \u2014 '+b.headline,language:'javascript',
     program:demoProgram(id,b.title,b.paper,b.date,b.headline,b.articles)},
   src:'signature-generated-sample',
   source_note:'Imagined period-style front page; clearly labeled sample, not a genuine historic scan.',
   note:'Generated sample front page.',
   sources:[{kind:'signature-generated',detail:'Original sample created by the JAH boundless generator.'}],
   _seed:seed,topic:topic||undefined
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-NWS-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<8)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!Array.isArray(r.articles)||r.articles.length<2)e.push('articles');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('jahdb-demo-1.0')<0)e.push('demo');
  if(r.src!=='signature-generated-sample')e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-newspapers-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-newspapers',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
