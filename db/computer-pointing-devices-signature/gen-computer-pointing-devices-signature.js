(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="computer-pointing-devices-signature";
var VERSION='jahdb-computer-pointing-devices-signature-1.0';
var PREFIX="JAH-PDEV-S-";
var CATS=["mouse","trackball","touchpad","pen-tablet","pen-display","ergonomic"];
var CORES=['Glide','Orbit','Morph','Wave','Spin','Bio'];
var FORMS=['Point','Pad','Pen','Ball','Ring','Puck'];
var DPIS=[8000,12000,16000,24000,32000,48000];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var core=pick(CORES,rnd),form=pick(FORMS,rnd),dpi=pick(DPIS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='JAH '+core+form;
  var prog='# '+title+'\ndpi='+ "'+dpi+'" +'\nprint("Counts per mm:",round(dpi/25.4))\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    brand:'JAH Signature',model:title,device_type:cat,dpi_max:dpi,
    sensor:core+' concept sensor',polling_hz:1000,buttons:ri(rnd,2,10),
    description:'Signature concept pointing device: the '+title+', an original JAH input design study. Clearly labeled Signature work — not a real product.',
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
