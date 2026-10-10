(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,a){return a[(r()*a.length)|0];}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad7(n){return String(n).padStart(7,'0');}
function fmtYear(y){return y<0?(Math.abs(y)+' BCE'):String(y);}
var BASE="law-study";
var SLUG="law-study-published";
var STUDYSLUG=(BASE.slice(-6)==='-study')?BASE:BASE+'-study';
var PREFIX="JAH-law-study-published-P-";
var FIELD="Law";
var GENVER="jahdb-law-study-published-1.0";
var CATS=["Constitutional Law", "Criminal Law", "Contract Law", "Torts", "Property Law", "International Law", "Legal Theory", "Civil Procedure"];
var L1=[["Brown v. Board of Education", ["U.S. Supreme Court"], "U.S. Reports, Vol. 347", 1954, 0, "The Supreme Court held unanimously that racial segregation in public schools violates the Equal Protection Clause of the Fourteenth Amendment. Chief Justice Warren wrote that separate educational facilities are inherently unequal. The decision overturned Plessy v. Ferguson in the schools and launched the modern civil rights era."], ["Marbury v. Madison", ["U.S. Supreme Court"], "U.S. Reports, Vol. 5", 1803, 0, "Chief Justice Marshall established the principle of judicial review: courts may strike down acts of Congress that conflict with the Constitution. William Marbury's undelivered judicial commission became the vehicle for the most consequential jurisdictional ruling in American law. The case made the Supreme Court a coequal branch."], ["Miranda v. Arizona", ["U.S. Supreme Court"], "U.S. Reports, Vol. 384", 1966, 1, "The Court required police to warn suspects of their rights — to remain silent, to counsel, and that statements may be used against them — before custodial interrogation. Chief Justice Warren's majority opinion created the warnings now read on every arrest. It remains the signature protection of the Fifth Amendment in the stationhouse."], ["Gideon v. Wainwright", ["U.S. Supreme Court"], "U.S. Reports, Vol. 372", 1963, 1, "The Court held that the Sixth Amendment guarantees every criminal defendant the right to appointed counsel, even in state courts. Clarence Gideon's handwritten petition from a Florida prison cell produced a unanimous ruling by Justice Black. Public defender systems across America trace their mandate to this case."], ["The Federalist Papers", ["Alexander Hamilton", "James Madison", "John Jay"], "Newspaper essays, collected 1788", 1788, 0, "Eighty-five essays urging ratification of the U.S. Constitution, written under the name Publius. Madison's Federalist No. 10 argues that a large republic controls faction; Hamilton's No. 78 defends judicial review. They remain the authoritative contemporary commentary on the Constitution's meaning."], ["Commentaries on the Laws of England", ["Sir William Blackstone"], "Clarendon Press, Oxford", 1769, 6, "Four volumes systematizing English common law — rights of persons, things, private wrongs, and public wrongs. Blackstone's elegant organization carried English law to America, where the Commentaries became the standard legal education of the founding generation. Few books have shaped a legal system so completely."], ["The Common Law", ["Oliver Wendell Holmes Jr."], "Little, Brown and Company", 1881, 6, "Holmes's lectures argue that the life of the law has not been logic but experience — felt necessities and moral judgments. Tracing doctrines from ancient forms to modern negligence, he founded American legal realism's spirit. The book remains the most quotable work in American jurisprudence."], ["The Nature of the Judicial Process", ["Benjamin N. Cardozo"], "Yale University Press", 1921, 6, "Cardozo's Storrs Lectures describe how judges actually decide cases: by logic, history, custom, and the social welfare. Written while he sat on New York's highest court, it demystified judging without diminishing it. Generations of law students meet the judicial mind here first."], ["The Concept of Law", ["H.L.A. Hart"], "Clarendon Press, Oxford", 1961, 6, "Hart's masterwork presents law as a system of primary rules of obligation united by secondary rules, especially the rule of recognition. It revived legal positivism and set the agenda for analytic jurisprudence for half a century. Dworkin built his career answering it."], ["A Theory of Justice", ["John Rawls"], "Harvard University Press", 1971, 6, "Rawls asks what principles free and equal persons would choose behind a veil of ignorance, deriving justice as fairness with its liberty principle and difference principle. The book revived political philosophy as a living discipline. Its apparatus dominates debates about distributive justice to this day."], ["The Bramble Bush", ["Karl N. Llewellyn"], "Oceana Publications", 1930, 6, "Llewellyn's lectures to first-year law students at Columbia demystify the common law as a working craft rather than a logic machine. Blunt, humane, and practical, it teaches students to see rules as tools. It remains the classic initiation into legal realism."], ["Restatement (Second) of Contracts", ["American Law Institute"], "American Law Institute", 1981, 2, "The ALI's systematic restatement of American contract doctrine — formation, consideration, interpretation, performance, breach, and remedies. Courts cite its sections as persuasive authority nationwide. It is the closest American law has to a contracts code."], ["Federal Rules of Civil Procedure", ["U.S. Courts"], "U.S. Government", 1938, 7, "The uniform procedural code governing civil cases in federal court, born of the 1934 Rules Enabling Act. Notice pleading, broad discovery, and summary judgment all flow from these rules. Every federal litigator practices inside their architecture."], ["New York Times Co. v. Sullivan", ["U.S. Supreme Court"], "U.S. Reports, Vol. 376", 1964, 0, "The Court held that public officials suing for defamation must prove actual malice — knowledge of falsity or reckless disregard for truth. Justice Brennan's opinion constitutionalized libel law around robust public debate. American press freedom rests on this rule."], ["Mapp v. Ohio", ["U.S. Supreme Court"], "U.S. Reports, Vol. 367", 1961, 1, "The Court applied the exclusionary rule to the states: evidence seized in violation of the Fourth Amendment cannot be used at trial. Dollree Mapp's obscenity prosecution became the vehicle for incorporating the rule. It reshaped American policing overnight."], ["Griswold v. Connecticut", ["U.S. Supreme Court"], "U.S. Reports, Vol. 381", 1965, 0, "Striking down a ban on contraceptives, the Court found a right to privacy in the penumbras of the Bill of Rights. Justice Douglas's opinion created the doctrinal home for later autonomy cases. Privacy jurisprudence begins here."], ["United States v. Nixon", ["U.S. Supreme Court"], "U.S. Reports, Vol. 418", 1974, 0, "The Court unanimously ordered President Nixon to surrender the Watergate tapes, rejecting absolute executive privilege. The decision precipitated Nixon's resignation within weeks. It stands for the proposition that not even the President is above the law."], ["McCulloch v. Maryland", ["U.S. Supreme Court"], "U.S. Reports, Vol. 17", 1819, 0, "Marshall upheld Congress's power to charter a national bank under the Necessary and Proper Clause and barred states from taxing federal instruments. The power to tax is the power to destroy. It fixed the broad reading of federal power."], ["Gibbons v. Ogden", ["U.S. Supreme Court"], "U.S. Reports, Vol. 22", 1824, 0, "The Court held that Congress's commerce power extends to navigation and overrides conflicting state monopolies. Aaron Ogden's steamboat monopoly fell to Thomas Gibbons's federal license. The dormant commerce doctrine starts here."], ["Dred Scott v. Sandford", ["U.S. Supreme Court"], "U.S. Reports, Vol. 60", 1857, 0, "Chief Justice Taney held that Black Americans could not be citizens and that Congress could not ban slavery in the territories. The decision deepened the sectional crisis and hastened the Civil War. It is the Court's most reviled opinion, undone by the Fourteenth Amendment."], ["Plessy v. Ferguson", ["U.S. Supreme Court"], "U.S. Reports, Vol. 163", 1896, 0, "The Court upheld separate-but-equal segregation, with Justice Harlan alone dissenting that the Constitution is color-blind. The doctrine licensed Jim Crow for six decades. Brown v. Board repudiated it in 1954."], ["The Path of the Law", ["Oliver Wendell Holmes Jr."], "Harvard Law Review, Vol. 10", 1897, 6, "Holmes's famous address urging lawyers to view law from the bad man's perspective — as predictions of what courts will do. It separated law from morals and founded predictive legal theory. Every jurisprudence course still assigns it."], ["Law's Empire", ["Ronald Dworkin"], "Harvard University Press", 1986, 6, "Dworkin presents law as integrity: judges should decide cases by the best constructive interpretation of the community's legal practice. The chain-novel metaphor made adjudication a literary enterprise. It is the great rival statement to Hart's positivism."], ["Taking Rights Seriously", ["Ronald Dworkin"], "Harvard University Press", 1977, 6, "Dworkin argues that individuals hold moral rights against the state that judges must enforce even against majoritarian policy. The hard-cases argument made rights the center of jurisprudence. It reshaped liberal legal theory."], ["The Rule of Law", ["Tom Bingham"], "Allen Lane", 2010, 6, "The former senior Law Lord distills the rule of law into eight principles, from accessible law to fair adjudication. Written for citizens, not lawyers, it became a civic bestseller. It is the modern classic statement of the ideal."], ["Justice: What's the Right Thing to Do?", ["Michael J. Sandel"], "Farrar, Straus and Giroux", 2009, 6, "Sandel's Harvard course in book form stages debates — trolleys, price gouging, affirmative action — between utilitarian, libertarian, Kantian, and Aristotelian theories. It made moral philosophy a public spectacle. Millions encountered philosophy through it."], ["A Civil Action", ["Jonathan Harr"], "Random House", 1995, 1, "The true story of the Woburn, Massachusetts toxic-tort case against Beatrice Foods and W.R. Grace over contaminated water. Harr follows plaintiffs' lawyer Jan Schlichtmann through financial ruin and moral reckoning. It is the great American litigation narrative."], ["The Hollow Hope", ["Gerald N. Rosenberg"], "University of Chicago Press", 1991, 0, "Rosenberg argues empirically that courts rarely produce significant social change on their own — Brown and Roe changed less than believed. The constrained-court thesis provoked fierce debate. It remains the skeptical counterweight to court-centered reform."], ["Model Penal Code", ["American Law Institute"], "American Law Institute", 1962, 1, "The ALI's systematic model criminal code — culpability levels, inchoate crimes, defenses — adopted in whole or part by most states. It rationalized American criminal law's chaos. Its mental-state hierarchy is now the lingua franca."], ["Uniform Commercial Code", ["American Law Institute", "National Conference of Commissioners on Uniform State Laws"], "American Law Institute", 1952, 2, "The uniform statute governing sales, negotiable instruments, and secured transactions, adopted in every state but Louisiana. Article 2 and Article 9 structure American commerce. Karl Llewellyn was its chief architect."], ["The Magna Carta", ["Barons of England"], "Runnymede, England", 1215, 6, "The Great Charter forced from King John, limiting royal power and guaranteeing due process — no free man shall be seized except by lawful judgment. Though mostly feudal administration, its clauses became liberty's scripture. Every constitution echoes it."], ["Letter from a Birmingham Jail", ["Martin Luther King Jr."], "Published pamphlet", 1963, 0, "King's open letter to eight clergymen defends nonviolent direct action and the moral duty to disobey unjust laws. An unjust law is no law at all. It is the American canon's great statement of civil disobedience."]];
var L1_TITLES=["Brown v. Board of Education", "Marbury v. Madison", "Miranda v. Arizona", "Gideon v. Wainwright", "The Federalist Papers", "Commentaries on the Laws of England", "The Common Law", "The Nature of the Judicial Process", "The Concept of Law", "A Theory of Justice", "The Bramble Bush", "Restatement (Second) of Contracts", "Federal Rules of Civil Procedure", "New York Times Co. v. Sullivan", "Mapp v. Ohio", "Griswold v. Connecticut", "United States v. Nixon", "McCulloch v. Maryland", "Gibbons v. Ogden", "Dred Scott v. Sandford", "Plessy v. Ferguson", "The Path of the Law", "Law's Empire", "Taking Rights Seriously", "The Rule of Law", "Justice: What's the Right Thing to Do?", "A Civil Action", "The Hollow Hope", "Model Penal Code", "Uniform Commercial Code", "The Magna Carta", "Letter from a Birmingham Jail"];
var EDITIONS=["First Edition", "Revised Edition", "Second Edition", "Third Edition", "Annotated Edition", "Illustrated Edition", "Updated Edition", "Centenary Edition", "Deluxe Edition", "Classroom Edition", "Scholar's Edition", "Abridged Edition"];
var OUTLINES=[["judicial review and its limits", "separation of powers", "federalism and the states", "the Bill of Rights", "equal protection", "substantive due process"], ["elements of criminal liability", "defenses and justification", "the law of homicide", "search, seizure, and privacy", "the right to counsel", "sentencing and punishment"], ["offer, acceptance, and consideration", "interpretation of contract terms", "breach and remedies", "third-party beneficiaries", "the parol evidence rule", "the Uniform Commercial Code"], ["negligence and the duty of care", "strict liability", "products liability", "defamation and dignitary harms", "damages and compensation", "comparative fault"], ["estates in land", "landlord and tenant", "easements and covenants", "adverse possession", "takings and eminent domain", "intellectual property foundations"], ["sources of international law", "treaties and custom", "international courts", "human rights law", "the law of armed conflict", "international trade law"], ["legal positivism", "natural law theory", "legal realism", "critical legal studies", "law and economics", "the nature of adjudication"], ["pleading and motion practice", "discovery", "summary judgment", "trial procedure", "appeals", "class actions"]];
var FRAMES=["reshaped how courts reason about individual rights", "supplied the vocabulary every later advocate had to use", "turned abstract principle into enforceable doctrine", "became the starting point of the modern curriculum", "forced the profession to rethink its first principles", "remains the authority cited when the stakes are highest"];
var T2_TOPICS=["constitutional interpretation", "criminal sentencing reform", "contract automation", "tort liability for AI systems", "digital property rights", "international climate law", "privacy jurisprudence", "restorative justice", "legal aid access", "corporate accountability", "digital evidence", "judicial ethics"];
var T2_ANGLES=["doctrinal evolution", "comparative analysis", "empirical impact study", "legislative forecasting", "case-law synthesis", "policy design", "historical trajectory", "enforcement modeling"];
var T2_METHODS=["corpus analysis of published opinions", "multi-jurisdiction survey", "longitudinal case tracking", "doctrinal meta-review", "stakeholder Delphi study", "computational legal analysis"];
var T2_OUTCOMES=["a unified test courts can apply consistently", "model statutory language for legislators", "a new balancing framework for hard cases", "clearer compliance guidance for practitioners", "a restatement-style synthesis of the doctrine", "benchmarks for measuring reform"];
var PROJ_BY="JAH Law Projection Unit";
function idOk(id){return new RegExp('^JAH-'+BASE+'-published-P-\\d{7}$').test(id||'');}
function sigOk(s){return new RegExp('^\\.\\./'+STUDYSLUG+'/index\\.html\\?sig=JAH-'+BASE+'-STUDY-S-\\d{6}$').test(s||'');}
function sigLink(addr){var n=1+((addr*13)%5000);return '../'+STUDYSLUG+'/index.html?sig=JAH-'+BASE+'-STUDY-S-'+String(n).padStart(6,'0');}
function buildL1(addr,rnd,catOv){
  var w=pick(rnd,L1);
  var cat=(catOv!==undefined)?catOv:CATS[w[4]];
  var ed=pick(rnd,EDITIONS),ol=pick(rnd,OUTLINES[w[4]]),frame=pick(rnd,FRAMES);
  var id=PREFIX+pad7(addr),auth=w[1].join(', ');
  var fc='This is the full published record for \u201c'+w[0]+'\u201d by '+auth+' ('+fmtYear(w[3])+'), published in '+w[2]+'. '+w[5]
   +' This archival entry preserves the '+ed+' of the work. Its contents are organized around: '+ol+'.'
   +' Its lasting contribution: '+frame+'.'
   +' Archival note: record '+id+' is preserved in the JAH '+FIELD+' Published Archive Database as a Level 1 real published work. Data may be augmented by the archive but never reduced below the original published file.';
  return {id:id,title:w[0],authors:w[1].slice(),publication:w[2],year:w[3],category:cat,full_content:fc,
   source_ref:'Published work catalog: '+w[2]+', '+fmtYear(w[3])+'. Verifiable via WorldCat, the Library of Congress catalog, and publisher records.',
   signature_link:sigLink(addr),level:1};
}
function buildL2(addr,rnd,catOv){
  var topic=pick(rnd,T2_TOPICS),angle=pick(rnd,T2_ANGLES),method=pick(rnd,T2_METHODS),out=pick(rnd,T2_OUTCOMES);
  var cat=(catOv!==undefined)?catOv:pick(rnd,CATS);
  var yr=ri(rnd,2027,2045);
  var bAddr=((addr*7)%500)*10;if(bAddr<10)bAddr=10;
  var b1=buildL1(bAddr,prng(bAddr*31+7)),baseId=PREFIX+pad7(bAddr),id=PREFIX+pad7(addr);
  var title='Level 2 \u2014 Projected '+angle+' in '+topic+': '+method+' outlook to '+yr;
  var fc='Level 2 projection record for the JAH '+FIELD+' Published Archive Database. Projected research direction: '+angle+' in '+topic+'.'
   +' Projected methodology: '+method+', carried through to '+yr+'. Expected findings: '+out+'.'
   +' This projection extends the Level 1 published record \u201c'+b1.title+'\u201d ('+baseId+') into the '+yr+' horizon. It is a model-derived projection of where the field is heading, not a record of an already-published work.'
   +' Archival note: record '+id+' is a Level 2 projection. Projections regenerate deterministically from seed '+addr+' via generator '+GENVER+'.';
  return {id:id,title:title,authors:[PROJ_BY],publication:'JAH Published Archive \u2014 Projection Series',year:yr,category:cat,full_content:fc,
   source_ref:'JAH Archive projection model v1.0 \u2014 projected from Level 1 record '+baseId+'. Reproducible via generator '+GENVER+' seed '+addr+'.',
   signature_link:sigLink(addr),level:2};
}
function generate(seed,opts,rnd){
  seed=(seed>>>0)||1;opts=opts||{};rnd=rnd||prng(seed);
  var addr=((seed-1)%1000000)+1;
  var cat=(opts.category&&CATS.indexOf(opts.category)>=0)?opts.category:undefined;
  return (addr%10===0)?buildL1(addr,rnd,cat):buildL2(addr,rnd,cat);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!idOk(r.id))e.push('id');
  if(typeof r.title!=='string'||r.title.length<1||r.title.length>220)e.push('title');
  if(!Array.isArray(r.authors)||!r.authors.length)e.push('authors');
  else r.authors.forEach(function(a){if(typeof a!=='string'||!a.length)e.push('author');});
  if(typeof r.publication!=='string'||!r.publication.length||r.publication.length>160)e.push('publication');
  if(!Number.isInteger(r.year)||r.year<-1000||r.year>2045)e.push('year');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.full_content!=='string'||r.full_content.length<400||r.full_content.length>4000)e.push('full_content');
  if(typeof r.source_ref!=='string'||r.source_ref.length<20)e.push('source_ref');
  if(!sigOk(r.signature_link))e.push('signature_link');
  if(r.level!==1&&r.level!==2)e.push('level');
  if(r.level===2&&r.title.indexOf('Level 2')!==0)e.push('l2prefix');
  if(r.level===1&&r.title.indexOf('Level 2')===0)e.push('l1prefix');
  var keys=Object.keys(r).sort().join('|');
  if(keys!=='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year')e.push('keys');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];(sample||[]).forEach(function(s){
   if(s&&s.id===rec.id)e.push('duplicate id in archive sample');
   if(s&&s.full_content===rec.full_content)e.push('duplicate content in archive sample');});
  return {ok:!e.length,errors:e};
}
var CHECKS=[
 {n:"id_format",f:function(r,x){try{return !!(idOk(r.id));}catch(e){return false;}}},
 {n:"id_matches_seed",f:function(r,x){try{return !!(r.id===PREFIX+pad7(x.seed));}catch(e){return false;}}},
 {n:"level_value",f:function(r,x){try{return !!(r.level===1||r.level===2);}catch(e){return false;}}},
 {n:"l2_title_starts_level2",f:function(r,x){try{return !!(r.level!==2||r.title.indexOf('Level 2')===0);}catch(e){return false;}}},
 {n:"l1_title_no_level2",f:function(r,x){try{return !!(r.level!==1||r.title.indexOf('Level 2')!==0);}catch(e){return false;}}},
 {n:"title_length",f:function(r,x){try{return !!(typeof r.title==='string'&&r.title.length>=1&&r.title.length<=220);}catch(e){return false;}}},
 {n:"authors_array",f:function(r,x){try{return !!(Array.isArray(r.authors)&&r.authors.length>=1);}catch(e){return false;}}},
 {n:"authors_strings",f:function(r,x){try{return !!(r.authors.every(function(a){return typeof a==='string'&&a.length>0;}));}catch(e){return false;}}},
 {n:"publication_length",f:function(r,x){try{return !!(typeof r.publication==='string'&&r.publication.length>=1&&r.publication.length<=160);}catch(e){return false;}}},
 {n:"year_integer_range",f:function(r,x){try{return !!(Number.isInteger(r.year)&&r.year>=-1000&&r.year<=2045);}catch(e){return false;}}},
 {n:"content_min_length",f:function(r,x){try{return !!(typeof r.full_content==='string'&&r.full_content.length>=400);}catch(e){return false;}}},
 {n:"content_max_length",f:function(r,x){try{return !!(r.full_content.length<=4000);}catch(e){return false;}}},
 {n:"content_sentences",f:function(r,x){try{return !!((r.full_content.match(/\.\s/g)||[]).length>=3);}catch(e){return false;}}},
 {n:"content_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.full_content));}catch(e){return false;}}},
 {n:"title_no_html",f:function(r,x){try{return !!(!/<[a-zA-Z][^>]*>/.test(r.title));}catch(e){return false;}}},
 {n:"source_ref_length",f:function(r,x){try{return !!(typeof r.source_ref==='string'&&r.source_ref.length>=20);}catch(e){return false;}}},
 {n:"sig_link_format",f:function(r,x){try{return !!(sigOk(r.signature_link));}catch(e){return false;}}},
 {n:"sig_link_range",f:function(r,x){try{return !!((function(){var m=/S-(\d{6})$/.exec(r.signature_link);var n=m?+m[1]:0;return n>=1&&n<=5000;})());}catch(e){return false;}}},
 {n:"category_valid",f:function(r,x){try{return !!(CATS.indexOf(r.category)>=0);}catch(e){return false;}}},
 {n:"category_option_honored",f:function(r,x){try{return !!(generate(x.seed,{category:CATS[2]}).category===CATS[2]);}catch(e){return false;}}},
 {n:"deterministic",f:function(r,x){try{return !!(JSON.stringify(generate(x.seed,{}))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"l2_contains_projection",f:function(r,x){try{return !!(r.level!==2||/projection/i.test(r.full_content));}catch(e){return false;}}},
 {n:"l1_contains_level1_marker",f:function(r,x){try{return !!(r.level!==1||/Level 1/.test(r.full_content));}catch(e){return false;}}},
 {n:"no_data_base_two_words",f:function(r,x){try{return !!(!/database/i.test(r.title+' '+r.full_content));}catch(e){return false;}}},
 {n:"no_original_website_refs",f:function(r,x){try{return !!(!/(JAH Wiki|Signature Math|cyber-patent|spec catalog|mega-mall|AI Olympics|Signature Llama|Wikileaks)/i.test(JSON.stringify(r)));}catch(e){return false;}}},
 {n:"l1_title_in_corpus",f:function(r,x){try{return !!(r.level!==1||L1_TITLES.indexOf(r.title)>=0);}catch(e){return false;}}},
 {n:"word_length_sane",f:function(r,x){try{return !!((r.title+' '+r.full_content).split(/\s+/).every(function(w){return w.length<=60;}));}catch(e){return false;}}},
 {n:"exact_keys",f:function(r,x){try{return !!(Object.keys(r).sort().join('|')==='authors|category|full_content|id|level|publication|signature_link|source_ref|title|year');}catch(e){return false;}}},
 {n:"json_roundtrip",f:function(r,x){try{return !!(JSON.stringify(JSON.parse(JSON.stringify(r)))===JSON.stringify(r));}catch(e){return false;}}},
 {n:"content_substantive",f:function(r,x){try{return !!(r.full_content.length>r.title.length+200);}catch(e){return false;}}},
 {n:"validate_ok",f:function(r,x){try{return !!(validate(r).ok);}catch(e){return false;}}},
 {n:"drift_ok_empty",f:function(r,x){try{return !!(driftCheck(r,[]).ok);}catch(e){return false;}}},
 {n:"addr_space_top",f:function(r,x){try{return !!(generate(1000000,{}).id===PREFIX+'1000000');}catch(e){return false;}}},
 {n:"seed_one_id",f:function(r,x){try{return !!(generate(1,{}).id===PREFIX+'0000001');}catch(e){return false;}}},
 {n:"l2_year_future",f:function(r,x){try{return !!(r.level!==2||(r.year>=2027&&r.year<=2045));}catch(e){return false;}}},
 {n:"l1_year_past",f:function(r,x){try{return !!(r.level!==1||(r.year>=-1000&&r.year<=2026));}catch(e){return false;}}},
 {n:"l2_source_ref_model",f:function(r,x){try{return !!(r.level!==2||/projection model/.test(r.source_ref));}catch(e){return false;}}},
 {n:"l1_source_ref_catalog",f:function(r,x){try{return !!(r.level!==1||/WorldCat/.test(r.source_ref));}catch(e){return false;}}},
 {n:"content_mentions_id",f:function(r,x){try{return !!(r.full_content.indexOf(r.id)>=0);}catch(e){return false;}}},
 {n:"l2_publication_series",f:function(r,x){try{return !!(r.level!==2||/Projection Series/.test(r.publication));}catch(e){return false;}}},
];
function selfTest(){
  var fails=[],total=0,passed=0,ids={},levels={1:0,2:0};
  for(var seed=1;seed<=40;seed++){
    var r=generate(seed,{});
    levels[r.level]++;
    if(ids[r.id])fails.push('suite duplicate id '+r.id);ids[r.id]=1;
    for(var i=0;i<CHECKS.length;i++){total++;
      var ok=false;try{ok=CHECKS[i].f(r,{seed:seed});}catch(e){ok=false;}
      if(ok)passed++;else fails.push('seed '+seed+' ['+CHECKS[i].n+']');}
  }
  if(levels[1]===0)fails.push('suite: no level-1 records in 40 seeds');
  if(levels[2]===0)fails.push('suite: no level-2 records in 40 seeds');
  return {seeds:40,checksPerSeed:CHECKS.length,total:total,passed:passed,
    failed:total-passed+((levels[1]===0||levels[2]===0)?1:0),
    suite:{uniqueIds:Object.keys(ids).length===40,levels:levels},
    failures:fails.slice(0,25),ok:fails.length===0};
}
var api={version:GENVER,generate:generate,validate:validate,driftCheck:driftCheck,selfTest:selfTest};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator(SLUG,api);
if(typeof module!=='undefined'&&module.exports)module.exports=api;
})();
