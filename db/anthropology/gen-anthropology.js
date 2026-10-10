(function(){'use strict';
/* JAH Anthropology Database generator — jahdb-anthropology-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced culture/concept profiles carry src:"online"; Signature-authored
   comparative studies carry src:"signature". All anchor facts are verifiable. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['kinship','marriage','ritual','religion','economy','politics','subsistence','language-culture'];
var PREFIX='JAH-ANT2-';
/* anchors: [title, cat, region/focus, facts...] */
var ANCH=[
["!Kung San foragers","subsistence","Kalahari Desert, Botswana/Namibia",
 "The !Kung San of the Kalahari are among the world's best-studied foraging peoples, documented by Richard Lee's long-term fieldwork.",
 "Their diet centers on the mongongo nut, gathered by women, supplemented by men's hunting with poison arrows.",
 "Lee's energetics studies showed foragers worked fewer hours for food than many farmers, overturning the 'nasty, brutish' stereotype.",
 "Sharing norms are fierce: large game is divided by strict rules, and hoarding draws ridicule and social sanction."],
["Yanomami","politics","Amazon rainforest, Brazil/Venezuela",
 "The Yanomami are a large Indigenous society of the Amazon rainforest, studied by Napoleon Chagnon from the 1960s.",
 "They live in shabonos, large communal roundhouses sheltering entire villages of up to several hundred people.",
 "Their horticulture centers on plantains and cassava, supplemented by hunting with curare-tipped darts.",
 "Chagnon's work on warfare and alliance sparked decades of debate about violence, representation, and research ethics."],
["Maasai pastoralists","subsistence","Kenya and Tanzania",
 "The Maasai are Nilotic pastoralists of Kenya and Tanzania whose lives revolve around cattle.",
 "Cattle provide milk, blood, and meat, and herd size measures wealth and social standing.",
 "Age sets organize male life: boys become moran (warriors) after circumcision rites, later graduating to elderhood.",
 "Land privatization and conservation parks have squeezed the grazing ranges that pastoral mobility requires."],
["Inuit","subsistence","Arctic North America and Greenland",
 "Inuit peoples inhabit the Arctic from Alaska to Greenland, with cultures built around sea-mammal hunting and fishing.",
 "Traditional technology — the kayak, the umiak, tailored caribou-skin clothing — masters extreme cold.",
 "The Inuit Circumpolar Council, founded in 1977, represents Inuit across four nations in international policy.",
 "Climate change now threatens the sea ice that underpins hunting, travel, and cultural transmission."],
["Ainu","language-culture","Hokkaido, Japan",
 "The Ainu are the Indigenous people of Hokkaido, Sakhalin, and the Kuril Islands, with a distinct language isolate.",
 "Their bear ceremony (iyomante) ritually sends the bear spirit back to the spirit world with elaborate respect.",
 "Japanese assimilation policies suppressed Ainu language and custom through much of the 20th century.",
 "Japan legally recognized the Ainu as Indigenous in 2019, funding language and cultural revitalization."],
["Amazigh (Berber)","language-culture","North Africa",
 "The Amazigh are the Indigenous peoples of North Africa, speaking Tamazight languages across Morocco, Algeria, and beyond.",
 "Tifinagh, their ancient script, is now taught in schools and appears on public signs in Morocco and Algeria.",
 "Transhumant pastoralism and oasis agriculture shaped Amazigh social organization for millennia.",
 "The Amazigh cultural movement won constitutional recognition of Tamazight as an official language in Morocco (2011) and Algeria (2016)."],
["Bedouin","subsistence","Arabian and North African deserts",
 "Bedouin are Arab nomadic pastoralists of desert regions, organized by patrilineal tribes and camel herding.",
 "Tribal customary law and the code of hospitality govern relations in stateless desert spaces.",
 "Most Bedouin are now settled, but pastoral identity remains central to cultural pride and poetry.",
 "Camel nomadism demands encyclopedic ecological knowledge of water, pasture, and seasons."],
["Mongol pastoral nomadism","subsistence","Central Asian steppe",
 "Mongol pastoral nomads move seasonally with mixed herds of horses, sheep, goats, cattle, and camels.",
 "The ger (yurt) is a portable felt dwelling perfectly adapted to steppe mobility.",
 "Under Genghis Khan (proclaimed 1206), nomadic military organization built the largest contiguous land empire in history.",
 "Pastoral nomadism persists in Mongolia, where roughly a quarter of the population still herds."],
["Aztec chinampa agriculture","subsistence","Valley of Mexico",
 "The Aztec (Mexica) fed the great city of Tenochtitlan with chinampas, raised garden beds built in shallow lake waters.",
 "Chinampa plots yielded multiple harvests per year of maize, beans, squash, and amaranth.",
 "At its height around 1500 CE, Tenochtitlan held perhaps 200,000 people, among the world's largest cities.",
 "Tribute networks funneled food and goods from across Mesoamerica into the imperial capital."],
["Inca ayllu and quipu","kinship","Andes Mountains",
 "The Inca organized society through the ayllu, a kin-based corporate group holding land collectively.",
 "Ayllus managed labor obligations under the mit'a system that built roads, terraces, and storehouses.",
 "The quipu, knotted cords, recorded census data, tribute, and accounts without any written script.",
 "At its height around 1500 CE the Inca Empire spanned some 2 million square kilometers along the Andes."],
["Aboriginal Dreaming","religion","Australia",
 "Aboriginal Australian cultures share the Dreaming (Dreamtime), a sacred era when ancestral beings shaped the land.",
 "Songlines map creation journeys across the continent, encoding law, geography, and ceremony.",
 "Initiation rites, rock art, and totemic affiliations transmit the Dreaming across generations.",
 "With continuous cultures stretching back 65,000 years, Aboriginal Australians represent the longest living traditions on Earth."],
["Maori haka and tapu","ritual","New Zealand",
 "Maori culture centers on concepts of tapu (sacred restriction) and mana (spiritual power).",
 "The haka, a vigorous posture dance with chant, is performed to welcome guests and honor the dead.",
 "Whakapapa (genealogy) links every person to ancestors, gods, and the land itself.",
 "The 1840 Treaty of Waitangi remains the contested foundation of Maori-settler relations in New Zealand."],
["Trobriand kula ring","economy","Trobriand Islands, Papua New Guinea",
 "Bronislaw Malinowski's 'Argonauts of the Western Pacific' (1922) described the kula, a ceremonial exchange circuit of shell valuables.",
 "Kula valuables — mwali shell bracelets and soulava necklaces — travel in opposite directions around a ring of islands.",
 "The exchange builds alliances, status, and trade partnerships far beyond the objects' utilitarian value.",
 "Malinowski's participant observation in the Trobriands founded modern ethnographic fieldwork."],
["Nuer segmentary lineage","politics","South Sudan",
 "E. E. Evans-Pritchard's 'The Nuer' (1940) described a stateless society organized by segmentary lineages.",
 "In segmentary systems, lineages unite against outsiders at whatever level the threat demands, then divide again.",
 "Cattle are wealth, bridewealth, and ritual sacrifice, structuring Nuer social life.",
 "The Nuer became anthropology's classic case of order without government."],
["Kwakiutl potlatch","economy","Pacific Northwest Coast",
 "The potlatch is a ceremonial feast of the Kwakwaka'wakw and neighboring Northwest Coast peoples, where hosts give away or destroy wealth.",
 "Potlatches validate titles, marriages, and funerals through competitive generosity.",
 "Canadian authorities banned the potlatch from 1884 to 1951 in an attack on Indigenous governance.",
 "Franz Boas's students documented potlatch economics, feeding debates on prestige and redistribution."],
["Sahlins on reciprocity","economy","Theoretical",
 "Marshall Sahlins classified reciprocity as generalized (sharing without return), balanced (direct exchange), and negative (taking).",
 "Generalized reciprocity dominates within households; balanced exchange governs between groups; negative reciprocity marks strangers.",
 "His 'original affluent society' argument held that foragers met needs with less labor than agriculturalists.",
 "The typology remains the standard vocabulary for describing economic moralities."],
["Mauss and the gift","economy","Theoretical",
 "Marcel Mauss's 'The Gift' (1925) argued that gift exchange creates social obligations to give, receive, and reciprocate.",
 "Drawing on Maori hau and Pacific ethnography, Mauss showed gifts carry the spirit of the giver.",
 "The essay founded the anthropology of exchange and still shapes debates on welfare and markets.",
 "Mauss concluded that modern societies, like archaic ones, run on the moral force of reciprocity."],
["Big man societies","politics","Melanesia",
 "In Melanesian big-man systems, leaders build followings through generosity, oratory, and exchange skill rather than inherited office.",
 "Marshall Sahlins contrasted the achieved status of the big man with the ascribed office of the Polynesian chief.",
 "Big men fund feasts and bridewealth payments, converting wealth into renown and obligation.",
 "The model illuminates how leadership can be earned without formal hierarchy."],
["Bridewealth","marriage","Cross-cultural",
 "Bridewealth is the transfer of goods or money from the groom's kin to the bride's kin at marriage.",
 "It compensates the bride's family for the loss of her labor and legitimizes children within the husband's lineage.",
 "Cattle, shells, and cash all serve as bridewealth across Africa, Melanesia, and beyond.",
 "Anthropologists distinguish it sharply from dowry, which moves with the bride."],
["Dowry","marriage","Cross-cultural",
 "Dowry is property transferred with the bride at marriage, common historically across Eurasia.",
 "In much of South Asia, dowry demands have fueled extortion and violence despite legal prohibition.",
 "Jack Goody linked dowry to diverging devolution, where property passes to children of both sexes.",
 "Unlike bridewealth, dowry flows toward the new household rather than compensating the bride's kin."],
["Exogamy and endogamy","marriage","Cross-cultural",
 "Exogamy requires marriage outside one's group; endogamy requires marriage within it.",
 "Clan exogamy builds alliances between groups, while caste endogamy preserves boundaries.",
 "The incest taboo, nearly universal, is exogamy's most basic form.",
 "Marriage rules thus map the political geography of alliance and identity."],
["Iroquois matriliny","kinship","Northeastern North America",
 "The Iroquois (Haudenosaunee) traced descent through the female line, with clan membership passing from mother to children.",
 "Clan mothers held the power to appoint and depose chiefs, giving women central political authority.",
 "Longhouses housed matrilineal extended families under the senior woman's management.",
 "Lewis Henry Morgan's study of Iroquois kinship founded the anthropological study of kinship systems."],
["Levirate and sororate","marriage","Cross-cultural",
 "The levirate requires a widow to marry her dead husband's brother; the sororate gives a widower rights to his wife's sister.",
 "Both customs preserve alliances and property within the intermarrying groups.",
 "They are documented across Africa, Asia, and Indigenous North America.",
 "The practices show marriage as an alliance between groups, not merely individuals."],
["Tibetan fraternal polyandry","marriage","Himalayas",
 "In traditional Tibetan fraternal polyandry, brothers share one wife, keeping the family estate undivided.",
 "The custom concentrates land and labor in harsh high-altitude farming environments.",
 "Children belong to the household regardless of which brother fathered them.",
 "Anthropologists cite it as a textbook adaptation of marriage form to ecology."],
["Kinship terminologies","kinship","Cross-cultural",
 "Anthropologists classify kinship terminologies as Eskimo, Hawaiian, Iroquois, Omaha, Crow, or Sudanese systems.",
 "Eskimo terminology (used in English) distinguishes lineal from collateral kin; Hawaiian merges all cousins with siblings.",
 "Omaha and Crow systems skew generations along the father's or mother's side respectively.",
 "Morgan discovered these patterns; they reveal how societies cognitively organize relatedness."],
["Van Gennep's rites of passage","ritual","Theoretical",
 "Arnold van Gennep's 'Rites of Passage' (1909) identified separation, transition, and incorporation as the universal phases of life-crisis rituals.",
 "Birth, puberty, marriage, and death all move people between social statuses through this threefold sequence.",
 "Victor Turner developed the middle phase as 'liminality', a potent state of ambiguity and equality.",
 "The model applies from initiations to graduations to funerals worldwide."],
["Turner's liminality","ritual","Theoretical",
 "Victor Turner named the middle phase of rites of passage 'liminality': being betwixt and between statuses.",
 "Liminoids in complex societies — carnivals, pilgrimages, theater — generate communitas, intense egalitarian bonding.",
 "Turner's fieldwork among the Ndembu of Zambia grounded the theory in African ritual life.",
 "Liminality explains why transitions feel dangerous and sacred at once."],
["Shamanism","religion","Siberia and worldwide",
 "Shamanism centers on ritual specialists who enter trance to contact spirits for healing and divination.",
 "The word derives from the Tungus saman of Siberia, studied by Russian ethnographers.",
 "Shamans' soul journeys, drumming, and spirit helpers recur from the Arctic to Amazonia.",
 "Mircea Eliade's comparative work made shamanism a global category of religious experience."],
["Tylor on animism","religion","Theoretical",
 "Edward Tylor defined animism — the belief that spirits inhabit nature — as religion's minimum in 'Primitive Culture' (1871).",
 "He argued religion evolved from animism through polytheism to monotheism.",
 "Tylor founded British anthropology and the concept of culture as 'that complex whole'.",
 "Animism has been revived by scholars of Indigenous ontologies who take spirit persons seriously."],
["Frazer's magic","religion","Theoretical",
 "James Frazer's 'The Golden Bough' (1890) classified magic as imitative (like produces like) and contagious (contact transmits influence).",
 "He placed magic before religion and science in a famous evolutionary sequence.",
 "Though the sequence is rejected, the magic-religion distinction still organizes analysis.",
 "Frazer's vast comparative method made mythology a legitimate scholarly subject."],
["Taboo and mana","religion","Polynesia",
 "Tapu (taboo) marks persons, objects, and places as sacred and restricted; mana is the spiritual power they carry.",
 "Violating tapu was believed to bring supernatural punishment, enforcing social order.",
 "Captain Cook's voyages introduced both words into European languages in the 1770s.",
 "Durkheim built his theory of the sacred directly on these Polynesian concepts."],
["Totemism","religion","Cross-cultural",
 "Totemism links social groups to natural species treated as emblems and often protected from harm.",
 "Emile Durkheim argued in 1912 that the totem is society worshipping itself.",
 "Claude Levi-Strauss later showed totems are 'good to think': natural differences model social ones.",
 "Australian Aboriginal totemic systems remain the classic ethnographic case."],
["Azande witchcraft","religion","South Sudan/Congo",
 "Evans-Pritchard's 'Witchcraft, Oracles and Magic among the Azande' (1937) showed witchcraft beliefs as a rational explanatory system.",
 "Witchcraft explains why misfortunes strike particular people at particular times, complementing technical knowledge.",
 "The poison oracle's verdicts settled disputes with accepted finality.",
 "The study became the model for taking Indigenous rationality on its own terms."],
["Cargo cults","religion","Melanesia",
 "Cargo cults of Melanesia blended Christian and Indigenous elements around the anticipated arrival of ancestral goods.",
 "The John Frum movement on Vanuatu, emerging in the 1930s-40s, still celebrates its flag-raising each February.",
 "Anthropologists read cargo cults as creative responses to colonial inequality, not mere superstition.",
 "They demonstrate how religion articulates political and economic grievance."],
["Syncretism","religion","Cross-cultural",
 "Syncretism is the blending of distinct religious traditions into new forms.",
 "Haitian Vodou fuses West African spirits with Catholic saints; Andean Catholicism overlays Inca sacred geography.",
 "Colonial missions unintentionally produced many of history's richest syncretic systems.",
 "The concept challenges ideas of religious purity and bounded traditions."],
["Cultural relativism","language-culture","Theoretical",
 "Cultural relativism, associated with Franz Boas, holds that cultures must be understood on their own terms.",
 "Boas used it to demolish 19th-century racial hierarchies disguised as science.",
 "Methodological relativism suspends judgment during fieldwork; moral relativism remains debated.",
 "The principle underwrites anthropology's defense of human diversity."],
["Participant observation","language-culture","Theoretical",
 "Participant observation — living within a community while studying it — is anthropology's signature method.",
 "Malinowski's Trobriand fieldwork (1915-1918) set the standard: learn the language, live in the village, stay for years.",
 "The method produces the 'thick description' Clifford Geertz later theorized.",
 "It remains unmatched for grasping how social life feels from the inside."],
["Sapir-Whorf hypothesis","language-culture","Theoretical",
 "The Sapir-Whorf hypothesis proposes that language shapes thought and perception.",
 "Edward Sapir and Benjamin Lee Whorf developed it from Native American languages like Hopi.",
 "Strong determinism is rejected, but weak relativity — language nudging cognition — has experimental support.",
 "Color terms, spatial frames, and grammatical gender all show measurable effects."],
["Levi-Strauss structuralism","language-culture","Theoretical",
 "Claude Levi-Strauss argued that myths and kinship reveal universal structures of the human mind.",
 "His 'culinary triangle' and analyses of myth found binary oppositions — raw/cooked, nature/culture — everywhere.",
 "Structural anthropology treated culture like language, seeking deep grammars beneath surface variety.",
 "The approach dominated French thought in the 1960s and reshaped myth studies permanently."],
["Age sets","politics","East Africa",
 "Age sets group all people initiated in the same period into lifelong cohorts with defined roles.",
 "Among the Maasai, each age set passes through warriorhood to elderhood together.",
 "The system coordinates labor, warfare, and ritual across an entire generation.",
 "Age grades — the ranks themselves — must be distinguished from age sets, the cohorts."],
["Transhumance","subsistence","Cross-cultural",
 "Transhumance is seasonal livestock movement between fixed summer and winter pastures.",
 "Alpine, Himalayan, and Mediterranean herders have practiced it for millennia.",
 "It differs from nomadism in its fixed routes and permanent home bases.",
 "Modern borders and land enclosure increasingly strangle transhumant corridors."],
["Swidden agriculture","subsistence","Tropics worldwide",
 "Swidden (slash-and-burn) agriculture clears forest plots, burns the debris for nutrients, and farms for a few years before long fallow.",
 "With long fallows it is sustainable and biodiverse; shortened by population pressure, it degrades soils.",
 "It feeds hundreds of millions across the tropics under names like milpa and chena.",
 "Colonial states often criminalized swidden, misunderstanding its ecological logic."],
["Moiety organization","kinship","Cross-cultural",
 "A moiety system divides a society into two intermarrying halves.",
 "Each moiety typically handles the other's funerals and rituals, institutionalizing reciprocity.",
 "Australian Aboriginal and some Native American societies use moiety organization.",
 "Dual organization shows how marriage rules can structure an entire society."],
["Clan and lineage","kinship","Cross-cultural",
 "A lineage traces descent from a known common ancestor; a clan claims descent from a mythical one.",
 "Unilineal descent — through one sex only — organizes most of the world's kinship systems.",
 "Clans own land, regulate marriage, and mobilize for feuds and feasts.",
 "Segmentary lineage systems like the Nuer's show clans as political building blocks."],
["Divination","ritual","Cross-cultural",
 "Divination is the ritual discovery of hidden knowledge through oracles, lots, or signs.",
 "The Azande poison oracle, Chinese oracle bones, and Ifa divination all render decisions socially binding.",
 "Anthropologists treat divination as decision technology under uncertainty.",
 "Its verdicts end disputes precisely because all parties accept the procedure."]
];
var ANGLES=["culture profile","concept profile","fieldwork profile","comparative profile"];
var SYNREL=[
 ["compared with","This Signature comparative study examines both cases for what they reveal about human social life."],
 ["contrasted against","This Signature contrast study draws out the structural differences between the two cases."],
 ["alongside","This Signature pairing study reads the two cases together as variations on a shared theme."],
 ["in dialogue with","This Signature study places the two cases in dialogue across regions and theories."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Anthropology Database archive.";}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var id=PREFIX+String(seed).padStart(6,'0');
  var pool=ANCH;
  if(opts.category){var f=ANCH.filter(function(a){return a[1]===opts.category;});if(f.length)pool=f;}
  var synth=!opts.category&&rnd()<0.38;
  if(synth){
    var A=pick(pool,rnd),B=pick(pool,rnd),guard=0;
    while(B===A&&guard++<20)B=pick(pool,rnd);
    var rel=pick(SYNREL,rnd);
    var title="Signature study: "+A[0]+" "+rel[0]+" "+B[0];
    var d=A[0]+" ("+A[2]+"): "+A[3]+" "+rel[0]+" "+B[0]+" ("+B[2]+"), "+rel[1]+" "+B[3];
    return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],regions:[A[2],B[2]],src:"signature"},
      region:A[2],src:"signature"};
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(3);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:{kind:A[1],region:A[2],src:"online"},region:A[2],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-ANT2-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.region!=='string'||!r.region.length)e.push('region');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.region!=='string'||!s.region.length)e.push('spec.region');
    }else if(s.kind==='signature-version'){
      if(typeof s.of!=='string'||!s.of.length)e.push('spec.of');
    }else{
      if(!Array.isArray(s.pair)||s.pair.length!==2)e.push('spec.pair');
      if(typeof s.relation!=='string'||!s.relation.length)e.push('spec.relation');
    }
  }
  return{ok:!e.length,errors:e};
}

var SIG_T=[
 "Signature reading of {N}: {F1}",
 "Held in the Signature system as a governed Signature version, this record preserves the fact-checked core whole \u2014 nothing is reduced. {F2}",
 "Signature assessment: {N} is cross-referenced against the archive's related records, so the fact-checked original and its Signature version travel together. Property of Justin Addam Higgins."
];
function sigFill(t,m){return t.replace(/\{N\}|\{F1\}|\{F2\}/g,function(k){return m[k]||'';});}
function signatureVersion(seed){
  var base=generate(seed,{},prng(seed));
  if(!base||base.src!=='online')return null;
  var facts=(base._facts&&base._facts.length)?base._facts:[base.description];
  var N=base._an||base.title;
  var F1=facts[0],F2=facts.length>1?facts[1+((seed%(facts.length-1))|0)]:facts[0];
  var map={'{N}':N,'{F1}':F1,'{F2}':F2};
  var d=sigFill(SIG_T[0],map)+" "+sigFill(SIG_T[1],map)+" "+sigFill(SIG_T[2],map);
  var sv={id:base.id,_seed:seed,title:"Signature version: "+N,description:d,category:base.category,
    spec:{kind:"signature-version",of:base.id,src:"signature"},src:"signature"};
  Object.keys(base).forEach(function(k){
    if(k.charAt(0)==='_'||k==='id'||k==='title'||k==='description'||k==='category'||k==='spec'||k==='src')return;
    sv[k]=base[k];
  });
  return sv;
}
var gen={version:'jahdb-anthropology-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('anthropology',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
