(function(){'use strict';
/* JAH Tai Chi Combat Database generator — jahdb-combat-tai-chi-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CBTC-";
var FIELDS=["Foundations","The Eight Gates","The Five Steps","Short Form Postures","Push Hands","Advanced Study"];
var TOPICS={
 "Foundations": [
  "Wuji Stance: The Neutral Standing Posture - Foundations",
  "Bow Stance (Gong Bu): The Forward Fighting Stance - Foundations",
  "Horse Stance (Ma Bu): The Sitting Stance - Foundations",
  "Empty Stance (Xu Bu): The Cat Stance - Foundations",
  "Tai Chi Walk: Advancing Without Telegraphing - Foundations",
  "Silk Reeling (Chan Si Jin): The Spiraling Engine - Foundations",
  "Peng (Ward Off): The First of the Eight Gates - Foundations",
  "Lu (Roll Back): The Second of the Eight Gates - Foundations",
  "Ji (Press): The Third of the Eight Gates - Foundations",
  "An (Push): The Fourth of the Eight Gates - Foundations",
 ],
 "The Eight Gates": [
  "Cai (Pluck): The Fifth of the Eight Gates - The Eight Gates",
  "Lie (Split): The Sixth of the Eight Gates - The Eight Gates",
  "Zhou (Elbow): The Seventh of the Eight Gates - The Eight Gates",
  "Kao (Shoulder Strike): The Eighth of the Eight Gates - The Eight Gates",
 ],
 "The Five Steps": [
  "Jin Bu (Advance): Stepping Forward - The Five Steps",
  "Tui Bu (Retreat): Stepping Back - The Five Steps",
  "Zuo Gu (Look Left): Guarding the Left - The Five Steps",
  "You Pan (Look Right): Guarding the Right - The Five Steps",
  "Zhong Ding (Central Equilibrium): The Fifth Step - The Five Steps",
 ],
 "Short Form Postures": [
  "Commencement (Qi Shi): The Opening Posture - Short Form Postures",
  "Grasp the Sparrow's Tail: Four Gates in One Sequence - Short Form Postures",
  "Single Whip (Dan Bian): The Signature Posture - Short Form Postures",
  "White Crane Spreads Wings (Bai He Liang Chi) - Short Form Postures",
  "Brush Knee and Twist Step (Lou Xi Ao Bu) - Short Form Postures",
  "Part the Wild Horse's Mane (Ye Ma Fen Zong) - Short Form Postures",
  "Repulse Monkey (Dao Juan Gong): Retreating Strikes - Short Form Postures",
  "Wave Hands Like Clouds (Yun Shou): The Turning Flow - Short Form Postures",
  "Needle at Sea Bottom (Hai Di Zhen): The Low Strike - Short Form Postures",
 ],
 "Push Hands": [
  "Tui Shou Basics: Single-Hand Fixed-Step Push Hands - Push Hands",
  "Tui Shou: Double-Hand Fixed Step and the Four-Gate Cycle - Push Hands",
  "Tui Shou: Moving-Step (Huo Bu) Push Hands - Push Hands",
 ],
 "Advanced Study": [
  "Martial Applications: Combat Reading of the Postures - Advanced Study",
  "Fair Lady Works at the Shuttles (Yu Nu Chuan Suo): Corners of the Form - Advanced Study",
  "Dan Tian Breathing: Combat Breath for Tai Chi Power - Advanced Study",
 ],
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\n"
   + '"""Tai Chi Technique Study: "+safe+" ['+field+"] - working sample demo.\n"
   + 'Property of Justin Addam Higgins (JAH)."""\n'
   + "GATES=['peng','lu','ji','an','cai','lie','zhou','kao']\n"
   + "STEPS=['jin bu','tui bu','zuo gu','you pan','zhong ding']\n"
   + "def main():\n"
   + "    print('sample study: '+\""+safe+"\")\n"
   + "    print('field: '+\""+field+"\")\n"
   + "    print('eight gates:', ', '.join(GATES))\n"
   + "    print('five steps:', ', '.join(STEPS))\n"
   + "    print('Sample record - structural sample, not an archive entry.')\n"
   + "if __name__=='__main__':\n"
   + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — combat technique record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A combat technique record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"tai-chi-technique-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-combat-tai-chi-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('combat-tai-chi',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
