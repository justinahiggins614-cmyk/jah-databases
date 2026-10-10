/* ✳ SIGNATURE — JAH Rare Book Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic generator over a 1,000,000-address space (seeds 0..999999 map to
   JAH-RB-0000001 .. JAH-RB-1000000). Browser: registers with JAHDB. Node:
   run `node gen-rare-books.js` for the 40/40 self-test harness. */
(function(){
'use strict';
var SLUG='rare-books', PREFIX='JAH-RB-', VERSION='jahdb-rare-books-1.0';
var KIND='rare book', AI='JAH Rare Book Creator';
var CATEGORIES=["incunabula", "first-editions", "manuscripts", "maps", "science", "literature", "americana", "bibles"];
var MAKERS=["Signature Press", "JAH Fine Press", "Meridian Press", "Heritage Book Atelier", "Apex Fine Books", "Continental Press", "Paramount Editions", "Golden Quill Press", "Vantage Fine Press", "Legacy Book House", "Copperline Press", "Regent Editions"], LINES=["Centennial Edition", "Founder Imprint", "Heritage Folio", "Atelier Edition", "Collector Imprint", "Golden Age", "Pioneer Press", "Masterwork Series", "Origin Imprint", "Legacy Folio"], WORDS=["a hand-sewn binding", "deckle-edged handmade paper", "a numbered limitation page", "letterpress printing", "a morocco leather binding", "gilt top edges", "a slipcase enclosure", "a signed colophon"], DESCS=["Folio", "Quarto", "Octavo", "Manuscript", "Atlas", "Bestiary", "Herbal", "Psalter", "Chronicle", "Treatise", "Compendium", "Codex"];
var SPEC_KEYS=["Format", "Pages", "Printing", "Binding", "Limitation", "Condition"], SPEC_VALS=[["folio", "quarto", "octavo", "folio"], ["240 pp.", "380 pp.", "512 pp.", "128 pp."], ["letterpress", "hand-set type", "fine press", "offset"], ["full morocco", "quarter cloth", "vellum", "boards"], ["numbered to 250", "numbered to 100", "numbered to 500", "unnumbered"], ["fine", "near fine", "very good", "mint"]];
var OPENERS=["Documented here as %s, this %s is a matter of public record.", "The archive holds this %s under %s, preserved as a full file.", "Filed in this database as %s, this %s carries verified facts.", "This database records the %s under %s with its facts checked."];
var FACTS=[{"t": "Gutenberg Bible", "mk": "Johann Gutenberg, Mainz", "yr": "1455", "cat": "bibles", "blurb": "The first substantial book printed with movable type, c. 1455; 49 copies survive.", "spec": {"Printer": "Gutenberg, Mainz", "Date": "c. 1455", "Surviving": "49 copies", "Note": "First movable-type book"}, "ref": "Incunabula scholarship; British Library holdings."}, {"t": "Shakespeare First Folio", "mk": "William Jaggard, London", "yr": "1623", "cat": "literature", "blurb": "The 1623 collection preserving 36 plays, 18 never printed before; about 230 survive.", "spec": {"Title": "Mr. William Shakespeares Comedies", "Date": "1623", "Plays": "36, 18 first printed", "Surviving": "~230"}, "ref": "Folger Shakespeare Library census."}, {"t": "The Birds of America — Audubon", "mk": "John James Audubon", "yr": "1827", "cat": "americana", "blurb": "The double-elephant folio of 435 hand-colored plates, issued 1827-1838; a set sold for $11.5 million in 2010.", "spec": {"Author": "John James Audubon", "Issued": "1827-1838", "Plates": "435 hand-colored", "Record": "$11.5M, 2010"}, "ref": "Sotheby's sale record, December 2010."}, {"t": "Bay Psalm Book", "mk": "Stephen Daye, Cambridge MA", "yr": "1640", "cat": "americana", "blurb": "The first book printed in British America; one of eleven survivors sold for $14.2 million in 2013.", "spec": {"Printer": "Stephen Daye", "Date": "1640", "Note": "First American book", "Record": "$14.2M, 2013"}, "ref": "Sotheby's sale record, November 2013."}, {"t": "Codex Leicester", "mk": "Leonardo da Vinci", "yr": "1510", "cat": "manuscripts", "blurb": "Leonardo's 72-page scientific manuscript, bought by Bill Gates for $30.8 million in 1994.", "spec": {"Author": "Leonardo da Vinci", "Date": "c. 1506-1510", "Pages": "72", "Record": "$30.8M, 1994"}, "ref": "Christie's sale record, November 1994."}, {"t": "Canterbury Tales — Caxton", "mk": "William Caxton", "yr": "1478", "cat": "incunabula", "blurb": "Caxton's 1478 second edition of Chaucer, the first great book printed in England.", "spec": {"Printer": "William Caxton", "Date": "1478", "Author": "Geoffrey Chaucer", "Note": "First English literary classic"}, "ref": "Incunabula scholarship; British Library."}, {"t": "Don Quixote, First Edition", "mk": "Juan de la Cuesta, Madrid", "yr": "1605", "cat": "literature", "blurb": "Cervantes' 1605 first part, the founding novel of modern literature.", "spec": {"Author": "Miguel de Cervantes", "Date": "1605", "Printer": "Juan de la Cuesta", "Note": "First modern novel"}, "ref": "Cervantine bibliography."}, {"t": "On the Origin of Species, First Edition", "mk": "John Murray, London", "yr": "1859", "cat": "science", "blurb": "Darwin's 1859 first edition of 1,250 copies, the book that changed biology.", "spec": {"Author": "Charles Darwin", "Date": "1859", "Print run": "1,250", "Legacy": "Founded evolutionary biology"}, "ref": "Darwin bibliography, Freeman."}, {"t": "Philosophiae Naturalis Principia Mathematica", "mk": "Royal Society, London", "yr": "1687", "cat": "science", "blurb": "Newton's 1687 Principia, the foundation of classical mechanics.", "spec": {"Author": "Isaac Newton", "Date": "1687", "Content": "Laws of motion, gravity", "Legacy": "Foundation of physics"}, "ref": "Newton bibliography."}, {"t": "De Revolutionibus — Copernicus", "mk": "Johannes Petreius, Nuremberg", "yr": "1543", "cat": "science", "blurb": "Copernicus's 1543 heliocentric treatise that moved the Earth from the center of the universe.", "spec": {"Author": "Nicolaus Copernicus", "Date": "1543", "Thesis": "Heliocentrism", "Legacy": "Copernican revolution"}, "ref": "Copernican bibliography."}, {"t": "Sidereus Nuncius — Galileo", "mk": "Venice", "yr": "1610", "cat": "science", "blurb": "Galileo's 1610 announcement of the Medicean stars, the birth of telescopic astronomy.", "spec": {"Author": "Galileo Galilei", "Date": "1610", "Content": "Jupiter's moons", "Legacy": "Telescopic astronomy"}, "ref": "Galileo bibliography."}, {"t": "De Humani Corporis Fabrica — Vesalius", "mk": "Johannes Oporinus, Basel", "yr": "1543", "cat": "science", "blurb": "Vesalius's 1543 illustrated anatomy that founded modern medicine's visual language.", "spec": {"Author": "Andreas Vesalius", "Date": "1543", "Content": "Human anatomy, illustrated", "Legacy": "Modern anatomy"}, "ref": "Vesalius bibliography."}, {"t": "Nuremberg Chronicle", "mk": "Anton Koberger, Nuremberg", "yr": "1493", "cat": "incunabula", "blurb": "Hartmann Schedel's 1493 world history with 1,809 woodcut illustrations.", "spec": {"Author": "Hartmann Schedel", "Date": "1493", "Illustrations": "1,809 woodcuts", "Note": "Great incunable chronicle"}, "ref": "Incunabula scholarship."}, {"t": "Hypnerotomachia Poliphili", "mk": "Aldus Manutius, Venice", "yr": "1499", "cat": "incunabula", "blurb": "The 1499 Aldine dream-romance, the most beautiful illustrated book of the Renaissance.", "spec": {"Printer": "Aldus Manutius", "Date": "1499", "Note": "Most beautiful Renaissance book", "Illustrations": "Woodcuts"}, "ref": "Aldine bibliography."}, {"t": "Ulysses — Joyce, First Edition", "mk": "Shakespeare and Company, Paris", "yr": "1922", "cat": "first-editions", "blurb": "The 1922 Paris first edition of Joyce's novel, printed by Sylvia Beach in an edition of 1,000.", "spec": {"Author": "James Joyce", "Date": "1922", "Publisher": "Shakespeare and Company", "Edition": "1,000 copies"}, "ref": "Joyce bibliography, Slocum."}, {"t": "The Great Gatsby, First Edition", "mk": "Charles Scribner's Sons", "yr": "1925", "cat": "first-editions", "blurb": "The 1925 first edition in the Francis Cugat dust jacket, the most famous jacket in American books.", "spec": {"Author": "F. Scott Fitzgerald", "Date": "1925", "Jacket": "Francis Cugat art", "Note": "Iconic dust jacket"}, "ref": "Fitzgerald bibliography, Bruccoli."}, {"t": "Frankenstein, First Edition", "mk": "Lackington, Hughes, London", "yr": "1818", "cat": "first-editions", "blurb": "Mary Shelley's 1818 three-volume first edition, published anonymously.", "spec": {"Author": "Mary Shelley", "Date": "1818", "Format": "Three volumes", "Note": "Anonymous first"}, "ref": "Shelley bibliography."}, {"t": "Moby-Dick, First American Edition", "mk": "Harper & Brothers, New York", "yr": "1851", "cat": "first-editions", "blurb": "Melville's 1851 first American edition, titled Moby-Dick after the London \"Whale\".", "spec": {"Author": "Herman Melville", "Date": "1851", "Title": "Moby-Dick (US)", "Note": "First American edition"}, "ref": "Melville bibliography."}, {"t": "Leaves of Grass, First Edition", "mk": "Self-published, Brooklyn", "yr": "1855", "cat": "first-editions", "blurb": "Whitman's self-printed 1855 first edition of twelve untitled poems, 795 copies.", "spec": {"Author": "Walt Whitman", "Date": "1855", "Print run": "795", "Note": "Self-published"}, "ref": "Whitman bibliography."}, {"t": "Alice's Adventures in Wonderland, First Edition", "mk": "Macmillan, London", "yr": "1865", "cat": "first-editions", "blurb": "The recalled 1865 first edition, withdrawn over Tenniel's objections to the printing.", "spec": {"Author": "Lewis Carroll", "Date": "1865", "Illustrator": "John Tenniel", "Note": "Recalled first issue"}, "ref": "Carroll bibliography."}, {"t": "A Christmas Carol, First Edition", "mk": "Chapman & Hall, London", "yr": "1843", "cat": "first-editions", "blurb": "Dickens's 1843 first edition in brown cloth with gilt, published at his own expense.", "spec": {"Author": "Charles Dickens", "Date": "1843", "Binding": "Brown cloth, gilt", "Note": "Author-financed"}, "ref": "Dickens bibliography, Smith."}, {"t": "The Hobbit, First Edition", "mk": "George Allen & Unwin", "yr": "1937", "cat": "first-editions", "blurb": "Tolkien's 1937 first edition with his own dust-jacket art, 1,500 copies.", "spec": {"Author": "J.R.R. Tolkien", "Date": "1937", "Print run": "1,500", "Jacket": "Author's own art"}, "ref": "Tolkien bibliography, Hammond."}, {"t": "Harry Potter and the Philosopher's Stone, First Edition", "mk": "Bloomsbury, London", "yr": "1997", "cat": "first-editions", "blurb": "The 1997 first edition of 500 copies, the most valuable modern children's book.", "spec": {"Author": "J.K. Rowling", "Date": "1997", "Print run": "500", "Note": "Scarce modern first"}, "ref": "Modern first-edition market records."}, {"t": "Kelmscott Chaucer", "mk": "Kelmscott Press", "yr": "1896", "cat": "first-editions", "blurb": "William Morris's 1896 Chaucer with Burne-Jones illustrations, the apex of the private press movement.", "spec": {"Printer": "Kelmscott Press", "Date": "1896", "Illustrator": "Edward Burne-Jones", "Note": "Private-press apex"}, "ref": "Kelmscott bibliography, Peterson."}];
var NOTE_SIG='This is a Signature version in the Signature system: an original creation of the JAH Databases, property of Justin Addam Higgins (JAH).';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(rnd,a){return a[Math.floor(rnd()*a.length)%a.length];}
function pad7(n){return String(n).padStart(7,'0');}
function fmt2(s,a,b){var i=0;return s.replace(/%s/g,function(){return (i++===0)?a:b;});}
function sigRecord(seed,rnd){
  var rid=PREFIX+pad7(seed+1);
  var g=pick(rnd,CATEGORIES);
  var maker=pick(rnd,MAKERS), line=pick(rnd,LINES), desc=pick(rnd,DESCS);
  var num=1+Math.floor(rnd()*899);
  var title=maker+' '+line+' '+desc+' '+num;
  var w1=pick(rnd,WORDS), w2=pick(rnd,WORDS), w3=pick(rnd,WORDS);
  var facts={}, i;
  for(i=0;i<SPEC_KEYS.length;i++){facts[SPEC_KEYS[i]]=pick(rnd,SPEC_VALS[i]);}
  return {
    id:rid, t:title, c:Math.floor(seed/100)+1, g:g,
    title:title, kind:KIND, category:g, maker:maker, series:line,
    description:'A Signature '+KIND+' from '+maker+', in the '+line+' series: '+w1+', finished with '+w2+'.',
    overview:'The '+title+' is an original '+KIND+' created in the Signature system under '+AI+'. It carries '+w1+' and '+w3+', and every example is documented with full provenance in this database. As a Signature version, it is an original work \u2014 never a copy of another maker\u2019s piece \u2014 and it is built to the same full-file standard as every record in the archive.',
    spotlight:'Collectors value the '+line+' for its '+w2+' and the '+line+' series\u2019 reputation for '+w3+'. Each record in this database holds the complete file for its '+KIND+': full description, specifications, and Signature lineage, readable as plain sentences and paragraphs.',
    facts:facts,
    source:'signature',
    source_ref:'Generated by '+AI+' \u2014 Signature version in the Signature system.',
    signature_version:true,
    signature_note:NOTE_SIG
  };
}
function factRecord(seed,rnd){
  var rid=PREFIX+pad7(seed+1);
  var fi=Math.floor(seed/5), f=FACTS[fi%FACTS.length];
  var angle=Math.floor(fi/FACTS.length)%3;
  var open=fmt2(pick(rnd,OPENERS),rid,KIND);
  var overview, spotlight;
  if(angle===0){
    overview=open+' '+f.blurb+' Made by '+f.mk+' in '+f.yr+', it stands as a reference point collectors return to again and again.';
    spotlight='Its place in history is secure: students of '+KIND+' study this piece the way scholars study landmark texts. The facts table below carries the verified particulars.';
  }else if(angle===1){
    overview=open+' '+f.blurb+' On the market it is a blue-chip holding \u2014 the kind of piece that anchors serious collections and headlines landmark sales.';
    spotlight='For the collector, condition and provenance decide everything with a piece like this. Documented examples with clean history command the strongest results, and this database keeps the full file so the facts travel with the '+KIND+'.';
  }else{
    overview=open+' '+f.blurb+' The technical particulars below are the verified reference collectors check first.';
    spotlight='Every detail in the facts table is drawn from published references and maker records. Where this database also holds a Signature version of the same idea, the counterpart link below connects the fact-checked original to its Signature companion.';
  }
  var cs=((seed+1)%5!==0)?seed+1:seed+2;
  return {
    id:rid, t:f.t, c:Math.floor(seed/100)+1, g:f.cat,
    title:f.t, kind:KIND, category:f.cat, maker:f.mk, year:f.yr,
    description:f.blurb, overview:overview, spotlight:spotlight,
    facts:f.spec,
    source:'fact-checked',
    source_ref:f.ref,
    signature_counterpart:PREFIX+pad7(cs+1),
    signature_version:true,
    signature_note:'Fact-checked real-world record. This database is a Signature version in the Signature system; the Signature counterpart linked above is the Signature-system companion to this verified item.'
  };
}
function generate(seed,opts,rnd){
  seed=(typeof seed==='number')?seed:0;
  rnd=rnd||prng(seed);
  var rec=(seed%5===0)?factRecord(seed,rnd):sigRecord(seed,rnd);
  if(opts&&opts.category&&CATEGORIES.indexOf(opts.category)>=0){rec.g=opts.category;rec.category=opts.category;}
  return rec;
}
function validate(rec){
  var errs=[];
  if(!rec||typeof rec!=='object')return{ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/[-\/\\^$*+?.()|[\]{}]/g,'\\$&')+'\\d{7}$').test(String(rec.id)))errs.push('bad id');
  ['t','title','description','overview','spotlight','facts','source','signature_version','g','c'].forEach(function(k){
    if(rec[k]===null||rec[k]===undefined||rec[k]==='')errs.push('missing '+k);
  });
  if(CATEGORIES.indexOf(rec.g)<0)errs.push('bad category');
  if(rec.source!=='fact-checked'&&rec.source!=='signature')errs.push('bad source');
  if(rec.signature_version!==true)errs.push('not marked signature_version');
  if(String(rec.overview||'').length+String(rec.spotlight||'').length<150)errs.push('narrative too short');
  if(JSON.stringify(rec).indexOf('word-break')>=0)errs.push('forbidden word-break');
  if(rec.source==='fact-checked'&&!rec.source_ref)errs.push('fact-checked without source_ref');
  return{ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  var errs=[];
  (sample||[]).forEach(function(s){
    if(s.id===rec.id)errs.push('duplicate id '+rec.id);
    else if(s.t===rec.t)errs.push('duplicate title '+rec.t);
  });
  return{ok:errs.length===0,errors:errs};
}
var gen={version:VERSION,generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'){module.exports=gen;module.exports.SLUG=SLUG;module.exports.PREFIX=PREFIX;module.exports.CATEGORIES=CATEGORIES;}
/* ---------------- 40/40 self-test harness (node) ---------------- */
if(typeof require!=='undefined'&&typeof process!=='undefined'&&require.main===module){runSelfTest();}
function runSelfTest(){
  var pass=0,fail=0;
  function t(name,cond){if(cond){pass++;}else{fail++;console.log('FAIL: '+name);}}
  var seeds=[0,1,7,42,999,2500,123456,999999];
  var i,s;
  for(i=0;i<8;i++){s=seeds[i];t('determinism seed '+s,JSON.stringify(generate(s,{}))===JSON.stringify(generate(s,{})));}
  var vseeds=[0,1,2,3,6,11,42];
  for(i=0;i<7;i++){s=vseeds[i];t('validate seed '+s,validate(generate(s,{})).ok);}
  t('validate rejects empty',!validate({}).ok);
  t('validate rejects bad source',!validate((function(){var r=generate(1,{});r.source='bogus';return r;})()).ok);
  var idre=new RegExp('^'+PREFIX+'\\d{7}$');
  var fseeds=[0,1,7,999];
  for(i=0;i<4;i++){s=fseeds[i];t('id format seed '+s,idre.test(generate(s,{}).id));}
  t('id seed 0 -> 0000001',generate(0,{}).id===PREFIX+'0000001');
  t('id seed 999999 -> 1000000',generate(999999,{}).id===PREFIX+'1000000');
  var seen={},dup=false;
  for(i=0;i<8;i++){s=seeds[i];var id=generate(s,{}).id;if(seen[id])dup=true;seen[id]=1;}
  t('ids unique across 8 seeds',!dup);
  t('id derives from seed',generate(424242,{}).id===PREFIX+'0424243');
  t('id zero-padded 7',generate(5,{}).id.length===PREFIX.length+7);
  var cseeds=[0,1,7,42,999];
  for(i=0;i<5;i++){s=cseeds[i];t('category valid seed '+s,CATEGORIES.indexOf(generate(s,{}).g)>=0);}
  var r0=generate(0,{}),r1=generate(1,{});
  t('field title present',!!r1.title);
  t('field source present',!!r1.source);
  t('narrative >150 chars',String(r1.overview).length+String(r1.spotlight).length>150);
  t('signature_version true',r1.signature_version===true);
  t('fact seed has source_ref',!!r0.source_ref);
  t('fact seed has counterpart',!!r0.signature_counterpart);
  t('sig seed source=signature',r1.source==='signature');
  t('no word-break in record',JSON.stringify(generate(12345,{})).indexOf('word-break')<0);
  t('driftCheck clean',driftCheck(r1,[{id:'X',t:'Y'}]).ok);
  console.log('SELFTEST '+SLUG+': '+pass+'/40 passed'+(fail?' ('+fail+' FAILED)':''));
  process.exitCode=fail?1:0;
}
})();
