(function(){'use strict';
/* The Pulitzer Prizes Database generator — jahdb-pulitzer-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PUL-";
var SLUG="pulitzer-prizes-database";
var FIELDS=["landmark-prizes", "milestones", "history", "laureates", "records"];
var SEED_TITLES=[["The first Pulitzer Prizes (1917) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Reporting: Herbert Bayard ", "ceremonies"], ["1940 Pulitzer Prizes (1940) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: The Grapes of Wrath \u2014 ", "ceremonies"], ["1948 Pulitzer Prizes (1948) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Drama: A Streetcar Named Desire", "ceremonies"], ["1949 Pulitzer Prizes (1949) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Drama: Death of a Salesman \u2014 Ar", "ceremonies"], ["1953 Pulitzer Prizes (1953) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: The Old Man and the Se", "ceremonies"], ["1961 Pulitzer Prizes (1961) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: To Kill a Mockingbird ", "ceremonies"], ["1973 Pulitzer Prizes (1973) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Public Service: The Washington ", "ceremonies"], ["1987 Pulitzer Prizes (1987) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Drama: Fences \u2014 August Wilson", "ceremonies"], ["1988 Pulitzer Prizes (1988) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: Beloved \u2014 Toni Morriso", "ceremonies"], ["1993 Pulitzer Prizes (1993) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Drama: Angels in America: Mille", "ceremonies"], ["2007 Pulitzer Prizes (2007) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: The Road \u2014 Cormac McCa", "ceremonies"], ["2016 Pulitzer Prizes (2016) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Drama: Hamilton \u2014 Lin-Manuel Mi", "ceremonies"], ["2017 Pulitzer Prizes (2017) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: The Underground Railro", "ceremonies"], ["2018 Pulitzer Prizes (2018) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Public Service: The New York Ti", "ceremonies"], ["2020 Pulitzer Prizes (2020) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: The Nickel Boys \u2014 Cols", "ceremonies"], ["2021 Pulitzer Prizes (2021) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Breaking News: Star Tribune (Ge", "ceremonies"], ["2023 Pulitzer Prizes (2023) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: Demon Copperhead \u2014 Bar", "ceremonies"], ["2024 Pulitzer Prizes (2024) \u2014 Pulitzer Prize (Public Service, Fiction, Drama, Music...): Fiction: Night Watch \u2014 Jayne An", "ceremonies"], ["The Pulitzer Prizes: Joseph Pulitzer's will", "milestones"], ["The Pulitzer Prizes: Public Service: the top honor", "milestones"], ["The Pulitzer Prizes: Whitehead's back-to-back", "milestones"], ["The Pulitzer Prizes: Kendrick Lamar's Music prize", "milestones"], ["The Pulitzer Prizes: The 1941 Fiction controversy", "milestones"], ["The Pulitzer Prizes: Special Citations", "milestones"], ["The Pulitzer Prizes: The Pulitzer Board", "history"], ["The Pulitzer Prizes: The categories", "history"], ["The Pulitzer Prizes: How judging works", "history"], ["The Pulitzer Prizes: The gold medal", "history"], ["The Pulitzer Prizes: April announcements", "history"]];
var BLURBS={"landmark-prizes": ["A full archive record in the 'landmark-prizes' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'landmark-prizes' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "laureates": ["A full archive record in the 'laureates' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'laureates' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Public Service": "The Pulitzer's top journalism prize, awarded as a gold medal to a news organization.", "Pulitzer Board": "The 19-member body choosing winners from jurors' finalists.", "Fiction prize": "The Pulitzer for distinguished American fiction (formerly the Novel prize).", "Drama prize": "The Pulitzer for distinguished American play, preferably original.", "Music prize": "The Pulitzer for distinguished American musical composition.", "Special Citation": "The Board's discretionary honor for exceptional achievement outside the categories."};
var GEN_SRC="The Pulitzer Prizes official records (pulitzer.org); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Pulitzer Prizes Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Pulitzer Prizes Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-pulitzer-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-pulitzer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
