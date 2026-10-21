(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["skeleton", "facial", "deformation", "retargeting", "export"];
var PREFIX='JAH-DHR-';
var USE="Used by character TDs and virtual production teams moving digital humans between tools.";
var FLD=[["check", "Check"], ["standard", "Standard"], ["pass_criterion", "Pass criterion"]];
var DEMO="# {title} - blendshape coverage (python3)\nhave={d1}\nneed={d2}\nmin_pct={d3}\npct=100.0*have/need\nprint(\"blendshapes: %d/%d (%.0f%%)\" % (have, need, pct))\nprint(\"RIG COMPATIBLE\" if pct >= min_pct else \"RIG INCOMPLETE\")\n";
var SIG=false;
var SRC="public-harvest";
var B=[["skeleton", "Bone Hierarchy Match", "Verifies joint names and parentage match the expected skeleton template.", "Bone Hierarchy Match", "studio skeleton", "names match", "48", "52", "90.0"], ["facial", "Blendshape Count", "Checks the facial rig carries the full expression set (e.g. ARKit 52).", "Blendshape Count", "ARKit 52", "count >= 52", "52", "52", "100.0"], ["deformation", "Joint Orientation", "Confirms joint local axes follow the studio convention for clean rotation.", "Joint Orientation", "Maya/Blender convention", "axes aligned", "48", "52", "90.0"], ["retargeting", "Skin Weight Normalization", "Ensures vertex weights sum to 1 so deformation never collapses.", "Skin Weight Normalization", "linear blend skinning", "sum = 1", "50", "52", "95.0"], ["export", "Facial Rig Retarget", "Tests that expressions transfer to the target rig without distortion.", "Facial Rig Retarget", "retarget solver", "expression error < 5%", "49", "52", "90.0"], ["skeleton", "Finger Rig Mapping", "Validates all finger joints map so hand poses survive transfer.", "Finger Rig Mapping", "hand standard", "15 joints mapped", "15", "15", "100.0"], ["facial", "Eye Gaze Rig", "Checks look-target controls drive both eyes with correct convergence.", "Eye Gaze Rig", "gaze rig", "converge at target", "8", "8", "100.0"], ["deformation", "Jaw Pivot Alignment", "Confirms the jaw pivot sits at the anatomical hinge for natural open/close.", "Jaw Pivot Alignment", "anatomy", "pivot error < 5mm", "1", "1", "100.0"], ["retargeting", "Cloth Sim Attachment", "Verifies cloth pin constraints attach to the right bones.", "Cloth Sim Attachment", "sim pins", "no sliding", "20", "20", "100.0"], ["export", "Hair Card Binding", "Checks hair cards follow the head and shoulders without detaching.", "Hair Card Binding", "groom", "bound", "30", "30", "100.0"], ["skeleton", "LOD Rig Parity", "Ensures lower LODs carry equivalent controls for seamless swaps.", "LOD Rig Parity", "LOD spec", "controls match", "40", "44", "90.0"], ["facial", "Motion-capture Retarget", "Tests full-body mocap retargets without foot sliding or popping.", "Motion-capture Retarget", "mocap", "foot lock held", "52", "56", "90.0"], ["deformation", "Scale Unit Consistency", "Confirms centimeters vs meters agree across DCC and engine.", "Scale Unit Consistency", "unit spec", "1 unit = 1 cm", "1", "1", "100.0"], ["retargeting", "Naming Convention", "Enforces L/R prefixes and namespaces so mirroring and scripts work.", "Naming Convention", "studio naming", "regex pass", "200", "200", "100.0"], ["export", "Twist Bone Setup", "Verifies forearm twist distributes rotation to avoid candy-wrapper collapse.", "Twist Bone Setup", "twist rig", "even distribution", "4", "4", "100.0"], ["skeleton", "Corrective Blendshapes", "Checks pose-space deformers fire to fix collapsing elbows and shoulders.", "Corrective Blendshapes", "PSD", "no collapse", "12", "12", "100.0"], ["facial", "IK/FK Switch", "Tests seamless IK/FK matching with no popping on switch.", "IK/FK Switch", "rig controls", "pop-free", "6", "6", "100.0"], ["deformation", "Root Motion Handling", "Confirms root motion extracts correctly for locomotion systems.", "Root Motion Handling", "game engine", "no sliding", "10", "10", "100.0"], ["retargeting", "Prop Attachment Points", "Validates hand and back sockets for attaching props.", "Prop Attachment Points", "sockets", "aligned", "8", "8", "100.0"], ["export", "Export Validation", "Round-trips through FBX/glTF and verifies nothing is lost.", "Export Validation", "FBX/glTF", "lossless", "1", "1", "100.0"]];
function buildTitle(b){ return SIG?('Signature '+b[1]):b[1]; }
function buildDesc(b){
  var d=b[2]+' Recorded facts \u2014 '+FLD[0][1]+': '+b[3]+'; '+FLD[1][1]+': '+b[4]+'; '+FLD[2][1]+': '+b[5]+'. '+USE;
  if(SIG) d='Signature-original: '+d+' Built as a Signature-authored original for the JAH network; clearly labeled Signature and never presented as a public record.';
  return d;
}
function buildDemo(b){
  return DEMO.split('{title}').join(b[1]).split('{d1}').join(b[6]).split('{d2}').join(b[7]).split('{d3}').join(b[8]);
}
function generate(seed,opts){
  opts=opts||{}; var rnd=prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title=buildTitle(b);
  var fields={}; fields[FLD[0][0]]=b[3]; fields[FLD[1][0]]=b[4]; fields[FLD[2][0]]=b[5];
  if(SIG) fields['signature_label']='Signature-authored original';
  return {id:id,title:title,description:buildDesc(b),category:cat,fields:fields,
    ladder_rank:1+(seed%3),
    demo:'# '+title+' \u2014 runnable demo (python3)\n'+buildDemo(b),
    provenance:'JAH Databases \u00b7 lane N3 build',last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    if(sample[i]&&sample[i].title===rec.title&&sample[i].category===rec.category)
      return {ok:false,errors:['duplicate of archive record '+sample[i].id]};
  }
  return {ok:true,errors:[]};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var idre=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
  if(!idre.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(['public-harvest','signature-generated-completion'].indexOf(r.src)<0)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-digital-human-rig-compatibility-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('digital-human-rig-compatibility',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
