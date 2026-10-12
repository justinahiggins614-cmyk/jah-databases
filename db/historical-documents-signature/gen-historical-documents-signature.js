(function(){'use strict';
/* Signature Historical Documents Database generator — jahdb-historical-documents-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature" = Signature-authored original (clearly labeled). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function escXml(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');}
function escUri(s){return encodeURIComponent(s).replace(/[!'()*]/g,function(c){return '%'+c.charCodeAt(0).toString(16).toUpperCase();});}
var PREFIX='JAH-HIS-SIG-';
var TYPELABEL='signature historical document';
var SRCSLUG='signature';
var TOPICS=[["The Charter of the Boundless Archive", "charter", "An original charter founding a boundless archive: its purposes, its powers, and its limits — the constitutional document of a collection without end.", "Article I establishes the archive's purpose: to keep complete works, label them truly, and make them findable — for readers living and unborn. Article II vests keeping-power in the keepers, bounded by the laws of completeness, truthful labeling, and sideways growth. Article III forbids the archive to destroy for convenience, to mislabel for advantage, or to close its doors to any reader.", "Article IV provides for the million-record march: the machinery shall be built for the millionth record from the hundredth, and tested at every scale. Article V reserves to the readers the final judgment: the archive serves them, not its keepers, and any law may be amended by the same care with which it was made. Done in the first year of the march, to bind the future."], ["A Declaration of the Reader's Rights", "declaration", "An original declaration enumerating the rights of every reader: what the archive — and every library — owes the person who walks in.", "We hold these truths to be self-evident: that every reader has the right to the complete work, not the excerpt; to the honest label, not the disguised advertisement; to find what is kept, through catalogs that actually work; to read without surveillance and without shame; to copy for study what the law allows; and to be welcomed regardless of credential, costume, or purpose.", "The declaration further holds that the reader has the right to quiet, to assistance cheerfully given, to the benefit of every doubt, and to leave with more than they came for. These rights are not granted by the archive but recognized by it — they belong to readers by nature, and the archive that denies them denies its own purpose."], ["Proclamation of the Long Maintenance", "proclamation", "An original proclamation declaring the doctrine of maintenance: that keeping is the work, and the work never ends.", "Whereas all things decay — iron rusts, vellum cockles, formats die, and even stone is weathered by rain — and whereas decay is patient and we must be more patient: now therefore it is proclaimed that maintenance is not the interruption of the work but the work itself, and that the keeper's highest art is the unglamorous tending by which things endure.", "Let it be known that oil shall be applied to hinges, paste to torn leaves, backups to databases, and attention to readers — regularly, cheerfully, and forever. Let no one despise the rota, the checklist, or the cleaning day; these are the liturgy of endurance. The proclamation shall remain in force until entropy is repealed."], ["The Covenant of the Generators", "covenant", "An original covenant governing the archive's generators: what the machines may make, and the humans' duty over them.", "The generators are bound by this covenant: to make full works, never stubs; to be deterministic, the same seed yielding the same work forever; to submit every work to validation before filing; and to drift-check against the archive, that new work honor old. These are the machines' articles, and they are not negotiable.", "The humans are bound in turn: to judge what is filed and what is refused; to never file blindly what the machine made swiftly; to label machine work truly; and to keep the generators' machinery plain enough to rebuild. The covenant's final article is its first principle: the machines serve the archive, the archive serves the readers, and the chain of service runs one way."], ["Edict on the Preservation of Formats", "edict", "An original edict on digital preservation: the formats shall be open, the masters kept, and no work shall depend on a single company's survival.", "It is decreed: that every work shall be kept in an open format readable without proprietary tools; that the highest-quality master shall be preserved alongside every access copy; that no work shall be entrusted solely to a format owned by a living corporation; and that migration to new formats shall be continuous, scheduled, and tested — not panicked, when the old format dies.", "The edict further requires that the preservation plan be written down, reviewed yearly, and simple enough that a new keeper can execute it. Formats are mortal; the edict intends the works to be otherwise. Let the file extensions change a hundred times — the texts shall persist."], ["The Petition of the Quiet Readers", "petition", "An original petition from the archive's quiet readers: those who never complain, never ask, and deserve everything.", "We, the quiet readers — the ones who reshelve correctly, who whisper, who never need to be told — respectfully petition for the following, which we will never ask for aloud: chairs that do not punish long sitting; light sufficient for old eyes; outlets for the devices we pretend not to need; and staff who understand that our silence is not absence but attention.", "We further petition that the rules be enforced against the loud, not the quiet — that the phone-talker be addressed before the sleeper is woken. We ask little, as is our way. Grant this, and we will do what we have always done: read, return, and come back tomorrow."], ["Charter of the Traveling Exhibition", "charter", "An original charter for exhibitions that travel: how the archive's treasures may go into the world and come home safe.", "The traveling exhibition is chartered on these terms: that every loan be documented to the nail; that couriers accompany the irreplaceable; that light, humidity, and handling be specified and monitored; that insurance reflect the true value — which for the unique is infinite, and so the unique travels rarely and with ceremony.", "The charter's deeper article is its purpose: exhibitions exist so the archive's wonders may meet the readers who cannot come to the archive — the schoolchild, the distant scholar, the curious stranger. The treasures travel that the idea of the archive may travel further: that keeping is a public trust, and the public is everywhere."], ["Declaration of Interdependence of Collections", "declaration", "An original declaration: that no archive stands alone, and the collections of the world are one collection with many doors.", "We declare that the world's archives, libraries, and museums form a single distributed collection — that the manuscript in London, the scroll in Jerusalem, and the codex in Timbuktu are neighbors in a neighborhood with no fences. No institution owns the past; each holds part of it in trust for all.", "Therefore we pledge: to share catalogs openly, to lend generously, to digitize cooperatively, to repatriate where justice requires, and to compete only in service. The declaration's final article is practical: when in doubt, ask what serves the reader, not the institution — and do that."], ["The Archivist's Bill of Rights", "bill-of-rights", "An original bill of rights for archivists and librarians: what the keepers are owed by the institutions they serve.", "Article I: the keeper shall have the resources to keep — boxes, shelves, systems, and staff — for responsibility without resources is blame without power. Article II: the keeper shall have professional independence in appraisal and description; no donor, board, or government shall dictate what is kept or how it is labeled.", "Article III: the keeper shall have time — the backlog acknowledged, the quiet years honored, the slow work respected. Article IV: the keeper shall have training and succession; no archive shall depend on one memory. Article V: the keeper shall have the public's trust, earned by transparency and kept by truth. These rights secure the keepers, that the keepers may secure the records."], ["Manifesto of the Complete Record", "manifesto", "An original manifesto: against the stub, the excerpt, the description posing as the thing — for the complete record.", "We, the keepers of the boundless archive, manifest the following: that a database of descriptions is a catalog of absences; that the reader came for the work and shall have the work; that 'full text' means full; that the generator that makes stubs makes litter; and that completeness is not a luxury of scale but the precondition of trust.", "The manifesto's program is plain: every record complete or plainly marked partial; every file whole; every text entire. We will be judged by what we kept, and keeping half is not keeping. The complete record or nothing — and we choose the record."], ["The Address to the Millionth Record", "address", "An original address prepared for the filing of the archive's millionth record: what the milestone means.", "Friends, readers, keepers: we file today the millionth record — a number we chose not from vanity but from discipline. A thousand records can be kept by enthusiasm; a million requires machinery, law, and care. The millionth record proves the system real.", "But the address warns against worshipping the number: the millionth record matters exactly as much as the first — one complete work, truly labeled, findable by a stranger. The milestone is not the mountain; it is the proof that the path holds. We dedicate the millionth record to the first reader who needs it — unknown, unborn perhaps — and we keep marching."], ["Covenant with the Future", "covenant", "An original covenant between the present archive and the future: what we promise the readers unborn.", "We, the keepers of the present, covenant with the readers of the future: to keep the works complete, the labels true, and the doors open; to build machinery you can rebuild; to write down what we know and mark what we guess; to grow without destroying; and to remember, in every decision, that you are the reason.", "In return we ask only what every covenant asks: that you keep the covenant — tend the archive, amend the laws with care, and write your own covenant with the future beyond you. The chain of keeping is the longest human project. Take your link. Hold it well."], ["The Edict of Open Doors", "edict", "An original edict: the archive's doors shall be open to all, and the meaning of 'all' shall not be narrowed.", "It is decreed that the archive admits every reader — the credentialed and the curious, the scholar and the schoolchild, the citizen and the stranger — without test of worthiness. 'All' means all: no reader shall be turned away for dress, accent, age, or the unfashionableness of their question.", "The edict provides for the practical: hours generous, fees none, assistance cheerful, rules few and kind. And it warns: every barrier raised against a reader must justify itself, for the default is openness and the burden of proof lies on the gate. The doors are open. Come in."], ["Proclamation of the Reading Hour", "proclamation", "An original proclamation establishing a daily reading hour: one hour a day for the book, protected by custom.", "Whereas the day conspires against reading — the bells, the feeds, the small urgencies — now therefore it is proclaimed that one hour each day is set apart for the book: no messages, no meetings, no multitasking, only the text and the attention it deserves. The hour is portable and non-negotiable.", "The proclamation recommends the practices of the hour: the comfortable chair, the pencil for the margin, the dictionary within reach, the phone in another room. It promises the hour's reward: that the reader who keeps it will, within a season, have read what the hurried only intended to. Let the hour be kept."], ["The Charter of Small Branches", "charter", "An original charter for the archive's smallest outposts: the village shelf, the bookmobile, the single-room library — chartered with full dignity.", "The small branch is chartered as equal in dignity to the greatest central library: its hundred books are a complete collection for its readers, its single keeper a full keeper, its reading corner a true reading room. Size is not significance; the branch serves its hundred as the great library serves its million.", "The charter provides: that the small branch shall have the network's full catalog at its call; that its keeper shall have training and a voice; and that no efficiency shall close it while readers use it. The archive's greatness is measured at its edges — by the farthest reader served, not the grandest hall built."]];
var SECTIONS=[["Historical context", "No document is born alone; each is the child of its crisis. Read first for the pressure that produced it: the war, the tyranny, the movement, the long grievance that finally found words. The context does not excuse the document, but it explains its urgency — why these words, in this order, at this hour. A document without its context is a verdict without its trial."], ["The text and its structure", "Great documents are built like buildings: a foundation of principle, walls of grievance or resolve, and a roof of action. Study the architecture — the preamble that states the why, the articles that state the what, the closing that states the who and when. The structure is itself an argument about how the world should be ordered."], ["Immediate impact", "What happened next belongs to the record. Some documents were obeyed at once; some were ignored for decades and then obeyed all at once; some were obeyed in ways their authors never intended. The immediate impact is told plainly, with dates and consequences — for a document’s first readers decide its first meaning."], ["Long legacy", "The long legacy is where documents become immortal — or irrelevant. Trace the citations, the imitations, the constitutions modeled on this one, the movements that claimed it. A living document is one still being argued about; this section records the argument as it stands, centuries or decades on."], ["On authenticity", "The archive states plainly what is known about each text: its sources, its transmission, its disputed passages. Where scholars disagree, the disagreement is reported, not hidden. A public record earns trust by showing its seams — the variant readings, the lost originals, the copies of copies. What is certain is marked certain; what is not is marked not."], ["Reading counsel", "Read the document aloud once, all the way through, as its first audience heard it — these texts were made for voices in halls, not eyes on screens. Then read it slowly, article by article, asking of each: whom does this protect, whom does this restrain, and what does it cost? The answers are the document’s real text, beneath the parchment."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('historical-documents-signature',{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
