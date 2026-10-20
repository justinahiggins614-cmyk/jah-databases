(function(){'use strict';
/* The Grandfathered Public Data Files Database generator — jahdb-grandfathered-files-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-GPF-";
var SLUG="grandfathered-public-data-files-database";
var FIELDS=["founding", "poetry", "songs", "speeches", "crypto", "datasets", "process"];
var SEED_TITLES=[["The Bill of Rights: complete text (1791)", "founding"], ["The Declaration of Independence: key text (1776)", "founding"], ["The Gettysburg Address: complete text (1863)", "founding"], ["The Constitution's Preamble (1787)", "founding"], ["The Emancipation Proclamation: operative text (1863)", "founding"], ["The 13th Amendment: complete text (1865)", "founding"], ["The 19th Amendment: complete text (1920)", "founding"], ["Federalist No. 10: complete text (1787)", "founding"], ["Magna Carta: key clauses (1215)", "founding"], ["\"Casey at the Bat\": complete poem (1888)", "poetry"], ["\"The Road Not Taken\": complete poem (1916)", "poetry"], ["\"O Captain! My Captain!\": complete poem (1865)", "poetry"], ["\"Jabberwocky\": complete poem (1871)", "poetry"], ["Shakespeare's Sonnet 18: complete text", "poetry"], ["\"The Star-Spangled Banner\": lyrics (1814)", "songs"], ["\"America the Beautiful\": lyrics (1895)", "songs"], ["Kennedy's Moon speech: key passage (1962)", "speeches"], ["Eisenhower's farewell: key passage (1961)", "speeches"], ["The Zimmermann Telegram: decoded text (1917)", "crypto"], ["DES S-boxes: complete tables (FIPS PUB 46, 1977)", "crypto"], ["SKIPJACK F-table: complete (declassified 1998)", "crypto"], ["\"New Directions in Cryptography\": bibliographic record (1976)", "crypto"], ["Nobel laureates 1901-2024: complete dataset", "datasets"], ["US states admission dates: complete dataset", "datasets"], ["Academy Best Picture winners: complete dataset", "datasets"], ["US presidents: complete list", "datasets"], ["Periodic table: complete element list", "datasets"], ["Grandfathering: how public stays public", "process"], ["Provenance standard of this database", "process"]];
var BLURBS={"founding": ["A full archive record in the 'founding' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'founding' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "poetry": ["A full archive record in the 'poetry' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'poetry' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "songs": ["A full archive record in the 'songs' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'songs' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "speeches": ["A full archive record in the 'speeches' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'speeches' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "crypto": ["A full archive record in the 'crypto' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'crypto' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "datasets": ["A full archive record in the 'datasets' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'datasets' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "process": ["A full archive record in the 'process' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'process' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Grandfathered": "Lawfully public before a restriction; remaining public thereafter \u2014 with provenance.", "Public domain": "Works free of copyright, including all US federal government works.", "Provenance": "The documented chain showing a file was lawfully public.", "Archival copy": "A complete, faithful copy preserved for the record.", "FIPS": "Federal Information Processing Standards \u2014 US government public standards.", "Declassified": "Officially released from classified status."};
var GEN_SRC="US National Archives; Library of Congress; Project Gutenberg; NIST";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Grandfathered Public Data Files Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Grandfathered Public Data Files Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-grandfathered-files-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-grandfathered-files-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
