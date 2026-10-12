/* JAH Public Art Database generator — jahdb-public-art-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   Generates COMPLETE original artwork studies (curatorial essay + viewing guide),
   clearly labeled src:"signature-generated-sample". */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function shuffle(s,arr){var a=arr.slice(),i,j,t;for(i=a.length-1;i>0;i--){j=(s()*(i+1))|0;t=a[i];a[i]=a[j];a[j]=t;}return a;}
var PREFIX='JAH-ART-';
var GENRES=['painting','sculpture','print','drawing','photograph-era'];

var TITLES=[['Harbor at First Light','painting'],['The Cartographer\'s Dream','painting'],['Study in Ochre and Blue','painting'],['Winter Ferry Crossing','painting'],['The Night Orchard','painting'],['Marble Silence','sculpture'],['Figure Rising','sculpture'],['The Weight of Air','sculpture'],['Thames Etching, No. 4','print'],['Woodcut: The Old Mill','print'],['Charcoal Harbor Study','drawing'],['Silver-Gelatin Nocturne','photograph-era']];
var ARTISTS=['E. Whitcombe (imagined)','The Meridian School (imagined)','Studio of A. Ferrand (imagined)','Anon., Northern manner (imagined)'];
var MEDIUMS={painting:'Oil on canvas',sculpture:'Carrara marble',print:'Etching on laid paper',drawing:'Charcoal on paper','photograph-era':'Silver-gelatin print'};
var MOVEMENTS=['Romantic','Realist','Impressionist','Symbolist','Arts-and-Crafts'];
function normGenre(g){return GENRES.indexOf(g)>=0?g:'';}
function buildArt(s,genre,topic){
  var t=pick(s,TITLES);
  var g=genre||t[1];
  var title=topic?('Study: '+topic):t[0];
  var artist=pick(s,ARTISTS), year=ri(s,1780,1925), movement=pick(s,MOVEMENTS);
  var medium=MEDIUMS[g]||'Mixed media';
  var stops=[
   'Stand back: take the whole composition at once \u2014 the '+(g==='sculpture'?'mass and its shadows':'light and its color')+' resolve into a single gesture.',
   'Context: an imagined '+movement.toLowerCase()+' work of '+year+', in the manner of the period, created as a Signature study for this archive.',
   'Technique: '+medium+'; observe the handling of '+(g==='sculpture'?'plane and edge':'brushwork and glaze')+'.',
   'Meaning: a meditation on labor and light \u2014 what the age made, and what it dreamed of making.'
  ];
  var essay=title.toUpperCase()+'\nA Signature artwork study ('+year+')\n\n'+stops.join('\n\n');
  return {title:title,genre:g,artist:artist,year:year,movement:movement,medium:medium,
    desc:title+' \u2014 imagined '+movement.toLowerCase()+' '+g+' ('+year+') by '+artist+'. Complete curatorial study: essay, viewing guide and technique notes.',
    essay:essay,stops:stops};
}
function demoProgram(rid,title,stops){
  var j=function(x){return JSON.stringify(x);};
  return '/* JAH art demo program \u2014 jahdb-demo-1.0\n'+
   ' * Database: public-art \u00b7 Record: '+rid+' \u00b7 '+title+'\n'+
   ' * Guided viewing tour.\n'+
   ' * RUN ON PC: save as demo.js, then run:  node demo.js\n'+
   ' * RUN IN BROWSER: press F12, paste into the console, press Enter. */\n'+
   '(function(){var STOPS='+j(stops)+';\n'+
   'console.log("GUIDED TOUR \u2014 '+title.replace(/"/g,'')+'");\n'+
   'STOPS.forEach(function(s,i){console.log("Stop "+(i+1)+": "+s);});\n'+
   'console.log("Tour complete.");})();';
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var topic=(opts.topic||'').toString().trim().slice(0,120)||null;
  var genre=normGenre(opts.genre)||null;
  var s=rnd, b=buildArt(s,genre,topic);
  var id=PREFIX+String(seed).padStart(7,'0');
  return {
   id:id,title:b.title,description:b.desc,genre:b.genre,type:'artwork study',
   artist:b.artist,year:b.year,movement:b.movement,medium:b.medium,
   essay:b.essay,viewing_guide:b.stops,
   image:'',image_full:'',image_credit:'',
   demo:{engine:'jahdb-demo-1.0',kind:'guided-tour',title:'Guided viewing tour \u2014 '+b.title,language:'javascript',
     program:demoProgram(id,b.title,b.stops)},
   src:'signature-generated-sample',note:'Original Signature artwork study; clearly labeled sample, not a public-domain harvest.',
   sources:[{kind:'signature-generated',detail:'Original study created by the JAH boundless generator.'}],
   _seed:seed,topic:topic||undefined
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-ART-\d{7}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(typeof r.essay!=='string'||r.essay.length<200)e.push('essay');
  if(!r.demo||typeof r.demo.program!=='string'||r.demo.program.indexOf('jahdb-demo-1.0')<0)e.push('demo');
  if(r.src!=='signature-generated-sample')e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-art-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-art',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
