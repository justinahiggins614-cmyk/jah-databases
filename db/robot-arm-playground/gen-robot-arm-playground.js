(function(){'use strict';
/* JAH The Robot Arm Playground generator — jahdb-robot-arm-playground-1.0.
   Property of Justin Addam Higgins (JAH).
   A REAL working robot-arm designer: every call designs an original arm concept —
   name, lane, segment plan with joint types, degrees of freedom, end effector,
   payload and reach specs, control notes — and renders an arm diagram SVG.
   Deterministic per seed: same seed, same arm. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pickN(r,s,n){var c=r.slice(),o=[];for(var i=0;i<n&&c.length;i++){o.push(c.splice((s()*c.length)|0,1)[0]);}return o;}
var PREFIX="JAH-RBAP-";
var FIELDS=["Desktop Maker Arm","Industrial Helper","Expressive Performer"];
var NAME_A=["Tinker","Atlas","Wren","Pivot","Juno","Cog","Mira","Axle","Nova","Gimbal"];
var NAME_B=["Arm","MK-II","Hand","Rig","Crane","Limb","Helper","Dancer","Builder","Scout"];
var JOINTS=["revolute base yaw","shoulder pitch","shoulder roll","elbow pitch","elbow roll","wrist pitch","wrist roll","tool flange rotate"];
var EFFECTOR={"Desktop Maker Arm":"magnetic quick-swap toolhead (pen, gripper, solder)","Industrial Helper":"vacuum gripper with force feedback","Expressive Performer":"soft silicone hand, five compliant fingers"};
var SPEC={"Desktop Maker Arm":{dof:5,payload:"0.5 kg",reach:"62 cm"},"Industrial Helper":{dof:6,payload:"8 kg",reach:"140 cm"},"Expressive Performer":{dof:7,payload:"1.2 kg",reach:"95 cm"}};
var CONTROL=["teach-pendant jogging","drag-to-teach waypoints","Python SDK scripting","safety-rated monitored stop"];
function armSVG(dof,name){
  var segs='',x=70,y=190,ang=-55;
  for(var i=0;i<dof;i++){
    var len=52-(i*3), nx=x+len*Math.cos(ang*Math.PI/180), ny=y+len*Math.sin(ang*Math.PI/180);
    segs+='<line x1="'+x+'" y1="'+y+'" x2="'+nx+'" y2="'+ny+'" stroke="#2B2D42" stroke-width="12" stroke-linecap="round"/>';
    segs+='<circle cx="'+x+'" cy="'+y+'" r="10" fill="#C8102E"/>';
    x=nx;y=ny;ang+=18;
  }
  segs+='<circle cx="'+x+'" cy="'+y+'" r="10" fill="#C8102E"/><rect x="'+(x-4)+'" y="'+(y-26)+'" width="26" height="22" rx="4" fill="#F7C548" stroke="#222"/>';
  return '<svg xmlns="http://www.w3.org/2000/svg" width="420" height="280" viewBox="0 0 420 280">'
  +'<rect width="420" height="280" fill="#FFFFFF"/>'
  +'<rect x="40" y="190" width="60" height="50" rx="8" fill="#8A8D93"/>'+segs
  +'<text x="210" y="268" font-family="Georgia,serif" font-size="15" font-weight="bold" text-anchor="middle" fill="#1A1A1A">'+name+' — '+dof+' DOF</text></svg>';
}
function generate(seed,opts){
  opts=opts||{}; var s=prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,s);
  var name=pick(NAME_A,s)+" "+pick(NAME_B,s);
  var spec=SPEC[field], joints=pickN(JOINTS,s,spec.dof), ctrl=pickN(CONTROL,s,2);
  var svg=armSVG(spec.dof,name);
  var title=name+" — "+field+" — seed "+seed;
  var desc='GENERATED ROBOT ARM — the '+name+', a '+field.toLowerCase()+'. '+spec.dof+' degrees of freedom ('+joints.join(', ')+'). End effector: '+EFFECTOR[field]+'. Payload '+spec.payload+', reach '+spec.reach+'. Control: '+ctrl.join(' + ')+'.';
  var prog="# Robot arm concept — "+name+" (seed "+seed+")\n"
    +"name = \""+name+"\"\n"+"lane = \""+field+"\"\n"+"dof = "+spec.dof+"\n"
    +"joints = "+JSON.stringify(joints)+"\n"+"effector = \""+EFFECTOR[field]+"\"\n"
    +"payload = \""+spec.payload+"\"\n"+"reach = \""+spec.reach+"\"\n"+"control = "+JSON.stringify(ctrl)+"\n"
    +"print(\"Arm:\", name, \"[\"+lane+\"]\", dof, \"DOF\")\n"
    +"[print(\" Joint %d: %s\" % (i+1, j)) for i, j in enumerate(joints)]\n"
    +"print(\"Effector:\", effector)\n"+"print(\"Payload:\", payload, \"| Reach:\", reach)\n"
    +"print(\"Control:\", \", \".join(control))\n"+"print(\"Diagram SVG bytes:\", "+svg.length+")\n";
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — arm record', title:title, description:desc,
    how_it_works:'The generator names an original arm, assigns the lane, reads its DOF/payload/reach spec, draws that many joint types without replacement, reads the lane\u2019s end effector, picks two control modes, and renders a jointed arm diagram SVG — deterministic per seed.',
    key_points:['Arm: '+name,'Lane: '+field,'DOF: '+spec.dof,'Joints: '+joints.join(', '),'Effector: '+EFFECTOR[field],'Payload: '+spec.payload+', Reach: '+spec.reach,'Control: '+ctrl.join(' + '),'Deterministic: seed '+seed+' always rebuilds this exact arm.'],
    requirements:['A seed number to regenerate this exact arm','An HTML file to view the diagram SVG'],
    standards:['Joint count matches the lane DOF','End effector specified per lane','Payload and reach in the spec block'],
    citations:['Robotics craft references: arm kinematics.','Design references: concept diagramming.'],
    field:field, src:'signature-generated-sample', sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    output:{arm:name,lane:field,dof:spec.dof,joints:joints,effector:EFFECTOR[field],payload:spec.payload,reach:spec.reach,control:ctrl,svg:svg},
    svg:svg,
    demo:{kind:'arm-plan',language:'python',program:prog,note:'Prints the arm spec: joints, effector, payload, reach.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  var o=r.output||{};
  if(!o.arm||!o.effector)e.push('design');
  if(!o.joints||o.joints.length!==o.dof)e.push('joints');
  if(!o.payload||!o.reach)e.push('specs');
  if(!o.svg||o.svg.indexOf('<svg')!==0)e.push('svg');
  if(!r.demo||!r.demo.program)e.push('demo');
  if(!r.key_points||!r.key_points.length)e.push('key_points');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate arm in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-robot-arm-playground-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('robot-arm-playground',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();