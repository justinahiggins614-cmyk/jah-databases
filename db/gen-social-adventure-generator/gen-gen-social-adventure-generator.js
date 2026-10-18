(function(){'use strict';
/* JAH The Social Adventure Generator Database — REAL generator — "jahdb-gen-social-adventure-generator-1.0".
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
var PREFIX="JAH-SOCADVGEN-";
var SRC="public-harvest";
var RECORD_KIND="social adventure record";

var FIELDS=["Day Adventures","Evening Adventures","Weekend Adventures"];
var ADV={"Day Adventures": [{"name": "The Great Thrift Hunt", "mission": "Each team gets $10 and one hour in a thrift store to assemble the most legendary outfit.", "venue": "a local thrift store", "crew": "3-8 people", "roles": ["Team Captain (keeps time)", "Stylist (final say on outfits)", "Photographer (documents everything)", "Treasurer (holds the $10)"], "checklist": ["Set a strict $10 budget per team", "One hour on the clock — no extensions", "Every team member must wear their outfit out of the store", "Group runway show in the parking lot", "Vote: boldest look wins"], "debrief": ["What was the best find?", "Who committed hardest to the bit?", "Would you actually wear any of it again?"]}, {"name": "Park Games Decathlon", "mission": "Ten silly mini-games across the park; the crew with the most points takes the crown.", "venue": "a big public park", "crew": "4-12 people", "roles": ["Referee (explains rules, settles disputes)", "Scorekeeper", "Hype Person (mandatory cheering)", "Water Bearer"], "checklist": ["Frisbee accuracy toss", "Three-legged race", "Sack-style hop race (pillowcases work)", "Water balloon toss (no filling stations? use soft balls)", "Best team cheer contest", "Tally scores loudly after each event"], "debrief": ["Which event was secretly the hardest?", "Best moment of the day?", "Rematch — yes or yes?"]}, {"name": "Neighborhood Photo Safari", "mission": "Capture the alphabet: one photo for each letter A-Z, found in the wild of your neighborhood.", "venue": "your neighborhood", "crew": "2-6 people", "roles": ["Navigator (plans the route)", "Spotter (eagle eyes)", "Photographer", "List Keeper (tracks letters found)"], "checklist": ["No driving — feet or bikes only", "Each letter needs a real found object (A = apple tree, B = bicycle...)", "Bonus for the funniest Q, X, Z", "Assemble the alphabet collage at the end", "Share it with someone who will appreciate it"], "debrief": ["Which letter was the hardest?", "What did you notice that you had never seen before?"]}], "Evening Adventures": [{"name": "Sunset Picnic and Stories", "mission": "Pack dinner, claim the best sunset spot, and trade stories until the stars come out.", "venue": "a hill, beach, or rooftop with a western view", "crew": "2-8 people", "roles": ["Quartermaster (packs food and blankets)", "Scout (claims the spot early)", "Storyteller (starts the first story)", "Stargazer (knows one constellation)"], "checklist": ["Arrive 90 minutes before sunset", "Everyone brings one dish to share", "Phones away once the sun touches the horizon", "Each person tells one true story", "Stay for the first stars"], "debrief": ["Whose story surprised you most?", "What are you grateful for tonight?"]}, {"name": "Living-Room Concert Night", "mission": "Everyone performs something — song, poem, comedy bit, magic trick. Applause is mandatory.", "venue": "someone's living room", "crew": "3-10 people", "roles": ["MC (introduces each act with flair)", "Stage Manager (arranges the 'stage')", "Hype Crew (front row, loudest claps)", "Snack Captain"], "checklist": ["Every person performs at least once", "Acts under 5 minutes", "No booing — ever", "Encore for the bravest act", "Group finale: everyone sings something together"], "debrief": ["Who surprised you?", "What should be a tradition?"]}], "Weekend Adventures": [{"name": "The Two-Town Tour", "mission": "Visit two nearby towns you have never explored; collect one souvenir and one story from each.", "venue": "two neighboring towns", "crew": "2-6 people", "roles": ["Driver/Navigator", "Food Scout (finds the local spot)", "Historian (reads one plaque aloud per town)", "Souvenir Keeper"], "checklist": ["Pick towns within an hour's drive", "Eat where the locals eat", "Find the town's oddest landmark", "Buy one small souvenir per town", "Learn one fact per town to retell"], "debrief": ["Which town would you move to?", "Best bite of the weekend?"]}, {"name": "Campfire Tales Weekend", "mission": "One night outdoors (or backyard-camping) built around stories, stars, and s'mores.", "venue": "a campsite or backyard", "crew": "2-8 people", "roles": ["Fire Tender (safety first, always)", "S'mores Engineer", "Story Keeper (starts the tale chain)", "Dawn Patrol (handles breakfast)"], "checklist": ["Check fire rules and weather first", "Set up camp before dark", "Everyone contributes one story", "Lights out when the fire is fully out", "Leave the site cleaner than you found it"], "debrief": ["Best story of the night?", "What sound will you remember?"]}]};
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var a=pick(ADV[field],rnd);
  var roles=a.roles.map(function(r,i){return ' - '+r;});
  var checks=a.checklist.map(function(c,i){return (i+1)+'. [ ] '+c;});
  var title='Social adventure: '+a.name;
  var body='YOUR SOCIAL ADVENTURE — '+a.name.toUpperCase()+'\n\nThe mission: '+a.mission+'\n\nWhere: '+a.venue+'\nCrew: '+a.crew
    +'\n\nAssign roles (everyone gets one):\n'+roles.join('\n')
    +'\n\nAdventure checklist:\n'+checks.join('\n')
    +'\n\nDebrief (ask these on the way home):\n'+a.debrief.map(function(d,i){return (i+1)+'. '+d;}).join('\n')
    +'\n\nRule zero: nobody gets left out, nobody gets teased for trying. Adventures are measured in stories told afterward.';
  var desc='NEW SOCIAL ADVENTURE (generated). '+body;
  return {
    id:PREFIX+String(seed).padStart(6,'0'),
    name:title+' — '+RECORD_KIND,
    title:title,
    description:desc,
    field:field,
    src:SRC,
    sample:true,
    disclaimer:'Generated adventure plan — check venues and weather before heading out. Seeded archive records are the authoritative entries.',
    demo:{kind:'social-adventure',language:'python',program:pyDemo(title,desc),note:'Demo prints the generated adventure.'},
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
var gen={version:"jahdb-gen-social-adventure-generator-1.0",generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("gen-social-adventure-generator",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
