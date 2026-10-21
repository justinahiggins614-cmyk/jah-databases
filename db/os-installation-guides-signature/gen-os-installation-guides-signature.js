(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG="os-installation-guides-signature";
var VERSION='jahdb-os-installation-guides-signature-1.0';
var PREFIX="JAH-OSINST-S-";
var CATS=["windows","linux-desktop","linux-server","usb-media","partitioning","boot-firmware","dual-boot","post-install"];
var CORES=['Station','Forge','Vault','Kiosk','Pocket','Studio'];
var FORMS=['Install','Setup','Deploy','Express'];

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var core=pick(CORES,rnd),form=pick(FORMS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='JAH '+core+' '+form+' Install';
  var steps=['Back up all data — a Signature install wipes the target drive.','Create Signature install media with the JAH media writer concept tool.','Boot UEFI with Signature Secure Boot keys enrolled.','Choose Express install for defaults or Custom for control.','Create your JAH identity profile and master passphrase.','Verify checksums after the installer finishes, then reboot.'];
  var prog='jah-media-writer --iso '+core.toLowerCase()+'.iso --usb /dev/sdX\njah-verify --media\njah-update --full\n';
  return {id:id,t:title,title:title,g:cat,category:cat,c:1,os:'JAH '+core+' '+form,difficulty:'beginner',
    steps:steps,commands:prog,
    description:'Signature concept install guide: '+title+', an original JAH workflow for setting up a Signature concept system. Clearly labeled Signature work — not a vendor manual.',
    ladder_rank:1+(seed%3),
    demo:{language:'bash',program:prog},
    provenance:'Signature-authored original created by the JAH system — clearly labeled Signature work, not a vendor manual.',
    src:'signature-generated-completion',last_verified:'2026-10-20',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!(new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$')).test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.indexOf('JAH ')!==0)e.push('title');
  if(CATS.indexOf(r.g)<0)e.push('g');
  if(r.src!=='signature-generated-completion')e.push('src');
  if(!Array.isArray(r.steps)||r.steps.length<3)e.push('steps');
  if(r.ladder_rank!==1&&r.ladder_rank!==2&&r.ladder_rank!==3)e.push('ladder_rank');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return{ok:!e.length,errors:e};
}

var gen={version:VERSION,generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
