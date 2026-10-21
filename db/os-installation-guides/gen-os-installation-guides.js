(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="os-installation-guides";
var VERSION='jahdb-os-installation-guides-1.0';
var PREFIX="JAH-OSINST-";
var CATS=["windows","linux-desktop","linux-server","usb-media","partitioning","boot-firmware","dual-boot","post-install"];
var OSLIST=['Windows 11','Windows 10','Ubuntu 24.04','Debian 12','Fedora 40','Linux Mint 21'];
var TOPICS=['pre-install backup checklist','USB media verification checklist','partition plan checklist','post-install update checklist'];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var os=pick(OSLIST,rnd),topic=pick(TOPICS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Generated '+topic+' for '+os;
  var steps=['Back up all data on the target machine before starting.','Verify the install media checksum against the published value.','Boot the installer in the firmware mode matching your partition scheme.','Follow the installer prompts, choosing manual partitioning for control.','Reboot, remove install media, and apply all updates before use.'];
  var prog='#!/bin/bash\nset -euo pipefail\n# '+title+'\necho "Step 1: back up data"\necho "Step 2: verify media checksum"\nsha256sum ~/download.iso\necho "Step 3: write USB and boot UEFI"\nlsblk -d -o NAME,SIZE,MODEL\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,os:os,difficulty:'beginner',
    steps:steps,commands:prog,
    description:'Generated install checklist: '+topic+' for '+os+'. A planning checklist from the boundless generator — always cross-check against the official '+os+' documentation before installing.',
    ladder_rank:1,generated:true,
    demo:{language:'bash',program:prog},
    provenance:'Generated checklist from the boundless generator — verify against official OS documentation.',
    src:'public-harvest',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(!Array.isArray(r.steps)||r.steps.length<3)e.push('steps');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
