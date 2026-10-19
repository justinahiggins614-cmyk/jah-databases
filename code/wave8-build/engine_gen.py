#!/usr/bin/env python3
"""JS generator scripts for wave 8. Each db/<slug>/gen-<slug>.js:
 - deterministic seeded generator (generate/validate/driftCheck) like canon
 - for GENERATOR-class items: a REAL working client-side builder: BUILDER_FIELDS
   (form spec) + build(inputs) producing genuine outputs.
Property of Justin Addam Higgins (JAH)."""
import json, subprocess, os

JS_HEAD = """(function(){'use strict';
/* __GENNAME__ — __GENVER__.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;var t=a[i];a[i]=a[j];a[j]=t;}return a;}
"""

JS_TAIL = """
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\\\-')+'\\\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
__BUILDER_EXPORT__
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('__SLUG__',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();"""

def js_str(s):
    return json.dumps(s)

def build_gen_js(item, slug, sig):
    """Returns JS source for gen-<slug>.js."""
    prefix = item['prefix_sig'] if sig else item['prefix']
    genname = ('The %s Signature generator' % item['name']) if sig else ('The %s generator' % item['name'])
    genver = 'jahdb-%s-%s-1.0' % (slug, 'sig' if sig else 'pub')
    fields = item['fields']
    topics = {}
    for tier_i, title, blurb in item['topics']:
        topics.setdefault(fields[tier_i], []).append(title)
    lines = [JS_HEAD.replace('__GENNAME__', genname).replace('__GENVER__', genver)]
    lines.append('var PREFIX=%s;' % js_str(prefix))
    lines.append('var GENVER=%s;' % js_str(genver))
    lines.append('var FIELDS=%s;' % js_str(fields))
    lines.append('var TOPICS=%s;' % json.dumps(topics, indent=1))
    lines.append('var BLURBS=%s;' % json.dumps({t: b for _, t, b in item['topics']}, indent=1))
    # demo program builder (python, deterministic)
    lines.append(r"""
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  var h=0;for(var i=0;i<safe.length;i++){h=(h*31+safe.charCodeAt(i))>>>0;}
  var steps=['Prepare the space','Gather the essentials','Do the core work','Review the result','Lock in the win'];
  var out='# '+safe+' — working demo\n# Field: '+field+'\n';
  out+='steps = '+JSON.stringify(steps)+'\n';
  out+='for i, s in enumerate(steps, 1):\n    print(f"{i}. {s}")\n';
  out+='print("Seed '+h+': repeat the steps in order and the result compounds.")\n';
  return out;
}""")
    lines.append(r"""
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||['General Study'];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — __KIND__',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). '+ (BLURBS[topic]||('A '+field+' study of "'+topic+'".')) +' Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:'sample-demo',language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}""".replace('__KIND__', item['kind']))
    builder_export = ''
    if item.get('builder'):
        bid, _btitle, _bdesc, bfields = item['builder']
        builder_export = ('gen.builderId=%s;\ngen.builderFields=%s;\ngen.build=%s;\n'
                          % (js_str(bid), json.dumps(bfields), 'BUILD_' + bid.upper().replace('-', '_')))
        lines.append(BUILDERS[bid])
    tail = (JS_TAIL.replace('__BUILDER_EXPORT__', builder_export)
                   .replace('__SLUG__', slug))
    lines.append(tail)
    return '\n'.join(lines)

# ------------------------------------------------------------------ builders
# Each BUILD_<ID>(inputs) returns {title, intro, sections:[{h, items:[...] or text}]}
BUILDERS = {}

BUILDERS['room-theme'] = r"""
var BUILD_ROOM_THEME=(function(){
var PALETTES={calm:[['#2b3a55','deep slate'],['#7fa6a3','sea mist'],['#e8e0d0','warm linen']],warm:[['#5b3a29','cocoa'],['#c98a5e','terracotta'],['#f2e3c6','sand']],bold:[['#1d1d2f','midnight'],['#e63946','signal red'],['#f1fa8c','neon lime']],forest:[['#22331f','pine'],['#5c7a4d','moss'],['#d9c9a3','straw']]};
var LAYOUTS=['Bed against the longest wall, desk by the window for daylight.','Bed in the corner nook, open floor kept clear for movement.','Bed centered as the anchor, zones split by a rug, not walls.'];
var LIGHT=['Warm 2700K bedside lamp for wind-down.','String lights along the headboard for soft glow.','One bright daylight bulb at the desk for focus work.'];
return function(inp){
  var r=prng(inp.seed||7);
  var pal=pick(Object.keys(PALETTES),r);
  var cols=PALETTES[pal];
  var budget=parseInt(inp.budget,10)||300;
  var parts=[['Bedding + textiles',0.35],['Lighting',0.2],['Wall decor + art',0.2],['Storage + organizers',0.15],['Plants + finishing',0.1]];
  var sections=[
    {h:'Palette — '+pal+' theme',items:cols.map(function(c){return c[1]+' ('+c[0]+')';})},
    {h:'Layout for a '+inp.size+' room',text:pick(LAYOUTS,r)+' Keep walkways at least 60cm wide so the room breathes.'},
    {h:'Lighting plan',items:shuffle(LIGHT,r).slice(0,2)},
    {h:'Budget split — $'+budget,items:parts.map(function(p){return p[0]+': $'+Math.round(budget*p[1]);})},
    {h:'First three buys',items:['A textile that sets the mood (throw, rug, or curtains).','The one light you will use every night.','Storage that hides the mess you actually make.']}
  ];
  return {title:'Dream bedroom studio: '+inp.style+' theme',intro:'A complete '+inp.style+' bedroom plan for a '+inp.size+' space on about $'+budget+'.',sections:sections};
};})();"""

BUILDERS['routine'] = r"""
var BUILD_ROUTINE=(function(){
return function(inp){
  var wake=inp.wake||'07:00', sleep=inp.sleep||'23:00';
  function mins(t){var p=t.split(':');return (+p[0])*60+(+p[1]);}
  function fmt(m){m=((m%1440)+1440)%1440;var h=(m/60)|0,mm=m%60;return (h<10?'0':'')+h+':'+(mm<10?'0':'')+mm;}
  var w=mins(wake), s=mins(sleep); if(s<=w)s+=1440;
  var day=s-w, focusH=parseFloat(inp.focus)||2;
  var blocks=[
    ['Wake + light + water', 20],
    ['Move (walk, stretch, or workout)', 30],
    ['Deep focus block 1', Math.round(focusH*60/2)],
    ['Lunch + true break (no screens ideally)', 45],
    ['Deep focus block 2', Math.round(focusH*60/2)],
    ['Errands / life admin', 30],
    ['Wind-down: dim lights, prep tomorrow', 30]
  ];
  var t=w, items=blocks.map(function(b){var o=fmt(t)+' – '+b[0]+' ('+b[1]+' min)';t+=b[1];return o;});
  items.push(fmt(s-30)+' – In bed, screens off');
  return {title:'Personal routine: '+wake+' to '+sleep,
    intro:'A flexible day built around '+focusH+' focused hours across a '+Math.round(day/60)+'h waking day. Move blocks freely — the order matters more than the clock.',
    sections:[{h:'Your day, block by block',items:items},{h:'Rules that make it stick',items:['Anchor the routine to wake time, not bedtime.','One missed block never cancels the day — resume at the next.','Review weekly: keep what gave energy, cut what drained it.']}]};
};})();"""

BUILDERS['random-fun'] = r"""
var BUILD_RANDOM_FUN=(function(){
var BANK={low:[['Living-room blanket fort + a film you have never seen','0-30 min, $0'],['Speed-clean one drawer while music plays','15 min, $0'],['Write a 6-word story about your day','5 min, $0'],['Video-call someone you miss','20 min, $0'],['Cook with only what is already open','30-45 min, $0']],mid:[['Thrift-store challenge: best find under $10','1-2 h, $10'],['Picnic in the nearest green space','1 h, $15'],['Try a free class or workshop nearby','1 h, $0-10'],['Photo walk: 20 shots, one theme','1 h, $0']],high:[['Day-trip to the next town over','half day, $40'],['Mini golf + ice cream run','2 h, $30'],['Sunset spot hunt with snacks','2 h, $20']]};
return function(inp){
  var r=prng(inp.seed||3);
  var budget=inp.budget||'low';
  var pool=BANK[budget]||BANK.low;
  var main=pick(pool,r);
  var others=shuffle(pool,r).filter(function(x){return x[0]!==main[0];}).slice(0,3);
  return {title:'Your random act of fun',intro:'Spontaneous, low-pressure, picked for a '+budget+' budget and about '+(inp.time||'an hour')+' of time.',
    sections:[{h:'Do this',items:[main[0]+' — '+main[1]]},{h:'Backups if the mood shifts',items:others.map(function(x){return x[0]+' — '+x[1];})},{h:'Make it stick',text:'Do it within 24 hours or it was just a nice idea. Send one photo to a friend.'}]};
};})();"""

BUILDERS['bucket-list'] = r"""
var BUILD_BUCKET_LIST=(function(){
var CATS={'Create':['Finish a 30-day creative streak','Make something and gift it','Learn one party trick well'],'Learn':['Hold a 5-minute conversation in a new language','Take a free online course to completion','Read 12 books in a year'],'Explore':['Watch sunrise from a high place','Visit a town you cannot pronounce','Take a train with no plan'],'Connect':['Host a dinner for old friends','Write letters to three people','Volunteer for one full day'],'Dare':['Perform on a stage once','Try the food that scares you','Do one thing that makes your hands shake (safely)']};
return function(inp){
  var r=prng(inp.seed||11);
  var interests=(inp.interests||'Create,Learn,Explore').split(',').map(function(s){return s.trim();});
  var cats=interests.filter(function(c){return CATS[c];});
  if(!cats.length)cats=['Create','Learn','Explore'];
  var sections=cats.map(function(c){
    return {h:c+' — pick one this season',items:shuffle(CATS[c],r).slice(0,2)};
  });
  sections.push({h:'How the list stays alive',items:['Review every 3 months; done items get a date and a story.','One item must scare you a little — comfort never made a memory.','Share the list with one person who will hold you to it.']});
  return {title:'Your evolving bucket list',intro:'Built around '+(inp.timeframe||'the next year')+' on a '+(inp.budget||'flexible')+' budget. The list grows as you do — check, add, repeat.',sections:sections};
};})();"""

BUILDERS['daily-skill'] = r"""
var BUILD_DAILY_SKILL=(function(){
var SKILLS=[['Speed reading','Time one page, then re-read for comprehension; track words per minute.'],['Knot tying','Learn the bowline today: rabbit, tree, hole. Ten reps each hand.'],['Memory palace','Place 10 grocery items along your hallway; walk it twice.'],['Whistling with fingers','Position, breath, adjust — 15 minutes of loud trial.'],['Touch typing home row','10 minutes on asdf jkl; no peeking, accuracy over speed.'],['Origami crane','One square of paper, 16 folds, follow along slowly.'],['Juggling 3 balls','Two-ball cascade first; add the third when throws land steady.'],['Basic beatboxing','Boots-n-cats: B-T-K-T sounds, loop them slow.'],['Napkin folding','The pocket fold: 6 folds, instant dinner-table upgrade.'],['Mental math: 2-digit multiply','Break into tens and ones; 5 problems, time yourself.'],['Drawing a face in proportion','Oval, eye-line halfway, thirds for nose and mouth.'],['Pen spinning (thumb-around)','Push, catch, repeat — 50 tries minimum.'],['Morse code basics','SOS first, then your initials; tap it on the table.'],['Card shuffle (riffle)','Split, bridge, square — practice over a table.'],['Lock picking (your own lock)','Tension wrench + pick on a practice lock only.'],['Speed cubing: first layer','White cross, then corners — one algorithm at a time.'],['Calligraphy: one letterform','Pick your initial; 20 slow reps with any pen.'],['Bird call: one species','Learn the robin or crow call; try it outside.'],['Balance: 60-second one-foot stand','Eyes open, then closed; switch feet.'],['Gratitude letter','Write 150 words to someone specific; send it.']];
return function(inp){
  var seed=parseInt(inp.seed,10)||((new Date().getFullYear()*1000)+(new Date().getMonth()*40)+(new Date().getDate()));
  var r=prng(seed);
  var pool=SKILLS.filter(function(s){return !inp.interest||s[1].toLowerCase().indexOf(inp.interest.toLowerCase())>=0;});
  if(!pool.length)pool=SKILLS;
  var s=pick(pool,r);
  return {title:'Skill of the day: '+s[0],intro:'One small skill, one 15-minute lesson. Do it today; the streak is the skill.',
    sections:[{h:'Your 15-minute lesson',items:['Minutes 0–3: watch or read how it is done once.', 'Minutes 3–10: '+s[1], 'Minutes 10–15: repeat the hardest part three times.']},{h:'Prove it',text:'Record a 30-second clip or write one sentence about what clicked. Tomorrow builds on today.'}]};
};})();"""

BUILDERS['challenge-calendar'] = r"""
var BUILD_CHALLENGE_CALENDAR=(function(){
var THEMES={fitness:['10 push-ups','15-min walk','30-sec plank','20 squats','Stretch routine','Rest + hydrate'],creative:['Sketch for 10 min','Write 200 words','Photo of the day','Hum a melody','Doodle challenge','Share your work'],mindful:['No-phone first hour','5-min breathing','Gratitude list x3','Compliment a stranger','Digital sunset','Journal one page'],tidy:['One drawer','Desktop clear','Closet 10 items out','Fridge clean','Inbox 20 archived','Whole-room reset']};
return function(inp){
  var days=Math.min(31,Math.max(3,parseInt(inp.days,10)||14));
  var theme=inp.theme||'fitness';
  var bank=THEMES[theme]||THEMES.fitness;
  var r=prng(inp.seed||5);
  var items=[];
  for(var d=1;d<=days;d++){items.push('Day '+d+': '+bank[(d-1)%bank.length]+(d%7===0?' (rest day — half effort counts)':''));}
  return {title:days+'-day '+(inp.theme||'personal')+' challenge',intro:'One small daily challenge at '+(inp.difficulty||'easy')+' difficulty. Miss a day? Never miss twice.',
    sections:[{h:'Your calendar',items:items},{h:'Rules',items:['Check off each day where you will see it.','Halve the task rather than skipping it.','Day '+(days)+' gets a real reward you choose now.']}]};
};})();"""

BUILDERS['celebration'] = r"""
var BUILD_CELEBRATION=(function(){
var THEMES=['Backwards day (dessert first)','Decade throwback','Color party (everyone wears one color)','Tiny awards night','Around-the-world snacks','Un-birthday for no reason','First-day-of-season festival','Achievement unlocked party'];
var ACTS=['Two-minute toast circle','DIY photo booth with props','Group playlist — everyone adds 3 songs','Trivia about the guest of honor','Time-capsule notes for next year','Dance-off, judged by applause'];
return function(inp){
  var r=prng(inp.seed||9);
  var theme=pick(THEMES,r), acts=shuffle(ACTS,r).slice(0,3);
  var budget=parseInt(inp.budget,10)||50, people=parseInt(inp.people,10)||6;
  return {title:'Celebration: '+theme,intro:'A small celebration for about '+people+' people on roughly $'+budget+' — because ordinary days deserve ceremonies too.',
    sections:[{h:'Theme',text:theme+'. Decor: one statement piece (banner, balloons, or lights) beats ten small ones.'},{h:'Run of show',items:acts},{h:'Budget sketch',items:['Food + drink: $'+Math.round(budget*0.6),'Decor: $'+Math.round(budget*0.25),'Wildcard fun: $'+Math.round(budget*0.15)]},{h:'The rule',text:'Someone takes photos; the host stays in at least three of them.'}]};
};})();"""

BUILDERS['tradition'] = r"""
var BUILD_TRADITION=(function(){
return function(inp){
  var who=inp.who||'friends', freq=inp.freq||'monthly', values=inp.values||'laughter and good food';
  var r=prng(inp.seed||13);
  var anchors=['First '+freq+' Friday','The same weekend every '+freq.replace('ly','')+' (pick a number and defend it)','The day the season changes','Whoever-hosts-chooses-the-theme rotation'];
  return {title:'A new '+freq+' tradition',intro:'A recurring ritual for '+who+', built on '+values+'. Traditions are just planned nostalgia.',
    sections:[{h:'The tradition',text:'“'+pick(['The Long Table','Second Sunday Supper','The Walk-and-Talk','Game Night Royale'],r)+'” — '+who+' gather '+freq+', same anchor date, no re-planning each time.'},{h:'Anchor it',items:[pick(anchors,r),'One standing group chat, one standing date.','A tiny ritual that repeats: same toast, same playlist opener, same silly trophy.']},{h:'Keep it alive 5 years',items:['Miss twice and it dies — protect the streak.','Let it evolve; the third year will not look like the first.','Document it: one photo per gathering, same album.']}]};
};})();"""

BUILDERS['adventure-plan'] = r"""
var BUILD_ADVENTURE_PLAN=(function(){
var HOOKS=['Follow the water: rivers, lakes, or coast.','Chase the high ground: hills, towers, rooftops (legal ones).','Eat your way through it: one dish per stop.','Hunt the weird: odd museums, strange statues, local legends.','Go analog: paper map, no GPS, ask humans.'];
return function(inp){
  var r=prng(inp.seed||17);
  var time=inp.time||'a free afternoon', budget=inp.budget||'$30';
  return {title:'Your life adventure: '+pick(HOOKS,r),intro:'A personalized plan for '+time+' on about '+budget+', tuned to '+(inp.interests||'curiosity')+'.',
    sections:[{h:'The mission',text:pick(HOOKS,r)+' Give the day a name — named days get remembered.'},{h:'The plan',items:['Hour 0: set out with one rule (e.g. turn left at every choice).','Midpoint: the meal stop — sit down, no rushing.','Hour X-1: the wildcard — ask a local for one recommendation and do it.','End: the debrief — best moment, funniest moment, one photo.']},{h:'Pack list',items:['Water + one snack more than you think','Charged phone + a little cash','Comfortable shoes (non-negotiable)']}]};
};})();"""

BUILDERS['brand-studio'] = r"""
var BUILD_BRAND_STUDIO=(function(){
var TONES={playful:['Witty sidekick','Chaos gremlin (lovable)','Hype friend'],calm:['Gentle guide','Thoughtful curator','Cozy narrator'],bold:['Hot-take machine','Myth-buster','High-energy coach'],nerdy:['Deep-dive analyst','Lore keeper','Experiment lab']};
var PALETTES=[['#0f172a midnight','#38bdf8 signal blue','#f8fafc paper white'],['#1a1a2e dusk purple','#e94560 punch pink','#f5f5f5 bone'],['#10231a forest','#a3e635 lime pop','#fefce8 cream'],['#2b2118 espresso','#d97706 amber','#fff7ed milk']];
var PILLARS=['Teach: one clear lesson per week','Entertain: one pure-fun piece per week','Connect: one community-driven piece per week'];
return function(inp){
  var r=prng(inp.seed||21);
  var niche=inp.niche||'gaming', tone=inp.tone||'playful';
  var names=[niche+' & chill', 'the '+niche+' lab', niche.charAt(0).toUpperCase()+niche.slice(1)+' FM', 'Ctrl+'+niche];
  var pal=pick(PALETTES,r), persona=pick(TONES[tone]||TONES.playful,r);
  return {title:'Creator brand: '+pick(names,r),intro:'A cohesive identity for a '+(tone)+' '+(niche)+' creator — name, look, voice, and content pillars in one kit.',
    sections:[{h:'Name shortlist',items:shuffle(names,r).slice(0,3)},{h:'Visual identity',items:pal},{h:'Voice — you are the '+persona,text:'Write every caption like the '+persona+' would say it out loud.'},{h:'Content pillars',items:PILLARS},{h:'Tagline starters',items:['"'+niche+', but funnier."','"New here? Start with the chaos."','"'+niche+' for people with 5 minutes."']}]};
};})();"""

BUILDERS['poll-gen'] = r"""
var BUILD_POLL_GEN=(function(){
return function(inp){
  var topic=inp.topic||'tonight\u2019s stream';
  var r=prng(inp.seed||23);
  var sets=[
    ['Which should we do first?',['Option A: the safe pick','Option B: the spicy pick','Option C: chat decides live']],
    ['Rate my last '+topic+':',['10/10 flawless','Solid 7','Needs work','Chaotic (affectionate)']],
    ['You choose the next '+topic+':',['The fan favorite','The underdog','Something brand new']],
    ['Hot take check:',['Agree strongly','Agree a little','Disagree','Fighting words']]
  ];
  var sections=shuffle(sets,r).slice(0,3).map(function(s){return {h:s[0],items:s[1]};});
  sections.push({h:'Poll craft rules',items:['Two to four options — more splits the vote into noise.','Always include one funny option; humor drives turnout.','Close the loop on stream: announce the winner and DO it.']});
  return {title:'Audience polls: '+topic,intro:'Polls tuned for '+(inp.platform||'stream chat')+' — built to pull lurkers into participants.',sections:sections};
};})();"""

BUILDERS['emote-studio'] = r"""
var BUILD_EMOTE_STUDIO=(function(){
var BASE=['Hype','Lurk','GG','RIP','Sus','Blessed','Cringe','Clutch','Nap','Snack'];
return function(inp){
  var r=prng(inp.seed||27);
  var vibe=inp.vibe||'cozy chaos';
  var n=Math.min(12,Math.max(3,parseInt(inp.count,10)||6));
  var emotes=shuffle(BASE,r).slice(0,n).map(function(b,i){
    return (inp.prefix||'chan')+b.toLowerCase()+' — '+b+' face, '+vibe+' style (variant '+(i+1)+')';
  });
  return {title:'Emote set: '+(inp.prefix||'your channel'),intro:n+' original emote concepts in a '+vibe+' style. Each reads clearly at tiny chat size.',
    sections:[{h:'The set',items:emotes},{h:'Design rules',items:['Silhouette first: readable at 28px or it fails.','Three colors max per emote.','One mascot cameo, one inside joke, rest are universal reactions.']}]};
};})();"""

BUILDERS['mascot'] = r"""
var BUILD_MASCOT=(function(){
var SPECIES=['a sleepy axolotl','a hyperactive raccoon','a chill capybara','a dramatic raven','a tiny dragon','a robot cat','a frog in a hoodie','a loaf-shaped blob'];
var TRAITS=['collects shiny things','naps through important moments','hypes up chat unprompted','judges silently, loves loudly','speaks only in emotes'];
return function(inp){
  var r=prng(inp.seed||29);
  var species=inp.species||pick(SPECIES,r);
  var trait=pick(TRAITS,r);
  return {title:'Channel mascot: '+species,intro:'A recognizable mascot for a '+(inp.theme||'variety')+' channel — design, personality, and expressions in one sheet.',
    sections:[{h:'Design',items:['Base: '+species+', 2-3 signature colors','One standout feature (oversized eyes, tiny hat, glowing accessory)','Chibi proportions: big head, small body — reads at any size']},{h:'Personality',text:'The mascot '+trait+'. It is the channel\u2019s emotional support creature.'},{h:'Expression sheet',items:['Hype (sparkles, open mouth)','Lurk (half-lidded, blanket)','GG (salute or bow)','RIP (X eyes, tiny ghost)','Sus (side-eye, magnifier)']},{h:'Backstory seed',text:'It showed up in chat one day during a raid and never left. The community named it; the lore writes itself from there.'}]};
};})();"""

BUILDERS['content-calendar'] = r"""
var BUILD_CONTENT_CALENDAR=(function(){
return function(inp){
  var perWeek=Math.min(14,Math.max(1,parseInt(inp.perweek,10)||4));
  var pillars=(inp.pillars||'Teach,Entertain,Community').split(',').map(function(s){return s.trim();});
  var platforms=(inp.platforms||'video,shorts,stream').split(',').map(function(s){return s.trim();});
  var days=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  var items=[];
  for(var i=0;i<perWeek;i++){items.push(days[i%days.length]+': '+pillars[i%pillars.length]+' → '+platforms[i%platforms.length]);}
  return {title:'Content calendar: '+perWeek+'/week',intro:'A sustainable rhythm across '+platforms.join(', ')+'. Batch, buffer, breathe.',
    sections:[{h:'The week',items:items},{h:'System rules',items:['One buffer slot per week — life happens.','Repurpose rule: every big piece becomes 3 small ones.','Monthly review: double what worked, drop what drained.']}]};
};})();"""

BUILDERS['badge-gen'] = r"""
var BUILD_BADGE_GEN=(function(){
return function(inp){
  var r=prng(inp.seed||31);
  var miles=(inp.milestones||'First stream,10 streams,1 year,Helper,Creator').split(',').map(function(s){return s.trim();});
  var shapes=['shield','star','coin','ribbon','gem','laurel'];
  var badges=miles.map(function(m,i){return m+': '+shapes[i%shapes.length]+' badge, tier '+(1+((i/3)|0))+' — earned, never bought';});
  return {title:'Community badge set',intro:badges.length+' meaningful badges for contributions and milestones — status people actually want.',
    sections:[{h:'The badges',items:badges},{h:'Design rules',items:['Milestone badges get fancier with tenure.','Contribution badges name the deed, not the donor.','Retire badges rarely; scarcity is earned over years, not manufactured.']}]};
};})();"""

BUILDERS['theory'] = r"""
var BUILD_THEORY=(function(){
return function(inp){
  var uni=inp.universe||'your favorite series';
  return {title:'Fan theory playground: '+uni,intro:'A structured way to build, compare, and stress-test theories about '+uni+'.',
    sections:[{h:'Theory templates',items:['The Hidden Identity: a minor character is secretly major — evidence, motive, reveal moment.','The Loop: events repeat with a twist — map the cycles and the break point.','The Unreliable Lens: the narrator is wrong — what changes if you flip one assumption?','The Merge: two separate threads are one — find the connecting scene.']},{h:'Score each theory',items:['Evidence (1-5): scenes that support it','Elegance (1-5): simplest explanation wins ties','Falsifiability (1-5): what would prove it wrong?']},{h:'Playground rules',items:['Steel-man the theory you dislike before attacking it.','One theory per thread; compare scores side by side.','Canon updates re-score everything — theories are living documents.']}]};
};})();"""

BUILDERS['project-factory'] = r"""
var BUILD_PROJECT_FACTORY=(function(){
return function(inp){
  var r=prng(inp.seed||37);
  var interest=inp.interest||'art';
  var size=parseInt(inp.size,10)||10;
  var formats=['Collaborative mural: one canvas per person, one theme','Community map: everyone pins a favorite spot with a story','Exquisite-corpse story: each person writes one paragraph','Sound collage: everyone records 10 seconds','Resource wiki: everyone adds their best tip'];
  return {title:'Community project: '+interest,intro:'Turn '+size+' interested people into one shared creation around '+interest+'.',
    sections:[{h:'Pick a format',items:[pick(formats,r)]},{h:'Run it in 4 phases',items:['Week 1: pitch + sign-ups (low barrier, one-click join)','Week 2: contributions roll in (daily prompts keep momentum)','Week 3: assembly + credits for everyone','Week 4: showcase + retrospective']},{h:'Roles (volunteer, rotate)',items:['Wrangler: keeps the timeline','Greeter: welcomes newcomers','Archivist: saves everything twice']}]};
};})();"""

BUILDERS['podcast-segments'] = r"""
var BUILD_PODCAST_SEGMENTS=(function(){
var SEGS=['Cold open: 60-second hook from the best moment','Listener mail: one question, real answer','The Deep Cut: 10 minutes on one idea','Game break: trivia, drafts, or debates','Hotline: voice notes from the audience','One Good Thing: end warm, every time'];
return function(inp){
  var r=prng(inp.seed||41);
  var mins=Math.min(180,Math.max(15,parseInt(inp.length,10)||45));
  var picks=shuffle(SEGS,r);
  var plan=[['Cold open',2],['Main topic 1',Math.round(mins*0.3)],['Game break',8],['Main topic 2',Math.round(mins*0.3)],['Listener mail',Math.round(mins*0.15)],['One Good Thing',3]];
  return {title:'Podcast lineup: '+(inp.theme||'your show'),intro:'A '+mins+'-minute episode structure with recurring segments listeners can love.',
    sections:[{h:'The rundown',items:plan.map(function(p){return p[0]+' — '+p[1]+' min';})},{h:'Segment bank (rotate weekly)',items:picks.slice(0,4)},{h:'Production rules',items:['Record the cold open LAST — steal it from the best moment.','One segment per episode is allowed to flop; two is a format problem.','Name segments like a local would: specific beats clever.']}]};
};})();"""

def node_check(path):
    r = subprocess.run(['node', '--check', path], capture_output=True, text=True, timeout=30)
    return r.returncode == 0, (r.stdout + r.stderr)[:300]
