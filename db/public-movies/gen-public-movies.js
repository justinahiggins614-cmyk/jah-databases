(function(){'use strict';
/* JAH Public Movies Database generator — jahdb-public-movies-1.0.
   Property of Justin Addam Higgins (JAH).
   Archive of public-domain movies, ready to watch. Seeded records are REAL
   public-domain films (Type 1 public info) with verified Internet Archive
   watch links. Generated records are CLEARLY labeled samples
   (src:"signature-generated-sample") — never presented as real films.
   Deterministic: same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-PM-';
var GENRES=['drama','comedy','horror','sci-fi','western','film-noir','adventure','silent-era','thriller','documentary','fantasy','war'];
var COUNTRIES=['United States','United Kingdom','France','Germany','Italy','Japan','Soviet Union','Sweden','Denmark','Spain'];
/* Fictional sample titles — clearly NOT real films. Generated records are
   structural samples only, never presented as real public-domain movies. */
var T_A=['Midnight','Crimson','Silent','Neon','Amber','Velvet','Iron','Golden','Hollow','Electric','Rustic','Phantom'];
var T_B=['Station','Harbor','Horizon','Reel','Alley','Lantern','Crossing','Voyage','Echo','Summit','Frontier','Marquee'];
var DIR_A=['Marlowe','Ellis','Vance','Harper','Quill','Sutton','Ridley','Ashford','Bellamy','Corbin'];
var DIR_B=['Thorne','Vega','Locke','Frost','Grady','Hale','Ivers','Judd','Kane','Lark'];
var CAST_A=['June','Walter','Iris','Claude','Mabel','Otto','Pearl','Silas','Nora','Emmett'];
var CAST_B=['Calloway','Drummond','Fairbanks','Grantham','Holloway','Ingram','Jarvis','Kingsley','Lovett','Mercer'];
var SYN=['A lost print resurfaces after decades in a studio vault, telling the story of ordinary people caught in extraordinary times.','A traveling showman arrives in a quiet town with a machine that shows moving pictures of possible futures.','Two strangers meet on the last train out of the city and discover they share the same impossible secret.','A night watchman at a grand theater finds a reel of film that seems to predict the next day\u2019s events.','A retired sea captain and a young cartographer team up to map an island that appears on no official chart.','During a city-wide blackout, a switchboard operator overhears a conversation that was never meant for her ears.','A projectionist discovers that one frame of every film he shows contains a hidden message addressed to him.','An inventor\u2019s daughter and a skeptical reporter chase a rumor of a working time machine across three counties.'];
function sampleTitle(s){return 'The '+pick(T_A,s)+' '+pick(T_B,s);}
function sampleDirector(s){return pick(DIR_A,s)+' '+pick(DIR_B,s);}
function sampleCast(s){var n=ri(s,2,4),out=[],i;for(i=0;i<n;i++){out.push(pick(CAST_A,s)+' '+pick(CAST_B,s));}return out;}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var genre=opts.genre&&GENRES.indexOf(opts.genre)>=0?opts.genre:pick(GENRES,rnd);
  var country=opts.country&&COUNTRIES.indexOf(opts.country)>=0?opts.country:pick(COUNTRIES,rnd);
  var year=ri(rnd,1902,1968);
  var title=sampleTitle(rnd);
  var director=sampleDirector(rnd);
  var cast=sampleCast(rnd);
  var dur=ri(rnd,58,128);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    title:title+' ('+year+')',
    name:title,
    year:year,
    director:director,
    cast:cast,
    synopsis:pick(SYN,rnd),
    description:'SAMPLE RECORD (generated — not a real film). A '+genre+' film entry in the format of the Public Movies Database. Seeded archive records are real public-domain films with verified watch links; this generated record is structural only.',
    genre:genre,
    country:country,
    duration_min:dur,
    public_domain:false,
    watch_url:'',
    embed_url:'',
    poster_url:'',
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not a real film. Seeded archive records are real public-domain movies with verified watch links; this generated record is structural only.',
    demo:{kind:'watch-link-check',program:"function ok(u){return /^https:\\/\\/archive\\.org\\/details\\//.test(u)?'watch link valid':'not an archive.org watch link';}",note:'Paste into any JS console with a watch_url to validate the link format.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PM-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<3)e.push('title');
  if(typeof r.year!=='number'||r.year<1890||r.year>2030)e.push('year');
  if(typeof r.director!=='string'||!r.director)e.push('director');
  if(!Array.isArray(r.cast))e.push('cast');
  if(GENRES.indexOf(r.genre)<0)e.push('genre');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.t===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-movies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,genres:GENRES,countries:COUNTRIES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-movies',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
