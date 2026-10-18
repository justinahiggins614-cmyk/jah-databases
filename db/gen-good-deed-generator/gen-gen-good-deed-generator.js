(function(){'use strict';
/* JAH The Good Deed Generator Database — REAL generator — "jahdb-gen-good-deed-generator-1.0".
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
var PREFIX="JAH-GOODEEGEN-";
var SRC="public-harvest";
var RECORD_KIND="good deed record";

var FIELDS=["Quick Deeds","Planned Deeds","Big-Hearted Deeds"];
var DEEDS={"Quick Deeds": [{"name": "The Two-Minute Note", "text": "Write a two-minute thank-you note to {who} and leave it {where}.", "slots": {"who": ["a coworker who looks tired", "an elderly neighbor", "a new student at school", "a busy parent at the park", "a cashier having a long day", "a friend you have not called in months", "a teacher", "a nurse", "a bus driver", "a librarian"], "where": ["on their desk", "in their mailbox", "taped to their locker", "on the break-room table", "inside a library book", "on their windshield (kindly!)"]}, "steps": ["Grab any paper and pen — fancy is optional.", "Write one specific thing you appreciate about {who}.", "Sign it, leave it {where}, and walk away smiling."], "time": "2 minutes", "cost": "free"}, {"name": "Compliment Relay", "text": "Give {who} a genuine, specific compliment today, then ask them to pass one on.", "slots": {"who": ["a coworker who looks tired", "an elderly neighbor", "a new student at school", "a busy parent at the park", "a cashier having a long day", "a friend you have not called in months", "a teacher", "a nurse", "a bus driver", "a librarian"]}, "steps": ["Notice one real thing {who} does well.", "Say it plainly: 'I noticed X, and it matters.'", "Ask them to compliment someone else before sundown."], "time": "3 minutes", "cost": "free"}, {"name": "Cart Return Hero", "text": "Return three stray shopping carts to the corral on your next store trip — including ones that are not yours.", "slots": {"who": ["a stranger", "the next shopper"]}, "steps": ["Spot stray carts in the lot.", "Wheel each one to the corral (three is the goal).", "Enjoy the tiny workout and the clear conscience."], "time": "5 minutes", "cost": "free"}, {"name": "Water-Bottle Refill", "text": "Refill the shared water pitcher or the pet bowls at {where}.", "slots": {"where": ["the office kitchen", "the park fountain area", "home"]}, "steps": ["Check the shared water source near you.", "Clean and refill it fully.", "Tell no one. Let someone just find it full."], "time": "4 minutes", "cost": "free"}], "Planned Deeds": [{"name": "The Neighbor Check-In", "text": "Visit {who} this week with {gift} and stay for a real conversation.", "slots": {"who": ["an elderly neighbor", "a new neighbor", "a neighbor living alone"], "gift": ["baked cookies", "extra soup", "a small plant", "a handwritten card"]}, "steps": ["Pick a day and a {gift} to bring.", "Knock, introduce (or reintroduce) yourself warmly.", "Ask one real question and actually listen to the answer.", "Offer one specific help: 'I can carry groceries Tuesdays.'"], "time": "30 minutes", "cost": "a few dollars"}, {"name": "Little Library Restock", "text": "Restock a little free library (or start a give-one box) near {where}.", "slots": {"where": ["your street", "the park", "school", "the community center"]}, "steps": ["Gather 5-10 books you have finished.", "Find the nearest little library or a visible shelf spot.", "Shelve them neatly; leave a kind note inside one.", "Check back next week — restocking is a habit, not an event."], "time": "45 minutes", "cost": "free"}, {"name": "Skill Gift", "text": "Teach {who} one useful skill you have, in a single one-hour session.", "slots": {"who": ["a younger cousin", "a neighbor kid", "a coworker", "a grandparent"]}, "steps": ["Pick one skill you can teach in an hour.", "Invite {who} with a specific time: 'Saturday at 2?'", "Teach slowly; let them do it, not watch you do it.", "End with a tiny certificate or high-five — ceremony matters."], "time": "1 hour", "cost": "free"}], "Big-Hearted Deeds": [{"name": "The Birthday They Would Skip", "text": "Throw a small surprise celebration for {who}, who would otherwise let the day pass quietly.", "slots": {"who": ["a coworker far from family", "an elderly neighbor", "a friend going through a hard year"]}, "steps": ["Quietly confirm the date with one insider.", "Gather 3-6 people and assign tiny jobs (cake, card, music).", "Keep the surprise kind, not startling — gentle reveal.", "Give them the card first; let the room applaud."], "time": "one evening", "cost": "shared cost"}, {"name": "Community Clean Hour", "text": "Organize a one-hour cleanup of {where} with whoever shows up.", "slots": {"where": ["your block", "the park", "the beach", "the schoolyard"]}, "steps": ["Pick a visible spot and a one-hour window.", "Bring spare bags and gloves; invite with a simple flyer.", "Work the full hour together, then take a group photo.", "Thank everyone by name — volunteers return when thanked."], "time": "2 hours", "cost": "bags and gloves"}]};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=DEEDS[field];
  var d=pick(pool,rnd);
  var text=fill(d.text,d.slots,rnd);
  var steps=d.steps.map(function(s,i){return (i+1)+'. '+fill(s,d.slots,rnd);});
  var title='Good deed: '+d.name;
  var body='YOUR GOOD DEED — '+d.name.toUpperCase()+'\n\n'+text+'\n\nHow to do it:\n'+steps.join('\n')
    +'\n\nTime needed: '+d.time+'. Cost: '+d.cost+'. '
    +'Do it today if you can — small kindnesses compound. When it is done, notice how it felt; that feeling is the real reward, and it is why this generator exists.';
  var desc='NEW GOOD DEED (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated good-deed plan. Seeded archive records are the authoritative entries.',
    demo:{kind:'good-deed-plan',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated deed plan.'},
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
var gen={version:"jahdb-gen-good-deed-generator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-good-deed-generator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
