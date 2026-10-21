(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="computer-pointing-devices";
var VERSION='jahdb-computer-pointing-devices-1.0';
var PREFIX="JAH-PDEV-";
var CATS=["mouse","trackball","touchpad","pen-tablet","pen-display","ergonomic"];
var DTYPES=['gaming mouse','productivity mouse','trackball','touchpad','pen tablet','pen display'];
var DPIS=[1600,3200,8000,12000,16000,25600,32000];
var POLLS=[125,500,1000,2000];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var dtype=pick(DTYPES,rnd),dpi=pick(DPIS,rnd),poll=pick(POLLS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Generated '+dtype+' '+dpi+'-DPI/'+poll+'Hz reference profile';
  var prog='# '+title+'\ndpi='+ "'+dpi+'" +'\npoll='+ "'+poll+'" +'\nprint("Poll interval ms:",round(1000/poll,2))\nprint("Counts per mm:",round(dpi/25.4))\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    brand:'Generated reference',model:'GEN-PTR-'+dpi,device_type:dtype,dpi_max:dpi,
    sensor:'reference optical',polling_hz:poll,buttons:ri(rnd,2,12),
    description:'Generated reference profile for a '+dtype+' at '+dpi+' DPI and '+poll+' Hz polling. Produced by the boundless generator as a specification-planning sample; it is not a real product.',
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
  if(!(r.dpi_max>=400&&r.dpi_max<=64000))e.push('dpi_max');
  if(!(r.polling_hz>=125&&r.polling_hz<=8000))e.push('polling_hz');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
