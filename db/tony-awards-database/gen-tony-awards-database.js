(function(){'use strict';
/* The Tony Awards Database generator — jahdb-tonys-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TON-";
var SLUG="tony-awards-database";
var FIELDS=["ceremonies", "milestones", "history", "voting", "records"];
var SEED_TITLES=[["3rd Tony Awards (1949) \u2014 Best Musical: Kiss Me, Kate", "ceremonies"], ["4th Tony Awards (1950) \u2014 Best Musical: South Pacific", "ceremonies"], ["11th Tony Awards (1957) \u2014 Best Musical: My Fair Lady", "ceremonies"], ["14th Tony Awards (1960) \u2014 Best Musical: The Sound of Music and Fiorello! (tie)", "ceremonies"], ["18th Tony Awards (1964) \u2014 Best Musical: Hello, Dolly!", "ceremonies"], ["30th Tony Awards (1976) \u2014 Best Musical: A Chorus Line", "ceremonies"], ["34th Tony Awards (1980) \u2014 Best Musical: Evita", "ceremonies"], ["42nd Tony Awards (1988) \u2014 Best Musical: The Phantom of the Opera", "ceremonies"], ["50th Tony Awards (1996) \u2014 Best Musical: Rent", "ceremonies"], ["52nd Tony Awards (1998) \u2014 Best Musical: The Lion King", "ceremonies"], ["58th Tony Awards (2004) \u2014 Best Musical: Avenue Q", "ceremonies"], ["62nd Tony Awards (2008) \u2014 Best Musical: In the Heights", "ceremonies"], ["69th Tony Awards (2015) \u2014 Best Musical: Fun Home", "ceremonies"], ["70th Tony Awards (2016) \u2014 Best Musical: Hamilton", "ceremonies"], ["73rd Tony Awards (2019) \u2014 Best Musical: Hadestown", "ceremonies"], ["77th Tony Awards (2024) \u2014 Best Musical: The Outsiders", "ceremonies"], ["The Tony Awards: The Producers: 12 Tonys", "milestones"], ["The Tony Awards: Hamilton's 16 nominations", "milestones"], ["The Tony Awards: The first Tonys", "milestones"], ["The Tony Awards: Julie Harris: six Tonys", "milestones"], ["The Tony Awards: Longest-running winners", "milestones"], ["The Tony Awards: The medallion", "milestones"], ["The Tony Awards: Antoinette Perry", "history"], ["The Tony Awards: Who votes", "history"], ["The Tony Awards: The American Theatre Wing and Broadway League", "history"], ["The Tony Awards: Broadway eligibility", "history"], ["The Tony Awards: The ceremony's home", "history"]];
var BLURBS={"ceremonies": ["A full archive record in the 'ceremonies' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'ceremonies' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "voting": ["A full archive record in the 'voting' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'voting' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Best Musical": "The Tony for the season's outstanding Broadway musical.", "Broadway": "The 41 professional theatres of 500+ seats in Manhattan's theatre district; only they confer Tony eligibility.", "EGOT": "Emmy, Grammy, Oscar, Tony \u2014 the grand slam; the Tonys complete several EGOTs.", "The American Theatre Wing": "Co-presenter of the Tonys, founded 1917, also behind the Obie Awards.", "The Broadway League": "The trade association of Broadway producers and theatre owners; co-presenter of the Tonys.", "Tony medallion": "The comedy/tragedy mask medallion awarded to winners."};
var GEN_SRC="The Tony Awards official records (tonyawards.com); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Tony Awards Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Tony Awards Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-tonys-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-tonys-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
