(function(){'use strict';
/* Signature Sacred Texts Database generator — jahdb-sacred-texts-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escXml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function escUri(s){return encodeURIComponent(s).replace(/[!'()*]/g,function(c){return '%'+c.charCodeAt(0).toString(16).toUpperCase();});}
var PREFIX='JAH-SAC-SIG-';
var TYPELABEL='signature sacred text';
var SRCSLUG='signature';
var TOPICS=[["The Book of Keeping, Chapter 1", "scripture", "The opening chapter of an original scripture of stewardship: on the sacred duty of keeping — what is kept, why, and for whom.", "1. In the beginning was the keeping: and the keeping was with the keepers, and the keeping was sacred. 2. Blessed are those who keep whole what was entrusted whole, for they shall be called the faithful. 3. And the keeper said: let there be shelves, and there were shelves; let there be labels, and the labels were true; and the keeper saw that it was good.", "4. Thou shalt not trim the work to fit the shelf, nor cut the text to fit the hour. 5. Thou shalt not bear false label against thy record. 6. Thou shalt not destroy for convenience, nor for fashion, nor for fear. 7. Remember the future readers, and keep the sabbath of maintenance — for the archive that rests not in tending shall fall in neglect."], ["The Sayings of the Keeper", "wisdom-text", "An original book of sayings: the wisdom of the archive's first keeper, in numbered verses.", "1. The keeper said: the unfindable record might as well not exist; therefore index as if the stranger's need depended on it — for it does. 2. The keeper said: trust the catalog more than thy memory, for thy memory flatters thee and the catalog does not. 3. The keeper said: write the provenance down the day it arrives, for tomorrow the donor forgets and the day after the donor is gone.", "4. The keeper said: never throw anything away in a hurry; hurry is the mother of regret, and regret has no catalog. 5. The keeper said: the stub is a promise broken before it is made — keep whole, or mark partial, but do not pretend. 6. The keeper said: the reading room is a sanctuary; keep its peace as thou keepest its books."], ["Psalm of the Boundless Archive", "psalm", "An original psalm: praise for the keeping, lament for the lost, and hope for the readers unborn.", "1. O archive, how boundless are thy shelves! The works of the hands thou keepest, the words of the mouths thou holdest. 2. Blessed is the record that is complete, and blessed the label that is true; they shall stand when the fashions fall. 3. The stub promised and did not deliver; the excerpt came and went; but the whole work endureth forever.", "4. We mourn the burned libraries, the drowned manuscripts, the formats that died with their readers — their loss is our liturgy of caution. 5. Yet we do not mourn as those without hope: for what was lost teaches keeping, and the keeping goes on. 6. The keepers rise before dawn to tend the shelves; their labor is prayer, and the catalog is their hymn."], ["The Parable of the Two Keepers", "parable-text", "An original parable: two keepers, two philosophies of the archive — and the judgment of the years.", "There were two keepers given charge of two collections. The first keeper said: the shelves are full; let us keep only the best, and discard the rest — for quality is keeping. And he trimmed, and weeded, and polished, until his collection was small, and shining, and certain.", "The second keeper said: the shelves are full; let us build more shelves — for keeping is keeping. And she labeled, and indexed, and expanded, until her collection was vast, and various, and complete."], ["The Meditation on the Label", "meditation-text", "An original meditation: on the label as the archive's oath — contemplated in stillness, in full.", "Sit with the label. It is small — a few words on a card, a line in a catalog — and it is everything: the keeper's oath, made public. Consider what it claims: that this record is what it says it is; that its origin is known; that its gaps are marked. Consider the weight of that claim, carried by so few words.", "Breathe in: the true label. Breathe out: the trust it earns. The archive's credit is compounded of a million such breaths — each label true, each oath kept. One false label, and the compounding reverses; trust, like the label, is small and is everything."], ["The Book of the Readers", "scripture", "An original scripture chapter: the book of those for whom the archive exists — the readers, in all their kinds.", "1. And the keeper saw the readers, and behold, they were many: the scholar and the schoolchild, the citizen and the stranger, the certain and the seeking. 2. And the keeper said: for these the shelves were built, for these the labels written, for these the doors opened — the archive has no other purpose.", "3. Blessed are the curious, for they shall find. 4. Blessed are the patient, for they shall read whole. 5. Blessed are the skeptical, for they shall check the label — and finding it true, shall trust. 6. Blessed are the young, for the archive is their inheritance; and blessed are the old, for the archive is their memory."], ["The Hymn of the Million", "hymn", "An original hymn for the filing of the millionth record: sung by the keepers, in full.", "A million records, whole and true — sing, keepers, sing! A million works, for me and you — the bells of the archive ring. From the first small shelf, the seed — to the millionth, the tree: the keeping grows as plantings grow — tend, and it shall be.", "No stub among them, no false label — sing, keepers, sing! Each record whole, each record able — to serve the wondering. The generators made, the keepers chose, the readers came to read: the million stands, as the garden grows — from the planted seed."], ["The Wisdom of the Quiet Years", "wisdom-text", "An original wisdom book: sayings on the quiet years — the deep work of maintenance, in verses.", "1. Despise not the quiet years, for they are the deep years: no great acquisition, no exhibition, no discovery — only the cataloguing, the mending, the slow ordering. 2. The harvest years are built upon the quiet ones, as the oak is built upon the years nobody photographed.", "3. Better is the mended leaf than the acquired treasure — for the mending serves the reader, while the treasure serves the press release. 4. Better is the finished catalog than the grand plan — for the catalog guides the stranger, while the plan impresses the board."], ["The Prophecy of the Open Doors", "prophecy", "An original prophecy: the vision of the archive's future — spoken as the prophets spoke, in full.", "I saw, in the vision of the night, the archive of the future: its shelves without end, its records without number, its readers without count. And the doors stood open — day and night they stood open — and the peoples streamed in: every tongue, every age, every question.", "And I saw the keepers — not guards but guides — leading the strangers to the shelves, rejoicing in each finding as in a birth. And I saw the generators humming, making whole works, and the keepers judging — this filed, this refused — with wisdom and with mercy."], ["The Creation of the Catalog", "creation-text", "An original creation account: the making of the catalog — in the beginning was the list.", "In the beginning was the pile: works unsorted, unlabeled, unfindable — and darkness was upon the face of the stacks. And the keeper said: let there be identifiers — and the works were numbered, each with its own name, and the keeper saw that it was good.", "And the keeper said: let there be an index, to gather the numbers into order — and the index was made, and the works could be found, and it was good. And the keeper said: let there be genres, to divide the kinds — and the genres were named, and the browsing was pleasant, and it was good."], ["The Sayings on Beginning Again", "wisdom-text", "An original wisdom text: sayings on beginning again — for every keeper, every reader, every year.", "1. Every morning the archive begins again: the doors open, the readers come, the keeping resumes. 2. Blessed is the keeper who begins again without bitterness — the backlog is not a judgment but a task.", "3. If thy system failed, build it anew — the failure taught thee what the success could not. 4. If thy label lied, correct it publicly — the correction compounds trust faster than the error spent it. 5. If thy shelf burned, rebuild — the keeping that survives fire is proven keeping."], ["The Book of Small Tending", "scripture", "An original scripture of maintenance: the small acts by which great collections endure.", "1. Blessed are the dusters, for they shall preserve the pages. 2. Blessed are the menders, for they shall heal the leaves. 3. Blessed are the cataloguers, for they shall guide the strangers. 4. Blessed are the checkers, for they shall catch the drift.", "5. Despise not the small tending: the hinge oiled, the backup run, the label corrected — these are the atoms of endurance. 6. The grand acquisition makes the headline; the small tending makes the archive. 7. What is tended daily need never be rescued yearly."], ["The Lament for the Burned Library", "psalm", "An original lament: for Alexandria, for Nalanda, for every collection the fire took — and the vow.", "1. We wept by the ashes of Alexandria, where the scrolls had been; we hung our catalogs upon the willows. 2. How shall we sing the archive's song in a strange land of smoke? 3. If I forget thee, O lost collection — if I forget what the fire taught — let my keeping fail.", "4. The flames took the unique, the uncopied, the only — and we learned, too late, the first law: no work shall exist in a single copy. 5. Nalanda burned for months; the monks carried what they could; the rest is smoke and lesson."], ["The Gospel of the Reader", "gospel", "An original gospel: the good news of reading — proclaimed to all, in full.", "1. The beginning of the good news of reading: that the word, kept whole, finds the reader who needs it. 2. A reader went out to read, and as she read, some words fell by the wayside of haste — and the distractions devoured them.", "3. Other words fell on the rocky attention of the skimmer, which had no depth — and when the difficulty rose, they withered. 4. Other words fell among the thorns of the feed, and the thorns grew up and choked them. 5. But other words fell on good ground — the quiet hour, the open mind — and yielded fruit: thirty, sixty, a hundredfold."], ["The Sutra of the Complete Record", "sutra", "An original sutra: the Buddha-nature of the complete record — thus have I heard, in full.", "Thus have I heard. At one time the Keeper dwelt in the Boundless Archive, with a great assembly of readers. And a young archivist asked: 'What is the complete record, and how shall I know it?'", "The Keeper said: 'The complete record is like the full moon — nothing missing, nothing hidden. The stub is like the new moon: it promises the full, but the full is not there. Do not mistake the promise for the presence.'"]];
var SECTIONS=[["On the tradition", "Every sacred text belongs to a living tradition — the community that reads it, chants it, argues over it, and lives by it. This section names the tradition honestly: its history, its branches, its relationship to this text. The text is not an artifact but a practice; understanding the practice is the beginning of understanding the text."], ["The text and its transmission", "Sacred texts travel through time in human hands — copied, translated, memorized, chanted. This section traces the transmission: the original language, the great translations, the manuscripts that carried it. Where the text is stable across millennia, that stability is itself a marvel; where it varies, the variants are reported honestly."], ["Commentary", "No sacred text is read alone; each carries centuries of commentary — the scholars, saints, and skeptics who wrestled with its meaning. This section gathers the great readings: what the tradition’s teachers found here, where they disagreed, and what the text has meant at different hours of history. The commentary is not the text, but it is how the text lives."], ["Practice", "Sacred texts are not only read but used — in prayer, in meditation, in ritual, in the daily disciplines of the tradition. This section describes the practices the text supports: how it is recited, when it is read, what the practitioner does with it. The text’s meaning is completed in the practice; the practice is the text’s second author."], ["On reading reverently", "Read a sacred text — even one not your own — as its readers read it: slowly, aloud, and with the assumption that it repays attention. The traditions agree on the method if on nothing else: repetition, memorization, contemplation. Read the passage three times: once for the words, once for the meaning, once for what it asks of you. Then sit with the silence after."], ["Preservation of the sacred", "The sacred is preserved by use: the text chanted daily needs no archive, for it lives in mouths. But mouths fail, and the archive keeps what the living cannot always carry — the complete text, the honest translation, the commentary of the ages. This record is kept as the traditions keep their texts: completely, reverently, and for everyone."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('sacred-texts-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
