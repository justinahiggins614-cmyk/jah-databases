(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="windows-command-prompt";
var VERSION='jahdb-windows-command-prompt-1.0';
var PREFIX="JAH-CMDP-";
var CATS=["file-ops","system-info","network","disk","process","batch"];
var CMDS=[['dir','dir C:\\Windows /o:-s','[path]','lists files and folders'],['copy','copy a.txt b.txt','source dest','duplicates files'],['ipconfig','ipconfig /all','','shows network configuration'],['ping','ping -n 4 8.8.8.8','target','tests connectivity'],['robocopy','robocopy C:\\A D:\\B /mir','source dest','robust tree copy'],['tasklist','tasklist | findstr chrome','','lists running processes']];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var cmd=pick(CMDS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Generated drill: '+cmd[0]+' practice exercise';
  var prog='@echo off\r\n:: '+title+'\r\n'+cmd[1]+'\r\necho Drill complete.\r\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,
    command:cmd[0],syntax:cmd[0]+' '+cmd[2],
    description:'Generated practice drill for the '+cmd[0]+' command: '+cmd[3]+' Produced by the boundless generator as a training exercise.',
    examples:[cmd[1]],batch_snippet:prog,
    ladder_rank:1,generated:true,
    demo:{language:'batch',program:prog},
    provenance:'Generated drill from the boundless generator — a training exercise, not documentation of a new command.',
    src:'public-harvest',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(typeof r.command!=='string'||!r.command.length)e.push('command');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
