(function(){'use strict';
/* JAH Political Sciences and Civics Published Archive Database — deterministic boundless generator (jahdb-political-science-civics-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='political-science-civics-published';
var BASE='political-science-civics';
var GENVER='jahdb-political-science-civics-published-1.0';
var PREFIX='JAH-political-science-civics-published-P-';
var CATS=["theory", "comparative", "international-relations", "public-policy", "civics", "political-economy"];
var WORKS=[["Politics", "Aristotle", "Penguin Classics", 350, "theory", "Aristotle classifies constitutions \u2014 monarchy, aristocracy, polity and their corruptions \u2014 and defends the mixed regime of the middle class. Political science\u2019s first textbook.", ["constitution", "polity", "citizenship"]], ["The Prince", "Niccol\u00f2 Machiavelli", "Antonio Blado d\u2019Asola", 1532, "theory", "Machiavelli advises rulers on acquiring and holding power, separating politics from Christian morals. Realism\u2019s founding handbook.", ["power", "virt\u00f9", "fortuna"]], ["Two Treatises of Government", "John Locke", "Awnsham Churchill", 1689, "theory", "Locke\u2019s Second Treatise grounds legitimate government in consent and natural rights to life, liberty, and property. The philosophical basis of liberal democracy.", ["consent", "natural rights", "property"]], ["The Federalist Papers", "Alexander Hamilton, James Madison, John Jay", "J. and A. McLean", 1788, "civics", "The 85 essays defended the U.S. Constitution \u2014 federalism, separation of powers, the extended republic. American civics\u2019 founding commentary.", ["federalism", "republic", "separation of powers"]], ["Democracy in America", "Alexis de Tocqueville", "Gosselin", 1835, "comparative", "Tocqueville\u2019s travel study found American democracy\u2019s strength in associations and mores \u2014 and warned of the tyranny of the majority. Comparative politics\u2019 first classic.", ["associations", "tyranny of majority", "mores"]], ["The Social Contract", "Jean-Jacques Rousseau", "Marc-Michel Rey", 1762, "theory", "Rousseau asks how free individuals can submit to law: through the general will, in which each obeys only himself. Democracy\u2019s most radical theory.", ["general will", "sovereignty", "freedom"]], ["The U.S. Constitution", "Constitutional Convention", "National Archives", 1787, "civics", "The Constitution\u2019s seven articles frame the federal government \u2014 Congress, presidency, courts \u2014 with amendment and supremacy clauses. The operating system of American government.", ["articles", "amendment", "supremacy"]], ["AP U.S. Government and Politics Course Description", "College Board", "College Board", 2019, "civics", "The College Board framework covers constitutional foundations, civil rights, and political participation. The national standard for high-school civics.", ["constitution", "civil rights", "participation"]], ["The Clash of Civilizations and the Remaking of World Order", "Samuel P. Huntington", "Simon & Schuster", 1996, "international-relations", "Huntington argued post-Cold War conflict would follow cultural-civilizational fault lines. The most debated IR thesis of the 1990s.", ["civilization", "fault line", "identity"]], ["Polyarchy: Participation and Opposition", "Robert A. Dahl", "Yale University Press", 1971, "comparative", "Dahl defines working democracy as polyarchy \u2014 contestation plus inclusive participation \u2014 and studies its conditions. Democratization\u2019s standard framework.", ["polyarchy", "contestation", "participation"]], ["The Civic Culture", "Gabriel Almond, Sidney Verba", "Princeton University Press", 1963, "comparative", "Almond and Verba\u2019s five-nation survey linked democratic stability to a participant civic culture. Political culture research began here.", ["political culture", "survey", "stability"]], ["The Origins of Totalitarianism", "Hannah Arendt", "Harcourt, Brace", 1951, "theory", "Arendt traces totalitarianism to antisemitism, imperialism, and mass loneliness, analyzing ideology and terror. The century\u2019s deepest study of total domination.", ["totalitarianism", "ideology", "loneliness"]], ["We the People: The Citizen and the Constitution", "Center for Civic Education", "Center for Civic Education", 1987, "civics", "The Center\u2019s textbook teaches constitutional principles through critical-thinking exercises and simulated hearings. The flagship U.S. civics curriculum.", ["citizenship", "hearing", "principle"]], ["Theory of International Politics", "Kenneth N. Waltz", "Addison-Wesley", 1979, "international-relations", "Waltz\u2019s neorealism explains state behavior by the anarchic structure of the system, not human nature. IR theory\u2019s structural turn.", ["anarchy", "structure", "balance of power"]], ["Introduction to Comparative Politics", "Mark Kesselman, Joel Krieger", "Houghton Mifflin", 1996, "comparative", "The thematic text compares Britain, France, Germany, Japan, and others on states, nations, and development. The comparative classroom standard.", ["state", "nation", "development"]], ["Politics as a Vocation", "Max Weber", "Duncker & Humblot", 1919, "political-economy", "Weber\u2019s lecture defines the state by its monopoly of legitimate violence and politics by the ethic of responsibility. The classic on power and vocation.", ["state", "violence", "responsibility"]], ["The Great Transformation", "Karl Polanyi", "Farrar & Rinehart", 1944, "political-economy", "Polanyi argues markets were politically created and that labor, land, and money are fictitious commodities. The double movement frames economy and society.", ["embeddedness", "double movement", "fictitious commodity"]], ["Policy Paradox: The Art of Political Decision Making", "Deborah Stone", "W. W. Norton", 1988, "public-policy", "Stone shows policy analysis is political storytelling \u2014 equity, efficiency, and liberty framed through paradox. The interpretive classic of policy studies.", ["paradox", "equity", "narrative"]]];
var PROJ=[["Digital Democracy Platforms", "Deliberation software in real legislatures."], ["AI in Governance", "Machine assistance in administration."], ["The Future of the Nation-State", "Sovereignty under pressure."], ["Climate Migration and Borders", "Law for the displaced."], ["Civic Education for Synthetic Media", "Teaching citizens to verify."], ["Citizens\u2019 Assemblies", "Sortition in policymaking."], ["Platform Power and Sovereignty", "Who governs the networks."], ["The Politics of Longevity", "Policy for 120-year lives."], ["Urban Governance 2040", "The city as the key polity."], ["Electoral Systems for Fragmented Publics", "Representation after the big tent."], ["Global Health Governance", "Institutions for the next pandemic."], ["Civic Tech Standards", "Interoperability for democratic tools."]];
var METHODS='survey research, comparative case studies, and institutional analysis';
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
