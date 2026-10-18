(function(){'use strict';
/* JAH The Celebration Message Generator Database — REAL generator — "jahdb-gen-celebration-message-1.0".
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same output. Every run produces a genuine,
   fully-formed new item — never a structural sample. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,s){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(s()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
function fill(t,slots,s){var out=t;Object.keys(slots).forEach(function(k){out=out.split('{'+k+'}').join(pick(slots[k],s));});return out;}
function pyDemo(title,text){
  var t=String(text).replace(/\\/g,'\\\\').replace(/"""/g,'\\"\\"\\"');
  var h=String(title).replace(/[\r\n]+/g,' ').slice(0,120);
  return '# '+h+'\n# Property of Justin Addam Higgins (JAH).\n'
    + 'ITEM = """'+t+'"""\n'
    + 'print(ITEM)\n'
    + 'assert len(ITEM) > 40, "empty generated item"\n'
    + 'assert "{" not in ITEM, "unfilled slot in generated item"\n'
    + 'print("generated_chars=%d" % len(ITEM))\n'
    + 'print("DEMO OK")\n';
}
var PREFIX="JAH-CELMES-";
var SRC="public-harvest";
var RECORD_KIND="celebration message record";

var FIELDS=["Birthday", "Graduation", "New Job", "New Home", "Wedding", "New Baby", "Retirement", "Thank You", "Get Well", "Congratulations"];
var RELS=["friend","sister","brother","mom","dad","partner","coworker","neighbor","grandparent","child","cousin","mentor"];
var NAMES=["Alex","Jordan","Taylor","Sam","Riley","Casey","Jamie","Morgan","Avery","Quinn","Drew","Robin"];
var TPL={"Birthday": ["Happy birthday, {name}! Another year of you being exactly the wonderful {rel} you are — I hope this one brings you everything you quietly wished for.", "{name}, happy birthday! You make being a {rel} look easy and being a human look fun. Cake first, wishes second, regrets never.", "To {name} on your birthday: may your year be as generous as you are to everyone lucky enough to call you {rel}. Eat something delicious today."], "Graduation": ["{name}, you did it! All those late nights just turned into a diploma. Proud does not even cover it — your {rel} is cheering the loudest.", "Congratulations, graduate! {name}, watching you work for this as your {rel} has been the honor. Now go use that big brain on something wonderful."], "New Job": ["Congratulations on the new job, {name}! They have no idea how lucky they are. Your {rel} knew all along — go show them.", "{name}, first day nerves are just excitement in disguise. You earned this. Your {rel} believes in you completely."], "New Home": ["Happy new home, {name}! May the walls hold laughter, the kitchen hold good smells, and the {rel} visits be frequent.", "{name}, a new home is a new chapter with better lighting. Congratulations from your {rel} — I am bringing snacks to the housewarming."], "Wedding": ["{name}, wishing you a marriage as joyful as this wedding day. Your {rel} is so happy to celebrate two wonderful people becoming one team.", "Congratulations, {name}! Love chose well. As your {rel}, I promise excellent wedding cake opinions and lifelong cheering."], "New Baby": ["Welcome to the world, little one — and congratulations, {name}! Your {rel} is over the moon. Sleep now; the baby years fly.", "{name}, you are going to be an amazing parent. Your {rel} already knows it. Congratulations on the beautiful new arrival!"], "Retirement": ["Happy retirement, {name}! You spent years making work better for everyone — now the calendar is yours. Your {rel} suggests naps first, adventures second.", "{name}, retirement looks good on you already. Congratulations from your {rel} — every Monday is now a Saturday."], "Thank You": ["{name}, thank you — truly. What you did meant more than you know, and your {rel} will not forget it.", "Just a note to say thank you, {name}. People like you are why people like me keep believing in people. Gratefully, your {rel}."], "Get Well": ["Get well soon, {name}! Rest up and let people fuss over you for once. Your {rel} is sending all the healing vibes and zero chores.", "Healing thoughts headed your way, {name}. Take it slow, take it easy — your {rel} has everything else covered."], "Congratulations": ["Congratulations, {name}! Big news deserves big cheers, and your {rel} is cheering the biggest. Savor this — you earned every bit.", "You did it, {name}! Congratulations from your {rel}, who is not even slightly surprised and enormously proud."]};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var tpls=TPL[field];
  var t=pick(tpls,rnd);
  var msg=fill(t,{name:pick(NAMES,rnd),rel:pick(RELS,rnd)},rnd);
  var title=field+' message for '+msg.split(' ')[0].replace(/[^A-Za-z]/g,'');
  var body='YOUR CELEBRATION MESSAGE — '+field.toUpperCase()+'\n\n'+msg+'\n\nCopy it as-is, or swap in the real name and one personal detail (an inside joke, a shared memory) to make it unmistakably yours. Handwritten beats typed; spoken beats texted.';
  var desc='NEW CELEBRATION MESSAGE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated message — personalize with a real name and detail before sending. Seeded archive records are the authoritative entries.',
    demo:{kind:'celebration-message',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated message.'},
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
  if(!r.description||r.description.length<40)e.push('description');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:"jahdb-gen-celebration-message-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-celebration-message",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
