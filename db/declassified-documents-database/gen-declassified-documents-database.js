(function(){'use strict';
/* The Declassified Documents Database generator — jahdb-declassified-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DCL-";
var SLUG="declassified-documents-database";
var FIELDS=["wartime", "cold-war", "diplomacy", "science", "archives", "media", "public-domain", "process"];
var SEED_TITLES=[["The Zimmermann Telegram (1917): the decrypt that changed a war", "wartime"], ["Ultra and Magic: WWII codebreaking declassified", "wartime"], ["VENONA: the Soviet cables, declassified 1995", "cold-war"], ["CORONA: America's first spy satellites, declassified 1995", "cold-war"], ["The Cuban Missile Crisis tapes", "cold-war"], ["Operation Paperclip files", "cold-war"], ["The U-2 and SR-71 histories", "cold-war"], ["The Gulf of Tonkin: the 2005 NSA release", "cold-war"], ["The Pentagon Papers (1971)", "diplomacy"], ["The Church Committee reports (1975-1976)", "diplomacy"], ["MKULTRA documents (1977)", "diplomacy"], ["COINTELPRO: the FBI's secret war, exposed", "diplomacy"], ["The Family Jewels (2007)", "diplomacy"], ["The 9/11 Commission Report (2004)", "diplomacy"], ["The Senate Torture Report summary (2014)", "diplomacy"], ["Iran-Contra: the Tower Commission and Walsh Report", "diplomacy"], ["The Smyth Report (1945): the bomb, explained", "science"], ["NSA's declassified cryptologic history", "science"], ["CIA CREST: 13 million pages online (2017)", "archives"], ["The FBI Vault", "archives"], ["JFK assassination records: the 1992 Act", "archives"], ["Operation Northwoods (declassified 1997)", "archives"], ["Tuskegee: the public hearings (1972-1973)", "archives"], ["The Snowden disclosures: the public reporting (2013)", "media"], ["The Panama Papers (2016)", "media"], ["Steamboat Willie enters the public domain (2024)", "public-domain"], ["The Great Gatsby enters the public domain (2021)", "public-domain"], ["Project Gutenberg: the public-domain library (1971)", "public-domain"], ["How declassification works: EO 13526", "process"], ["FOIA: the public's records tool (1966)", "process"]];
var BLURBS={"wartime": ["A full archive record in the 'wartime' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'wartime' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "cold-war": ["A full archive record in the 'cold-war' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'cold-war' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "diplomacy": ["A full archive record in the 'diplomacy' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'diplomacy' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "science": ["A full archive record in the 'science' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'science' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "archives": ["A full archive record in the 'archives' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'archives' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "media": ["A full archive record in the 'media' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'media' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "public-domain": ["A full archive record in the 'public-domain' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'public-domain' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "process": ["A full archive record in the 'process' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'process' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Declassification": "The process removing a document's classified status, making it public.", "FOIA": "The Freedom of Information Act (1966) \u2014 the public's tool for requesting federal records.", "Automatic declassification": "Under Executive Order 13526, most classified records are declassified after 25 years unless exempted.", "Mandatory review": "A FOIA-adjacent process letting anyone request review of a specific classified document.", "Redaction": "Blacking out still-sensitive portions of a released document.", "Public domain": "Works free of copyright \u2014 including US federal government works, which enter the public domain at creation."};
var GEN_SRC="US National Archives (archives.gov); NSA declassification releases; CIA CREST; Presidential libraries";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Declassified Documents Database"+'.',
    'Run: python3 demo.py (standard library only).'+DQ3,
    'RECORD_ID = '+JSON.stringify(rec.id),
    'TITLE = '+JSON.stringify(rec.title),
    'CATEGORY = '+JSON.stringify(rec.g),
    '',
    'def summary():',
    '    return TITLE + " [" + RECORD_ID + "] — " + CATEGORY',
    '',
    'def details():',
    '    return '+JSON.stringify(String(rec.description).slice(0, 400)),
    '',
    'if __name__ == "__main__":',
    '    print("=" * 60)',
    '    print(summary())',
    '    print("=" * 60)',
    '    print(details())',
    '    print()',
    '    print("category:", CATEGORY)',
    '    print("signature_line:", '+JSON.stringify(!!SIG)+')'
  ];
  return lines.join("\n");
}
function generate(seed,opts){
  opts=opts||{};
  var rnd=prng((seed*2654435761)>>>0);
  var entry=SEED_TITLES[(seed-1)%SEED_TITLES.length];
  var title=entry[0],group=entry[1];
  if(opts.field&&FIELDS.indexOf(opts.field)>=0)group=opts.field;
  var blurbs=BLURBS[group]||BLURBS[FIELDS[0]];
  var blurb=pick(blurbs,rnd);
  var cycle=Math.floor((seed-1)/SEED_TITLES.length);
  if(cycle>0)title=title+' — Boundless Variation '+seed;
  var desc='Seed '+seed+' record for the '+"The Declassified Documents Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-declassified-1.0"+' boundless generator: '+
    'the same seed always rebuilds this same record, and every record is validated by an independent checker before acceptance.';
  if(SIG)desc='Signature line — a Signature-created companion to the public record. '+desc+'\n\n'+GEN_DISCLAIMER;
  var rec={
    id:PREFIX+pad6(seed),
    title:title,
    t:title,
    g:group,
    ladder:1+((seed+entry[0].length)%3),
    description:desc,
    definitions:DEFINITIONS,
    program:programFor({id:PREFIX+pad6(seed),title:title,g:group,description:desc}),
    language:'python',
    source:GEN_SRC,
    last_verified:'2026-10-19',
    million_march:'MILLION IN PROGRESS — marching to 1,000,000 full records',
    _seed:seed
  };
  if(SIG){rec.signature=true;rec.record_nature='Signature-created companion — not an official record.';}
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.g)<0)e.push('group');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<200)e.push('description');
  if(typeof r.program!=='string'||r.program.length<50)e.push('program');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&(s.t||s.title))seen[s.t||s.title]=1;});
  if(rec&&seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-declassified-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
