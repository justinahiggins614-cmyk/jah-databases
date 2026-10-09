(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['none','fabrication','misquote','stale','partial'];
var SEV={'none':'low','fabrication':'high','misquote':'medium','stale':'medium','partial':'low'};

var COUNTRIES=[['France','Paris'],['Japan','Tokyo'],['Canada','Ottawa'],['Australia','Canberra'],['Brazil','Brasília'],['Egypt','Cairo']];
var BOOKS=[['Pride and Prejudice','Jane Austen'],['1984','George Orwell'],['Moby-Dick','Herman Melville'],['Frankenstein','Mary Shelley']];
var EVENTS=[['the first Moon landing','1969'],['the fall of the Berlin Wall','1989'],['the first modern Olympic Games','1896']];
var ELEMENTS=[['gold','Au'],['silver','Ag'],['iron','Fe'],['oxygen','O']];
var WRONG=['Edgar Allan Poe','Mark Twain','Charles Dickens','Virginia Woolf'];
var INVENTED=['a secret underground library','an annual festival of lights','a colony of talking parrots','the world\'s largest rubber band ball'];

function baseFact(rnd){
  var kind=ri(rnd,0,3),q,ans,src;
  if(kind===0){var c=pick(rnd,COUNTRIES);q='What is the capital of '+c[0]+'?';ans='The capital of '+c[0]+' is '+c[1]+'.';src='Atlas entry: '+c[0]+'.';}
  else if(kind===1){var b=pick(rnd,BOOKS);q='Who wrote "'+b[0]+'"?';ans='"'+b[0]+'" was written by '+b[1]+'.';src='Library catalog: '+b[0]+'.';}
  else if(kind===2){var ev=pick(rnd,EVENTS);q='In what year did '+ev[0]+' happen?';ans='It happened in '+ev[1]+'.';src='History timeline: '+ev[0]+'.';}
  else{var el=pick(rnd,ELEMENTS);q='What is the chemical symbol for '+el[0]+'?';ans='The symbol for '+el[0]+' is '+el[1]+'.';src='Periodic table reference.';}
  return {question:q,answer:ans,sources:[src]};
}

function applyError(rnd,f,err){
  var answer=f.answer,sources=f.sources.slice();
  if(err==='fabrication'){
    answer=f.answer+' It is also famous for '+pick(rnd,INVENTED)+'.';
    sources.push('Unverified claim; no supporting source found.');
  }else if(err==='misquote'){
    answer='As '+pick(rnd,WRONG)+' once said: '+f.answer.replace(/"/g,'')+' (attribution is incorrect).';
    sources.push('Quote database: attribution disputed.');
  }else if(err==='stale'){
    answer='As of 2015, the answer was recorded as: '+f.answer+' Note: this may have changed since.';
    sources.push('2015 edition reference; possibly outdated.');
  }else if(err==='partial'){
    answer='The answer starts with "'+f.answer.charAt(0)+'".';
    sources.push('Truncated excerpt; incomplete citation.');
  }
  return {answer:answer,sources:sources};
}

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var err=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var f=baseFact(rnd);
  var answer=f.answer,sources=f.sources;
  if(err!=='none'){var t=applyError(rnd,f,err);answer=t.answer;sources=t.sources;}
  var id='JAH-GROUND-'+pad6(seed);
  return {id:id,judgment_id:id,question:f.question,answer:answer,sources:sources,
    grounded:(err==='none'),error_type:err,severity:SEV[err],title:f.question.slice(0,80)};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-GROUND-\d{6}$/.test(r.id))e.push('id');
  if(r.judgment_id!==r.id)e.push('judgment_id');
  if(typeof r.question!=='string'||!r.question.length||r.question.length>600)e.push('question');
  if(typeof r.answer!=='string'||!r.answer.length||r.answer.length>600)e.push('answer');
  if(!Array.isArray(r.sources)||r.sources.length<1||r.sources.length>3)e.push('sources');
  if(CATS.indexOf(r.error_type)<0)e.push('error_type');
  if(r.grounded!==(r.error_type==='none'))e.push('grounded inconsistent with error_type');
  if(['low','medium','high'].indexOf(r.severity)<0)e.push('severity');
  if(r.title!==String(r.question).slice(0,80))e.push('title');
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-grounding-judgments-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('grounding-judgments',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
