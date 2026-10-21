(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="display-monitors-signature";
var VERSION='jahdb-display-monitors-signature-1.0';
var PREFIX="JAH-MON-S-";
var CATS=["gaming","professional","office","ultrawide","oled"];
var CORES=['Helio','Nebula','Photon','CurveField','TrueBlack','ColorForge'];
var FORMS=['View','Panel','Field','Stage','Station','Wall'];
var SIZES=[24,27,32,34,38,49];
var RATES=[120,144,165,240,360];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var core=pick(CORES,rnd),form=pick(FORMS,rnd),size=pick(SIZES,rnd),hz=pick(RATES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='JAH '+core+form+' '+size;
  var prog='import math\nw,h=3840,2160\ndiag='+ "'+size+'" +'\nhz='+ "'+hz+'" +'\nppi=math.hypot(w,h)/diag\nprint("PPI:",round(ppi,1))\nprint("Bandwidth Gbps:",round(w*h*hz*30/1e9,1))\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    brand:'JAH Signature',model:title,panel_type:core+' concept panel',size_in:size,
    resolution:'3840x2160',refresh_hz:hz,response_ms:ri(rnd,1,5),brightness_nits:600,
    description:'Signature concept monitor: the JAH '+core+form+' '+size+', a '+size+'-inch concept panel simulated at '+hz+' Hz. An original JAH design study — clearly labeled Signature work, not a real product.',
    ladder_rank:1+(seed%3),
    demo:{language:'python',program:prog},
    provenance:'Signature-authored original created by the JAH system — clearly labeled Signature work, not a real product.',
    src:'signature-generated-completion',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.indexOf('JAH ')!==0)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(r.brand!=='JAH Signature')e.push('brand');
  if(r.src!=='signature-generated-completion')e.push('src');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
