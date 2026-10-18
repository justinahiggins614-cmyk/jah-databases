(function(){'use strict';
/* JAH The Friendship Builder Signature Generator Database — REAL generator — "jahdb-gen-friendship-builder-signature-1.0".
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
var PREFIX="JAH-FRIBUIS-";
var SRC="signature";
var RECORD_KIND="friendship builder record";

var FIELDS=["Friendship Activities","Conversation Decks","Kindness Challenges"];
var ACTIVITIES=[{"name": "The Two-Dollar Challenge", "desc": "Each person gets two dollars (or the local equivalent) and one hour to find the most delightful thing possible.", "steps": ["Hand everyone two dollars.", "Split up for exactly one hour.", "Return and present your find like a museum curator.", "Vote: most delightful wins eternal glory."], "materials": "two dollars per person", "time": "1.5 hours", "group": "2-6 friends"}, {"name": "Cook-Off: Mystery Box", "desc": "Everyone draws three random ingredients and must cook something edible with them.", "steps": ["Fill a box with random pantry ingredients.", "Each cook draws three.", "45 minutes to create a dish.", "Everyone tastes; vote on taste AND bravery."], "materials": "pantry ingredients, basic kitchen", "time": "2 hours", "group": "2-5 friends"}, {"name": "Memory Lane Walk", "desc": "Walk a route full of shared memories; at each stop someone tells the story.", "steps": ["Pick a route with 4-5 meaningful stops.", "At each stop, the person with the best memory tells it.", "Others add details they remember differently.", "End with dessert at the final stop."], "materials": "comfortable shoes", "time": "2-3 hours", "group": "2-8 friends"}, {"name": "Skill Swap Night", "desc": "Everyone teaches the group one small skill in 15 minutes.", "steps": ["Each person picks one teachable skill.", "15 minutes to teach, 5 for questions.", "Rotate until everyone has taught.", "Vote for the skill you will actually keep using."], "materials": "whatever each skill needs", "time": "2 hours", "group": "3-6 friends"}, {"name": "The Gratitude Circle", "desc": "Go around the circle; each person thanks the person to their left with one specific story.", "steps": ["Sit in a circle, phones away.", "Each person thanks the person on their left.", "The thanks must include one specific story.", "No deflecting — receive it graciously."], "materials": "a quiet room", "time": "45 minutes", "group": "3-10 friends"}];
var QUESTIONS=["What is a small thing that always makes your day better?", "What skill do you wish you had learned as a kid?", "What is the best meal you have ever had, and who made it?", "If you could have dinner with anyone, living or not, who would it be?", "What is something you believed as a child that turned out to be gloriously wrong?", "What place have you never been that you dream about visiting?", "What is the kindest thing a stranger has ever done for you?", "What would you do with a completely free Saturday?", "What is a talent you have that most people do not know about?", "What movie or book changed how you see the world?", "What is your favorite memory from the past year?", "What advice would you give your ten-years-ago self?", "What is something you are looking forward to right now?", "What food could you eat every single day?", "What is the bravest thing you have ever done?", "What makes you laugh no matter how bad the day is?", "If you could master any instrument overnight, which one?", "What is a tradition from your family you want to keep?", "What is the most beautiful place you have ever seen?", "What small habit improved your life the most?"];
var CHALLENGES=[{"name": "Seven-Day Compliment Streak", "desc": "Give one genuine, specific compliment to a different person every day for a week.", "steps": ["Pick your seven people (or find them as you go).", "Each compliment must be specific and true.", "Log each one with the date.", "On day seven, notice how people stand taller around you."], "window": "seven days"}, {"name": "The Reconnection Week", "desc": "Contact one old friend you have lost touch with, every day for five days.", "steps": ["List five people you miss.", "Send each a real message — not just 'hey'.", "Mention one specific shared memory.", "Suggest one small concrete plan with at least one of them."], "window": "five days"}, {"name": "Secret Supporter", "desc": "Do three anonymous kind acts for people you know this week.", "steps": ["Pick three people and three small acts.", "Do them without being seen.", "Leave zero evidence it was you.", "Enjoy the mystery — the secret is the point."], "window": "one week"}];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var title,body;
  if(field==="Friendship Activities"){
    var a=pick(ACTIVITIES,rnd);
    var steps=a.steps.map(function(s,i){return (i+1)+'. '+s;});
    title='Friendship activity: '+a.name;
    body='YOUR FRIENDSHIP SESSION\n\nActivity: '+a.name+'\n'+a.desc+'\n\nPlan:\n'+steps.join('\n')
      +'\n\nYou will need: '+a.materials+'. Time: '+a.time+'. Best with '+a.group+'. '
      +'Then open the conversation deck below — three cards, everyone answers.\n\nConversation cards:\n'
      +shuffle(QUESTIONS,rnd).slice(0,3).map(function(q,i){return 'Card '+(i+1)+': '+q;}).join('\n');
  }else if(field==="Conversation Decks"){
    var cards=shuffle(QUESTIONS,rnd).slice(0,5);
    title='Conversation deck ('+cards.length+' cards)';
    body='YOUR CONVERSATION DECK — deal one card at a time, everyone answers before moving on.\n\n'
      +cards.map(function(q,i){return 'Card '+(i+1)+': '+q;}).join('\n')
      +'\n\nHouse rule: no deflecting with "what about you?" until you have answered yourself. The deck works because the questions do the asking for you.';
  }else{
    var c=pick(CHALLENGES,rnd);
    var steps=c.steps.map(function(s,i){return (i+1)+'. '+s;});
    title='Kindness challenge: '+c.name;
    body='YOUR KINDNESS CHALLENGE — '+c.name.toUpperCase()+'\n\n'+c.desc+'\n\nSteps:\n'+steps.join('\n')
      +'\n\nComplete it within '+c.window+'. Tell one person you did it — not to brag, but because kindness told is kindness multiplied.';
  }
  var desc='NEW FRIENDSHIP BUILDER SESSION (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated friendship session. Seeded archive records are the authoritative entries.',
    demo:{kind:'friendship-session',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated session.'},
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
var gen={version:"jahdb-gen-friendship-builder-signature-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-friendship-builder-signature",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
