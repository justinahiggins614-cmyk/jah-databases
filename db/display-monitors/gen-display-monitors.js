(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="display-monitors";
var VERSION='jahdb-display-monitors-1.0';
var PREFIX="JAH-MON-";
var CATS=["gaming","professional","office","ultrawide","oled"];
var PANELS=['IPS','VA','OLED','Mini-LED VA','QD-OLED','Nano IPS'];
var SIZES=[24,27,32,34,38,49];
var RES=[[1920,1080],[2560,1440],[3440,1440],[3840,1600],[3840,2160],[5120,1440],[5120,2880]];
var RATES=[60,75,120,144,165,240,360];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var panel=pick(PANELS,rnd),size=pick(SIZES,rnd),res=pick(RES,rnd),hz=pick(RATES,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Generated '+size+'-inch '+panel+' '+res[0]+'x'+res[1]+'/'+hz+'Hz reference profile';
  var prog='import math\nw,h='+ "'+res[0]+','+res[1]+'" +'\ndiag='+ "'+size+'" +'\nhz='+ "'+hz+'" +'\nppi=math.hypot(w,h)/diag\nprint("PPI:",round(ppi,1))\nprint("Bandwidth Gbps:",round(w*h*hz*30/1e9,1))\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    brand:'Generated reference',model:'GEN-'+size+'-'+hz,panel_type:panel,size_in:size,
    resolution:res[0]+'x'+res[1],refresh_hz:hz,response_ms:ri(rnd,1,8),brightness_nits:ri(rnd,250,1200),
    description:'Generated reference profile for a '+size+'-inch '+panel+' panel at '+res[0]+'x'+res[1]+' and '+hz+' Hz. Produced by the boundless generator as a specification-planning sample; it is not a real product.',
    ladder_rank:1+(seed%3),generated:true,
    demo:{language:'python',program:prog},
    provenance:'Generated reference profile from the boundless generator — a planning sample, not a real product.',
    src:'public-harvest',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(!(r.size_in>=13&&r.size_in<=65))e.push('size_in');
  if(!(r.refresh_hz>=30&&r.refresh_hz<=540))e.push('refresh_hz');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
