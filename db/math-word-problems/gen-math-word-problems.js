(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function gcd(a,b){return b?gcd(b,a%b):a;}
var CATS=['arithmetic','algebra','geometry','fractions','percentages','logic'];
var PREFIX='JAH-MWP-';

function build(rnd,cat){
  var text,steps,answer;
  if(cat==='arithmetic'){
    if(rnd()<0.5){
      var a=ri(rnd,2,40),b=ri(rnd,2,90),r=a*b;
      text='Maria buys '+a+' apples at '+b+' cents each. How many cents does she spend?';
      steps=['Price per apple: '+b+' cents','Count: '+a+' apples',''+a+' x '+b+' = '+r,'She spends '+r+' cents.'];
      answer=String(r);
    }else{
      var m=ri(rnd,20,100),g=ri(rnd,2,19),r2=m-g;
      text='Tom has '+m+' marbles and gives '+g+' to his sister. How many does he have left?';
      steps=['Start: '+m+' marbles','Give away: '+g+' marbles',''+m+' - '+g+' = '+r2,'He has '+r2+' marbles left.'];
      answer=String(r2);
    }
  }else if(cat==='algebra'){
    var x=ri(rnd,2,25),ad=ri(rnd,1,30),tot=ad+x;
    text='Solve for x: x + '+ad+' = '+tot+'.';
    steps=['x + '+ad+' = '+tot,'x = '+tot+' - '+ad,'x = '+x];
    answer=String(x);
  }else if(cat==='geometry'){
    var l=ri(rnd,2,20),w=ri(rnd,2,20),ar=l*w;
    text='A rectangle is '+l+' cm long and '+w+' cm wide. What is its area?';
    steps=['Area = length x width','Area = '+l+' x '+w,'Area = '+ar+' square cm'];
    answer=ar+' square cm';
  }else if(cat==='fractions'){
    var d1=pick([2,4,8],rnd),d2=pick([2,4,8],rnd),n1=ri(rnd,1,d1-1),n2=ri(rnd,1,d2-1);
    var num=n1*d2+n2*d1,den=d1*d2,g=gcd(num,den),rn=num/g,rd=den/g;
    var ans=rd===1?String(rn):rn+'/'+rd;
    text='What is '+n1+'/'+d1+' + '+n2+'/'+d2+'?';
    steps=['Common denominator: '+den,''+n1+'/'+d1+' = '+(n1*(den/d1))+'/'+den,''+n2+'/'+d2+' = '+(n2*(den/d2))+'/'+den,'Sum = '+(num)+'/'+den+' = '+ans];
    answer=ans;
  }else if(cat==='percentages'){
    var p=pick([10,20,25,40,50],rnd),n=ri(rnd,5,50)*4,r3=p*n/100;
    text=p+'% of '+n+' is what number?';
    steps=[p+'% = '+p+'/100',''+p+'/100 x '+n+' = '+r3,'The number is '+r3+'.'];
    answer=String(r3);
  }else{
    var n4=ri(rnd,25,60),a4=ri(rnd,5,(n4/2)|0),b4=ri(rnd,5,(n4/2)|0);
    var c4=ri(rnd,1,Math.min(a4,b4)),r4=n4-(a4+b4-c4);
    text='In a class of '+n4+' students, '+a4+' like math, '+b4+' like science, and '+c4+' like both. How many like neither?';
    steps=['Like at least one: '+a4+' + '+b4+' - '+c4+' = '+(a4+b4-c4),'Like neither: '+n4+' - '+(a4+b4-c4)+' = '+r4,r4+' students like neither.'];
    answer=String(r4);
  }
  return {text:text,steps:steps,answer:answer};
}
/* independent re-solver: parse the problem text, recompute, compare */
function resolve(text,subject){
  var m;
  if(subject==='arithmetic'){
    m=text.match(/buys (\d+) apples at (\d+) cents/);if(m)return String(+m[1]*+m[2]);
    m=text.match(/has (\d+) marbles and gives (\d+)/);if(m)return String(+m[1]-+m[2]);
  }else if(subject==='algebra'){
    m=text.match(/x \+ (\d+) = (\d+)/);if(m)return String(+m[2]-+m[1]);
  }else if(subject==='geometry'){
    m=text.match(/is (\d+) cm long and (\d+) cm wide/);if(m)return (+m[1]*+m[2])+' square cm';
  }else if(subject==='fractions'){
    m=text.match(/(\d+)\/(\d+) \+ (\d+)\/(\d+)/);
    if(m){var num=+m[1]*+m[4]+ +m[3]*+m[2],den=+m[2]*+m[4],g=gcd(num,den);
      return (den/g===1)?String(num/g):(num/g)+'/'+(den/g);}
  }else if(subject==='percentages'){
    m=text.match(/(\d+)% of (\d+)/);if(m)return String(+m[1]*+m[2]/100);
  }else if(subject==='logic'){
    m=text.match(/class of (\d+) students, (\d+) like math, (\d+) like science, and (\d+) like both/);
    if(m)return String(+m[1]-(+m[2]+ +m[3]- +m[4]));
  }
  return null;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var b=build(rnd,cat);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,problem_id:id,title:b.text.slice(0,80),problem_text:b.text,steps:b.steps,final_answer:b.answer,subject:cat,grade_level:ri(rnd,3,8),verified:true,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-MWP-\d{6}$/.test(r.id||''))e.push('id');
  if(r.problem_id!==r.id)e.push('problem_id');
  if(r.title!==r.problem_text.slice(0,80))e.push('title');
  if(typeof r.problem_text!=='string'||!r.problem_text.length)e.push('problem_text');
  if(!Array.isArray(r.steps)||r.steps.length<3||r.steps.length>6)e.push('steps');
  if(CATS.indexOf(r.subject)<0)e.push('subject');
  if(!(r.grade_level>=3&&r.grade_level<=8))e.push('grade_level');
  if(r.verified!==true)e.push('verified');
  var expect=resolve(r.problem_text,r.subject);
  if(expect===null)e.push('unparseable problem');
  else if(expect!==r.final_answer)e.push('answer mismatch: steps solve to '+expect);
  else{
    var last=r.steps[r.steps.length-1]||'';
    if(last.indexOf(r.final_answer)<0&&r.steps.join(' ').indexOf(r.final_answer)<0)e.push('answer missing from steps');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-math-word-problems-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('math-word-problems',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
