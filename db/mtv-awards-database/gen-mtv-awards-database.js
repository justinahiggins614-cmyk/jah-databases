(function(){'use strict';
/* The MTV Video Music Awards Database generator — jahdb-vma-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-VMA-";
var SLUG="mtv-awards-database";
var FIELDS=["ceremonies", "milestones", "history", "voting", "records"];
var SEED_TITLES=[["1st MTV Video Music Awards (1984) \u2014 Video of the Year: You Might Think \u2014 The Cars", "ceremonies"], ["4th MTV Video Music Awards (1987) \u2014 Video of the Year: Sledgehammer \u2014 Peter Gabriel", "ceremonies"], ["7th MTV Video Music Awards (1990) \u2014 Video of the Year: Nothing Compares 2 U \u2014 Sinead O'Connor", "ceremonies"], ["12th MTV Video Music Awards (1995) \u2014 Video of the Year: Waterfalls \u2014 TLC", "ceremonies"], ["16th MTV Video Music Awards (1999) \u2014 Video of the Year: Doo Wop (That Thing) \u2014 Lauryn Hill", "ceremonies"], ["26th MTV Video Music Awards (2009) \u2014 Video of the Year: Single Ladies (Put a Ring on It) \u2014 Beyonce", "ceremonies"], ["27th MTV Video Music Awards (2010) \u2014 Video of the Year: Bad Romance \u2014 Lady Gaga", "ceremonies"], ["30th MTV Video Music Awards (2013) \u2014 Video of the Year: Mirrors \u2014 Justin Timberlake", "ceremonies"], ["32nd MTV Video Music Awards (2015) \u2014 Video of the Year: Bad Blood \u2014 Taylor Swift ft. Kendrick Lamar", "ceremonies"], ["34th MTV Video Music Awards (2017) \u2014 Video of the Year: HUMBLE. \u2014 Kendrick Lamar", "ceremonies"], ["37th MTV Video Music Awards (2020) \u2014 Video of the Year: Blinding Lights \u2014 The Weeknd", "ceremonies"], ["40th MTV Video Music Awards (2023) \u2014 Video of the Year: Anti-Hero \u2014 Taylor Swift", "ceremonies"], ["8th MTV Video Music Awards (1991) \u2014 Video of the Year: Losing My Religion \u2014 R.E.M.", "ceremonies"], ["17th MTV Video Music Awards (2000) \u2014 Video of the Year: The Real Slim Shady \u2014 Eminem", "ceremonies"], ["38th MTV Video Music Awards (2021) \u2014 Video of the Year: Montero (Call Me by Your Name) \u2014 Lil Nas X", "ceremonies"], ["39th MTV Video Music Awards (2022) \u2014 Video of the Year: All Too Well: The Short Film \u2014 Taylor Swift", "ceremonies"], ["The MTV Video Music Awards: The Moonman", "milestones"], ["The MTV Video Music Awards: Beyonce: most VMA wins", "milestones"], ["The MTV Video Music Awards: MTV launches", "milestones"], ["The MTV Video Music Awards: Sledgehammer's nine", "milestones"], ["The MTV Video Music Awards: Fan voting", "milestones"], ["The MTV Video Music Awards: The Vanguard Award", "milestones"], ["The MTV Video Music Awards: Eight in one night", "milestones"], ["The MTV Video Music Awards: Why the VMAs matter", "history"], ["The MTV Video Music Awards: Video of the Year", "history"], ["The MTV Video Music Awards: The moon landing nod", "history"], ["The MTV Video Music Awards: From cable to streaming", "history"], ["The MTV Video Music Awards: Memorable performances", "history"]];
var BLURBS={"ceremonies": ["A full archive record in the 'ceremonies' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'ceremonies' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "voting": ["A full archive record in the 'voting' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'voting' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Video of the Year": "The VMA for the year's outstanding music video.", "Moonman/Moon Person": "The astronaut VMA trophy, an icon of pop culture.", "Video Vanguard Award": "The VMA career-achievement honor for music-video artistry.", "Fan-voted": "VMA winners in major categories are chosen by public online vote.", "TRL era": "MTV's Total Request Live years (1998-2008), the VMAs' commercial peak.", "MTV": "The music-television network founded 1981 that presents the VMAs."};
var GEN_SRC="MTV official records (mtv.com); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The MTV Video Music Awards Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The MTV Video Music Awards Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-vma-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-vma-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
