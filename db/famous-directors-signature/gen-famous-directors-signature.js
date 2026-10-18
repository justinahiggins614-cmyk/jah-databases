(function(){'use strict';
/* Signature Famous Directors Database generator — jahdb-famous-directors-signature-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"signature-generated" = Signature-authored original (clearly labeled) */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-DIRE-S-";
var GENNAME="jahdb-famous-directors-signature-generator-1.0";
var SUBJECT="famous directors";
var KIND="Signature famous directors study";
var ISSIG=true;
var TOPICS=[["Alfred Hitchcock: The Master of Suspense", "Silent and Golden Age", "1920s-1970s", "Alfred Hitchcock", "Hitchcock directed 53 features, from silent thrillers to Psycho, perfecting suspense as a science.", "His cameos, his TV show, and his showmanship made him the first director as celebrity.", "The auteur critics' canonization of him changed film history's verdicts."], ["Stanley Kubrick: The Perfectionist", "Modern Masters", "1950s-1999", "Stanley Kubrick", "Kubrick's thirteen features, from Paths of Glory to Eyes Wide Shut, each reinvented a genre.", "His legendary perfectionism, dozens of takes, total control, produced images of uncanny precision.", "2001: A Space Odyssey remains the most influential film ever made."], ["Steven Spielberg: The Blockbuster Humanist", "Modern Masters", "1970s-present", "Steven Spielberg", "Spielberg invented the modern blockbuster and then spent decades proving blockbusters could have souls.", "Schindler's List and Saving Private Ryan won him Best Director Oscars.", "No director has shaped popular cinema more."], ["Martin Scorsese: Cinema's Scholar", "Modern Masters", "1970s-present", "Martin Scorsese", "Scorsese's Catholic guilt, rock-and-roll cutting, and De Niro/DiCaprio partnerships defined serious American film.", "His Film Foundation has preserved hundreds of classics.", "He remains, at 80-plus, the most vital American director."], ["Akira Kurosawa: The Emperor", "Silent and Golden Age", "1940s-1990s", "Akira Kurosawa", "Kurosawa's samurai epics and moral dramas made him world cinema's most imitated director.", "Seven Samurai's action template underlies half of Hollywood.", "His late color films, Kagemusha and Ran, are among cinema's most beautiful."], ["Federico Fellini: The Dreamer", "New Waves", "1950s-1990s", "Federico Fellini", "Fellini turned his dreams, memories, and Rome into cinema's great carnival: La Dolce Vita, 8 1/2, Amarcord.", "\"Felliniesque\" entered the language for the extravagantly surreal.", "He won four foreign-language Oscars, still the record."], ["Ingmar Bergman: The Philosopher", "New Waves", "1950s-1980s", "Ingmar Bergman", "Bergman's chamber dramas faced God, death, and silence with a theater director's rigor.", "The Seventh Seal's chess game with Death is art cinema's signature image.", "His Faro island films are the most sustained self-examination in cinema."], ["Orson Welles: The Boy Wonder", "Silent and Golden Age", "1940s-1980s", "Orson Welles", "Welles made Citizen Kane at 25 with total freedom, then spent forty years fighting for final cut.", "His baroque visuals and radio-trained sound design influenced everyone.", "The Magnificent Ambersons' mutilation is Hollywood's great what-if."], ["Charlie Chaplin: The Tramp Behind the Camera", "Silent and Golden Age", "1910s-1960s", "Charlie Chaplin", "Chaplin wrote, directed, starred in, and scored his features, the most complete filmmaker ever.", "City Lights and Modern Times are silent and sound masterpieces alike.", "Exiled from America in 1952, he remains cinema's first global icon."], ["Billy Wilder: The Cynic with a Heart", "Silent and Golden Age", "1940s-1970s", "Billy Wilder", "Wilder's range, Double Indemnity to Some Like It Hot, is unmatched in Hollywood history.", "His screenplays are the most quotable ever written.", "He trusted audiences to be as smart as he was."], ["John Ford: The Poet of the West", "Silent and Golden Age", "1920s-1960s", "John Ford", "Ford's four Best Director Oscars remain the record.", "His Monument Valley westerns defined America's self-image.", "The Searchers' darkness revealed the melancholy under the myth."], ["Howard Hawks: The Professional", "Silent and Golden Age", "1930s-1960s", "Howard Hawks", "Hawks mastered every genre with the same credo: professionals doing their jobs, well.", "His overlapping dialogue invented a new speed for screen talk.", "The auteurists' favorite craftsman became the critics' favorite artist."], ["Frank Capra: The Common Man's Champion", "Silent and Golden Age", "1930s-1940s", "Frank Capra", "Capra's populist fables made decency dramatic.", "He won three Best Director Oscars in five years.", "It's a Wonderful Life's afterlife proved his faith in audiences."], ["F.W. Murnau: The Silent Visionary", "Silent and Golden Age", "1920s", "F.W. Murnau", "Murnau's Nosferatu and Sunrise are silent cinema's twin peaks.", "His moving camera freed film from the tripod.", "His death at 42 cut short cinema's most promising career."], ["Fritz Lang: The Architect of Destiny", "Silent and Golden Age", "1920s-1950s", "Fritz Lang", "Lang's Metropolis and M invented screen modernity; his American noirs perfected fatalism.", "His Mabuse films spanned four decades of paranoia.", "No director better filmed systems crushing individuals."], ["Sergei Eisenstein: The Montage Theorist", "Silent and Golden Age", "1920s-1940s", "Sergei Eisenstein", "Eisenstein's montage theory made editing cinema's essence.", "Potemkin's Odessa Steps is the most analyzed sequence ever cut.", "His writings remain film theory's foundation."], ["Jean Renoir: The Humanist", "Silent and Golden Age", "1930s", "Jean Renoir", "Renoir's Rules of the Game and Grand Illusion found humanity in every character, even the villains.", "\"Everyone has their reasons\" is cinema's most generous line.", "The New Wave worshipped him as the father of modern film."], ["Vittorio De Sica: The Neorealist", "New Waves", "1940s-1950s", "Vittorio De Sica", "De Sica's Bicycle Thieves, shot with non-actors on real streets, defined neorealism.", "His collaborations with Zavattini made poverty visible without pity.", "Umberto D. is neorealism's quietest masterpiece."], ["Michelangelo Antonioni: The Modernist", "New Waves", "1960s", "Michelangelo Antonioni", "Antonioni's trilogy of alienation, L'Avventura, La Notte, L'Eclisse, made boredom profound.", "Blow-Up brought his modernism to swinging London.", "His empty landscapes externalized interior states."], ["Andrei Tarkovsky: The Mystic", "New Waves", "1960s-1980s", "Andrei Tarkovsky", "Tarkovsky's long takes sculpted time itself: Andrei Rublev, Solaris, Stalker.", "His Sculpting in Time remains filmmakers' spiritual manual.", "Exiled from the USSR, he died in Paris at 54."], ["David Lean: The Epic Craftsman", "Silent and Golden Age", "1940s-1980s", "David Lean", "Lean's Brief Encounter is intimate perfection; his Lawrence of Arabia and Doctor Zhivago defined the epic.", "His cutting, learned as an editor, was invisible and perfect.", "The epic's decline sidelined him; his reputation only grows."], ["Michael Powell: The Maverick", "Silent and Golden Age", "1940s-1950s", "Michael Powell", "Powell and Pressburger's Archers films, The Red Shoes, A Matter of Life and Death, were Britain's most imaginative.", "Peeping Tom (1960) destroyed his career and is now a horror landmark.", "Scorsese's advocacy restored him to the canon."], ["Francis Ford Coppola: The Ambitious Auteur", "New Waves", "1970s", "Francis Ford Coppola", "Coppola's 1970s, the Godfathers, The Conversation, Apocalypse Now, is the greatest decade any American director has had.", "His gambles built and nearly destroyed Zoetrope.", "No career better shows the New Hollywood arc."], ["Jean-Luc Godard: The Revolutionary", "New Waves", "1960s-present", "Jean-Luc Godard", "Godard reinvented cinema's language yearly through the 1960s.", "After 1968 he made political and video-essay work of uncompromising difficulty.", "He remained cinema's conscience and provocateur to the end."], ["Francois Truffaut: The Romantic", "New Waves", "1959-1984", "Francois Truffaut", "Truffaut's humanism balanced the New Wave's radicalism.", "The Antoine Doinel cycle is cinema's great longitudinal portrait.", "His love of cinema itself, Day for Night, was his truest subject."], ["Yasujiro Ozu: The Quiet Master", "Silent and Golden Age", "1930s-1960s", "Yasujiro Ozu", "Ozu's tatami-mat camera and family stories created cinema's most distinctive style.", "Tokyo Story is regularly voted among the greatest films ever.", "His influence on slow cinema is foundational."], ["Satyajit Ray: Bengal's Humanist", "New Waves", "1950s-1990s", "Satyajit Ray", "Ray's Apu Trilogy brought Indian cinema to the world stage.", "His humanism, music, and economy influenced generations.", "He received an honorary Oscar in 1992."], ["Werner Herzog: The Mad Adventurer", "New Waves", "1970s-present", "Werner Herzog", "Herzog's ecstatic truth took him to jungles, volcanoes, and penguins.", "Fitzcarraldo's ship over the mountain is cinema's maddest shoot.", "His documentaries reinvented nonfiction as fever dream."], ["David Lynch: The Dream Detective", "Modern Masters", "1970s-present", "David Lynch", "Lynch's Eraserhead, Blue Velvet, and Mulholland Drive made the uncanny mainstream.", "Twin Peaks reinvented television.", "\"Lynchian\" describes the everyday revealing its nightmare."], ["Quentin Tarantino: The Video-Store Auteur", "Modern Masters", "1990s-present", "Quentin Tarantino", "Tarantino's Reservoir Dogs and Pulp Fiction detonated 1990s cinema.", "His encyclopedic genre knowledge became a filmmaking method.", "He plans to retire at ten films, directing scarcity as art."], ["Christopher Nolan: The Blockbuster Formalist", "Modern Masters", "2000s-present", "Christopher Nolan", "Nolan brought art-film structure to blockbusters: Memento, Inception, Dunkirk, Oppenheimer.", "His IMAX 70mm evangelism kept film alive.", "Oppenheimer's Best Picture win crowned the formalist blockbuster."], ["The Coen Brothers: America's Eccentrics", "Modern Masters", "1980s-present", "Joel and Ethan Coen", "The Coens' genre pastiches, Fargo, The Big Lebowski, No Country, hide philosophical depths.", "Their dialogue is the most imitated in modern American film.", "They make studio films with indie souls."], ["Wes Anderson: The Miniaturist", "Modern Masters", "1990s-present", "Wes Anderson", "Anderson's symmetrical dioramas, Rushmore to Asteroid City, created an instantly recognizable world.", "His fussiness divides critics and delights fans.", "He proved a personal style could be a commercial brand."], ["Bong Joon-ho: The Genre Blender", "Modern Masters", "2000s-present", "Bong Joon-ho", "Bong's Memories of Murder, The Host, and Snowpiercer blended genres with political bite.", "Parasite won Best Picture, the first non-English film to do so.", "His class rage is cinema's most entertaining."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator("famous-directors-signature",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
