(function(){'use strict';
/* Signature Sitcoms History Database generator — jahdb-sitcoms-history-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature-generated" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-SITC-S-";
var GENNAME="jahdb-sitcoms-history-signature-generator-1.0";
var SUBJECT="sitcoms history";
var KIND="Signature sitcoms history study";
var ISSIG=true;
var TOPICS=[["What Is a Sitcom", "Foundations", "1940s-present", "the situation comedy", "The sitcom is television's signature form: recurring characters in a fixed situation, problems resolved in 22 minutes.", "Its rhythms come from radio comedy, vaudeville, and the theater of embarrassment.", "No form has shaped domestic life's image more."], ["I Love Lucy (1951): The Template", "Foundations", "1951-1957", "Lucille Ball and Desi Arnaz", "I Love Lucy invented the sitcom: the multi-camera setup, the live studio audience, the rerun.", "Desi Arnaz's Desilu pioneered filming before audiences and owning the reruns.", "Lucy's chocolate-factory conveyor belt is TV comedy's founding image."], ["The Honeymooners (1955)", "Foundations", "1955-1956", "Jackie Gleason", "The Honeymooners' 39 episodes created the blue-collar sitcom: Ralph Kramden's schemes, Alice's patience.", "Its live intensity came from Gleason's refusal to rehearse.", "Every working-class sitcom descends from it."], ["The Dick Van Dyke Show (1961)", "Foundations", "1961-1966", "Carl Reiner", "Carl Reiner's showbiz sitcom brought sophistication: a comedy writer's work life and home life.", "Mary Tyler Moore's Laura Petrie redefined the TV wife.", "Its writing, by Reiner's room, set the quality bar."], ["The Andy Griffith Show (1960)", "Foundations", "1960-1968", "Andy Griffith", "Mayberry's gentle sheriff and his deputy Barney Fife offered an idealized small town.", "Don Knotts's Barney won five Emmys.", "The show's nostalgia became American mythology."], ["Bewitched (1964) and the Fantasy Sitcom", "Foundations", "1964-1972", "the magic comedies", "Bewitched's suburban witch made fantasy domestic and hilarious.", "I Dream of Jeannie and the genre's magic were really about 1960s gender roles.", "The fantasy sitcom let TV literalize its metaphors."], ["The Mary Tyler Moore Show (1970)", "Foundations", "1970-1977", "Mary Tyler Moore", "MTM's Minneapolis newsroom made the single working woman TV's heroine.", "\"You've got spunk\" and the hat toss are feminist TV's founding moments.", "Its writers' room launched a generation of showrunners."], ["All in the Family (1971): The Sitcom Grows Teeth", "Foundations", "1971-1979", "Norman Lear", "Lear's Archie Bunker brought bigotry, politics, and social issues into the living room.", "The show was number one for five straight years.", "Its spin-offs, Maude, The Jeffersons, built an empire."], ["The Multi-Camera Format and the Laugh Track", "Foundations", "1950s-present", "the studio audience", "Multi-camera sitcoms film like plays before live audiences, with laugh tracks sweetening the response.", "The format's theatricality suits joke-driven comedy.", "Single-camera's rise never killed it: the laugh track endures."], ["The Writers' Room", "Foundations", "1950s-present", "the comedy collective", "The writers' room, jokes pitched around a table, is sitcom's engine.", "Your Show of Shows' room invented the form; every room since imitates it.", "The showrunner, writer-as-boss, emerged from the room."], ["Syndication: The Afterlife of Sitcoms", "Foundations", "1960s-present", "the rerun economy", "Syndication made sitcoms immortal: 100 episodes meant eternal reruns and eternal profits.", "The syndication threshold shaped how many episodes shows made.", "Streaming is syndication's heir and executioner."], ["Cheers (1982)", "Classics", "1982-1993", "the Charles brothers", "Cheers' Boston bar where everybody knows your name perfected the hangout sitcom.", "Its Sam-and-Diane will-they-won't-they set the romance template.", "The show's finale was a national event."], ["The Cosby Show (1984)", "Classics", "1984-1992", "Bill Cosby", "The Cosby Show's affluent Black Huxtables redefined representation and dominated ratings.", "Its legacy is now inseparable from Cosby's crimes.", "The show's cultural impact and its star's fall are both historic."], ["Seinfeld (1989): The Show About Nothing", "Classics", "1989-1998", "Jerry Seinfeld and Larry David", "Seinfeld's comedy of manners for sociopaths made selfishness hilarious.", "Its \"no hugging, no learning\" rule broke sitcom sentimentality.", "The finale's divisiveness proved how much the show mattered."], ["Friends (1994)", "Classics", "1994-2004", "David Crane and Jeffrey Klarik", "Friends' six twenty-somethings in impossible apartments defined 1990s youth culture.", "Its Central Perk hangout and Rachel haircut were global phenomena.", "The reunion proved its afterlife is eternal."], ["Frasier (1993)", "Classics", "1993-2004", "the Cheers spin-off", "Frasier proved spin-offs could surpass originals: eleven seasons, 37 Emmys.", "Its farce episodes are the genre's most perfectly constructed.", "Kelsey Grammer played Frasier Crane for twenty years."], ["Everybody Loves Raymond (1996)", "Classics", "1996-2004", "Ray Romano", "Raymond's Long Island family squabbles made the in-law sitcom universal.", "Doris Roberts and Peter Boyle stole every scene.", "Its warmth hid impeccable joke construction."], ["The Simpsons (1989): The Animated Sitcom", "Classics", "1989-present", "Matt Groening", "The Simpsons made the animated sitcom TV's sharpest satire and its longest-running scripted show.", "Its golden-age seasons are the most quotable in television.", "The show predicted the future so often it became a meme."], ["The Office (UK 2001 / US 2005): Cringe Comedy", "Classics", "2001-2013", "Ricky Gervais and Greg Daniels", "The UK Office's David Brent made embarrassment the joke; the US version made it warm.", "Steve Carell's Michael Scott is cringe comedy's American apotheosis.", "The mockumentary format freed the sitcom from the stage."], ["30 Rock (2006)", "Classics", "2006-2013", "Tina Fey", "Tina Fey's showbiz satire packed more jokes per minute than any sitcom before.", "Alec Baldwin's Jack Donaghy is the great comic creation of the 2000s.", "Its live episodes proved the form's theatrical roots."], ["Parks and Recreation (2009)", "Classics", "2009-2015", "Greg Daniels and Michael Schur", "Parks and Rec's Leslie Knope made optimism funny, the decade's hardest trick.", "Its mockumentary warmth influenced every hangout comedy after.", "\"Treat yo self\" entered the language."], ["Modern Family (2009): The Mockumentary Sitcom", "Classics", "2009-2020", "Christopher Lloyd and Steven Levitan", "Modern Family's talking-head family comedy won five straight Best Comedy Emmys.", "Its three-family structure updated the family sitcom for modern America.", "The show's success prolonged the mockumentary's reign."], ["The Big Bang Theory (2007)", "Classics", "2007-2019", "Chuck Lorre", "Big Bang's nerds made geek culture mainstream and multi-camera viable again.", "Its twelve seasons made it the longest multi-camera sitcom ever.", "The show's laugh track divided critics and delighted millions."], ["Brooklyn Nine-Nine (2013): The Workplace Comedy Evolves", "The Modern Sitcom", "2013-2021", "Dan Goor and Michael Schur", "Brooklyn Nine-Nine's precinct made the workplace comedy warm, diverse, and joke-dense.", "Its cancellation and fan-led revival proved fandom's power.", "The show navigated policing's politics with unusual grace."], ["British Sitcoms: A Parallel Tradition", "The Modern Sitcom", "1960s-present", "the UK tradition", "British sitcoms run shorter, darker, and more class-conscious than American ones.", "Fawlty Towers' twelve perfect episodes are the tradition's peak.", "The Office's export proved the traditions could merge."], ["Single-Camera vs. Multi-Camera", "The Modern Sitcom", "2000s-present", "the format war", "Single-camera's filmic freedom challenged multi-camera's theatrical punch.", "The 2000s belonged to single-camera; the 2010s saw multi-camera's streaming revival.", "The format shapes the joke: setups differ, payoffs differ."], ["The Showrunner Era", "The Modern Sitcom", "2000s-present", "the writer-boss", "The showrunner, exemplified by Tina Fey, Michael Schur, and Dan Harmon, became TV's auteur.", "Streaming gave showrunners film-like control.", "The era's best comedies are unmistakably personal."], ["Streaming Sitcoms", "The Modern Sitcom", "2013-present", "Netflix and beyond", "Streaming freed sitcoms from 22-minute, 22-episode constraints.", "Master of None, Fleabag, and Hacks made the sitcom prestige.", "The binge changed the joke's rhythm."], ["Comfort TV: Why We Rewatch", "The Modern Sitcom", "ongoing", "the rewatch phenomenon", "Sitcoms are the most rewatched television: familiarity as therapy.", "Streaming data shows comfort viewing dominates.", "The laugh track's warmth is the point."], ["The Great Series Finales", "The Modern Sitcom", "ongoing", "saying goodbye", "Finales from Cheers to The Office are cultural events.", "Sticking the landing, or failing to, defines a show's legacy.", "The finale is the sitcom's final joke."], ["Animated Sitcoms Beyond The Simpsons", "The Modern Sitcom", "1990s-present", "the animation boom", "King of the Hill, Bob's Burgers, and Rick and Morty expanded the animated sitcom's range.", "Animation frees sitcoms from physical limits.", "The form's future is increasingly drawn."], ["The Family Sitcom Through the Decades", "The Modern Sitcom", "1950s-present", "the evolving family", "The family sitcom tracked America's families: Leave It to Beaver to Modern Family to Black-ish.", "Each decade's family reveals its anxieties.", "The form endures because families endure."], ["Workplace Comedies", "The Modern Sitcom", "1970s-present", "the office as family", "From MTM to The Office to Abbott Elementary, work is TV's second family.", "The workplace lets strangers become intimates.", "Abbott Elementary's mockumentary revival proves the form's health."], ["The Sitcom Today", "The Modern Sitcom", "present", "the form's future", "Today's sitcoms span network multi-camera, streaming single-camera, and animated experiments.", "The form's 75-year run shows no sign of ending.", "As long as people live together, the situation will be comedy."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator("sitcoms-history-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
