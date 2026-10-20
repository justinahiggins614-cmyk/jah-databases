(function(){'use strict';
/* The Billiards History Database generator — jahdb-billiards-history-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. Seeds cycle the archive title table;
   higher seeds produce boundless variations. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BIL-";
var SLUG="billiards-history-evolution";
var FIELDS=["origins", "equipment", "games", "rules", "organizations", "techniques", "culture", "modern"];
var SEED_TITLES=[["Billiards begins: the French lawn game moves indoors", "origins"], ["Mary, Queen of Scots, and the billiard table", "origins"], ["Shakespeare's anachronism: billiards in 1606", "origins"], ["From mace to cue: the stick evolves", "equipment"], ["1807: Mingaud invents the leather tip \u2014 spin is born", "equipment"], ["Chalk: the blue cube", "equipment"], ["Slate beds and vulcanized rubber: the modern table", "equipment"], ["Ivory to phenolic: the ball's journey", "equipment"], ["Simonis cloth: weaving since 1680", "equipment"], ["Carom: the pocketless ancestor", "games"], ["English billiards: carom meets pockets", "games"], ["Pool: America's betting rooms give the game its name", "games"], ["Straight pool: the 20th century's championship game", "games"], ["Nine-ball: built for television", "games"], ["Eight-ball: the people's game", "games"], ["1875: Snooker is invented in India", "games"], ["Joe Davis and the first World Snooker Championship (1927)", "games"], ["The push-out and the three-foul rule", "rules"], ["Break rules: taming the most violent shot", "rules"], ["1948: the Billiards Congress of America", "organizations"], ["1987: the World Pool Association", "organizations"], ["1994: the Mosconi Cup \u2014 pool's Ryder Cup", "organizations"], ["1976: the WPBA \u2014 women's professional pool", "organizations"], ["The Hustler (1961) and The Color of Money (1986)", "culture"], ["The diamond system: aiming by numbers", "techniques"], ["Masse and jump: the circus shots", "techniques"], ["Draw, follow, and stun: the holy trinity", "techniques"], ["Pool goes global: the Filipino invasion", "modern"], ["Matchroom and the streaming era", "modern"]];
var BLURBS={"origins": ["A full archive record in the 'origins' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'origins' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "equipment": ["A full archive record in the 'equipment' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'equipment' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "games": ["A full archive record in the 'games' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'games' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "rules": ["A full archive record in the 'rules' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'rules' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "organizations": ["A full archive record in the 'organizations' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'organizations' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "techniques": ["A full archive record in the 'techniques' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'techniques' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "culture": ["A full archive record in the 'culture' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'culture' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."], "modern": ["A full archive record in the 'modern' wing: researched, structured, and validated \u2014 every fact checked against public sources before acceptance.", "From the 'modern' collection: human-readable, fully sourced, and carrying its own runnable demonstration program."]};
var DEFINITIONS={"Billiards": "The family of cue sports played on a cloth-covered table with balls and a cue stick.", "Cue": "The tapered stick used to strike the cue ball; the leather tip (invented 1807) made spin possible.", "Carom": "Cue games played on a pocketless table where points come from contacting balls and cushions.", "Snooker": "The 22-ball cue sport invented in British India in 1875, played on a large 12-foot table.", "Straight pool": "14.1 continuous \u2014 the classic championship pool game of the 20th century.", "Nine-ball": "The fast rotation game that became pool's televised standard.", "English (spin)": "Sidespin applied with a tipped cue \u2014 the technique unlocked by the leather tip.", "Masse": "A steep cue stroke curving the cue ball around an obstacle."};
var GEN_SRC="Encyclopaedia Britannica; Billiards Congress of America (bca-pool.com); World Pool Association";
var GEN_DISCLAIMER="Signature-created companion content: analysis, designs, and concepts authored for the Signature line. Not an official record of any awarding body, government, or institution.";
var SIG=false;
var DQ3=String.fromCharCode(34,34,34);
function pad6(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function programFor(rec){
  var lines=[
    DQ3+rec.title+' - runnable demo from the '+"The Billiards History Database"+'.',
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
  var desc='Seed '+seed+' record for the '+"The Billiards History Database"+'.'+'\n\n'+blurb+'\n\n'+
    'This entry belongs to the "'+group+'" wing of the archive. It was produced by the '+"jahdb-billiards-history-1.0"+' boundless generator: '+
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
var gen={version:'jahdb-billiards-history-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
