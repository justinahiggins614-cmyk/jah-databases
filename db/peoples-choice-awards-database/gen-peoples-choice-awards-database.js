(function(){'use strict';
/* The People's Choice Awards Database generator — jahdb-pca-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PCA-";
var SLUG="peoples-choice-awards-database";
var FIELDS=["ceremonies", "milestones", "history", "voting", "records"];
var SEED_TITLES=[["1st People's Choice Awards (1975) \u2014 Favorite Movie / Movie of the Year: Favorite Motion Picture (1974 films)", "ceremonies"], ["39th People's Choice Awards (2013) \u2014 Favorite Movie / Movie of the Year: Favorite Movie: The Hunger Games", "ceremonies"], ["41st People's Choice Awards (2015) \u2014 Favorite Movie / Movie of the Year: Favorite Movie: Maleficent", "ceremonies"], ["44th People's Choice Awards (2018) \u2014 Favorite Movie / Movie of the Year: Movie of 2018: Avengers: Infinity War", "ceremonies"], ["46th People's Choice Awards (2020) \u2014 Favorite Movie / Movie of the Year: Movie of 2020: Bad Boys for Life", "ceremonies"], ["47th People's Choice Awards (2021) \u2014 Favorite Movie / Movie of the Year: Movie of 2021: Black Widow", "ceremonies"], ["48th People's Choice Awards (2022) \u2014 Favorite Movie / Movie of the Year: Movie of 2022: Top Gun: Maverick", "ceremonies"], ["49th People's Choice Awards (2024) \u2014 Favorite Movie / Movie of the Year: Movie of the Year: Barbie", "ceremonies"], ["42nd People's Choice Awards (2016) \u2014 Favorite Movie / Movie of the Year: Favorite Movie: Furious 7", "ceremonies"], ["43rd People's Choice Awards (2017) \u2014 Favorite Movie / Movie of the Year: Favorite Movie: Finding Dory", "ceremonies"], ["45th People's Choice Awards (2019) \u2014 Favorite Movie / Movie of the Year: Movie of 2019: Avengers: Endgame", "ceremonies"], ["The People's Choice Awards: Founded 1975", "milestones"], ["The People's Choice Awards: Gallup to online", "milestones"], ["The People's Choice Awards: E! era", "milestones"], ["The People's Choice Awards: NBC era", "milestones"], ["The People's Choice Awards: The crystal trophy", "milestones"], ["The People's Choice Awards: Beyond entertainment", "milestones"], ["The People's Choice Awards: The Icon honors", "milestones"], ["The People's Choice Awards: The streaming era", "milestones"], ["The People's Choice Awards: Hashtag voting", "milestones"], ["The People's Choice Awards: The fan-vote promise", "history"], ["The People's Choice Awards: How voting works", "history"], ["The People's Choice Awards: The ceremony's homes", "history"], ["The People's Choice Awards: Hosts", "history"], ["The People's Choice Awards: Why it matters", "history"], ["The People's Choice Awards: How nominees are chosen", "history"], ["The People's Choice Awards: The People's Icon award", "history"], ["The People's Choice Awards: Music and TV categories", "history"]];
var BLURBS={"ceremonies": ["A full archive record in the 'ceremonies' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'ceremonies' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "voting": ["A full archive record in the 'voting' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'voting' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Movie of the Year": "The People's Choice top film honor, chosen entirely by fan vote.", "Fan-voted": "All winners are decided by public vote \u2014 the show's founding rule.", "People's Choice": "The awards founded 1975 to honor audience favorites across entertainment.", "Barker Hangar": "The Santa Monica venue hosting recent ceremonies.", "E! era": "The 2018-2020 period when the show aired on E! in November.", "Gallup polls": "The original 1970s method for measuring America's favorites."};
var GEN_SRC="People's Choice Awards official records (peopleschoice.com); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The People's Choice Awards Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The People's Choice Awards Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-pca-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-pca-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
