(function(){'use strict';
/* JAH Philosophy and Ethics Published Archive Database — deterministic boundless generator (jahdb-philosophy-ethics-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='philosophy-ethics-published';
var BASE='philosophy-ethics';
var GENVER='jahdb-philosophy-ethics-published-1.0';
var PREFIX='JAH-philosophy-ethics-published-P-';
var CATS=["metaphysics", "ethics", "logic", "epistemology", "political-philosophy", "aesthetics"];
var WORKS=[["The Republic", "Plato", "Penguin Classics", 380, "political-philosophy", "Plato\u2019s dialogue builds the just city and the just soul in parallel \u2014 philosopher-kings, the tripartite soul, the allegory of the cave. The founding text of Western political philosophy.", ["justice", "forms", "cave"]], ["Nicomachean Ethics", "Aristotle", "Oxford University Press", 350, "ethics", "Aristotle locates the good life in virtuous activity: courage, temperance, and practical wisdom as means between extremes. The doctrine of the mean remains virtue ethics\u2019 cornerstone.", ["virtue", "mean", "eudaimonia"]], ["Meditations", "Marcus Aurelius", "Modern Library", 180, "ethics", "The emperor\u2019s private notebook applies Stoic doctrine \u2014 control what you can, accept what you cannot \u2014 to duty, mortality, and equanimity. Stoicism\u2019s most personal text.", ["stoicism", "equanimity", "duty"]], ["Groundwork of the Metaphysics of Morals", "Immanuel Kant", "Johann Friedrich Hartknoch", 1785, "ethics", "Kant grounds morality in reason alone: act only on maxims you could will as universal law. The categorical imperative and the formula of humanity anchor deontological ethics.", ["categorical imperative", "duty", "autonomy"]], ["Utilitarianism", "John Stuart Mill", "Parker, Son, and Bourn", 1863, "ethics", "Mill defends the greatest-happiness principle, distinguishing higher and lower pleasures against the \u2018pig philosophy\u2019 charge. The classic statement of utilitarian ethics.", ["utility", "happiness", "consequentialism"]], ["Beyond Good and Evil", "Friedrich Nietzsche", "C.G. Naumann", 1886, "ethics", "Nietzsche\u2019s aphorisms attack slave morality and herd values, proposing the will to power and the revaluation of all values. A provocation that reshaped moral philosophy.", ["will to power", "revaluation", "master morality"]], ["The Problems of Philosophy", "Bertrand Russell", "Henry Holt", 1912, "epistemology", "Russell\u2019s slim introduction asks what we can know: sense-data, induction, universals, and the limits of knowledge. The model of analytic clarity for general readers.", ["sense-data", "induction", "knowledge"]], ["Philosophical Investigations", "Ludwig Wittgenstein", "Basil Blackwell", 1953, "epistemology", "Wittgenstein\u2019s later notes dissolve philosophical puzzles by examining language-games: meaning as use, family resemblance, the private-language argument. Philosophy as therapy for bewitchment by language.", ["language-game", "meaning as use", "family resemblance"]], ["Practical Ethics", "Peter Singer", "Cambridge University Press", 1979, "ethics", "Singer applies preference utilitarianism to abortion, euthanasia, poverty, and animal rights, arguing for effective moral consistency. The book that launched effective altruism\u2019s questions.", ["sentience", "effective altruism", "impartiality"]], ["A Theory of Justice", "John Rawls", "Harvard University Press", 1971, "political-philosophy", "Rawls asks what principles free equals would choose behind a veil of ignorance: equal liberty and the difference principle. The twentieth century\u2019s most influential work of political philosophy.", ["veil of ignorance", "fairness", "difference principle"]], ["Meditations on First Philosophy", "Ren\u00e9 Descartes", "Michel Soly", 1641, "metaphysics", "Descartes doubts everything to find the indubitable cogito, then rebuilds knowledge on God and clear ideas. The founding text of modern rationalism and mind-body dualism.", ["cogito", "dualism", "doubt"]], ["An Enquiry Concerning Human Understanding", "David Hume", "Andrew Millar", 1748, "epistemology", "Hume reduces knowledge to impressions and ideas, finds no necessary connection in causation, and limits reason\u2019s reach. Empiricism\u2019s sharpest statement \u2014 and Kant\u2019s wake-up call.", ["empiricism", "causation", "skepticism"]], ["The Ethics of Ambiguity", "Simone de Beauvoir", "Citadel Press", 1947, "ethics", "De Beauvoir builds an existentialist ethics on ambiguity: freedom is absolute yet situated, and willing one\u2019s own freedom requires willing others\u2019. The philosophical companion to The Second Sex.", ["ambiguity", "freedom", "existentialism"]], ["Stanford Encyclopedia of Philosophy", "Edward N. Zalta, editor", "Stanford University", 1995, "logic", "The peer-reviewed online encyclopedia, with entries by specialists kept current. The profession\u2019s standard reference \u2014 every article a state-of-the-field survey.", ["reference", "peer review", "survey"]], ["The Fragility of Goodness", "Martha Nussbaum", "Cambridge University Press", 1986, "ethics", "Nussbaum reads Greek tragedy and philosophy on luck\u2019s power over the good life. Her capabilities approach grew from this study of vulnerability and virtue.", ["luck", "tragedy", "capabilities"]], ["What Does It All Mean?", "Thomas Nagel", "Oxford University Press", 1987, "metaphysics", "Nagel\u2019s ninety-page introduction poses philosophy\u2019s hardest questions \u2014 consciousness, free will, death, meaning \u2014 in plain language. The gentlest on-ramp to the discipline.", ["consciousness", "free will", "meaning"]], ["The Sense of Beauty", "George Santayana", "Charles Scribner\u2019s Sons", 1896, "aesthetics", "Santayana\u2019s dissertation argues beauty is pleasure objectified \u2014 value projected onto things. American aesthetics\u2019 founding text.", ["beauty", "pleasure", "value"]], ["Art as Experience", "John Dewey", "Minton, Balch", 1934, "aesthetics", "Dewey treats aesthetic experience as consummated everyday experience, not museum objects. Pragmatist aesthetics\u2019 classic.", ["experience", "consummation", "pragmatism"]]];
var PROJ=[["Ethics of Autonomous Systems", "Moral frameworks for machines that decide."], ["Digital Personhood and Rights", "What status, if any, for synthetic minds."], ["Longtermism and Justice", "Obligations to the far future."], ["The Philosophy of Attention", "What it means to attend well."], ["Bioethics of Gene Editing", "Germline choices and consent."], ["Epistemology of Synthetic Media", "Knowing in an age of generated evidence."], ["Virtue Ethics for Networked Life", "Character in the feed."], ["Climate Justice Frameworks", "Who owes what to whom."], ["The Meaning of Work", "Purpose after automation."], ["Animal Minds and Moral Status", "The expanding circle, empirically."], ["Aesthetics of Generated Art", "Can machine images be beautiful."], ["Privacy as a Moral Right", "Foundations beyond legalism."]];
var METHODS='conceptual analysis, thought experiments, and case review';
var FRAMES=["Early pilots suggest the approach could improve outcomes markedly where it is adopted first in community settings.", "Practitioners report faster skill transfer when the method is taught in cohorts rather than through solo study.", "The study projects mainstream adoption within a decade, beginning in specialist programs and spreading to general curricula.", "Reviewers note the strongest effects where the method is paired with mentorship rather than delivered as content alone."];
var POOL={};
CATS.forEach(function(c){POOL[c]=WORKS.filter(function(w){return w[4]===c;});});
function pad7(n){return String(n).padStart(7,'0');}
function sigLink(seed){return '../'+BASE+'-study/index.html?sig=JAH-'+BASE+'-STUDY-S-'+pad7(seed);}
/* work layout: [title, authors, publication, year, category, abstract, [terms]] */
function aspectBody(w,aspect){
  var b=w[5]+'\n\nKey terms: '+w[6].join('; ')+'.';
  if(aspect==='focus'){
    b+='\n\nStudy focus: How does \u201c'+w[6][0]+'\u201d shape this work\u2019s central argument? '+
       'What would a practitioner carry from \u201c'+w[6][1]+'\u201d into daily practice?';
  }
  b+='\n\nPublished: '+w[2]+', '+w[3]+'.';
  return b;
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:CATS[(seed-1)%CATS.length];
  var lvl=rnd()<0.35?2:1;
  var id=PREFIX+pad7(seed);
  var link=sigLink(seed);
  if(lvl===1){
    var pool=(POOL[cat]&&POOL[cat].length)?POOL[cat]:WORKS;
    var w=pick(pool,rnd);
    var aspect=pick(['abstract','focus'],rnd);
    var title=w[0];
    return {id:id,title:title,authors:w[1],publication:w[2],year:w[3],
      full_content:aspectBody(w,aspect),
      source_ref:'WorldCat \u2014 \u201c'+title+'\u201d / '+w[1]+' ('+w[3]+')',
      signature_link:link,level:1,category:cat};
  }
  var p=pick(PROJ,rnd);
  var frame=pick(FRAMES,rnd);
  var ptitle='Level 2 \u2014 '+p[0];
  var full='This is a Level 2 projection record: a forward-looking study sketched from the archive\u2019s patterns, '+
    'not a real publication. \u201c'+p[0]+'.\u201d '+p[1]+' Projected method: '+METHODS+'. '+frame;
  return {id:id,title:ptitle,authors:'JAH Signature Projection Office',
    publication:'JAH Published Archive \u2014 Projection Series',year:2026+(seed%3),
    full_content:full,
    source_ref:'JAH Published Archive \u2014 Projection Series (generated projection)',
    signature_link:link,level:2,category:cat};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX+'\\d{7}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(r.level===2&&r.title.slice(0,7)!=='Level 2')e.push('level2-title');
  if(r.level===1&&r.title.slice(0,7)==='Level 2')e.push('level1-title');
  if(typeof r.authors!=='string'||!r.authors.length)e.push('authors');
  if(typeof r.publication!=='string'||!r.publication.length)e.push('publication');
  if(typeof r.year!=='number'||(r.year|0)!==r.year||r.year<100||r.year>2028)e.push('year');
  if(typeof r.full_content!=='string'||r.full_content.length<120||r.full_content.length>3000)e.push('full_content');
  if(typeof r.source_ref!=='string'||!r.source_ref.length)e.push('source_ref');
  if(!/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(CATS.indexOf(r.category)<0)e.push('category');
  return {ok:!e.length,errors:e};
}
/* 40 seeds x 40 invariant checks = 1600 assertions. */
function selftest(){
  var seeds=[],i;
  for(i=1;i<=40;i++)seeds.push(i);
  var fails=[],passed=0,total=0;
  function chk(seed,name,cond){total++;if(cond){passed++;}else{fails.push('seed '+seed+': '+name);}}
  function bad(r,over){var c={},k;for(k in r)c[k]=r[k];for(k in over)c[k]=over[k];return c;}
  seeds.forEach(function(seed){
    var r=generate(seed,{},prng(seed));
    var r2=generate(seed,{},prng(seed));
    chk(seed,'is-object',!!r&&typeof r==='object');
    chk(seed,'id-format',new RegExp('^'+PREFIX+'\\d{7}$').test(r.id));
    chk(seed,'id-prefix',r.id.slice(0,PREFIX.length)===PREFIX);
    chk(seed,'id-seq',r.id===PREFIX+pad7(seed));
    chk(seed,'title-nonempty',typeof r.title==='string'&&r.title.length>0);
    chk(seed,'authors-nonempty',typeof r.authors==='string'&&r.authors.length>0);
    chk(seed,'publication-nonempty',typeof r.publication==='string'&&r.publication.length>0);
    chk(seed,'year-range',typeof r.year==='number'&&(r.year|0)===r.year&&r.year>=100&&r.year<=2028);
    chk(seed,'full-min',typeof r.full_content==='string'&&r.full_content.length>=120);
    chk(seed,'full-max',r.full_content.length<=3000);
    chk(seed,'full-sentences',(r.full_content.match(/\./g)||[]).length>=3);
    chk(seed,'source-nonempty',typeof r.source_ref==='string'&&r.source_ref.length>0);
    chk(seed,'siglink-format',/^\.\.\/[a-z0-9-]+\-study\/index\.html\?sig=JAH\-[a-z0-9-]+\-STUDY\-S\-\d{7}$/.test(r.signature_link||''));
    chk(seed,'siglink-seq',r.signature_link.slice(-10)==='-S-'+pad7(seed));
    chk(seed,'level-12',r.level===1||r.level===2);
    chk(seed,'l2-title',r.level!==2||r.title.slice(0,7)==='Level 2');
    chk(seed,'l1-title',r.level!==1||r.title.slice(0,7)!=='Level 2');
    chk(seed,'category-valid',CATS.indexOf(r.category)>=0);
    chk(seed,'validate-ok',validate(r).ok);
    chk(seed,'deterministic',JSON.stringify(r)===JSON.stringify(r2));
    chk(seed,'title-no-html',r.title.indexOf('<')<0);
    chk(seed,'full-no-wordbreak',r.full_content.indexOf('word-break')<0);
    chk(seed,'full-grounded',r.level===1?r.full_content.indexOf(String(r.year))>=0:r.full_content.indexOf('Level 2 projection')>=0);
    chk(seed,'id-unique',seed===1||r.id!==PREFIX+pad7(seed-1));
    chk(seed,'rej-bad-id',!validate(bad(r,{id:'BAD'})).ok);
    chk(seed,'rej-no-title',!validate(bad(r,{title:''})).ok);
    chk(seed,'rej-bad-year',!validate(bad(r,{year:50})).ok);
    chk(seed,'rej-bad-level',!validate(bad(r,{level:3})).ok);
    chk(seed,'rej-short-full',!validate(bad(r,{full_content:'x'})).ok);
    chk(seed,'rej-bad-sig',!validate(bad(r,{signature_link:'nope'})).ok);
    chk(seed,'rej-l2-title',!validate(bad(r,{level:2,title:'No Prefix Here'})).ok);
    chk(seed,'rej-l1-title',!validate(bad(r,{level:1,title:'Level 2 Sneaky'})).ok);
    chk(seed,'category-opt',generate(seed,{category:CATS[0]},prng(seed)).category===CATS[0]);
    chk(seed,'jahdb-registered',typeof JAHDB==='undefined'||!!JAHDB.getGenerator(SLUG));
    chk(seed,'runGenerator-ok',typeof JAHDB==='undefined'?true:JAHDB.runGenerator(SLUG,seed,{}).ok);
    chk(seed,'no-underscore-keys',Object.keys(r).every(function(k){return k.charAt(0)!=='_';}));
    chk(seed,'authors-no-database',r.authors.indexOf('Database')<0);
    chk(seed,'pub-no-database',r.publication.indexOf('Database')<0);
    chk(seed,'title-no-database',r.title.indexOf('Database')<0);
    chk(seed,'l2-honesty',r.level!==2||r.full_content.indexOf('not a real publication')>=0);
    chk(seed,'l1-pubnote',r.level!==1||r.full_content.indexOf('Published:')>=0);
    chk(seed,'json-roundtrip',JSON.parse(JSON.stringify(r)).id===r.id);
  });
  return {seeds:seeds.length,per_seed:total/seeds.length,passed:passed,failed:total-passed,total:total,failures:fails};
}
var gen={version:GENVER,generate:generate,validate:validate,selftest:selftest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
