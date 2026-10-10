(function(){'use strict';
/* JAH Handicrafts Published Archive Database — deterministic boundless generator (jahdb-handicrafts-published-1.0).
   Published-work archive records: Level 1 = real published works
   (real authors/titles); Level 2 = Signature projections (title always
   begins "Level 2"). Same seed always makes the same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var SLUG='handicrafts-published';
var BASE='handicrafts';
var GENVER='jahdb-handicrafts-published-1.0';
var PREFIX='JAH-handicrafts-published-P-';
var CATS=["textiles", "ceramics", "woodwork", "papercraft", "metalwork", "design-theory"];
var WORKS=[["A Potter\u2019s Book", "Bernard Leach", "Faber and Faber", 1940, "ceramics", "Leach sets out the philosophy and practice of the studio potter, blending English slipware traditions with Japanese and Korean influences learned from Shoji Hamada. It covers clay bodies, glazes, kiln firing, and the ethics of handmade production, arguing that the potter\u2019s character shows in the work.", ["stoneware", "celadon glaze", "throwing"]], ["On Weaving", "Anni Albers", "Wesleyan University Press", 1965, "textiles", "Albers treats weaving as both ancient craft and modern design language. She traces fibers, looms, and drafts from pre-Columbian Peru to the Bauhaus, insisting that material knowledge \u2014 how thread behaves under tension \u2014 is the weaver\u2019s true theory.", ["plain weave", "warp", "weft"]], ["The Soul of a Tree: A Woodworker\u2019s Reflections", "George Nakashima", "Kodansha International", 1981, "woodwork", "Nakashima describes a woodworking life guided by the tree itself: reading grain, honoring knots and voids with butterfly joints, and building furniture \u2014 especially his live-edge tables \u2014 that lets the wood speak. A blend of memoir, technique, and spiritual craft.", ["live edge", "butterfly joint", "grain"]], ["The Craftsman", "Richard Sennett", "Yale University Press", 2008, "woodwork", "Sennett examines craftsmanship as a human impulse \u2014 the desire to do a job well for its own sake \u2014 across workshops from Stradivari\u2019s Cremona to modern laboratories. He argues that skill develops through slow, repetitive practice and that material resistance teaches thinking.", ["workmanship", "material resistance", "workshop"]], ["The Nature and Art of Workmanship", "David Pye", "Cambridge University Press", 1968, "woodwork", "Pye distinguishes the \u2018workmanship of risk\u2019 \u2014 where quality depends on the maker\u2019s judgment moment by moment \u2014 from the \u2018workmanship of certainty\u2019 of mass production. The book defends hand skill as a distinct, irreplaceable kind of knowledge.", ["workmanship of risk", "workmanship of certainty", "hand skill"]], ["Japanese Woodworking Tools: Their Tradition, Spirit, and Use", "Toshio Odate", "Linden Publishing", 1984, "woodwork", "Odate explains the selection, tuning, and use of Japanese planes, chisels, and saws, rooted in the carpenter\u2019s spiritual discipline. The pull-stroke, waterstone sharpening, and tool maintenance are presented as a unified practice of respect for material and tool.", ["kanna (plane)", "pull saw", "waterstone"]], ["Mary Thomas\u2019s Knitting Book", "Mary Thomas", "Hodder & Stoughton", 1938, "textiles", "Thomas compiled stitch dictionaries, garment construction, and a history of knitting from Egyptian socks to Shetland lace. It remains a reference for stitch patterns, shaping, and finishing, written for knitters who want both technique and tradition.", ["stitch pattern", "shaping", "grafting"]], ["A Handweaver\u2019s Pattern Book", "Marguerite P. Davison", "Marguerite P. Davison", 1944, "textiles", "Davison\u2019s draft collection gave home weavers hundreds of four-shaft threading drafts with tie-ups and treadlings. It standardized how drafts are written and read, making complex twills, overshot, and summer-and-winter accessible to small looms.", ["threading draft", "tie-up", "treadling"]], ["The Development of Embroidery in America", "Candace Wheeler", "Harper & Brothers", 1921, "textiles", "Wheeler, a founder of American art needlework, traces embroidery from colonial samplers to the professional workshops of the early 1900s. She documents stitches, design transfer, and the movement that made needlework a respected applied art for women.", ["sampler", "art needlework", "stitch"]], ["Paper Magic: The Art of Paper Folding", "Robert Harbin", "Oldbourne", 1956, "papercraft", "Harbin\u2019s book introduced origami to English readers with step-by-step diagrams for classic models. It established the diagram conventions \u2014 valley and mountain folds, squash and petal folds \u2014 that Western folders still learn first.", ["valley fold", "mountain fold", "diagram"]], ["Origami for the Enthusiast", "Kunihiko Kasahara", "Japan Publications", 1998, "papercraft", "Kasahara\u2019s collection moves from simple traditional models to complex original designs, teaching the geometry hidden in each fold. A bridge from beginner paper-folding to serious origami design.", ["crease pattern", "folding sequence", "modular origami"]], ["The Unknown Craftsman: A Japanese Insight into Beauty", "Soetsu Yanagi", "Kodansha International", 1972, "ceramics", "Yanagi, founder of the mingei folk-craft movement, argues that beauty lives in humble, anonymous, everyday objects made by unknown craftspeople. The essays defend handmade folk wares against industrial uniformity and connoisseur snobbery alike.", ["mingei", "folk craft", "wabi"]], ["Hopes and Fears for Art", "William Morris", "Ellis & White", 1882, "design-theory", "Morris\u2019s lectures attack industrial shoddiness and call for joyful, skilled hand labor in the decorative arts. The book became the manifesto of the Arts and Crafts movement, linking craft quality to the dignity of the worker.", ["Arts and Crafts", "hand labor", "pattern design"]], ["The Grammar of Ornament", "Owen Jones", "Day and Son", 1856, "design-theory", "Jones assembled one hundred color plates of ornament from Egyptian to Elizabethan, deriving thirty-seven propositions of design. It became the pattern bible of the Victorian decorative arts and still guides craft surface design.", ["ornament", "pattern", "chromolithograph"]], ["Oriental Carpets: An Essay on Their History", "Kurt Erdmann", "Universe Books", 1970, "textiles", "Erdmann brought scholarly rigor to carpet studies, classifying Anatolian and Persian pile carpets by structure, knot, and dated examples. The book teaches collectors and makers to read a carpet\u2019s origin in its weave.", ["pile knot", "warp", "kilim"]], ["Metalwork and Enamelling", "Herbert Maryon", "Chapman & Hall", 1912, "metalwork", "Maryon, metalsmith of the British Museum, gives a practical treatise on forging, soldering, chasing, and enamelling. Workshop technique recorded by a master restorer of ancient metalwork.", ["chasing", "enamelling", "soldering"]], ["Jewelry: Concepts and Technology", "Oppi Untracht", "Doubleday", 1982, "metalwork", "Untracht\u2019s comprehensive manual covers jewelry techniques from fabrication to stone setting, with attention to tools across cultures. The standard reference for professional jewelers and metalsmiths.", ["fabrication", "stone setting", "soldering"]], ["National Core Arts Standards", "National Coalition for Core Arts Standards", "National Coalition for Core Arts Standards", 2014, "design-theory", "The U.S. National Core Arts Standards define what students should know in visual and media arts, including craft processes. They frame creating, presenting, responding, and connecting as the artistic processes behind every handmade discipline.", ["creating", "presenting", "responding"]]];
var PROJ=[["Bio-Material Basketry", "Mycelium and bacterial cellulose woven into load-bearing vessels."], ["Robotic Loom Apprenticeship", "Cobot-assisted weaving that teaches draft reading by doing."], ["Zero-Waste Pattern Drafting", "Algorithmic nesting for small-studio textile cutting."], ["Digital Kiln Twins", "Sensor-mirrored firings that predict glaze outcomes."], ["Craft Micro-Factories", "Neighborhood workshops sharing kiln, loom, and bench time."], ["Augmented-Reality Joinery Tutoring", "Headset overlays that guide saw and chisel in real time."], ["Heritage Craft Knowledge Archives", "Motion-captured hand skills of master makers, preserved."], ["Circular Textile Economies", "Fiber-to-fiber loops designed at the pattern stage."], ["Community Kiln Networks", "Shared firing schedules across city studio cooperatives."], ["Parametric Carving for Beginners", "Rule-based relief design carved with guided hand tools."], ["Craft Therapy Protocols", "Measured clinical programs using handwork for recovery."], ["Open-Source Tool Libraries", "Borrowable woodworking kits with video instruction."]];
var METHODS='studio trials, material testing, and interviews with working makers';
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
