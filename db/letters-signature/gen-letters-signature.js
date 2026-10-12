(function(){'use strict';
/* Signature Letters Database generator — jahdb-letters-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escXml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function escUri(s){return encodeURIComponent(s).replace(/[!'()*]/g,function(c){return '%'+c.charCodeAt(0).toString(16).toUpperCase();});}
var PREFIX='JAH-LET-SIG-';
var TYPELABEL='signature letter';
var SRCSLUG='signature';
var TOPICS=[["A Letter to the Future Keeper", "philosophical-letter", "An original letter addressed to whoever keeps the archive a century hence: instructions, warnings, and encouragement from the first generation.", "You will find our machinery quaint and our anxieties familiar. We worried about formats dying, about truth decaying into content, about the million-record march outrunning our care. You will worry about your own versions of the same things. The counsel is the same across the century: keep the originals, label everything, trust the catalog more than your memory.", "Do not judge us too harshly for what we got wrong — we were building at speed, and speed leaves marks. Judge us instead by whether the archive survived us intact and grew kinder in your hands. If you are reading this, it did. Tend it well, future keeper. The readers are counting on you, as we counted on those before us."], ["Letters from the Long Voyage", "personal-letter", "An original series of shipboard letters: daily dispatches from an imagined long voyage, on distance, routine, and the widening of the mind.", "Day 40: the sea has become a calendar — we mark time by watches and weather, and the shore feels like a story someone told us once. Routine is the voyage's great invention: the same knots, the same meals, the same stars, and inside that sameness the mind finally has room to think its long thoughts. I understand now why sailors return philosophers or not at all.", "Day 90: landfall tomorrow, and I find I am not eager. The voyage has become the home and the destination the interruption. This is the traveler's secret, the one the brochures never mention: motion becomes belonging, and arrival is a kind of exile. I will step ashore a different person than the one who embarked — which was, I suppose, the entire point of the ticket."], ["The Cartographer's Farewell", "farewell-letter", "An original farewell letter from a retiring mapmaker to their apprentice: the craft, its ethics, and what the maps never show.", "Take the instruments; they are yours now, and they are honest tools — they report what they measure, no more. The dishonesty, when it comes, comes from us: the coastline smoothed for beauty, the village omitted for politics, the blank space that says 'nothing here' when we mean 'we did not look.' Your maps will be judged by what you chose to show.", "What the maps never show is the walking: the blisters, the wrong turns, the farmer who corrected your road over tea. Remember that every line on your vellum was once a day of someone's life. Draw accordingly. And when you retire, write this letter to your own apprentice — the craft continues not in the instruments but in the instruction."], ["An Open Letter to the Hasty", "open-letter", "An original open letter addressed to everyone in a hurry: a defense of slowness, written at walking pace.", "You are reading this quickly, I know — skimming for the point, already halfway to the next thing. That is the haste talking, and this letter is its intervention. Nothing you are hurrying toward is improved by your hurry; the meeting will not go better for your racing, the meal will not taste finer, the child will not feel more loved for your efficiency.", "Try the experiment the letter prescribes: one day at walking pace. Walk instead of ride. Read the whole page. Let the kettle boil without checking the phone. You will discover that slowness is not the absence of speed but its master — and that the hasty, for all their rushing, arrive no earlier at anything that matters."], ["Love Letter to the Library", "love-letter", "An original love letter addressed to libraries: ardent, specific, and unembarrassed.", "My dearest library: I love your smell first — dust and glue and the faint vanilla of aging paper, the perfume of kept promises. I love your silence, which is not empty but full: the held breath of ten thousand minds waiting to be consulted. I love your democracy — the same chair for the professor and the runaway, the same light for the scholar and the sleeper.", "I love that you keep what the world discarded and discard nothing the world might need. I love your patience with my lateness, your forgiveness of my fines, your faith that I will return the book — a faith in human nature no other institution sustains. Yours, in overdue devotion, a reader."], ["The Beekeeper's Last Letter", "last-letter", "An original last letter from a beekeeper to their successor: the hives, the seasons, and the philosophy of tending.", "The hives are yours now — all fourteen, and the wild one in the oak that I never had the heart to move. The calendar is on the shed wall, but the real calendar is in your hands: lift the frames, feel the weight, smell the entrance. The bees will teach you everything if you stop long enough to be taught.", "Take only the surplus; leave them their winter; never open a hive in anger. These three rules are the whole of the craft, and the whole of more than the craft. I have kept bees for forty years and they have kept me — patient, observant, humble before a society that needs no keeper but tolerates one. Tend them well."], ["Letter from the Lighthouse", "personal-letter", "An original letter written from a lighthouse posting: on solitude, duty, and the rhythm of the light.", "The light turns every twelve seconds, and I have come to measure my thoughts by it: twelve seconds to notice, twelve to consider, twelve to release. Solitude here is not emptiness but structure — the day divided into watches, the watches into tasks, the tasks into the small satisfactions of oil, glass, and logbook.", "Ships pass that will never know my name, and that is the job's quiet glory: the unwitnessed good. I keep the light not for thanks but because darkness is the alternative. If you ever feel your own work goes unseen, remember the lighthouse keeper — the whole point is that no one needs to see you, only the light."], ["The Clockmaker's Apology", "personal-letter", "An original letter of apology from a clockmaker: on being wrong about time, and what a repaired clock teaches about repaired trust.", "I told you the clock would keep perfect time, and it did not — it lost three minutes a week, and I blamed your winding. The fault was mine: a pivot I had burnished too eagerly, running dry. I write not only to confess the error but to report the repair, and to note what the clock taught me about apologies.", "A clock, like trust, is repaired by attention to the actual fault, not by polishing the case. I have rebushed the pivot, and the clock now keeps the time I promised. The apology keeps its own time — it arrives late, as apologies do, but it arrives true. Please set the clock by it."], ["Letter to a Young Archivist", "philosophical-letter", "An original letter of counsel to someone beginning in the archive profession: what school does not teach.", "They will teach you the standards, the schemas, the acid-free everything — learn them, they matter. But no course teaches the real curriculum: how to say no to a donor with grace, how to catalog the box that makes you weep, how to keep going when the backlog outlives your career. That you learn at the bench, from keepers who learned it the same way.", "Cultivate two virtues above all: patience with the material and impatience with the obstacle. The material — the fragile, the faded, the difficult — deserves all the time it takes. The obstacle — the broken process, the pointless rule — deserves none. And write everything down. Your memory is not the archive; the archive is the archive."], ["The Diplomat's Unsent Letter", "diplomatic-letter", "An original diplomatic letter that was never sent: the honest draft beneath the official note, on what negotiations really cost.", "The official note will speak of 'frank and constructive exchanges' and 'areas of continuing divergence.' This is the unsent version: we sat across the table for eleven days, and on the ninth day I understood that your minister wants the agreement and your general does not, and that you are negotiating with me while negotiating with him. I do not blame you; I have a general of my own.", "What negotiations really cost is not the concessions — those are arithmetic — but the trust spent to get them. Every bluff called, every deadline faked, every smile that was not meant: these are drawn on an account that the next crisis will need. Spend carefully. The table will be here again, and so will we."], ["A Mother's Letter, 2124", "family-letter", "An original letter from an imagined future: a mother writes to her daughter about the world being rebuilt.", "You ask what it was like before — the before you learn about in school, the years of the great repair. It was like watching someone you love recover from a long illness: slow, then sudden, then slow again. We planted things we would not live to sit under. That is the whole of it, and the whole of every good thing.", "Your generation inherits the orchards, not the planting — do not feel guilty about this; it was the point. Tend them, add your own rows, and write your own letters to the future. The repair is never finished; it is only handed on. That is not a burden. It is a belonging."], ["The Gardener's Letter to Winter", "personal-letter", "An original seasonal letter: a gardener addresses winter directly, with complaints, gratitude, and terms.", "Dear Winter: we need to talk about the roses. I accept the necessity of your office — the seeds need their cold, the soil needs its rest, and I confess the garden is more beautiful for having been without it. But the roses, Winter. There are limits, and you know them.", "Terms for the season: you may have the nights, but the days are mine for planning — seed catalogs, rotations, the new bed along the wall. You keep the ground asleep; I will keep the hope awake. Come spring, we will both pretend this negotiation never happened, and the garden will be the better for our diplomacy."], ["Farewell to the Reading Room", "farewell-letter", "An original farewell from a retiring librarian to the reading room itself: forty years of readers, remembered.", "I am saying goodbye to you, room — to the green lamps, the oak tables worn smooth by a million elbows, the particular hush that falls at nine when the doors open. I have watched generations learn to be quiet here: the freshmen loud in September, silent by December, gone by June, replaced. You taught them all.", "Keep the chairs comfortable and the rules kind. Forgive the sleepers; they are tired, and the books will keep. Welcome the nervous ones; they become the devoted. And when I am gone, keep one lamp lit late — for the reader who arrives at closing with the one question that cannot wait. There is always one."], ["The Explorer's Letter Home", "personal-letter", "An original letter from an imagined expedition: the farthest point, and what it feels like to stand there.", "We reached the farthest point yesterday — the place no one had stood, now stood upon by us, which makes it no longer the farthest point. That is the explorer's paradox, and standing in it, I felt not triumph but tenderness: for the untouched snow, the unphotographed ridge, the silence that had kept itself for so long and has now been spent.", "Do not worry; we are well provisioned and the return is planned to the day. But know that I understand now why they go: not for the flag or the record, but for the moment the map ends and the world begins — the moment you are nowhere, and therefore, completely, somewhere."], ["Open Letter to the Future Reader", "open-letter", "An original open letter to whoever reads the archive in the centuries ahead: what we were, what we hoped.", "Dear future reader: we were the people of the great acceleration, living faster than our wisdom, building larger than our understanding. Do not mistake our noise for our nature — beneath the hurry we were still the old animal, wanting food, shelter, love, and a story that made sense. The archive is our attempt to leave you the story part.", "We hoped you would be kinder than we were, and wiser, and we tried to give you the materials: the records complete, the labels honest, the machinery plain. Use them well. Forgive our blind spots — every age has them, including yours, though you cannot see them yet. And write your own letter to the future. The chain continues through you."]];
var SECTIONS=[["On the writer", "Every letter is a portrait taken without the sitter knowing. The writer reveals themselves in the choice of what to report, what to withhold, and what to circle back to three paragraphs later. Read for the person behind the pen: their worries, their vanities, their unguarded hours. The best letters are the ones the writer did not know were literature."], ["On the occasion", "Letters are written on occasions, and the occasion shapes the letter more than the writer admits. War, exile, love, business, grief — each imposes its form. Note what prompted this writing: the news just received, the departure imminent, the silence that had grown too long. The occasion is the letter’s hidden first paragraph."], ["The material letter", "Paper, ink, hand, seal, postmark: the physical letter carried meaning before a word was read. A hurried hand means urgency; a fair copy means care; the crossed letter means paper was dear. This record notes the material facts where they are known — for the letter was an object before it was a text, and objects testify."], ["Aftermath", "What happened after the letter was sent — or whether it was ever sent — belongs to the record. Some letters changed history; most changed only the afternoon of one reader, which is change enough. The aftermath is told plainly: the reply if any, the consequence if known, the silence if that is all there was."], ["On reading letters", "Read a letter twice: once for the news, once for the writer. The first reading belongs to the recipient; the second belongs to you, reading over their shoulder across the years. Notice what is not said — the subject avoided, the name never mentioned. Letters are as eloquent in their omissions as in their sentences."], ["Preservation", "Letters survive by affection and accident: kept in a drawer, bundled with ribbon, rescued from the estate sale. The great correspondences reached us because someone could not bear to throw them away. This archive continues that affection by design — every letter kept complete, every letter kept findable, every letter kept as if someone loved the writer."]];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function svgScan(seed,title,genre){
  var s=prng(seed*7+3);
  var tones=['#e8d9b0','#dcc79a','#efe3c2','#e2d3a8'], inks=['#3a2c18','#2c2416','#4a3a22'];
  var tone=tones[(s()*tones.length)|0], ink=inks[(s()*inks.length)|0];
  var lines='',y=130,i,w;
  for(i=0;i<13;i++){w=55+((s()*32)|0);lines+='<rect x="60" y="'+y+'" width="'+w+'%" height="7" rx="3" fill="'+ink+'" opacity="0.5"/>';y+=24;}
  var svg='<svg xmlns="http://www.w3.org/2000/svg" width="600" height="760" viewBox="0 0 600 760">'
    +'<rect width="600" height="760" fill="'+tone+'"/>'
    +'<rect x="18" y="18" width="564" height="724" fill="none" stroke="'+ink+'" stroke-width="4"/>'
    +'<text x="300" y="72" text-anchor="middle" font-family="Georgia,serif" font-size="25" fill="'+ink+'">'+escXml(String(title).slice(0,44))+'</text>'
    +'<text x="300" y="102" text-anchor="middle" font-family="Georgia,serif" font-size="14" fill="'+ink+'" opacity="0.7">'+escXml(genre)+'</text>'
    +lines
    +'<circle cx="516" cy="678" r="34" fill="none" stroke="#8a1f1f" stroke-width="4"/><text x="516" y="688" text-anchor="middle" font-family="Georgia,serif" font-size="22" fill="#8a1f1f">JAH</text>'
    +'</svg>';
  return 'data:image/svg+xml;utf8,'+escUri(svg);
}
function svgPlate(seed,title,kind){
  var s=prng(seed*13+7), hues=[210,275,150,20,340,190], i, rays='';
  var h=hues[(s()*hues.length)|0];
  for(i=0;i<12;i++){var a=i*30*Math.PI/180;rays+='<line x1="200" y1="200" x2="'+(200+150*Math.cos(a)).toFixed(1)+'" y2="'+(200+150*Math.sin(a)).toFixed(1)+'" stroke="hsl('+h+',60%,70%)" stroke-width="3" opacity="0.5"/>';}
  var svg='<svg xmlns="http://www.w3.org/2000/svg" width="400" height="400" viewBox="0 0 400 400">'
    +'<rect width="400" height="400" fill="hsl('+h+',30%,10%)"/>'+rays
    +'<circle cx="200" cy="200" r="110" fill="none" stroke="hsl('+h+',70%,60%)" stroke-width="5"/>'
    +'<circle cx="200" cy="200" r="80" fill="none" stroke="hsl('+h+',70%,60%)" stroke-width="2" opacity="0.7"/>'
    +'<text x="200" y="192" text-anchor="middle" font-family="Georgia,serif" font-size="30" fill="hsl('+h+',80%,85%)">JAH</text>'
    +'<text x="200" y="222" text-anchor="middle" font-family="Georgia,serif" font-size="13" fill="hsl('+h+',60%,75%)">'+escXml(kind.slice(0,30))+'</text>'
    +'<text x="200" y="330" text-anchor="middle" font-family="Georgia,serif" font-size="15" fill="hsl('+h+',40%,80%)">'+escXml(String(title).slice(0,36))+'</text>'
    +'</svg>';
  return 'data:image/svg+xml;utf8,'+escUri(svg);
}
var DEMO_LINES=[
'/* JAH reading-room demo \\u2014 jahdb-demo-1.0',
' * Record: __RID__ \\u00b7 __TITLE__',
' * A working program: search the text, read it aloud, and track progress.',
' * Run: paste into any browser console on the record page, or save as .html.',
' */',
'(function(){',
'  "use strict";',
'  var TITLE=__TITLEQ__;',
'  function words(t){return t.trim().split(/\\s+/).length;}',
'  function reader(text){',
'    var box=document.createElement("div");',
'    box.style.cssText="position:fixed;right:12px;bottom:12px;width:320px;max-height:60vh;overflow:auto;background:#0d1526;color:#e8f1ff;border:1px solid #1d2c4d;border-radius:12px;padding:12px;z-index:9999;font-family:Arial,sans-serif";',
'    box.innerHTML="<b>"+TITLE+"</b><br><span style=\'color:#9fb3d8\'>"+words(text)+" words</span><br><br>"',
'      +"<input id=jahq placeholder=\'Search the text\\u2026\' style=\'width:100%;margin-bottom:6px\'>"',
'      +"<div style=\'display:flex;gap:6px\'><button id=jahread>\\u25b6 Read aloud</button><button id=jahstop>\\u25a0 Stop</button><button id=jahx>\\u2715</button></div>"',
'      +"<div id=jahhits style=\'margin-top:8px;font-size:.9em\'></div>";',
'    document.body.appendChild(box);',
'    var q=box.querySelector("#jahq"),hits=box.querySelector("#jahhits");',
'    q.addEventListener("input",function(){',
'      var needle=q.value.toLowerCase();if(!needle){hits.textContent="";return;}',
'      var n=0,idx=-1,low=text.toLowerCase();',
'      while((idx=low.indexOf(needle,idx+1))>=0)n++;',
'      hits.textContent=n+" match"+(n===1?"":"es");',
'    });',
'    box.querySelector("#jahread").addEventListener("click",function(){',
'      try{speechSynthesis.cancel();var u=new SpeechSynthesisUtterance(text.slice(0,4000));speechSynthesis.speak(u);}catch(e){alert("Read-aloud not available here.");}',
'    });',
'    box.querySelector("#jahstop").addEventListener("click",function(){try{speechSynthesis.cancel();}catch(e){}});',
'    box.querySelector("#jahx").addEventListener("click",function(){try{speechSynthesis.cancel();}catch(e){}box.remove();});',
'    return box;',
'  }',
'  if(typeof module!=="undefined"&&module.exports){module.exports={reader:reader,words:words};}',
'  else if(typeof window!=="undefined"){window.JAHReader={open:reader,title:TITLE};}',
'})();'
];
function demoProg(id,title){
  var src=DEMO_LINES.join('\n').split('__RID__').join(id).split('__TITLEQ__').join(JSON.stringify(title)).split('__TITLE__').join(String(title).replace(/\*\//g,'* /'));
  return {engine:'jahdb-demo-1.0',kind:'read',title:'Reading room \\u2014 '+title,language:'javascript',program:src};
}
function generate(seed,opts){
  var s=prng(seed);
  var ti=(s()*TOPICS.length)|0, T=TOPICS[ti];
  var genre=(opts&&opts.genre)||T[1];
  var id=PREFIX+pad(seed), title=T[0], hook=T[2];
  var i1=(s()*SECTIONS.length)|0, i2=(s()*SECTIONS.length)|0;
  var S1=SECTIONS[i1], S2=SECTIONS[i2];
  var text=String(title).toUpperCase()+'\n\n'+hook+'\n\n'+T[3]+'\n\n'+T[4]+'\n\n'+String(S1[0]).toUpperCase()+'\n'+S1[1]+'\n\n'+String(S2[0]).toUpperCase()+'\n'+S2[1];
  var images=[svgScan(seed,title,genre),svgPlate(seed,title,TYPELABEL)];
  return {id:id,title:title,description:String(hook).slice(0,170),genre:genre,type:TYPELABEL,content:text,images:images,clips:[],demo:demoProg(id,title),src:SRCSLUG,_seed:seed};
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<400)errs.push('content too short (full work required)');
  if(!r.images||!r.images.length)errs.push('missing images');
  if(!r.demo||!r.demo.program)errs.push('missing demo program');
  return {ok:errs.length===0, errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('letters-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
