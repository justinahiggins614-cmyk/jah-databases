(function(){'use strict';
/* JAH Public Comics Database generator — jahdb-public-comics-1.0.
   Property of Justin Addam Higgins (JAH).
   Archive of PUBLIC-DOMAIN comics — Golden Age titles whose copyrights
   lapsed, plus openly-licensed works. Distinct from the Signature Comic
   Store Database (original Signature works).
   Seeded records are REAL public-domain comics (Type 1 public info).
   Generated records are CLEARLY labeled samples (src:"signature-generated-sample")
   — never presented as real comics. Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-PUBC-';
var ERAS=['golden-age','silver-age','public-domain','open-license'];
var ERA_LABEL={'golden-age':'Golden Age (1938–1956)','silver-age':'Silver Age (1956–1970)','public-domain':'Public Domain','open-license':'Open License'};
var GENRES=['superhero','adventure','mystery','horror','western','sci-fi','funny-animal','romance','war','crime'];
var HERO_A=['Captain','Major','Sergeant','Doctor','Professor','Mister','Master','Colonel'];
var HERO_B=['Comet','Thunder','Falcon','Meteor','Blaze','Storm','Rocket','Crimson','Iron','Silver'];
var HERO_C=['Man','Kid','Boy','Ace','King','Star','Shield','Bolt'];
var PUBLISHERS=['Fox Comics','Lev Gleason','Standard Comics','Continental','Fiction House','Centaur Comics','Harvey Comics','Prize Comics'];
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var era=opts.era&&ERAS.indexOf(opts.era)>=0?opts.era:pick(ERAS,rnd);
  var genre=pick(GENRES,rnd);
  var hero=pick(HERO_A,rnd)+' '+pick(HERO_B,rnd)+' '+pick(HERO_C,rnd);
  var title=hero+' Comics';
  var year=era==='golden-age'?ri(rnd,1938,1956):era==='silver-age'?ri(rnd,1956,1970):ri(rnd,1930,1965);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:title,
    title:title+' — '+ERA_LABEL[era],
    description:'SAMPLE COMIC LISTING (generated — not a real comic). A '+genre+' public-domain-style comic entry from the '+ERA_LABEL[era].toLowerCase()+'. Generated samples must never be treated as real publications.',
    comic_title:title,
    hero:hero,
    publisher:pick(PUBLISHERS,rnd),
    first_published:year,
    issues:ri(rnd,1,60),
    genre:genre,
    era:era,
    era_label:ERA_LABEL[era],
    pages:ri(rnd,32,68),
    public_domain_note:'Sample entry — generated for structural purposes. Seeded archive records document real public-domain comics.',
    country:'United States',
    year:2026,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample listing — not a real comic. Seeded archive records are real public-domain comics; this generated record is structural only.',
    demo:{kind:'catalog-card',program:"function comicCard(c){return c.comic_title+' ('+c.first_published+') — '+c.publisher+'; '+c.issues+' issues, '+c.genre;}",note:'Paste into any JS console with a comic record to render a one-line catalog card.'},
    _seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-PUBC-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.comic_title!=='string'||r.comic_title.length<3)e.push('comic_title');
  if(typeof r.first_published!=='number'||r.first_published<1900||r.first_published>1975)e.push('first_published');
  if(ERAS.indexOf(r.era)<0)e.push('era');
  if(typeof r.publisher!=='string'||!r.publisher)e.push('publisher');
  if(!r.src)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.comic_title===record.comic_title&&r.publisher===record.publisher;});
  return dups.length?{ok:false,errors:['duplicate title+publisher in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-public-comics-1.0',generate:generate,validate:validate,driftCheck:driftCheck,eras:ERAS,genres:GENRES};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-comics',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
