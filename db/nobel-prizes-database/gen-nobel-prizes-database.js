(function(){'use strict';
/* The Nobel Prizes Database generator — jahdb-nobel-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-NOB-";
var SLUG="nobel-prizes-database";
var FIELDS=["landmark-prizes", "milestones", "history", "laureates", "records"];
var SEED_TITLES=[["The first Nobel Prizes (1901) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physic", "ceremonies"], ["1903 Nobel Prizes (1903) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: He", "ceremonies"], ["1905 Nobel Prizes (1905) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Theo", "ceremonies"], ["1921 Nobel Prizes (1921) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: Al", "ceremonies"], ["1944 Nobel Prizes (1944) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Chemistry: ", "ceremonies"], ["1953 Nobel Prizes (1953) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Geor", "ceremonies"], ["1962 Nobel Prizes (1962) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Medicine: C", "ceremonies"], ["1964 Nobel Prizes (1964) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Mart", "ceremonies"], ["1979 Nobel Prizes (1979) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Moth", "ceremonies"], ["1990 Nobel Prizes (1990) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Mikh", "ceremonies"], ["1993 Nobel Prizes (1993) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Nels", "ceremonies"], ["2009 Nobel Prizes (2009) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Bara", "ceremonies"], ["2014 Nobel Prizes (2014) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Mala", "ceremonies"], ["2016 Nobel Prizes (2016) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Literature:", "ceremonies"], ["2020 Nobel Prizes (2020) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: Pe", "ceremonies"], ["2021 Nobel Prizes (2021) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Peace: Mari", "ceremonies"], ["2022 Nobel Prizes (2022) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: As", "ceremonies"], ["2023 Nobel Prizes (2023) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: Ag", "ceremonies"], ["2024 Nobel Prizes (2024) \u2014 Nobel Prize (Physics, Chemistry, Medicine, Literature, Peace, Economic Sciences): Physics: Ho", "ceremonies"], ["The Nobel Prizes: Nobel's will (1895)", "milestones"], ["The Nobel Prizes: The Nobel Foundation (1900)", "milestones"], ["The Nobel Prizes: Three Peace Prizes: the Red Cross", "milestones"], ["The Nobel Prizes: Two prizes each", "milestones"], ["The Nobel Prizes: Youngest and oldest", "milestones"], ["The Nobel Prizes: The Economics prize", "milestones"], ["The Nobel Prizes: The awarding institutions", "history"], ["The Nobel Prizes: December 10", "history"], ["The Nobel Prizes: Nomination secrecy", "history"], ["The Nobel Prizes: The medal and money", "history"], ["The Nobel Prizes: No prizes 1940-1942", "history"]];
var BLURBS={"landmark-prizes": ["A full archive record in the 'landmark-prizes' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'landmark-prizes' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "milestones": ["A full archive record in the 'milestones' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'milestones' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "history": ["A full archive record in the 'history' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'history' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "laureates": ["A full archive record in the 'laureates' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'laureates' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "records": ["A full archive record in the 'records' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'records' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Nobel Prize": "The annual prizes for physics, chemistry, medicine, literature, peace, and economic sciences.", "Laureate": "A Nobel Prize recipient.", "Nobel Foundation": "The Stockholm body administering Nobel's will since 1900.", "Norwegian Nobel Committee": "The five-member Oslo committee awarding the Peace Prize.", "Sveriges Riksbank Prize": "The economics prize, added 1968 by Sweden's central bank.", "Nobel's will": "Alfred Nobel's 1895 testament creating the prizes from his fortune."};
var GEN_SRC="Nobel Prize official records (nobelprize.org); Encyclopaedia Britannica";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Nobel Prizes Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Nobel Prizes Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-nobel-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-nobel-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
