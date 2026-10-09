/* ✳ JAH Sports Stats Database generator. Property of Justin Addam Higgins (JAH).
   Deterministic (seeded) match record generator: jahdb-sports-stats-1.0.
   All teams, scores and fixtures are synthetically generated. */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function pad(n){return String(n).padStart(6,'0');}

var CATS=['soccer','basketball','baseball','football','tennis','hockey'];
var LEAGUES={
soccer:['Continental Soccer League','United Premier League','Metro Football Circuit'],
basketball:['National Basketball Circuit','Continental Hoops League'],
baseball:['American Diamond League','National Pastime Circuit'],
football:['Gridiron Championship League','Continental Football Alliance'],
tennis:['Grand Circuit Tour','World Open Series'],
hockey:['Northern Ice Hockey League','Continental Hockey Circuit']
};
var CITIES=['Springfield','Riverdale','Lakeside','Cedar Falls','Brookfield','Fairview','Maple Grove','Hillcrest','Oakdale','Pinehurst','Westfield','Northgate','Elmwood','Clearwater','Stonebridge','Meadowbrook','Sunnyvale','Ridgemont','Ashford','Granite City','Willow Creek','Bayport','Summit','Harborview','Kingsport','Milltown','Eastvale','Portside','Fairhaven','Crestview'];
var MASCOTS=['Falcons','Wolves','Tigers','Bears','Hawks','Lions','Sharks','Panthers','Eagles','Cobras','Mustangs','Rhinos','Vipers','Bison','Cougars','Stallions','Badgers','Otters','Ravens','Grizzlies','Coyotes','Jaguars','Thunder','Comets','Blaze','Storm','Rockets','Titans','Warriors','Knights'];

var SCORE_RANGE={soccer:[0,6],basketball:[80,140],baseball:[0,15],football:[0,45],hockey:[0,8]};

function isoDate(rnd){
  var y=ri(rnd,2024,2026),mo=ri(rnd,1,12),d=ri(rnd,1,28);
  function z(n){return (n<10?'0':'')+n;}
  return y+'-'+z(mo)+'-'+z(d);
}
function teamName(rnd){
  return pick(rnd,CITIES)+' '+pick(rnd,MASCOTS);
}
function tennisScore(rnd){
  var sets=ri(rnd,2,3),parts=[];
  for(var i=0;i<sets;i++){
    var w=ri(rnd,6,7),l=ri(rnd,0,5);
    if(rnd()<0.5){var t=w;w=l;l=t;}
    parts.push(w+'-'+l);
  }
  return parts.join(', ');
}
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=(opts&&opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:pick(rnd,CATS);
  var league=pick(rnd,LEAGUES[cat]);
  var home=teamName(rnd),away;
  do{away=teamName(rnd);}while(away===home);
  var hs,as;
  if(cat==='tennis'){hs=tennisScore(rnd);as=tennisScore(rnd);}
  else{var sr=SCORE_RANGE[cat];hs=ri(rnd,sr[0],sr[1]);as=ri(rnd,sr[0],sr[1]);}
  return {
    id:'JAH-MATCH-'+pad(seed),
    match_id:'JAH-MATCH-'+pad(seed),
    sport:cat,
    league:league,
    date:isoDate(rnd),
    home_team:home,
    away_team:away,
    home_score:hs,
    away_score:as
  };
}
function validate(r){
  var e=[];
  if(typeof r.id!=='string'||!/^JAH-MATCH-\d{6}$/.test(r.id))e.push('id');
  if(typeof r.match_id!=='string'||r.match_id!==r.id)e.push('match_id');
  if(CATS.indexOf(r.sport)<0)e.push('sport');
  if(typeof r.league!=='string'||!r.league.length)e.push('league');
  if(typeof r.date!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(r.date))e.push('date');
  if(typeof r.home_team!=='string'||!r.home_team.length)e.push('home_team');
  if(typeof r.away_team!=='string'||!r.away_team.length)e.push('away_team');
  if(r.home_team===r.away_team)e.push('teams differ');
  if(r.sport==='tennis'){
    var fmt=/^\d{1,2}-\d{1,2}(, \d{1,2}-\d{1,2}){1,2}$/;
    if(typeof r.home_score!=='string'||!fmt.test(r.home_score))e.push('home_score sets');
    if(typeof r.away_score!=='string'||!fmt.test(r.away_score))e.push('away_score sets');
  }else{
    var sr=SCORE_RANGE[r.sport];
    if(typeof r.home_score!=='number'||r.home_score<sr[0]||r.home_score>sr[1])e.push('home_score range');
    if(typeof r.away_score!=='number'||r.away_score<sr[0]||r.away_score>sr[1])e.push('away_score range');
  }
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-sports-stats-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('sports-stats',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
