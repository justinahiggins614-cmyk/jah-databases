(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["etymology", "naming-convention", "brand-naming", "place-naming"];
var PREFIX="JAH-NAMES-";
/* rows: [category, display name, meaning, origin, ladder_rank] */
var B=[
 ["etymology","How name etymology works","Name etymology traces a name back through its root words: the earliest recorded form, the language family it belongs to, and the sound changes that shaped it on","name collection",1],
 ["naming-convention","Patronymic surnames worldwide","Across cultures, 'son of' became a surname: English -son (Johnson), Scottish and Irish Mac and O' (MacDonald, O'Brien), Arabic ibn (Ibn Battuta), Russian -ovich","name collection",2],
 ["naming-convention","Occupational surnames worldwide","Jobs became last names on every continent: Smith, Schmidt, Kowalski, and Ferrari all mean the smith; Taylor, Weber, and Haddad name the tailor, weaver, and blac","name collection",2],
 ["naming-convention","Descriptive surnames","Before surnames were inherited, people were told apart by description: Brown and Rossi for coloring, Short and Long for build, Young for the younger of two same","name collection",2],
 ["naming-convention","Place-based surnames","Many surnames are addresses in disguise: Hill and Dubois ('of the wood') for where a family lived, Van den Berg ('from the mountain') and Yamamoto ('base of the","name collection",2],
 ["naming-convention","Chinese naming conventions","Chinese names put the family name first — Wang Wei is Mr. Wang — followed by a one- or two-character given name. Siblings often share a generation character, on","name collection",2],
 ["naming-convention","Arabic naming conventions","A classical Arabic name is a chain: the ism (personal name, e.g. Muhammad), the nasab (lineage — ibn/bint, 'son/daughter of'), the kunya (Abu/Umm, 'father/mothe","name collection",2],
 ["naming-convention","Spanish and Portuguese naming","Spanish speakers traditionally carry two surnames — the father's first surname followed by the mother's first surname — so both family lines stay visible for a ","name collection",2],
 ["naming-convention","Russian naming","A full Russian name has three parts: given name, patronymic, and surname — Ivan Ivanovich Petrov is Ivan, son of Ivan, of the Petrov family. Surnames take gende","name collection",2],
 ["naming-convention","Korean naming","Korean names are usually three syllables: a one-syllable family name (Kim, Lee, Park) followed by a two-syllable given name. The given name's meaning is fixed b","name collection",2],
 ["naming-convention","Icelandic naming","Iceland still uses a living patronymic system instead of inherited surnames: Jon's son is Jonsson, his daughter is Jonsdottir. Phone books sort by first name, a","name collection",3],
 ["naming-convention","South Asian naming conventions","South Asian naming runs on several tracks at once: Sikh men take Singh ('lion') and women Kaur ('princess'); Tamil names often use a patronymic initial plus giv","name collection",3],
 ["brand-naming","Brand and product naming conventions","Product names follow a small set of proven patterns: descriptive (General Motors), invented (Kodak — chosen because it meant nothing in any language), portmante","name collection",3],
 ["place-naming","Place-naming conventions","Settlers name new places the same few ways everywhere: after the homeland (New York, New Orleans), after a founder or patron (Washington, Johannesburg), after t","name collection",3],
 ["naming-convention","Naming taboos and honorifics","Many cultures fence names with rules: imperial China forbade writing an emperor's given name (the naming taboo); Burmese names take honorifics U and Daw instead","name collection",3]
];
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=B.filter(function(b){return b[0]===cat;});
  var b=pick(pool.length?pool:B,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,name:b[1],title:(b[1]+' \u2014 '+b[2]).slice(0,80),meaning:b[2],origin:b[3],category:cat,ladder_rank:b[4],_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var esc="JAH-NAMES-".replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+esc+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.meaning!=='string'||!r.meaning.length)e.push('meaning');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  return {ok:!e.length,errors:e};
}
var gen={version:"jahdb-names-database-1.0",generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("names-database",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
