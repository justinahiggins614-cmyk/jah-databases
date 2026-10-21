(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="windows-command-prompt-signature";
var VERSION='jahdb-windows-command-prompt-signature-1.0';
var PREFIX="JAH-CMDP-S-";
var CATS=["file-ops","system-info","network","disk","process","batch"];
var CORES=['snap','find','net','crypt','clip','hash'];
var FORMS=['Snapshot Tool','Smart Finder','Doctor','Vault','Manager','Checker'];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var core=pick(CORES,rnd),form=pick(FORMS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var cmdname='jah'+core.toLowerCase()+form.toLowerCase().replace(/[^a-z]/g,'');
  var title=cmdname+' — '+form;
  var prog='@echo off\r\n:: '+title+' (Signature concept)\r\n'+cmdname+' --help\r\necho Concept demo complete.\r\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    command:cmdname,syntax:cmdname+' [options]',
    description:'Signature concept command: '+cmdname+', an original JAH utility design ('+form.toLowerCase()+'). Clearly labeled Signature work — not a real Windows command.',
    examples:[cmdname+' --help'],batch_snippet:prog,
    ladder_rank:1+(seed%3),
    demo:{language:'batch',program:prog},
    provenance:'Signature-authored original created by the JAH system — clearly labeled Signature work, not a real command.',
    src:'signature-generated-completion',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.command!=='string'||r.command.indexOf('jah')!==0)e.push('command');
  if(r.src!=='signature-generated-completion')e.push('src');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
