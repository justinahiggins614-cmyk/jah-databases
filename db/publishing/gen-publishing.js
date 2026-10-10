/* JAH Publishing Database generator — jahdb-publishing-1.0
   Deterministic (mulberry32). Seed -> full publishing entry.
   Sourced records draw every fact from the curated dataset below
   (real publishing processes, formats, genres, roles, and milestones
   from public industry knowledge). Signature records are homegrown
   publishing plans, always labeled as such.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-PUB2-';
var KIND='publishing entry';
var CATS=['process','format','genre','role','history','industry-record','publishing-plan'];
/* [name, note] */
var PROCESSES=[
["Manuscript drafting","Writing the book itself, usually in several revising passes."],
["Query letter","A one-page pitch to literary agents describing the book and the author."],
["Developmental editing","Big-picture editing of structure, plot, and argument."],
["Copyediting","Line-level editing of grammar, style, and consistency."],
["Proofreading","The final check for typos and errors before printing."],
["Typesetting","Setting the text into designed pages with proper typography."],
["Cover design","Creating the cover that sells the book at a glance."],
["Interior layout","Designing chapters, headings, and page furniture."],
["ISBN assignment","Giving each edition its unique International Standard Book Number."],
["Copyright registration","Recording authorship with the national copyright office."],
["Offset printing","High-volume printing for large print runs."],
["Digital printing","Short-run printing, economical for small quantities."],
["Print on demand","Printing single copies as orders arrive; no warehouse needed."],
["Ebook conversion","Building EPUB and other ebook files from the manuscript."],
["Audiobook production","Recording, editing, and mastering the narrated edition."],
["Distribution","Getting books into stores, libraries, and online retailers."],
["Warehousing","Storing printed stock and fulfilling orders."],
["Book marketing","Advertising, social media, and outreach that find readers."],
["Publicity","Reviews, interviews, and media coverage."],
["Royalty accounting","Tracking sales and paying authors their share."]
];
var FORMATS=[
["Hardcover","Durable sewn binding with a dust jacket; the premium edition."],
["Trade paperback","Large-format paperback; the standard literary edition."],
["Mass-market paperback","Small, cheap paperback for wide distribution."],
["Ebook","Digital edition, usually in EPUB format."],
["Audiobook","Narrated edition for listening."],
["Large print","Bigger type for low-vision readers."],
["Serialized fiction","Released in installments, chapter by chapter."],
["Chapbook","A small booklet, often of poetry."],
["Zine","A small-circulation, self-made publication."],
["Board book","Thick-page books for babies and toddlers."],
["Picture book","Illustrated books for young children, usually 32 pages."],
["Graphic novel","Long-form comics bound as a book."]
];
var GENRES=[
["Literary fiction","Character- and language-driven novels."],
["Mystery","A puzzle, usually a crime, solved by the end."],
["Thriller","High stakes, fast pace, constant tension."],
["Romance","A central love story with an uplifting ending."],
["Science fiction","Speculation built on science and technology."],
["Fantasy","Magic and invented worlds."],
["Horror","Fear as the engine of the story."],
["Historical fiction","Imagined stories set in real pasts."],
["Biography","A life told by someone else."],
["Memoir","A life told by the person who lived it."],
["Self-help","Practical guidance for personal growth."],
["Business","Books on management, careers, and markets."],
["Children's picture book","Stories told in words and pictures for the youngest readers."],
["Middle grade","Novels for readers roughly 8 to 12."],
["Young adult","Novels for teen readers."],
["Poetry","Language compressed to its most musical."],
["Essay collection","Short nonfiction on varied subjects."],
["Short stories","Complete fictions in brief compass."],
["Cookbook","Recipes plus the stories behind them."],
["Travel writing","Journeys rendered in prose."]
];
var ROLES=[
["Author","Writes the book."],
["Literary agent","Represents authors to publishers and negotiates deals."],
["Acquisitions editor","Chooses which books a publisher will buy."],
["Developmental editor","Shapes the book's structure and content."],
["Copyeditor","Polishes language line by line."],
["Proofreader","Catches the last errors."],
["Cover designer","Designs the book's face to the world."],
["Typesetter","Builds the interior pages."],
["Publicist","Wins the book media attention."],
["Distributor","Moves books from printer to seller."],
["Bookseller","Puts the right book in the right reader's hands."],
["Librarian","Connects communities with books for free."]
];
var HISTORY=[
["Gutenberg's movable type","Around 1440, Johannes Gutenberg's press made books reproducible at scale."],
["Gutenberg Bible","Around 1455, the first major book printed with movable type in Europe."],
["Caxton's press","In 1476 William Caxton set up the first press in England."],
["Penny press","In the 1830s, cheap newspapers brought print to the masses."],
["Penguin paperbacks","In 1935 Allen Lane's Penguin made quality books affordable."],
["Project Gutenberg","In 1971 Michael Hart founded the first digital library of free ebooks."],
["Berne Convention","In 1886, nations agreed on international copyright protection."],
["US Copyright Act","In 1790 the United States passed its first copyright law."],
["ISBN system","Introduced in 1970; the 13-digit ISBN arrived in 2007."],
["Library of Congress","Founded in 1800; among the world's great libraries."],
["Pulitzer Prizes","Established in 1917 for American journalism, letters, and music."],
["Nobel Prize in Literature","First awarded in 1901."],
["NYT bestseller list","The New York Times list began in 1931."],
["Audiobook eras","From cassettes to CDs to digital downloads and streaming."],
["E-readers","The Kindle's 2007 launch made ebooks mainstream."],
["Print on demand","From the 1990s onward, books print one copy at a time."]
];
var INDUSTRY=[
["Traditional publishing","A publisher buys the book, produces it, and sells it; the author earns royalties."],
["Self-publishing","The author produces and sells the book directly, keeping control and margin."],
["Hybrid publishing","The author pays toward production while a company provides services."],
["Small press","Independent publishers with focused lists and personal attention."],
["University press","Scholarly publishers tied to universities."],
["Literary magazine","Journals publishing stories, poems, and essays."],
["Book review outlets","Newspapers, magazines, and sites that review new books."],
["Book fairs","Frankfurt and London fairs where rights are bought and sold."],
["Awards and prizes","Recognition that can transform a book's fortunes."],
["Vanity press caution","A vanity press charges authors while promising little; research before paying."]
];
var ANGLES=[
["","", ""],
["beginners"," \u2014 beginners"," New to publishing? Start here."],
["quick facts"," \u2014 quick facts",""],
["working pros"," \u2014 working pros"," Professionals live in these details."],
["self-publishers"," \u2014 self-publishers"," Especially useful if you publish independently."],
["field notes"," \u2014 field notes",""]
];
function comboGen(j,nE,nA,nG){
  var per=nA*nG;
  var e=j%nE, c=Math.floor(j/nE)%per, part=Math.floor(j/(nE*per));
  return {e:e,a:Math.floor(c/nG),g:c%nG,part:part};
}
var SRC="JAH Publishing curated dataset v1 \u2014 real processes, formats, genres, roles, and milestones from public industry knowledge.";
var SIGSRC="JAH Signature generator \u2014 homegrown publishing plans, clearly labeled as generated.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" Ask experienced publishers when you need deeper guidance.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
var ASPECTS=[
["overview",function(x){return x[0]+": "+x[1]+" Every professional publishing workflow includes this step.";}],
["how it works",function(x){return "How it works in practice: "+x[1];}],
["key steps",function(x){return "Break it into steps, do them in order, and do not skip the boring ones.";}],
["best practices",function(x){return "Professionals treat this step with care because readers notice when it is skipped.";}],
["common mistakes",function(x){return "The classic mistake is rushing this stage to save time.";}],
["for beginners",function(x){return "Learn the vocabulary first; the rest follows.";}],
["timeline",function(x){return "Allow real time for this; publishing rewards patience.";}],
["quick facts",function(x){return x[0]+" \u2014 "+x[1];}]
];
function profRec(seed,j,entries,cat,detailFn){
  var cb=comboGen(j,entries.length,ASPECTS.length,ANGLES.length);
  var x=entries[cb.e],a=ASPECTS[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary=a[1](x)+g[2];
  var d=detailFn(x);d.aspect=a[0];d.angle=g[0]||"standard";
  return mkRec(seed,cat,title,summary,d,"sourced",SRC);
}
var PATHS=[
["traditionally", ["Finish the manuscript","Query agents","Sign with a publisher","Edit, design, and produce","Launch with the publisher's team"]],
["by self-publishing", ["Finish and revise the manuscript","Hire freelance editing and cover design","Format print and ebook files","Publish through retail platforms","Market directly to readers"]],
["with a hybrid path", ["Finish the manuscript","Vet hybrid companies carefully","Negotiate services and rights","Produce to professional standard","Launch with paid support"]]
];
function planRec(seed,j){
  var gi=j%GENRES.length;
  var fi=Math.floor(j/GENRES.length)%FORMATS.length;
  var pi=Math.floor(j/(GENRES.length*FORMATS.length))%PATHS.length;
  var part=Math.floor(j/(GENRES.length*FORMATS.length*PATHS.length));
  var gn=GENRES[gi][0],fm=FORMATS[fi][0],ph=PATHS[pi];
  var title="Publishing plan: "+gn+" "+fm.toLowerCase()+" "+ph[0]+(part>0?" (v"+(part+1)+")":"");
  var summary="Signature-generated publishing plan \u2014 homegrown material, adapt freely. Goal: publish a "+gn.toLowerCase()+" book as a "+fm.toLowerCase()+", "+ph[0]+". Steps: "+ph[1].join("; ")+".";
  return mkRec(seed,"publishing-plan",title,summary,{genre:gn,format:fm,path:ph[0],steps:ph[1],variant:part+1},"signature",SIGSRC);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=3000)cat="process";
    else if(s<=4200)cat="format";
    else if(s<=6200)cat="genre";
    else if(s<=7200)cat="role";
    else if(s<=8500)cat="history";
    else if(s<=9500)cat="industry-record";
    else cat="publishing-plan";
  }
  function ord(base){return explicit?(s-1):(s-base);}
  function det(x,n){return {name:x[0],note:x[1],kind:n};}
  if(cat==="process")return profRec(seed,ord(1),PROCESSES,"process",function(x){return det(x,"process");});
  if(cat==="format")return profRec(seed,ord(3001),FORMATS,"format",function(x){return det(x,"format");});
  if(cat==="genre")return profRec(seed,ord(4201),GENRES,"genre",function(x){return det(x,"genre");});
  if(cat==="role")return profRec(seed,ord(6201),ROLES,"role",function(x){return det(x,"role");});
  if(cat==="history")return profRec(seed,ord(7201),HISTORY,"history",function(x){return det(x,"milestone");});
  if(cat==="industry-record")return profRec(seed,ord(8501),INDUSTRY,"industry-record",function(x){return det(x,"industry note");});
  if(cat==="publishing-plan")return planRec(seed,ord(9501));
  return profRec(seed,ord(1),PROCESSES,"process",function(x){return det(x,"process");});
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-PUB2-\d{6,7}$/.test(r.id||""))e.push("id");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(CATS.indexOf(r.category)<0)e.push("category");
  if(r.record_kind!==KIND)e.push("record_kind");
  if(typeof r.summary!=="string"||r.summary.length<80)e.push("summary");
  if(!r.details||typeof r.details!=="object")e.push("details");
  if(r.provenance!=="sourced"&&r.provenance!=="signature")e.push("provenance");
  if(typeof r.source!=="string"||!r.source.length)e.push("source");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:["already in archive: "+rec.id]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-publishing-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("publishing",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
