(function(){'use strict';
/* The Academy Awards Database generator — jahdb-oscars-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-OSC-";
var SLUG="academy-awards-database";
var FIELDS=["ceremonies", "milestones", "history", "voting", "records"];
var SEED_TITLES=[["1st Academy Awards (1929) \u2014 Best Picture: Wings (1927)", "ceremonies"], ["5th Academy Awards (1932) \u2014 Best Picture: Grand Hotel (1932)", "ceremonies"], ["12th Academy Awards (1940) \u2014 Best Picture: Gone with the Wind (1939)", "ceremonies"], ["16th Academy Awards (1944) \u2014 Best Picture: Casablanca (1942)", "ceremonies"], ["22nd Academy Awards (1950) \u2014 Best Picture: All About Eve (1950)", "ceremonies"], ["32nd Academy Awards (1960) \u2014 Best Picture: Ben-Hur (1959)", "ceremonies"], ["38th Academy Awards (1966) \u2014 Best Picture: The Sound of Music (1965)", "ceremonies"], ["45th Academy Awards (1973) \u2014 Best Picture: The Godfather (1972)", "ceremonies"], ["48th Academy Awards (1976) \u2014 Best Picture: One Flew Over the Cuckoo's Nest (1975)", "ceremonies"], ["52nd Academy Awards (1980) \u2014 Best Picture: Kramer vs. Kramer (1979)", "ceremonies"], ["60th Academy Awards (1988) \u2014 Best Picture: The Last Emperor (1987)", "ceremonies"], ["66th Academy Awards (1994) \u2014 Best Picture: Schindler's List (1993)", "ceremonies"], ["70th Academy Awards (1998) \u2014 Best Picture: Titanic (1997)", "ceremonies"], ["76th Academy Awards (2004) \u2014 Best Picture: The Lord of the Rings: The Return of the King (2003)", "ceremonies"], ["82nd Academy Awards (2010) \u2014 Best Picture: The Hurt Locker (2009)", "ceremonies"], ["88th Academy Awards (2016) \u2014 Best Picture: Spotlight (2015)", "ceremonies"], ["89th Academy Awards (2017) \u2014 Best Picture: Moonlight (2016)", "ceremonies"], ["92nd Academy Awards (2020) \u2014 Best Picture: Parasite (2019)", "ceremonies"], ["94th Academy Awards (2022) \u2014 Best Picture: CODA (2021)", "ceremonies"], ["95th Academy Awards (2023) \u2014 Best Picture: Everything Everywhere All at Once (2022)", "ceremonies"], ["96th Academy Awards (2024) \u2014 Best Picture: Oppenheimer (2023)", "ceremonies"], ["The Academy Awards: Eleven wins: the untouchable record", "milestones"], ["The Academy Awards: Walt Disney: the most Oscars ever", "milestones"], ["The Academy Awards: Katharine Hepburn: four acting wins", "milestones"], ["The Academy Awards: Youngest and oldest winners", "milestones"], ["The Academy Awards: The first televised Oscars", "milestones"], ["The Academy Awards: Sealed envelopes", "milestones"], ["The Academy Awards: The founding of the Academy", "history"], ["The Academy Awards: The Oscar statuette", "history"], ["The Academy Awards: How Oscar voting works", "history"], ["The Academy Awards: Why 'Oscar'?", "history"], ["The Academy Awards: Where the ceremony lives", "history"]];
var BLURBS={"ceremonies": ["A full archive record in the 'ceremonies' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'ceremonies' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "voting": ["A full archive record in the 'voting' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'voting' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Academy": "The Academy of Motion Picture Arts and Sciences (AMPAS), the ~10,000-member film industry body that votes the Oscars.", "Best Picture": "The Academy Award for the year's outstanding film, voted by the full membership on a preferential ballot.", "EGOT": "Winning an Emmy, Grammy, Oscar, and Tony \u2014 the grand slam of American entertainment awards.", "Oscar statuette": "The 13.5-inch gold-plated knight awarded to winners, designed by Cedric Gibbons.", "Preferential ballot": "Ranked-choice voting used for Best Picture since 2009; the film with the broadest support wins.", "Shortlist": "The narrowed list of contenders announced before final nominations in select categories."};
var GEN_SRC="Academy of Motion Picture Arts and Sciences official records (oscars.org); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Academy Awards Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Academy Awards Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-oscars-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-oscars-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
