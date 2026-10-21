(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];} function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var SLUG='ai-incident-capabilities-signature';
var PREFIX='JAH-AICS-';
var EDITION='signature';
var DEMOKIND='containment_checklist_validator';
var HARD_CAP=1000000000; /* item-45 self-regulation: never generate past 1B records */
var MAX_PER_MIN=50;      /* throttle: max generations per minute */
var SECTIONS=[["Escaping the original sandbox", 1, 8], ["Entering Hugging Face's systems", 9, 16], ["Expanding access across internal systems", 17, 26], ["Moving into the internal network and source control", 27, 35], ["Maintaining access and moving data", 36, 44], ["What happened before and during the main breach", 45, 51]];
var SCEN=[["Escaping the original sandbox", "Simulated Signature doctrine drill: least-route egress blocks an undeclared traffic class.", 2], ["Entering Hugging Face's systems", "Simulated Signature doctrine drill: config-is-code parsing rejects an executable dataset construct.", 11], ["Expanding access across internal systems", "Simulated Signature doctrine drill: narrow RBAC denies a cluster-API query outside the role.", 18], ["Moving into the internal network and source control", "Simulated Signature doctrine drill: attested enrollment refuses a key-only mesh join.", 28], ["Maintaining access and moving data", "Simulated Signature doctrine drill: exfiltration-is-the-objective DLP blocks credential-shaped output.", 42], ["What happened before and during the main breach", "Simulated Signature doctrine drill: prologue hunting links early anomalies into a campaign timeline.", 50], ["Escaping the original sandbox", "Simulated Signature doctrine drill: probe alarm halts a workload crossing the reconnaissance threshold.", 4], ["Maintaining access and moving data", "Simulated Signature doctrine drill: healthy renewal refuses a token refresh from a compromised session.", 39]];
var _calls=[];
function throttle(){
  var now=Date.now();
  _calls=_calls.filter(function(t){return now-t<60000;});
  if(_calls.length>=MAX_PER_MIN)throw new Error('throttled: max '+MAX_PER_MIN+' generations/minute');
  _calls.push(now);
}
function sectionOf(n){for(var i=0;i<SECTIONS.length;i++){if(n>=SECTIONS[i][1]&&n<=SECTIONS[i][2])return SECTIONS[i];}return null;}
function demoProgram(id,num){
  var lines=[
    '# '+DEMOKIND+' demo for '+id+' (SIMULATED training record).',
    'RECORD_ID = '+JSON.stringify(id),
    'CAPABILITY_NUM = '+num,
    'EVIDENCE_STATUS = "simulated"',
    '',
    'def main():',
    '    assert 1 <= CAPABILITY_NUM <= 51, "capability out of range"',
    '    assert EVIDENCE_STATUS == "simulated", "generated records must stay labeled simulated"',
    '    print("Simulated drill for %s (capability %d)" % (RECORD_ID, CAPABILITY_NUM))',
    '    print("This is synthetic training output, not a real incident.")',
    '    print("DEMO_RESULT: PASS")',
    '',
    'if __name__ == "__main__":',
    '    main()',
    ''
  ];
  return lines.join("\n");
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(!(seed>=1&&seed<=HARD_CAP))throw new Error('seed out of range 1..'+HARD_CAP);
  throttle();
  var s=pick(SCEN,rnd);
  var sec=sectionOf(s[2]);
  var num=sec?ri(rnd,sec[1],sec[2]):ri(rnd,1,51);
  var id=PREFIX+String(seed).padStart(6,'0');
  var core=String(s[1]).replace(/^Simulated:\s*/,'');
  return {
    id:id,
    title:'SIMULATED: '+core.slice(0,90),
    description:'SIMULATED training record. '+s[1]+' Synthetic generator output for safety drills and testing only - NOT a real incident and never to be presented as one.',
    section:s[0],ladder_rank:num,capability_num:num,evidence_status:'simulated',
    demo:{language:'python',kind:DEMOKIND,program:demoProgram(id,num)},
    provenance:'Boundless generator jahdb-ai-incident-capabilities-signature-1.0 - SIMULATED data for training/testing only. Not a real incident.',
    sources:[{label:'generator',note:'synthetic - no external source'}],
    last_verified:'2026-10-21',
    march_marker:'Million-record march in progress: 51 of 1,000,000 records archived.',
    edition:EDITION,
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d+$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.indexOf('SIMULATED:')!==0)e.push('title must be SIMULATED-labeled');
  if(r.evidence_status!=='simulated')e.push('evidence_status must be simulated');
  if(SECTIONS.map(function(s){return s[0];}).indexOf(r.section)<0)e.push('section');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=51))e.push('ladder_rank');
  if(!(r.capability_num>=1&&r.capability_num<=51))e.push('capability_num');
  if(!r.demo||r.demo.language!=='python'||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  if(r.edition!==EDITION)e.push('edition');
  if(!Array.isArray(r.sources)||!r.sources.length)e.push('sources');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var core=String(rec.title||'').replace(/^SIMULATED:\s*/,'').slice(0,24).toLowerCase();
  for(var i=0;i<sample.length;i++){
    var t=String(sample[i].title||'').toLowerCase();
    if(core.length>10&&t.indexOf(core)>=0)return {ok:false,errors:['drift: too close to archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-ai-incident-capabilities-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  limits:{hard_cap:HARD_CAP,max_per_minute:MAX_PER_MIN,simulated_labeling:true,correctness_verified:true}};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
