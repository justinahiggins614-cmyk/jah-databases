/* JAH Public Plays Database generator — jahdb-public-plays-1.0
   Study guides and analyses of REAL public-domain plays. Type 1.
   NEVER generates fake "public" plays — only guides for the seeded real plays. */
(function(){
'use strict';
var GEN_NAME='jahdb-public-plays-1.0';
function prng(seed){var s=seed>>>0;return function(){s=(s*1664525+1013904223)>>>0;return s/4294967296;};}
function pick(r,arr){return arr[Math.floor(r()*arr.length)];}

/* Real public-domain plays that are seeded in the archive */
var REAL_PLAYS=[
  {title:'Hamlet',playwright:'William Shakespeare',year:1603,genre:'tragedy'},
  {title:'Romeo and Juliet',playwright:'William Shakespeare',year:1597,genre:'tragedy'},
  {title:'Macbeth',playwright:'William Shakespeare',year:1606,genre:'tragedy'},
  {title:'A Midsummer Night\'s Dream',playwright:'William Shakespeare',year:1600,genre:'comedy'},
  {title:'The Cherry Orchard',playwright:'Anton Chekhov',year:1904,genre:'drama'},
  {title:'A Doll\'s House',playwright:'Henrik Ibsen',year:1879,genre:'drama'},
  {title:'The Importance of Being Earnest',playwright:'Oscar Wilde',year:1895,genre:'comedy'},
  {title:'Antigone',playwright:'Sophocles',year:-441,genre:'tragedy'},
  {title:'Oedipus Rex',playwright:'Sophocles',year:-429,genre:'tragedy'},
  {title:'Faust',playwright:'Johann Wolfgang von Goethe',year:1808,genre:'tragedy'}
];
var GUIDE_TYPES=['Character Analysis','Theme Study','Historical Context','Performance Guide','Act-by-Act Summary','Symbolism Guide','Language and Verse Study','Modern Adaptation Notes'];

function makeGuide(seed){
  var r=prng(seed);
  var play=REAL_PLAYS[Math.floor(r()*REAL_PLAYS.length)];
  var gtype=pick(r,GUIDE_TYPES);
  return {
    id:'JAH-PPLAY-'+String(seed).padStart(6,'0'),
    title:gtype+': '+play.title,
    play_title:play.title, playwright:play.playwright, year:play.year, genre:play.genre,
    guide_type:gtype,
    content:'A '+gtype.toLowerCase()+' for '+play.playwright+'\'s '+play.title+' ('+play.year+'). '+
      'This guide examines the play\'s structure, characters, and lasting significance. '+
      '[Full study guide content generated from the archived play record.]',
    play_ref:play.title,
    src:'signature', _seed:seed,
    note:'Study guide — the full play text is in the archive record for "'+play.title+'".'
  };
}
function validate(rec){
  if(!rec||!rec.id||!rec.title||!rec.play_title)return false;
  if(!/^JAH-PPLAY-\d{6}$/.test(rec.id))return false;
  return true;
}
function driftCheck(a,b){return JSON.stringify(a)===JSON.stringify(b);}
var gen={name:GEN_NAME,generate:function(seed){return makeGuide(seed);},
  generateIndexed:function(i){return makeGuide(i+1);},validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator('public-plays',gen);}
if(typeof module!=='undefined'&&module.exports){module.exports=gen;}
})();
