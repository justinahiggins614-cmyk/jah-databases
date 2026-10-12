/* JAH Public Photography Database generator — jahdb-public-photography-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Generates COMPLETE original photograph studies (subject/craft/context analysis),
   clearly labeled src:"signature-generated-sample". */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-PHT-';
var GENRES=['street','portrait','landscape','documentary','still-life'];

var SUBJECTS=[['Fog over the harbor','street'],['The night ferryman','portrait'],['Orchard in October','landscape'],['Breadline, winter','documentary'],['Tools of the trade','still-life'],['Rain on cobblestones','street'],['The lighthouse keeper\'s wife','portrait'],['Dunes at dawn','landscape'],['Market day','documentary'],['Pewter and pears','still-life']];
var CAMERAS=['large-format view camera','medium-format folding camera','35mm rangefinder'];
var PROCESSES=['silver-gelatin','albumen','platinum'];
function normGenre(g){return GENRES.indexOf(g)>=0?g:'';}
function buildPhoto(s,genre,topic){
  var t=pick(s,SUBJECTS);
  var g=genre||t[1];
  var title=topic?('Photograph study: '+topic):t[0];
  var year=ri(s,1850,1945), camera=pick(s,CAMERAS), process=pick(s,PROCESSES);
  var steps=[
   'SUBJECT: '+title+' \u2014 an imagined '+process+' study in the '+g+' tradition, '+year+'.',
   'CRAFT: '+camera+'; '+process+' print; natural light; composed in camera, not cropped.',
   'CONTEXT: a meditation on ordinary labor and ordinary light \u2014 the archive\'s imagined record of a moment that feels remembered.',
   'MAKER: an imagined practitioner of the period manner, created as a Signature study for this archive.'
  ];
  var analysis='PHOTO ANALYSIS: '+title.toUpperCase()+'\n\n'+steps.join('\n\n');
  return {title:title,genre:g,year:year,camera:camera,process:process,
    desc:title+' \u2014 imagined '+process+' '+g+' photograph study ('+year+'). Complete analysis: subject, craft, context and maker notes.',
    analysis:analysis,steps:steps};
}
function demoProgram(rid,title,steps){
  var j=function(x){return JSON.stringify(x);};
  return '/* JAH photography demo program \u2014 jahdb-demo-1.0\n'+
   ' * Database: public-photography \u00b7 Record: '+rid+' \u00b7 '+title+'\n'+
   ' * Guided photo analysis.\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js\n'+
   ' * RUN IN BROWSER: press F12, paste into the console, press Enter. */\n'+
   '(function(){var STEPS='+j(steps)+';\n'+
   'STEPS.forEach(function(s){console.log(s);});\n'+
   'console.log("Analysis complete.");})();';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120)||null;
  var genre=normGenre(opts.genre)||null;
  var s=rnd, b=buildPhoto(s,genre,topic);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {
   id:id,title:b.title,description:b.desc,genre:b.genre,type:'photograph study',
   year:b.year,camera:b.camera,process:b.process,
   analysis:b.analysis,study_steps:b.steps,
   image:'',image_full:'',image_credit:'',
   demo:{engine:'jahdb-demo-1.0',kind:'photo-analysis',title:'Photo analysis \u2014 '+b.title,language:'javascript',
     program:demoProgram(id,b.title,b.steps)},
   src:'signature-generated-sample',note:'Original Signature photograph study; clearly labeled sample, not a public-domain harvest.',
   sources:[{kind:'signature-generated',detail:'Original study created by the JAH boundless generator.'}],
   _seed:seed,topic:topic||undefined
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PHT-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(typeof r.analysis!=='string'||r.analysis.length<200)e.push('analysis');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('jahdb-demo-1.0')<0)e.push('demo');
  if(r.src!=='signature-generated-sample')e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-photography-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-photography',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
