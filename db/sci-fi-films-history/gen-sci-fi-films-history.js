(function(){'use strict';
/* The Sci-Fi Films History Database generator — jahdb-sci-fi-films-history-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-SCIF-";
var GENNAME="jahdb-sci-fi-films-history-generator-1.0";
var SUBJECT="sci-fi films history";
var KIND="sci-fi film history record";
var ISSIG=false;
var TOPICS=[["What Is Science Fiction Film", "Foundations", "1902-present", "the literature of ideas on screen", "Science fiction film extrapolates science and society into imagined futures, alternate presents, and distant worlds.", "Its great subjects are technology's promise and peril, and humanity's place in the cosmos.", "The genre has produced both the biggest blockbusters and the most cerebral art films."], ["A Trip to the Moon (1902): The First Sci-Fi Film", "Foundations", "1902", "Georges Melies", "Melies's lunar voyage, with its rocket in the Man in the Moon's eye, invented science fiction cinema.", "Its theatrical tricks, trapdoors, and painted backdrops, were the effects industry's birth.", "The film remains the genre's founding dream."], ["Metropolis (1927)", "Foundations", "1927", "Fritz Lang", "Lang's future city and robot Maria created science fiction's visual vocabulary.", "Its Art Deco towers and worker catacombs are quoted in every screen future since.", "The film's design outlived its simplistic politics."], ["Things to Come (1936)", "Foundations", "1936", "H.G. Wells", "Wells scripted his own future history, from world war to utopian technocracy.", "Its predictions, aerial bombing, world government, were startlingly prescient.", "The film is science fiction's first serious futurism."], ["The Day the Earth Stood Still (1951)", "Foundations", "1951", "Robert Wise", "The alien Klaatu's warning to humanity gave 1950s sci-fi its conscience.", "Bernard Herrmann's theremin score invented the sound of the uncanny.", "Its pacifist message stood apart from invasion paranoia."], ["1950s B-Movie Sci-Fi: Invasion Paranoia", "Foundations", "1950s", "the flying saucer cycle", "1950s sci-fi channeled Cold War and atomic fears into invaders, mutants, and giant insects.", "Them! (1954) and Invasion of the Body Snatchers (1956) are the cycle's peaks.", "The cheapies' imagination outran their budgets gloriously."], ["Forbidden Planet (1957)", "Foundations", "1957", "Fred Wilcox", "Forbidden Planet's Shakespeare-in-space, electronic score, and Robby the Robot set new standards.", "Its \"monsters from the id\" gave sci-fi Freudian depth.", "The film's influence runs through Star Trek and beyond."], ["Soviet Sci-Fi: Solaris (1972)", "Foundations", "1972", "Andrei Tarkovsky", "Tarkovsky's answer to 2001 was inner space: an ocean planet materializing the cosmonauts' memories.", "Its slowness was philosophical method, not flaw.", "Soviet sci-fi offered contemplation where Hollywood offered action."], ["2001: A Space Odyssey (1968)", "Foundations", "1968", "Stanley Kubrick", "Kubrick and Arthur C. Clarke's voyage from ape to star-child remains the genre's summit.", "Its effects, front projection, and model work, still convince.", "The film treats the audience as intelligent, its greatest radicalism."], ["Planet of the Apes (1968)", "Foundations", "1968", "Franklin Schaffner", "The apes' upside-down world delivered sci-fi's greatest twist ending.", "John Chambers' prosthetic makeup won an honorary Oscar.", "The franchise's 2010s reboot proved the premise's durability."], ["Star Wars (1977) and the Space Opera", "Foundations", "1977", "George Lucas", "Star Wars revived the space opera as mythic blockbuster, the genre's commercial big bang.", "Its used-future aesthetic, dented and dirty, changed production design.", "The film made science fiction Hollywood's dominant genre."], ["Alien (1979): Sci-Fi Horror", "Classics", "1979", "Ridley Scott", "Alien's haunted-house-in-space fused horror dread with sci-fi world-building.", "Giger's xenomorph is the genre's perfect organism.", "Ripley became the genre's defining hero."], ["Blade Runner (1982): Cyberpunk on Screen", "Classics", "1982", "Ridley Scott", "Blade Runner's rain-soaked Los Angeles invented cyberpunk's look: neon, noir, Asian-futurist.", "Its replicants ask what makes us human.", "Flopping on release, it became the genre's most influential film."], ["E.T. (1982): The Friendly Visitor", "Classics", "1982", "Steven Spielberg", "E.T.'s suburban alien made first contact a childhood fable.", "Its glowing finger and bicycle flight are the genre's tenderest images.", "The film held the box-office record for a decade."], ["The Terminator (1984): The Killer Robot", "Classics", "1984", "James Cameron", "Cameron's relentless time-travel chase was made for $6.4 million and launched his career.", "Schwarzenegger's T-800 is the genre's most imitated machine.", "Its sequel redefined the action blockbuster."], ["Back to the Future (1985): Time Travel Done Right", "Classics", "1985", "Robert Zemeckis", "Zemeckis's clockwork comedy made time travel's paradoxes pure fun.", "The DeLorean became pop culture's time machine.", "Its script is the most tightly constructed in Hollywood history."], ["Jurassic Park (1993): Digital Dinosaurs", "Classics", "1993", "Steven Spielberg", "Jurassic Park's CGI dinosaurs ended the practical-effects era and began the digital one.", "Its \"life finds a way\" warned about the science it celebrated.", "The film's effects pipeline became the industry's."], ["The Matrix (1999)", "Classics", "1999", "the Wachowskis", "The Matrix's simulated reality and bullet time defined turn-of-the-millennium sci-fi.", "Its red-pill/blue-pill choice entered philosophy and politics alike.", "The film's anime and cyberpunk debts were worn proudly."], ["Inception (2010): Dreams Within Dreams", "Classics", "2010", "Christopher Nolan", "Nolan's heist-in-dreams made exposition thrilling and ambiguity mainstream.", "Its folding Paris and hallway fight are the genre's recent peaks.", "The spinning top's ending is still debated."], ["District 9 (2009): Sci-Fi with Something to Say", "Classics", "2009", "Neill Blomkamp", "Blomkamp's Johannesburg aliens-as-apartheid allegory was made for $30 million.", "Its documentary style gave the fantastic urgency.", "The film proved indie sci-fi could compete."], ["Interstellar (2014): Hard Sci-Fi Returns", "Classics", "2014", "Christopher Nolan", "Nolan's relativist epic consulted physicist Kip Thorne on its black hole.", "Its father-daughter story grounded the cosmic in the intimate.", "The film made theoretical physics emotional."], ["Arrival (2016): First Contact Grown Up", "Classics", "2016", "Denis Villeneuve", "Villeneuve's linguist-first-contact story treated language as the real alien.", "Its circular-time revelation recontextualizes everything.", "The film is the genre's most humane recent masterpiece."], ["Dune (2021): The Unfilmable Filmed", "Classics", "2021", "Denis Villeneuve", "Villeneuve's Dune finally filmed Herbert's \"unfilmable\" novel through scale and patience.", "Its sandworms and stillsuits are design triumphs.", "Part Two completed the prestige blockbuster's statement."], ["Cyberpunk Cinema", "Themes and Futures", "1982-present", "high tech, low life", "Cyberpunk's neon dystopias, from Blade Runner to The Matrix, warned about corporate futures.", "The genre's hackers and replicants are now our reality's metaphors.", "Cyberpunk's warnings keep coming true."], ["Dystopian Cinema", "Themes and Futures", "ongoing", "the bad future", "Dystopias from Metropolis to The Hunger Games imagine power's worst outcomes.", "The YA dystopia wave made the subgenre teen-literate.", "Dystopia is sci-fi's cautionary mode."], ["Time-Travel Films", "Themes and Futures", "ongoing", "the paradox machine", "Time travel's paradoxes, from Primer's rigor to Looper's emotion, are the genre's logic puzzles.", "The subgenre's rules vary by film, which is half the fun.", "Every time-travel film is really about regret."], ["AI on Screen", "Themes and Futures", "1968-present", "the machine minds", "Screen AI evolved from HAL's calm murder to Her's tender romance to M3GAN's camp horror.", "Each era's AI reflects its technological anxieties.", "The films ask what we want from minds we make."], ["First-Contact Films", "Themes and Futures", "1951-present", "meeting the alien", "First contact ranges from Klaatu's warning to Arrival's linguistics to Independence Day's invasion.", "The subgenre stages humanity's self-image.", "How we imagine aliens reveals how we see ourselves."], ["Space Opera vs. Hard Sci-Fi", "Themes and Futures", "ongoing", "the genre's two poles", "Space opera offers mythic adventure; hard sci-fi offers scientific rigor.", "Star Wars and 2001 are the poles; most films fall between.", "The tension drives the genre's creativity."], ["Sci-Fi Horror Hybrids", "Themes and Futures", "1979-present", "fear in the future", "Alien proved the future is scary; Event Horizon and Life confirmed it.", "The hybrid uses sci-fi's unknown as horror's monster.", "Space's indifference is horror's perfect setting."], ["Indie Sci-Fi: Primer to Ex Machina", "Themes and Futures", "2004-present", "the low-budget idea film", "Primer's $7,000 time-travel puzzle proved ideas beat budgets.", "Ex Machina's three-hander made AI intimate.", "Indie sci-fi is the genre's R&D lab."], ["Afrofuturism on Screen", "Themes and Futures", "2018-present", "Black Panther and beyond", "Black Panther's Wakanda brought Afrofuturism to the blockbuster.", "The movement imagines Black futures outside colonial frames.", "Its influence is reshaping the genre's defaults."], ["Anime Sci-Fi: A Brief Survey", "Themes and Futures", "1988-present", "Japan's futures", "Anime sci-fi from Akira to Ghost in the Shell offered the genre's most radical visions.", "Its cyberpunk preceded and influenced Hollywood's.", "The survey here is brief; the anime-history database covers it fully."], ["The Future of Sci-Fi Film", "Themes and Futures", "present", "tomorrow's futures", "Sci-fi's future includes AI-made images, virtual production, and stories about the technologies reshaping us.", "The genre's job, imagining consequences, has never mattered more.", "The next classic is already in someone's head."]];
var ANGLES=['overview','detailed','examples','faq','history','applications'];
function pad(n){var s=String(n);while(s.length<6)s='0'+s;return s;}
function ladderOf(i){return i<11?'simple':(i<23?'compounded':'complex');}
function compose(tp,angle){
  var subj=SUBJECT, p;
  if(!ISSIG){
    p=tp[0]+" ("+tp[2]+") stands among the defining entries in "+subj+", associated above all with "+tp[3]+". "+tp[4];
    p+="\n\n"+tp[5]+" Seen in context, it shows how craft and circumstance combined to make something lasting.";
    p+="\n\n"+tp[6]+" Its influence runs through everything that followed in "+subj+".";
    p+="\n\nKey details \u2014 Era: "+tp[2]+". Key figure: "+tp[3]+". Area: "+tp[1]+". Angle: "+angle+".";
    p+="\n\nWhy it matters: "+tp[0]+" remains essential knowledge for anyone studying "+subj+".";
  } else {
    p="A Signature-original study of "+tp[0]+" ("+tp[2]+"). This entry is an original work of analysis by the Signature system, not a public record. "+tp[4];
    p+="\n\nThe Signature reading: "+tp[5]+" Read this way, "+tp[0]+" becomes a lesson in deliberate craft.";
    p+="\n\nWhat to take for your own work: "+tp[6]+" The Signature method is to isolate one working principle and carry it into original practice.";
    p+="\n\nTry it yourself: apply the strongest idea above to a new, original subject of your own invention.";
  }
  return p;
}
function makeDemo(rid,title,era,key,g){
  var prog="// Demo: "+rid+" - "+title+"\n// Run with: node demo.js\n"
    +"const record={id:"+JSON.stringify(rid)+",title:"+JSON.stringify(title)+",era:"+JSON.stringify(era)+",keyFigure:"+JSON.stringify(key)+",area:"+JSON.stringify(g)+"};\n"
    +"function showRecord(r){console.log(\"RECORD \"+r.id);console.log(\"Title: \"+r.title);console.log(\"Era: \"+r.era);console.log(\"Key figure: \"+r.keyFigure);}\n"
    +"showRecord(record);\nconsole.log(\"demo ok\");\n";
  return {language:"javascript",run:"node demo.js",program:prog};
}
function generate(seed,opts){
  var s=prng(seed), ti, tp, angle, id, title;
  opts=opts||{};
  if(opts.topic){
    var q=String(opts.topic).toLowerCase(), f=-1, i;
    for(i=0;i<TOPICS.length;i++){ if(TOPICS[i][0].toLowerCase().indexOf(q)>=0){f=i;break;} }
    ti=(f>=0)?f:((s()*TOPICS.length)|0);
  } else ti=(s()*TOPICS.length)|0;
  tp=TOPICS[ti]; angle=ANGLES[(s()*ANGLES.length)|0];
  id=PREFIX+pad(seed);
  title=(ISSIG?"Signature Study: ":"")+tp[0]+" ("+angle+")";
  var content=compose(tp,angle);
  var rec={id:id,t:title,g:tp[1],c:1,title:title,
    description:(tp[0]+" ("+tp[2]+"). "+tp[4]).slice(0,220),
    genre:tp[1],type:KIND,ladder:ladderOf(ti),era:tp[2],key_figure:tp[3],
    key_facts:[tp[4],tp[5],tp[6]],content:content,
    demo:makeDemo(id,title,tp[2],tp[3],tp[1]),
    src:ISSIG?"signature-generated":"public-harvest",_seed:seed};
  if(ISSIG)rec.signature_label="Signature-generated original \u2014 a Signature-original study by the Signature system, not a public record. Property of Justin Addam Higgins.";
  return rec;
}
function validate(r){
  var errs=[];
  if(!r.id)errs.push('missing id');
  if(!r.title)errs.push('missing title');
  if(!r.content||r.content.length<300)errs.push('content too short');
  if(!r.demo||!r.demo.program)errs.push('missing demo');
  if(ISSIG&&!/Signature/.test(r.signature_label||''))errs.push('missing signature_label');
  return {ok:errs.length===0,errors:errs};
}
function driftCheck(rec,sample){
  for(var i=0;i<sample.length;i++){if(sample[i].t===rec.title)return {ok:false,errors:['duplicate title']};}
  return {ok:true,errors:[]};
}
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator("sci-fi-films-history",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
