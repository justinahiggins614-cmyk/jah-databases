(function(){'use strict';
/* JAH The Volunteering Database generator — jahdb-volunteering-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VLNT-";
var FIELDS=["Finding Your Cause","Hunger & Homelessness","Kids & Education","Environment","Animals","Seniors & Neighbors","Skilled & Virtual Volunteering"];
var TOPICS={
 "Finding Your Cause": [
  "Finding the Cause That Fits You - Finding Your Cause",
  "Volunteer Rights and Expectations - Finding Your Cause",
  "Volunteering With Your Family - Finding Your Cause",
  "Corporate and Group Volunteering - Finding Your Cause",
  "Measuring Your Volunteer Impact - Finding Your Cause"
 ],
 "Hunger & Homelessness": [
  "Food Banks: Sorting, Packing, and Distributing - Hunger & Homelessness",
  "Soup Kitchens and Meal Service - Hunger & Homelessness",
  "Homeless Outreach: What Actually Helps - Hunger & Homelessness",
  "Food Rescue and Gleaning - Hunger & Homelessness",
  "Fundraising for Hunger Causes - Hunger & Homelessness"
 ],
 "Kids & Education": [
  "Tutoring and Mentoring Youth - Kids & Education",
  "Coaching Youth Sports and Activities - Kids & Education",
  "School Volunteering: Classrooms and Libraries - Kids & Education",
  "Big Brothers Big Sisters and Formal Mentoring - Kids & Education",
  "After-School Programs and Summer Camps - Kids & Education"
 ],
 "Environment": [
  "Park and Trail Cleanups - Environment",
  "Tree Planting and Habitat Restoration - Environment",
  "Community Gardens - Environment",
  "Wildlife Monitoring and Citizen Science - Environment",
  "Advocacy: Environmental Policy Volunteering - Environment"
 ],
 "Animals": [
  "Animal Shelter Volunteering - Animals",
  "Fostering Animals - Animals",
  "Wildlife Rehabilitation Support - Animals",
  "Spay/Neuter and TNR Programs - Animals"
 ],
 "Seniors & Neighbors": [
  "Visiting Isolated Seniors - Seniors & Neighbors",
  "Meals on Wheels and Senior Nutrition - Seniors & Neighbors",
  "Helping Neighbors in Need - Seniors & Neighbors",
  "Senior Centers and Activity Programs - Seniors & Neighbors"
 ],
 "Skilled & Virtual Volunteering": [
  "Skills-Based Volunteering: Pro Bono Power - Skilled & Virtual Volunteering",
  "Virtual Volunteering From Home - Skilled & Virtual Volunteering",
  "Crisis Lines and Emotional Support - Skilled & Virtual Volunteering",
  "Board Service for Nonprofits - Skilled & Virtual Volunteering",
  "Starting Your Own Volunteer Project - Skilled & Virtual Volunteering",
  "The Lifetime Volunteer: Sustaining Service for Decades - Skilled & Virtual Volunteering"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Volunteering Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — volunteering guide record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A volunteering guide record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"volunteering-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-volunteering-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('volunteering',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
