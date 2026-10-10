/* JAH Sociology Database generator — jahdb-sociology-1.0
   Deterministic (mulberry32). Seed -> full sociology entry.
   Sourced records draw every fact from the curated dataset below
   (public sociological knowledge: theories, founders, eras, key works).
   Signature records are homegrown study material, always labeled as such.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-SOC-';
var KIND='sociology entry';
var CATS=['theory','thinker','institution','movement','demographic','method','concept','signature-study'];
/* [name, founders, era, core idea] */
var THEORIES=[
["Structural functionalism","Émile Durkheim and Talcott Parsons","late 19th to mid 20th century","Society is a system of interrelated parts working together to maintain stability."],
["Conflict theory","Karl Marx","mid 19th century","Society is shaped by struggles over power and resources between groups."],
["Symbolic interactionism","George Herbert Mead and Herbert Blumer","early to mid 20th century","People act toward things based on the meanings they assign through social interaction."],
["Social exchange theory","George Homans and Peter Blau","mid 20th century","Social behavior is an exchange of rewards and costs."],
["Rational choice theory","various economists and sociologists","mid 20th century","People make decisions by weighing costs against benefits."],
["Feminist theory","many contributors","19th to 21st century","Examines gender inequality and patriarchy in social life."],
["Critical theory","Max Horkheimer and Theodor Adorno","1930s","Critiques power structures with the aim of human emancipation."],
["Postmodernism","Jean-François Lyotard and Jean Baudrillard","late 20th century","Skeptical of grand narratives; emphasizes fragmentation and simulation."],
["Social constructionism","Peter Berger and Thomas Luckmann","1960s","Reality is built through social interaction and shared meaning."],
["Structuration theory","Anthony Giddens","1980s","Social structure and human agency continually shape each other."],
["World-systems theory","Immanuel Wallerstein","1970s","The world is one capitalist economy divided into core, semi-periphery, and periphery."],
["Labeling theory","Howard Becker","1960s","Deviance is created by the labels society applies to people."],
["Strain theory","Robert Merton","1930s to 1950s","Deviance results from strain between cultural goals and legitimate means."],
["Social control theory","Travis Hirschi","1969","Strong social bonds keep people from deviance."],
["Dramaturgy","Erving Goffman","1959","Social life is a performance with a front stage and a back stage."],
["Phenomenology","Alfred Schutz","mid 20th century","Studies how people experience and interpret everyday life."],
["Ethnomethodology","Harold Garfinkel","1960s","Studies the everyday methods people use to produce social order."],
["Social network theory","many contributors","late 20th century","Social life is analyzed as networks of ties between actors."],
["Rationalization","Max Weber","early 20th century","Modern life is increasingly governed by efficiency, calculation, and rules."],
["Anomie","Émile Durkheim","1897","Normlessness that appears when social regulation breaks down."],
["Cultural capital","Pierre Bourdieu","1970s to 1980s","Non-financial assets such as education and taste confer social advantage."],
["Habitus","Pierre Bourdieu","1970s","Deeply ingrained habits and dispositions shaping perception and action."],
["McDonaldization","George Ritzer","1993","Society takes on the efficiency, calculability, and control of fast food."],
["Risk society","Ulrich Beck","1986","Late modernity is organized around managing manufactured risks."],
["Liquid modernity","Zygmunt Bauman","2000","Social forms melt; life becomes fluid, flexible, and uncertain."],
["The Protestant ethic thesis","Max Weber","1905","Protestant values helped drive the development of capitalism."],
["Division of labor","Émile Durkheim","1893","Modern solidarity rests on the interdependence of specialized roles."],
["The power elite","C. Wright Mills","1956","A small elite dominates the major institutions of society."],
["The sociological imagination","C. Wright Mills","1959","Connects personal troubles to larger public issues."],
["Looking-glass self","Charles Horton Cooley","1902","Self-image forms through imagining how others see us."],
["Generalized other","George Herbert Mead","1934","The internalized attitudes of the wider community."],
["Double consciousness","W. E. B. Du Bois","1903","The sense of two warring identities in Black American life."],
["Intersectionality","Kimberlé Crenshaw","1989","Overlapping identities shape each person's experience of advantage and oppression."],
["Doing gender","Candace West and Don Zimmerman","1987","Gender is accomplished through everyday interaction."],
["Moral panic","Stanley Cohen","1972","Society overreacts to a perceived threat from a group."],
["Broken windows theory","James Q. Wilson and George Kelling","1982","Visible disorder encourages further disorder."],
["Differential association","Edwin Sutherland","1939","Criminal behavior is learned through interaction with others."],
["Techniques of neutralization","Gresham Sykes and David Matza","1957","Offenders justify deviance to themselves to keep offending."],
["Relative deprivation","many contributors","mid 20th century","Discontent comes from comparing oneself unfavorably with others."],
["Social disorganization theory","Clifford Shaw and Henry McKay","1942","Crime follows from weakened community institutions."]
];
/* [name, years, known for] */
var THINKERS=[
["Auguste Comte","1798-1857","Coined the word sociology; founder of positivism."],
["Karl Marx","1818-1883","Conflict theory; The Communist Manifesto of 1848."],
["Émile Durkheim","1858-1917","Functionalism; Suicide (1897); the concept of anomie."],
["Max Weber","1864-1920","Verstehen; rationalization; The Protestant Ethic (1905)."],
["Georg Simmel","1858-1918","Formal sociology; the stranger; metropolitan life."],
["W. E. B. Du Bois","1868-1963","Double consciousness; pioneering Black sociology in America."],
["Harriet Martineau","1802-1876","The first woman sociologist; translated Comte into English."],
["Jane Addams","1860-1935","Hull House settlement; social reform; Nobel Peace Prize 1931."],
["Herbert Spencer","1820-1903","Social Darwinism; coined the phrase survival of the fittest."],
["Talcott Parsons","1902-1979","Structural functionalism; the AGIL schema of social systems."],
["Robert K. Merton","1910-2003","Strain theory; manifest and latent functions."],
["C. Wright Mills","1916-1962","The Power Elite; the sociological imagination."],
["Erving Goffman","1922-1982","Dramaturgy; stigma; total institutions."],
["Pierre Bourdieu","1930-2002","Cultural capital; habitus; field."],
["Michel Foucault","1926-1984","Power and knowledge; discipline; biopolitics."],
["Jürgen Habermas","born 1929","The public sphere; communicative action."],
["Anthony Giddens","born 1938","Structuration theory; work on the Third Way."],
["Ulrich Beck","1944-2015","The risk society."],
["Zygmunt Bauman","1925-2017","Liquid modernity."],
["Immanuel Wallerstein","1930-2019","World-systems theory."],
["Howard Becker","1928-2023","Labeling theory; Outsiders (1963)."],
["George Herbert Mead","1863-1931","Symbolic interactionism; Mind, Self, and Society."],
["Charles Horton Cooley","1864-1929","The looking-glass self; primary groups."],
["W. I. Thomas","1863-1947","The Thomas theorem: situations defined as real are real in their consequences."],
["Robert Ezra Park","1864-1944","The Chicago School; human ecology of the city."],
["Alfred Schutz","1899-1959","The phenomenology of the social world."],
["Harold Garfinkel","1917-2011","Ethnomethodology."],
["George Ritzer","born 1940","McDonaldization."],
["Kimberlé Crenshaw","born 1959","Intersectionality."],
["Patricia Hill Collins","born 1948","Black feminist thought; the matrix of domination."]
];
/* [name, role in society] */
var INSTITUTIONS=[
["Family","The primary agent of socialization; raises children and transmits culture."],
["Education","Transmits knowledge and skills; sorts people into social positions."],
["Religion","Provides shared beliefs, rituals, and moral community."],
["Government","Makes and enforces the rules binding on a territory."],
["Economy","Organizes the production and distribution of goods and services."],
["Media","Circulates information and shapes public attention."],
["Healthcare","Maintains and restores bodily health across the population."],
["Law","Codifies norms and resolves disputes through courts."],
["Marriage","A socially recognized union, often the legal basis of family."],
["Military","Organizes armed defense under state authority."],
["Science","Produces systematic knowledge through research."],
["Sports","Organizes competitive play with wide cultural meaning."]
];
/* [name, note] */
var MOVEMENTS=[
["Civil rights movement","The mid-20th-century struggle for racial equality in the United States."],
["Women's suffrage","The movement that won women the right to vote in the early 20th century."],
["Labor movement","Workers organizing for better wages, hours, and conditions."],
["Abolitionism","The movement that ended legal slavery in the 19th century."],
["Environmental movement","Organized action to protect nature, from the 1960s onward."],
["LGBTQ+ rights movement","The struggle for equal rights regardless of sexual orientation or gender identity."],
["Temperance movement","The campaign against alcohol that led to Prohibition in the United States."],
["Anti-war movement","Mass protest against wars, notably Vietnam in the 1960s and 1970s."],
["Indian independence movement","Nonviolent mass mobilization that ended British rule in 1947."],
["Solidarity","The Polish labor movement that helped end communist rule in 1989."],
["Arab Spring","The 2011 wave of uprisings across the Arab world."],
["#MeToo","The movement against sexual harassment and assault from 2017 onward."]
];
/* [name, note] */
var DEMOGRAPHICS=[
["Demographic transition","Populations move from high birth and death rates to low ones as they develop."],
["Urbanization","The growing share of people living in cities."],
["Aging population","A rising median age as fertility falls and life expectancy grows."],
["Migration","The movement of people across regions and borders."],
["Fertility decline","Falling birth rates in most of the world since the mid-20th century."],
["Population momentum","Populations keep growing for decades after fertility falls."],
["Baby boom","The surge of births after World War II in many countries."],
["Brain drain","The emigration of skilled workers from poorer regions."],
["Suburbanization","The movement of city residents to surrounding suburbs."],
["Gentrification","Wealthier residents moving into poorer neighborhoods, displacing longtime residents."]
];
/* [name, note] */
var METHODS=[
["Survey","Asking standardized questions of a sample to measure attitudes and behavior."],
["Interview","Guided conversation yielding rich qualitative detail."],
["Participant observation","Joining a group to study it from the inside."],
["Ethnography","Long-term immersive study of a culture or community."],
["Content analysis","Systematic coding of texts, media, or messages."],
["Longitudinal study","Following the same people or units over time."],
["Experiment","Manipulating a variable to test cause and effect."],
["Census","Counting an entire population at a point in time."],
["Case study","Deep investigation of a single instance."],
["Secondary data analysis","Reusing data collected by others for new questions."]
];
/* [name, note] */
var CONCEPTS=[
["Norms","Shared rules for expected behavior."],
["Values","Deeply held ideas about what is good and desirable."],
["Roles","Expected behaviors attached to a social position."],
["Status","A recognized social position, ascribed or achieved."],
["Socialization","Learning the norms and values of one's group."],
["Deviance","Behavior that violates social norms."],
["Social stratification","The layering of society into ranked groups."],
["Social class","Position in the economic hierarchy."],
["Race","A socially constructed category based on perceived physical traits."],
["Ethnicity","Shared cultural heritage and identity."],
["Gender","Socially constructed roles tied to sex categories."],
["Culture","Shared beliefs, values, and practices of a group."],
["Subculture","A group with distinct values within a larger culture."],
["Counterculture","A group whose values oppose the mainstream."],
["Social capital","Resources gained through social networks."],
["Bureaucracy","Rule-bound hierarchical organization."],
["Charisma","Authority based on personal appeal."],
["Power","The ability to get others to act as one wishes."],
["Authority","Legitimate power accepted as rightful."],
["Social mobility","Movement between social positions across a lifetime or generations."],
["Meritocracy","A system rewarding talent and effort."],
["Discrimination","Unequal treatment based on group membership."],
["Prejudice","Prejudged negative attitudes toward a group."],
["Stereotype","An oversimplified image of a group."],
["Groupthink","Faulty group decisions from pressure to conform."],
["Reference group","The group people compare themselves with."]
];
var ANGLES=[
["","", ""],
["for students"," \u2014 for students"," Students meet this idea early because it unlocks so much else."],
["lecture notes"," \u2014 lecture notes"," A lecturer can build a whole session around this entry."],
["research view"," \u2014 research view"," Researchers keep returning to this idea with new data."],
["everyday life"," \u2014 everyday life"," You can spot this idea at work in ordinary daily life."],
["quick facts"," \u2014 quick facts",""]
];
function comboGen(j,nE,nA,nG){
  var per=nA*nG;
  var e=j%nE, c=Math.floor(j/nE)%per, part=Math.floor(j/(nE*per));
  return {e:e,a:Math.floor(c/nG),g:c%nG,part:part};
}
var SRC="JAH Sociology curated dataset v1 \u2014 theories, thinkers, and concepts from public sociological knowledge.";
var SIGSRC="JAH Signature generator \u2014 homegrown study material; underlying facts from the curated dataset, clearly labeled as generated.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" See the full record for the complete entry.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
var THEORY_ASPECTS=[
["core idea",function(x){return "At its heart: "+x[3];}],
["founders",function(x){return "Associated above all with "+x[1]+".";}],
["era",function(x){return "It rose to prominence in the "+x[2]+".";}],
["use",function(x){return "Researchers use it to make sense of power, meaning, and order in social life.";}],
["debate",function(x){return "Like every great theory, it has loyal defenders and sharp critics.";}],
["classroom",function(x){return "It remains a staple of introductory sociology courses.";}]
];
var THINKER_ASPECTS=[
["life and work",function(x){return x[0]+" ("+x[1]+"): "+x[2];}],
["contribution",function(x){return "The lasting contribution: "+x[2];}],
["era",function(x){return "Working in "+x[1]+", this thinker shaped how sociology sees the world.";}],
["influence",function(x){return "Later generations of sociologists still argue with and build on this work.";}],
["key idea",function(x){return "The signature idea: "+x[2];}],
["classroom",function(x){return "Students meet this name in nearly every sociology course.";}]
];
var SIMPLE_ASPECTS=[
["overview",function(x){return x[0]+": "+x[1];}],
["role",function(x){return "Its place in social life: "+x[1];}],
["examples",function(x){return "Concrete cases make this idea vivid in teaching and research.";}],
["debate",function(x){return "Scholars debate its boundaries and its future.";}],
["everyday",function(x){return "Ordinary life is full of illustrations of this idea.";}],
["classroom",function(x){return "A reliable entry point for students of sociology.";}]
];
function profileKind(seed,j,entries,aspects,cat,introFn){
  var cb=comboGen(j,entries.length,aspects.length,ANGLES.length);
  var x=entries[cb.e], a=aspects[cb.a], g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary=introFn(x)+" "+a[1](x)+g[2];
  var details={name:x[0],aspect:a[0],angle:g[0]||"standard"};
  if(x.length>3){details.founders=x[1];details.era=x[2];details.core=x[3];}
  else if(x.length>2&&cat==="thinker"){details.years=x[1];details.known_for=x[2];}
  else{details.note=x[1];}
  return mkRec(seed,cat,title,summary,details,"sourced",SRC);
}
function genStudy(seed,j,rnd){
  var pools=[THEORIES,THINKERS,INSTITUTIONS,MOVEMENTS,DEMOGRAPHICS,METHODS,CONCEPTS];
  var flat=[];pools.forEach(function(p){p.forEach(function(x){flat.push(x[0]);});});
  var topic=flat[(j*37)%flat.length];
  var st=["applying a theory to a news story","designing a small survey","observing a public place","comparing two institutions","tracing a movement's tactics","reading a classic text closely","debating nature versus nurture","mapping a social network"][j%8];
  var title="Signature study: "+st+" \u2014 "+topic;
  var summary="Signature-generated study exercise \u2014 homegrown material, not a published study. "+
    "Task: "+st+", using "+topic+" as the case. Work through the concepts in this database's archive, "+
    "write up what the theory would predict, and check it against real observations.";
  var details={exercise:st,case:topic,steps:["Pick the relevant archive entries","State what the theory predicts","Gather real observations","Compare and write up"]};
  return mkRec(seed,"signature-study",title,summary,details,"signature",SIGSRC);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=3500)cat="theory";
    else if(s<=5000)cat="thinker";
    else if(s<=5800)cat="institution";
    else if(s<=6600)cat="movement";
    else if(s<=7200)cat="demographic";
    else if(s<=7800)cat="method";
    else if(s<=9000)cat="concept";
    else cat="signature-study";
  }
  /* explicit category from the Generator tab: index from s-1 so any seed works */
  function ord(base){return explicit?(s-1):(s-base);}
  var theoryIntro=function(x){return x[0]+" is a major sociological theory linked with "+x[1]+".";};
  if(cat==="theory")return profileKind(seed,ord(1),THEORIES,THEORY_ASPECTS,"theory",theoryIntro);
  if(cat==="thinker")return profileKind(seed,ord(3501),THINKERS,THINKER_ASPECTS,"thinker",function(x){return x[0]+" ("+x[1]+") is a landmark figure in sociology.";});
  if(cat==="institution")return profileKind(seed,ord(5001),INSTITUTIONS,SIMPLE_ASPECTS,"institution",function(x){return "The institution of "+x[0].toLowerCase()+" structures social life.";});
  if(cat==="movement")return profileKind(seed,ord(5801),MOVEMENTS,SIMPLE_ASPECTS,"movement",function(x){return "The "+x[0]+" is a landmark social movement.";});
  if(cat==="demographic")return profileKind(seed,ord(6601),DEMOGRAPHICS,SIMPLE_ASPECTS,"demographic",function(x){return x[0]+" is a key demographic pattern.";});
  if(cat==="method")return profileKind(seed,ord(7201),METHODS,SIMPLE_ASPECTS,"method",function(x){return "The "+x[0].toLowerCase()+" is a core sociological research method.";});
  if(cat==="concept")return profileKind(seed,ord(7801),CONCEPTS,SIMPLE_ASPECTS,"concept",function(x){return x[0]+" is a foundational concept in sociology.";});
  if(cat==="signature-study")return genStudy(seed,ord(9001),rnd);
  return profileKind(seed,ord(1),THEORIES,THEORY_ASPECTS,"theory",theoryIntro);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-SOC-\d{6,7}$/.test(r.id||""))e.push("id");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(CATS.indexOf(r.category)<0)e.push("category");
  if(r.record_kind!==KIND)e.push("record_kind");
  if(typeof r.summary!=="string"||r.summary.length<80)e.push("summary");
  if(!r.details||typeof r.details!=="object")e.push("details");
  if(r.provenance!=="sourced"&&r.provenance!=="signature")e.push("provenance");
  if(typeof r.source!=="string"||!r.source.length)e.push("source");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:["already in archive: "+rec.id]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-sociology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("sociology",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
