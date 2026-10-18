(function(){'use strict';
/* JAH The Thank-You Note Creator Generator Database — REAL generator — "jahdb-gen-thank-you-note-creator-1.0".
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
var PREFIX="JAH-THAYOUNOT-";
var SRC="public-harvest";
var RECORD_KIND="thank-you note record";

var FIELDS=["For a Gift","For Help","For Hospitality","For Kind Words","For an Opportunity"];
var NAMES=["Alex","Jordan","Taylor","Sam","Riley","Casey","Jamie","Morgan","Avery","Quinn"];
var TPL={"For a Gift": ["Dear {name}, thank you so much for the beautiful book. It was thoughtful, perfect, and so very you. I thought of you the moment I opened it, and I have smiled about it every day since. With gratitude, your friend.", "Dear {name}, thank you so much for the handmade scarf. It was thoughtful, perfect, and so very you. I thought of you the moment I opened it, and I have smiled about it every day since. With gratitude, your friend.", "{name}, the beautiful book made my whole week. Thank you for knowing me so well — that is the real gift. I am lucky to have you in my life.", "{name}, the handmade scarf made my whole week. Thank you for knowing me so well — that is the real gift. I am lucky to have you in my life."], "For Help": ["Dear {name}, thank you for stepping in with the move when I needed it most. You made something hard feel manageable, and I will not forget it. I owe you one — and I mean that happily.", "Dear {name}, thank you for stepping in with the big project when I needed it most. You made something hard feel manageable, and I will not forget it. I owe you one — and I mean that happily.", "{name}, your help with the move saved the day. Thank you for giving your time so generously. People like you make hard weeks survivable.", "{name}, your help with the big project saved the day. Thank you for giving your time so generously. People like you make hard weeks survivable."], "For Hospitality": ["Dear {name}, thank you for the wonderful dinner party. Your home felt like a hug, the food was perfect, and the company was even better. Let me return the favor soon — my place, my cooking (be brave).", "Dear {name}, thank you for the wonderful weekend stay. Your home felt like a hug, the food was perfect, and the company was even better. Let me return the favor soon — my place, my cooking (be brave).", "{name}, thank you for dinner party. I left feeling rested, fed, and reminded how lucky I am to know you. Hospitality like yours is a gift.", "{name}, thank you for weekend stay. I left feeling rested, fed, and reminded how lucky I am to know you. Hospitality like yours is a gift."], "For Kind Words": ["Dear {name}, your encouraging letter arrived exactly when I needed to hear it. Thank you for saying the true thing kindly. I have kept your words close all week.", "Dear {name}, your kind message arrived exactly when I needed to hear it. Thank you for saying the true thing kindly. I have kept your words close all week.", "{name}, thank you for encouraging letter. Encouragement from you carries weight, and it lifted me more than you know.", "{name}, thank you for kind message. Encouragement from you carries weight, and it lifted me more than you know."], "For an Opportunity": ["Dear {name}, thank you for trusting me with the interview. I will work hard to be worthy of the chance. Your belief in me means everything.", "Dear {name}, thank you for trusting me with the introduction. I will work hard to be worthy of the chance. Your belief in me means everything.", "{name}, thank you for opening the door to the interview. Opportunities like this change trajectories, and I am deeply grateful you thought of me.", "{name}, thank you for opening the door to the introduction. Opportunities like this change trajectories, and I am deeply grateful you thought of me."]};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var tpls=TPL[field];
  var t=pick(tpls,rnd);
  var note=fill(t,{name:pick(NAMES,rnd)},rnd);
  var title='Thank-you note ('+field.toLowerCase()+')';
  var body='YOUR THANK-YOU NOTE\n\n'+note+'\n\nThe anatomy of a note that lands: name the thing, name the feeling, name the future. Replace the sample name with the real one, add one specific detail only you would know, and send it within a week — late gratitude still counts.';
  var desc='NEW THANK-YOU NOTE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated note — personalize before sending. Seeded archive records are the authoritative entries.',
    demo:{kind:'thank-you-note',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated note.'},
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
var gen={version:"jahdb-gen-thank-you-note-creator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-thank-you-note-creator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
