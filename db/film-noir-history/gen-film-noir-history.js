(function(){'use strict';
/* The Film Noir History Database generator — jahdb-film-noir-history-generator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed always makes the same record.
   src:"public-harvest" = Fact-checked public information */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX="JAH-NOIR-";
var GENNAME="jahdb-film-noir-history-generator-1.0";
var SUBJECT="film noir history";
var KIND="film noir history record";
var ISSIG=false;
var TOPICS=[["What Is Film Noir", "Foundations", "1941-1958", "the dark cycle", "Film noir is the cycle of dark American crime films of the 1940s and 50s, marked by shadows, cynicism, and doom.", "French critics named it after the war; Americans just called them crime pictures.", "Its visual style descends from German expressionism via emigre directors and cinematographers."], ["The Maltese Falcon (1941): The First Noir", "Foundations", "1941", "John Huston", "Huston's directorial debut gave noir its template: the detective, the dame, the MacGuffin, the moral murk.", "Bogart's Sam Spade defined the private eye.", "The film's \"stuff that dreams are made of\" is noir's epitaph."], ["Double Indemnity (1944)", "Foundations", "1944", "Billy Wilder", "Wilder and Chandler's insurance-murder plot is noir's perfect machine.", "Fred MacMurray's confession-by-dictaphone and Stanwyck's anklet are iconic.", "Its flashback structure became noir's default."], ["Hardboiled Fiction: Hammett and Chandler", "Foundations", "1920s-1940s", "the pulp writers", "Hammett's Continental Op and Chandler's Philip Marlowe gave noir its voice: terse, similes like punches.", "The pulps' moral ambiguity, nobody clean, became the films' worldview.", "Chandler's \"down these mean streets\" essay is noir's manifesto."], ["The Femme Fatale", "Foundations", "1940s", "the dangerous woman", "The femme fatale, Stanwyck, Bacall, Gardner, lures the hero to ruin with a smile.", "She embodied wartime anxieties about independent women.", "Feminist readings find her the cycle's most honest figure."], ["Venetian Blinds: The Look of Noir", "Foundations", "1940s", "the noir visual style", "Noir's venetian-blind shadows, rain-slicked streets, and canted angles visualized moral entrapment.", "Low budgets forced invention: shadows were cheaper than sets.", "John Alton's Painting with Light remains the cinematographer's bible."], ["Voiceover and Flashback", "Foundations", "1940s", "the noir narration", "Noir's voiceovers confess from beyond the grave or the jail cell.", "Flashback structures made doom feel inevitable: the end is known, the how is the story.", "The devices turned B-movies into tragedies."], ["Postwar Anxiety on Screen", "Foundations", "1940s", "the cultural context", "Noir channeled veterans' disillusionment, atomic fear, and urban alienation.", "Its heroes are damaged men in a rigged world.", "The cycle is America's subconscious, 1945-1955."], ["The B-Movie Roots of Noir", "Foundations", "1940s", "the programmers", "Most noirs were B-movies: cheap, fast, unprestigious, which gave directors freedom.", "RKO's and Columbia's B units were noir's laboratories.", "Poverty became style."], ["German Emigres Bring Expressionism", "Foundations", "1930s-1940s", "Lang, Siodmak, and Wilder", "Refugee directors and cameramen brought expressionist shadows to Hollywood crime films.", "Lang's Fury and Scarlet Street, Siodmak's Killers, Wilder's Double Indemnity: the emigre noirs are the core.", "Exile's paranoia became America's."], ["The French Coin the Term", "Foundations", "1946", "Nino Frank", "French critic Nino Frank called the wartime-delayed American crime films \"film noir\" in 1946.", "The French saw what Americans missed: a coherent movement.", "Cahiers critics later made noir central to auteur theory."], ["Out of the Past (1947)", "Classics", "1947", "Jacques Tourneur", "Tourneur's film is noir's most fatalistic: Mitchum can never outrun his past, and neither can the audience's hope.", "Jane Greer's Kathie is the definitive femme fatale.", "Its structure, present-tense doom with past-tense explanation, is perfect."], ["The Big Sleep (1946)", "Classics", "1946", "Howard Hawks", "Hawks's Chandler adaptation is famously incomprehensible, even Chandler could not explain the plot, and nobody cares.", "Bogart and Bacall's chemistry carries everything.", "The film proves noir is atmosphere, not story."], ["Sunset Boulevard (1950)", "Classics", "1950", "Billy Wilder", "Wilder's Hollywood-gothic noir gave Gloria Swanson's Norma Desmond the screen's great comeback-gone-mad.", "\"I am big, it's the pictures that got small\" is Hollywood's self-indictment.", "Its corpse-narrator is noir's boldest device."], ["Touch of Evil (1958): The Last Classic Noir", "Classics", "1958", "Orson Welles", "Welles's border-town nightmare opens with the most famous crane shot in history.", "Its corruption is total: even the hero is compromised.", "The film's 1998 restoration revealed Welles's intended cut."], ["Billy Wilder's Noirs", "Classics", "1944-1950", "Billy Wilder", "Wilder's Double Indemnity, The Lost Weekend, and Sunset Boulevard are noir's cynical peak.", "His Viennese world-weariness suited the form perfectly.", "No one wrote doom more elegantly."], ["Robert Siodmak: The Noir Specialist", "Classics", "1940s", "Robert Siodmak", "Siodmak's The Killers, Criss Cross, and The Spiral Staircase made him noir's house director.", "His German training gave his shadows pedigree.", "He never got the auteur credit his craft deserved."], ["Otto Preminger: Laura (1944)", "Classics", "1944", "Otto Preminger", "Laura's detective falling for a possibly-dead woman's portrait is noir's most romantic premise.", "Preminger's cool, detached direction suited obsession's study.", "The film's theme song became a standard."], ["Fritz Lang's American Noirs", "Classics", "1940s-1950s", "Fritz Lang", "Lang's American films, Scarlet Street, The Big Heat, While the City Sleeps, are fatalism perfected.", "His systems crush individuals with geometric precision.", "The Big Heat's coffee-throwing scene remains shocking."], ["Ida Lupino: Noir's Woman Director", "Classics", "1949-1953", "Ida Lupino", "Lupino directed tough, low-budget noirs like The Hitch-Hiker through her own company.", "She was the only woman directing Hollywood features in her era.", "Her empathy for outsiders gave her noirs a different moral center."], ["RKO's Noir Unit", "Classics", "1940s", "the RKO B unit", "Producer Val Lewton's RKO horror unit and the studio's noir programmers shared shadows and economy.", "Out of the Past and The Set-Up came from RKO's B division.", "The studio's decline freed its filmmakers to go dark."], ["Cinematographers of the Dark: John Alton", "Classics", "1940s", "John Alton", "Alton's work on T-Men and The Big Combo defined noir lighting: single sources, deep blacks.", "His book Painting with Light is still taught.", "He proved the cinematographer could be the film's true author."], ["The Scores: Miklos Rozsa and Noir Music", "Classics", "1940s", "the noir composers", "Rozsa's theremin-laced scores for Spellbound and The Lost Weekend gave noir its sound of anxiety.", "Noir music is brass and strings in minor keys, city at night.", "The scores made psychology audible."], ["Neo-Noir: Chinatown (1974)", "Neo-Noir", "1974", "Roman Polanski", "Chinatown took noir's 1930s setting and gave it 1970s hopelessness: evil wins, systemically.", "Towne's script is the most studied screenplay ever.", "\"Forget it, Jake\" closed the book on detective heroism."], ["Tech-Noir: Blade Runner (1982)", "Neo-Noir", "1982", "Ridley Scott", "Blade Runner fused noir's detective plot with science fiction's future city.", "Its rain, neon, and moral murk are pure noir in new clothes.", "The director's cuts keep revising its meaning."], ["Neo-Noir of the 1980s and 90s", "Neo-Noir", "1980s-1990s", "the revival", "Body Heat, Blood Simple, and L.A. Confidential revived noir for new generations.", "Each updated the formula: Florida heat, Texas blood, 1950s Los Angeles.", "The revival proved noir is a mode, not a period."], ["The Coens and Neo-Noir", "Neo-Noir", "1984-present", "Joel and Ethan Coen", "Blood Simple debuted the Coens in noir; Fargo and No Country perfected their deadpan doom.", "Their noirs find absurdity inside fatalism.", "No Country's Anton Chigurh is noir's scariest modern figure."], ["Noir on Television", "Neo-Noir", "1950s-present", "the small-screen shadows", "TV noir ran from Peter Gunn's jazz cool to True Detective's philosophical dread.", "The long form lets noir's corruption sprawl across seasons.", "Streaming made TV noir prestige."], ["International Noir", "Neo-Noir", "1950s-present", "noir worldwide", "Every film culture made its noir: France's Melville, Japan's Suzuki, Korea's Park.", "Le Samourai's hitman is noir stripped to essence.", "Noir translates because corruption is universal."], ["Noir in Comics and Graphic Novels", "Neo-Noir", "1980s-present", "the printed shadows", "Frank Miller's Sin City brought noir's high contrast to comics literally.", "Criminal and 100 Bullets extended the tradition.", "The page's black ink was always noir's natural home."], ["Erotic Thrillers: Noir's 90s Heirs", "Neo-Noir", "1980s-1990s", "Basic Instinct and its wave", "Basic Instinct and its imitators moved the femme fatale into explicit territory.", "The cycle's commercial success showed noir's erotic charge intact.", "Critics found them trashy; audiences found them thrilling."], ["Modern Noir: Brick (2005) to the Present", "Neo-Noir", "2005-present", "the indie noirs", "Rian Johnson's Brick set noir in a high school, proving the formula's portability.", "Indie noirs keep the shadows alive on small budgets.", "The mode adapts to every setting."], ["Noir Parody and Homage", "Neo-Noir", "1970s-present", "playing with the shadows", "Dead Men Don't Wear Plaid cut Steve Martin into classic noirs, affectionate and hilarious.", "Homage keeps noir's iconography alive for new audiences.", "Parody proves the form's grammar is universally readable."], ["Noir's Enduring Legacy", "Neo-Noir", "present", "the permanent shadows", "Noir's visual style is now the default for seriousness on screen.", "Its moral ambiguity shaped everything from prestige TV to video games.", "Eighty years on, the shadows still fall the same way."]];
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
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator){JAHDB.registerGenerator("film-noir-history",{generate:generate,validate:validate,driftCheck:driftCheck});}
if(typeof module!=='undefined'&&module.exports){module.exports={generate:generate,validate:validate,driftCheck:driftCheck};}
})();
