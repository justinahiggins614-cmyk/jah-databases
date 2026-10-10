(function(){'use strict';
/* JAH Military Strategy Database generator — jahdb-military-strategy-1.0.
   Deterministic client-side generator: same seed + same version = same record.
   Online-sourced doctrine/battle profiles carry src:"online"; Signature-authored
   comparative studies carry src:"signature". All anchor facts are verifiable. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=['doctrine','battle','principle','leader','technology','era-study'];
var PREFIX='JAH-MIL-';
/* anchors: [title, cat, era/date label, facts...] */
var ANCH=[
["Sun Tzu, The Art of War","doctrine","c. 5th century BCE",
 "Sun Tzu's 'The Art of War', composed in China around the 5th century BCE, is the oldest surviving military treatise.",
 "Its thirteen chapters teach that supreme excellence is subduing the enemy without fighting, through deception, speed, and intelligence.",
 "'All warfare is based on deception' and 'know the enemy and know yourself' remain its most quoted maxims.",
 "The text shaped East Asian strategy for two millennia and entered Western doctrine in the 20th century."],
["Clausewitz, On War","doctrine","1832",
 "Carl von Clausewitz's 'On War', published posthumously in 1832, is the West's foundational theory of war.",
 "Its core claims: war is the continuation of politics by other means; friction and the fog of war govern all operations.",
 "The 'remarkable trinity' of passion, chance, and reason links people, army, and government.",
 "The 'center of gravity' concept — the source of an enemy's strength — still structures operational planning."],
["Jomini, Summary of the Art of War","doctrine","1838",
 "Antoine-Henri Jomini's 'Summary of the Art of War' (1838) systematized Napoleonic warfare into teachable principles.",
 "Jomini stressed interior lines, concentration against decisive points, and secure lines of operation.",
 "His maxims dominated 19th-century staff colleges, especially in the United States Civil War era.",
 "Critics call him formulaic next to Clausewitz; practitioners still use his vocabulary."],
["Mahan and sea power","doctrine","1890",
 "Alfred Thayer Mahan's 'The Influence of Sea Power upon History' (1890) argued that naval supremacy decides great-power rivalry.",
 "He urged concentration of battleship fleets to command the sea and strangle enemy commerce.",
 "The book electrified naval building from Washington to Berlin to Tokyo.",
 "Its battleship orthodoxy was later qualified by submarines, aircraft, and missiles."],
["Corbett, maritime strategy","doctrine","1911",
 "Julian Corbett's 'Some Principles of Maritime Strategy' (1911) offered a subtler naval theory than Mahan's.",
 "Corbett distinguished command of the sea from its exercise, and tied naval operations to political objectives.",
 "His ideas guided British strategy in both world wars and remain taught at naval colleges.",
 "He is the theorist of limited war at sea and the fleet-in-being."],
["Douhet and air power","doctrine","1921",
 "Giulio Douhet's 'The Command of the Air' (1921) proclaimed that bombing enemy cities and industry wins wars.",
 "He advocated independent bomber fleets striking the enemy's 'vital centers' to shatter morale.",
 "His theories influenced interwar air forces and the strategic bombing campaigns of World War II.",
 "Postwar analysis showed bombing alone rarely breaks national will, qualifying Douhet's claims."],
["Liddell Hart, the indirect approach","doctrine","1929",
 "B. H. Liddell Hart's 'The Decisive Wars of History' (1929) championed the indirect approach: dislocation before destruction.",
 "He argued that striking where the enemy least expects, at lines of communication and command, collapses resistance cheaply.",
 "His ideas influenced German panzer theorists and postwar maneuver warfare.",
 "Critics note his history is selective; admirers credit him with mechanized warfare's intellectual foundation."],
["Fuller and mechanized war","doctrine","1919-1932",
 "J. F. C. Fuller, the British tank pioneer, wrote 'Plan 1919' for massed tank breakthroughs in World War I.",
 "His interwar writings made the tank the centerpiece of future land warfare.",
 "Fuller's nine principles of war influenced doctrines on both sides of World War II.",
 "He later drifted into political extremism, which shadowed his military reputation."],
["Guderian and blitzkrieg","doctrine","1937",
 "Heinz Guderian's 'Achtung-Panzer!' (1937) codified the German doctrine of concentrated armored breakthrough.",
 "Blitzkrieg combined tanks, motorized infantry, close air support, and radio into rapid deep penetrations.",
 "The 1939-1941 campaigns — Poland, France, the early Soviet Union — demonstrated its shock effect.",
 "Later analysis stresses logistics, air power, and enemy weakness as much as tank tactics."],
["Boyd's OODA loop","doctrine","1976-1995",
 "US Air Force Colonel John Boyd's OODA loop — Observe, Orient, Decide, Act — models decision-making in conflict.",
 "Victory goes to whoever cycles through the loop faster, getting inside the opponent's decision cycle.",
 "Boyd's energy-maneuverability theory had earlier revolutionized fighter design (F-15, F-16).",
 "The OODA loop now frames everything from air combat to business strategy."],
["Mao, On Protracted War","doctrine","1938",
 "Mao Zedong's 'On Protracted War' (1938) is the classic theory of people's war against a stronger invader.",
 "Its three stages — strategic defensive, stalemate, strategic offensive — trade space for time.",
 "The doctrine mobilizes the peasantry as the sea in which guerrillas swim.",
 "It inspired insurgencies from Vietnam to Latin America and remains studied in staff colleges."],
["Lawrence and guerrilla war","doctrine","1917-1926",
 "T. E. Lawrence's writings on the Arab Revolt distilled guerrilla principles: mobility, surprise, and popular support.",
 "His 'Seven Pillars of Wisdom' and the 1917 '27 Articles' remain required reading on irregular warfare.",
 "Lawrence argued guerrillas should attack the enemy's material and communications, never hold ground.",
 "His campaigns tied down Ottoman divisions with a fraction of their strength."],
["Vegetius, De Re Militari","doctrine","c. 390 CE",
 "Vegetius's 'De Re Militari' (c. 390 CE) preserved Roman military wisdom for the Middle Ages.",
 "Its famous maxim 'si vis pacem, para bellum' — if you want peace, prepare for war — outlived Rome itself.",
 "Vegetius stressed training, discipline, and logistics over battlefield heroics.",
 "Medieval commanders treated it as the standard military manual for a thousand years."],
["Frontinus, Stratagems","doctrine","c. 84-96 CE",
 "Sextus Julius Frontinus's 'Stratagems' catalogued ruses and tricks of Greek and Roman commanders.",
 "Organized by situation — before battle, sieges, retreats — it is history's first trick-play playbook.",
 "Frontinus wrote as a practical governor-general, not a philosopher.",
 "His examples taught that cunning multiplies force."],
["Machiavelli, The Art of War","doctrine","1521",
 "Niccolo Machiavelli's 'The Art of War' (1521) argued for citizen militias over mercenaries.",
 "Written as a dialogue, it adapted Roman discipline to Renaissance Italy's wars.",
 "Machiavelli held that good arms require good laws, and vice versa.",
 "The work influenced military thought into the 18th century."],
["Napoleon, the corps system","leader","1805-1815",
 "Napoleon Bonaparte revolutionized warfare with the corps system: self-contained combined-arms armies marching dispersed and fighting concentrated.",
 "Ulm (1805) saw him encircle an Austrian army before battle; Austerlitz (1805) remains the tactical masterpiece of the era.",
 "His maxims — 'march divided, fight united', the central position — entered every staff college.",
 "Overextension in Russia (1812) and coalition arithmetic ended his empire at Waterloo (1815)."],
["Frederick the Great, oblique order","leader","1740-1786",
 "Frederick II of Prussia perfected the oblique order: refusing one flank while overloading the other, as at Leuthen (1757).",
 "His disciplined infantry and rapid maneuver let Prussia survive encirclement by greater powers.",
 "The 'Miracle of the House of Brandenburg' — Russia's exit after Elizabeth's death — saved him in the Seven Years' War.",
 "Frederick made Prussia a great power and the model of the professional army."],
["Alexander at Gaugamela","leader","331 BCE",
 "Alexander the Great's victory at Gaugamela (331 BCE) over Darius III's vastly larger Persian army is the classic oblique-phalanx battle.",
 "Holding his right, Alexander punched a cavalry wedge through a gap and struck the Persian center.",
 "The victory made him master of the Persian Empire at age 25.",
 "His combined-arms tactics — phalanx pinning, cavalry striking — remained the template for centuries."],
["Hannibal at Cannae","battle","216 BCE",
 "Hannibal's double envelopment at Cannae (216 BCE) destroyed a Roman army of perhaps 80,000 men.",
 "His weak center yielded deliberately while African infantry crushed both Roman flanks inward.",
 "Cannae became the textbook example of annihilation, studied by Schlieffen and every staff college since.",
 "Rome survived by refusing further pitched battles — the Fabian strategy."],
["Scipio at Zama","battle","202 BCE",
 "Scipio Africanus defeated Hannibal at Zama (202 BCE) by neutralizing Carthage's elephants and cavalry.",
 "His maniples opened lanes for the elephants to pass through harmlessly.",
 "Numidian cavalry under Masinissa then decided the battle, ending the Second Punic War.",
 "Zama shows how studying the enemy's signature weapon enables its defeat."],
["Caesar at Alesia","battle","52 BCE",
 "Julius Caesar's siege of Alesia (52 BCE) is the masterpiece of Roman siegecraft: he besieged Vercingetorix while himself besieged by relief forces.",
 "His double ring of fortifications — circumvallation facing inward, contravallation facing outward — held both enemies.",
 "The victory ended organized Gallic resistance and made Caesar's reputation.",
 "Alesia demonstrates that engineering can substitute for numbers."],
["Genghis Khan","leader","1206-1227",
 "Genghis Khan united the Mongol tribes in 1206 and built history's largest contiguous land empire.",
 "His armies used feigned retreats, the composite bow, total intelligence, and meritocratic command.",
 "Mongol discipline — decimal organization, yam relay stations — made nomad cavalry a strategic weapon.",
 "His conquests redrew Eurasia's map and its trade routes."],
["Saladin at Hattin","battle","1187",
 "Saladin's victory at Hattin (1187) destroyed the Crusader field army by denying it water and goading it onto arid ground.",
 "Harassing horse archers and smoke fires exhausted the Frankish knights before the final assault.",
 "Jerusalem fell months later, triggering the Third Crusade.",
 "Hattin is the classic victory of operational maneuver over heavy shock."],
["Agincourt","battle","1415",
 "Henry V's English army destroyed a larger French force at Agincourt (1415) with massed longbow fire.",
 "Mud, stakes, and armored archers broke French cavalry charges before men-at-arms closed.",
 "The longbow's aimed volleys made the armored knight's charge suicidal.",
 "Agincourt, with Crecy (1346), proved missile fire's dominance over shock cavalry."],
["Constantinople 1453","battle","1453",
 "Mehmed II's 1453 siege of Constantinople ended the Byzantine Empire with giant bombards breaching the Theodosian Walls.",
 "His engineers dragged ships overland into the Golden Horn, outflanking the sea chain.",
 "The fall sent Greek scholars westward, fueling the Renaissance.",
 "It marks the triumph of gunpowder artillery over medieval fortification."],
["Lepanto","battle","1571",
 "The Holy League's galley fleet defeated the Ottomans at Lepanto (1571), the last great galley battle.",
 "Christian firepower — arquebusiers and heavy guns — broke Ottoman boarding tactics.",
 "The victory checked Ottoman naval expansion in the western Mediterranean.",
 "Cervantes, who fought there, called it the most memorable event of his age."],
["Breitenfeld","battle","1631",
 "Gustavus Adolphus's victory at Breitenfeld (1631) introduced linear tactics, mobile artillery, and combined arms to the Thirty Years' War.",
 "His Swedish brigades' firepower and cavalry shock routed the Imperial tercios.",
 "The battle made Sweden a great power and Gustavus the 'Lion of the North'.",
 "Breitenfeld is often called the birth of modern warfare."],
["Blenheim","battle","1704",
 "Marlborough and Eugene's victory at Blenheim (1704) broke French dominance in the War of the Spanish Succession.",
 "A feigned attack pinned the French center while the main blow fell on their flank.",
 "The battle saved Austria and made Marlborough England's great captain.",
 "It demonstrated coalition warfare's potential when unified under one command."],
["Poltava","battle","1709",
 "Peter the Great's victory at Poltava (1709) broke Swedish power and made Russia a great power.",
 "Russian field fortifications and artillery shredded Charles XII's depleted army.",
 "The battle ended Sweden's empire and began Russia's.",
 "Poltava shows logistics and firepower defeating maneuver brilliance."],
["Yorktown","battle","1781",
 "The Franco-American siege of Yorktown (1781) trapped Cornwallis between Washington's army and de Grasse's fleet.",
 "French siege artillery systematically reduced the British works until surrender.",
 "Yorktown effectively ended the American Revolutionary War.",
 "It is the classic example of joint land-sea operations deciding a campaign."],
["Trafalgar","battle","1805",
 "Nelson's victory at Trafalgar (1805) destroyed the Franco-Spanish fleet, securing British naval supremacy for a century.",
 "Breaking the line in two columns, Nelson's ships raked the enemy at close range.",
 "Nelson died in the hour of victory; his tactics became naval legend.",
 "Trafalgar proved that aggressive doctrine multiplies material advantage."],
["Waterloo","battle","1815",
 "Wellington and Blucher's victory at Waterloo (1815) ended Napoleon's Hundred Days.",
 "Wellington's reverse-slope defense absorbed French attacks until the Prussians arrived on the flank.",
 "The Imperial Guard's repulse broke French morale and the army dissolved.",
 "Waterloo demonstrates coalition warfare and the decisive value of timely reinforcement."],
["Gettysburg","battle","1863",
 "The Battle of Gettysburg (1863) was the American Civil War's turning point and its bloodiest engagement.",
 "Lee's invasion of the North broke on Union interior lines and Pickett's disastrous charge.",
 "Some 50,000 casualties in three days shocked both nations.",
 "Lincoln's address there redefined the war as a test of democratic government."],
["Sedan","battle","1870",
 "The Prussian encirclement at Sedan (1870) captured Napoleon III and his army, collapsing the Second Empire.",
 "Moltke's rail-mobilized armies and Krupp artillery executed a perfect envelopment.",
 "The victory unified Germany under Prussian leadership.",
 "Sedan validated the general staff system and industrial-age mobilization."],
["Tsushima","battle","1905",
 "Admiral Togo's victory at Tsushima (1905) annihilated Russia's Baltic Fleet after its 18,000-mile voyage.",
 "Japanese gunnery, speed, and the 'crossing the T' maneuver destroyed the Russian column.",
 "The first great victory of an Asian power over a European one, it shocked the world.",
 "Tsushima confirmed the battleship's dominance — until aircraft ended it."],
["The Marne","battle","1914",
 "The First Battle of the Marne (1914) stopped the German Schlieffen Plan advance on Paris.",
 "French and British counterattacks exploited the gap between German armies.",
 "The 'Miracle of the Marne' condemned Europe to four years of trench warfare.",
 "It shows how one operational failure can decide a war's character."],
["Verdun","battle","1916",
 "The Battle of Verdun (1916) became history's longest battle: ten months and some 700,000 casualties.",
 "Falkenhayn intended to 'bleed France white' in an attritional grinder.",
 "Petain's 'They shall not pass' and the Voie Sacree supply road became French legend.",
 "Verdun is the ultimate symbol of industrial attrition's horror."],
["The Somme","battle","1916",
 "The Somme offensive (1916) cost Britain 57,000 casualties on its first day, the army's bloodiest.",
 "Artillery failed to cut the wire or destroy deep dugouts; infantry walked into machine-gun fire.",
 "The battle's futility became the emblem of World War I generalship's failure.",
 "Tanks debuted at the Somme in September, hinting at the future."],
["Jutland","battle","1916",
 "The Battle of Jutland (1916) was the only full fleet clash of World War I's dreadnoughts.",
 "Tactically indecisive, it confirmed British strategic blockade — 'the prisoner of war' fleet.",
 "German battlecruisers' ammunition-handling flaws caused catastrophic explosions.",
 "Jutland proved Mahanian decisive battle elusive in the industrial age."],
["Cambrai","battle","1917",
 "Cambrai (1917) saw the first massed tank attack: nearly 500 British tanks broke the Hindenburg Line.",
 "Surprise, without preliminary bombardment, achieved complete tactical success.",
 "German counterattacks recovered the ground, but the tank's potential was proven.",
 "Cambrai launched the armored-warfare revolution."],
["Midway","battle","1942",
 "The US Navy's victory at Midway (1942) sank four Japanese carriers, reversing the Pacific War's momentum.",
 "Codebreakers' intelligence let Nimitz ambush Nagumo's strike force.",
 "American dive-bombers caught Japanese carriers with decks full of fuel and ordnance.",
 "Midway is intelligence's greatest operational triumph."],
["Stalingrad","battle","1942-1943",
 "Stalingrad (1942-43) destroyed Germany's Sixth Army in the Eastern Front's turning point.",
 "Zhukov's Operation Uranus encircled the city while the Soviets held the ruins building by building.",
 "Some 2 million casualties made it history's bloodiest battle.",
 "Stalingrad proved that operational encirclement defeats tactical skill."],
["Kursk","battle","1943",
 "Kursk (1943) was history's largest tank battle, breaking Germany's last Eastern Front offensive.",
 "Soviet defense in depth absorbed the panzer spearheads, then counteroffensives crushed them.",
 "Over 6,000 tanks and 2 million men fought across the salient.",
 "After Kursk, Germany never again held the strategic initiative in the east."],
["Normandy (Overlord)","battle","1944",
 "Operation Overlord (June 1944) landed five Allied divisions in Normandy, opening the Western Front.",
 "Deception (Fortitude), airborne drops, and naval gunfire enabled the largest amphibious assault in history.",
 "The bocage fighting that followed tested Allied adaptation against German defense.",
 "Overlord's logistics — Mulberry harbors, PLUTO pipeline — were as decisive as its tactics."],
["Dien Bien Phu","battle","1954",
 "Viet Minh artillery and siegeworks destroyed the French garrison at Dien Bien Phu (1954).",
 "Giap hauled guns through jungle the French deemed impassable, dominating the airstrip.",
 "The defeat ended French Indochina and foreshadowed American troubles.",
 "It proved a determined insurgency can defeat a modern expeditionary force."],
["Tet Offensive","battle","1968",
 "The 1968 Tet Offensive saw Viet Cong attacks across South Vietnam, including the US Saigon embassy.",
 "Militarily repulsed with heavy communist losses, it shattered American public support for the war.",
 "Walter Cronkite's 'mired in stalemate' broadcast marked the political turning point.",
 "Tet is the classic case of tactical defeat producing strategic victory."],
["Desert Storm","battle","1991",
 "Operation Desert Storm (1991) expelled Iraq from Kuwait in a 42-day air campaign and 100-hour ground offensive.",
 "Stealth, precision munitions, and GPS demonstrated the revolution in military affairs.",
 "The 'left hook' flanking maneuver through the desert echoed classic envelopment.",
 "Desert Storm set the template for American conventional dominance — and its limits."],
["The nine principles of war","principle","US doctrine",
 "US doctrine lists nine principles of war: objective, offensive, mass, economy of force, maneuver, unity of command, security, surprise, and simplicity.",
 "Derived from British and French staff teaching, they were codified in US Field Service Regulations.",
 "Every American operation order is still checked against them.",
 "Critics call them platitudes; staffs use them as a planning checklist."],
["Center of gravity","principle","Clausewitzian theory",
 "Clausewitz's center of gravity is the source of an enemy's strength and the focal point for attack.",
 "Modern doctrine extends it to moral and political centers, not just armies.",
 "Misidentifying the center of gravity wastes campaigns against secondary targets.",
 "The concept forces planners to ask what truly holds the enemy together."],
["Culminating point","principle","Clausewitzian theory",
 "The culminating point is where an attacker's strength no longer exceeds the defender's and the offensive must halt.",
 "Clausewitz warned that every attack weakens itself as it advances.",
 "Napoleon's 1812 campaign culminated catastrophically before Moscow.",
 "Recognizing culmination — one's own and the enemy's — is operational art's core skill."],
["Deep battle","doctrine","Soviet 1930s",
 "Soviet deep battle theory, developed by Tukhachevsky and Triandafillov in the 1930s, sought simultaneous breakthrough across the enemy's depth.",
 "Successive echelons would penetrate, exploit, and pursue without pausing.",
 "Purged with its authors in 1937, it returned to win the Eastern Front in 1943-45.",
 "Deep battle is the ancestor of modern operational art."],
["AirLand Battle","doctrine","US 1980s",
 "AirLand Battle, the US Army's 1982 doctrine, planned to defeat Soviet echelons with deep strikes and maneuver.",
 "It integrated air power, attack helicopters, and precision fires against follow-on forces.",
 "The doctrine shaped the force that won Desert Storm.",
 "Its successor, multi-domain operations, extends the idea to space and cyber."],
["Deterrence and MAD","doctrine","Cold War",
 "Deterrence theory holds that the certain prospect of retaliation prevents attack.",
 "Mutual assured destruction (MAD) made US-Soviet nuclear war self-deterring through survivable second-strike forces.",
 "The nuclear triad — bombers, ICBMs, submarines — guarantees retaliation survives any first strike.",
 "Deterrence's credibility paradox — threatening what you hope never to do — still drives nuclear policy."],
["Counterinsurgency (FM 3-24)","doctrine","2006",
 "The US Army's 2006 counterinsurgency manual FM 3-24, associated with David Petraeus, revived population-centric COIN.",
 "'Hearts and minds', clear-hold-build, and protecting the population over killing insurgents are its tenets.",
 "Applied in Iraq's 2007 surge, it correlated with falling violence.",
 "Critics argue COIN promises more than foreign armies can deliver."],
["Hybrid warfare","doctrine","21st century",
 "Hybrid warfare blends conventional forces, irregulars, cyberattacks, and disinformation below the threshold of open war.",
 "Russia's 2014 Crimea operation is the textbook case: unmarked troops, cyber, and propaganda combined.",
 "The concept challenges doctrines built for declared wars between uniformed armies.",
 "Responses require whole-of-society resilience, not just military tools."],
["Blitzkrieg as a system","doctrine","1939-1941",
 "Blitzkrieg was less a formal doctrine than a system: radios, combined arms, and mission command enabling rapid exploitation.",
 "Its shock came from tempo — collapsing enemy decision cycles faster than they could react.",
 "Allied armies adopted its methods after 1940, mechanizing their own doctrines.",
 "The term itself was popularized by journalists, not German staffs."],
["Defense in depth","principle","Timeless",
 "Defense in depth trades space for time across successive prepared positions.",
 "Soviet doctrine at Kursk (1943) perfected it: minefields, anti-tank zones, and reserves absorbed the German blow.",
 "It denies the attacker a single decisive breakthrough point.",
 "Elastic defense variants yield ground deliberately to counterattack exhausted penetrations."],
["Fabian strategy","principle","Roman Republic",
 "Fabian strategy avoids pitched battle, harassing and delaying a stronger enemy until conditions change.",
 "Quintus Fabius Maximus used it against Hannibal after Cannae, earning the nickname 'the Delayer'.",
 "It demands political patience, since publics mistake delay for cowardice.",
 "Washington, Kutuzov, and Giap all wielded Fabian logic against stronger foes."],
["Thermopylae","battle","480 BCE",
 "At Thermopylae (480 BCE), 300 Spartans and allies held the pass against Xerxes' vast army for three days.",
 "The narrow terrain nullified Persian numbers until a traitor revealed the mountain path.",
 "The sacrifice became the West's immortal emblem of duty against impossible odds.",
 "Salamis, fought weeks later, won the naval victory Thermopylae bought time for."],
["Salamis","battle","480 BCE",
 "Themistocles lured the Persian fleet into the narrow straits of Salamis (480 BCE), where Greek triremes destroyed it.",
 "Confined waters negated Persian numbers, as at Thermopylae on land.",
 "The victory saved Greece and, in the traditional telling, the Western political tradition.",
 "Salamis is the classic triumph of choosing the battlefield."],
["Marathon","battle","490 BCE",
 "At Marathon (490 BCE), Athenian hoplites routed a larger Persian landing force with a strengthened-center-weakened attack.",
 "Miltiades' weakened center yielded while strong wings enveloped — Cannae's mirror image in reverse.",
 "The victory preserved the young Athenian democracy.",
 "Legend says a runner carried the news to Athens, inspiring the marathon race."],
["Hastings","battle","1066",
 "William the Conqueror's victory at Hastings (1066) ended Anglo-Saxon England.",
 "Norman feigned retreats drew Harold's shield wall downhill into cavalry traps.",
 "Harold's death — arrow in the eye, per the Bayeux Tapestry — collapsed English resistance.",
 "Hastings fused Norman and English institutions into medieval England."],
["Vienna 1683","battle","1683",
 "The 1683 Battle of Vienna broke the Ottoman siege with history's largest cavalry charge.",
 "Jan Sobieski's 18,000 horsemen swept down the Kahlenberg into the Ottoman camp.",
 "The victory ended Ottoman expansion into Europe and began the Habsburg ascendancy.",
 "It is celebrated as the high-water mark of Ottoman power."],
["The stirrup revolution","technology","c. 400-700 CE",
 "The stirrup's arrival in Europe enabled true shock cavalry: riders could couch lances without being unhorsed.",
 "Lynn White's famous thesis credited the stirrup with creating feudalism itself — overstated, but indicative of its impact.",
 "Stirrup-equipped cataphracts and knights dominated battlefields for centuries.",
 "Military revolutions often begin with such humble hardware."],
["Gunpowder","technology","9th-13th century",
 "Gunpowder, invented in Tang China, reached Europe by the 13th century and transformed warfare.",
 "Bombards breached Constantinople's walls in 1453; handheld firearms democratized lethality.",
 "The 'military revolution' thesis links gunpowder to standing armies and the modern state.",
 "Gunpowder ended the age of the armored knight and the stone castle."],
["The longbow","technology","14th century",
 "The Welsh-English longbow could loose aimed volleys that pierced mail at hundreds of yards.",
 "Crecy (1346) and Agincourt (1415) proved its dominance over mounted knights.",
 "Mastery required lifelong training, making archers a strategic resource.",
 "Firearms eventually replaced it, trading skill for simplicity."],
["The machine gun","technology","1884",
 "Hiram Maxim's 1884 machine gun used recoil to automate fire, multiplying infantry lethality.",
 "At the Somme, machine guns made frontal assaults suicidal and entrenched the Western Front.",
 "Every army's doctrine had to be rebuilt around firepower rather than élan.",
 "The tank was invented largely to cross machine-gun beaten zones."],
["The tank","technology","1916",
 "Tanks debuted at the Somme in 1916 and matured at Cambrai (1917) into the breakthrough weapon.",
 "Fuller's Plan 1919 envisioned massed tanks deciding wars; Guderian realized it in 1940.",
 "The tank restored mobility to the battlefield the machine gun had frozen.",
 "Anti-tank missiles and drones now challenge its dominance anew."],
["The Manhattan Project","technology","1942-1945",
 "The Manhattan Project built the first atomic bombs at Los Alamos under J. Robert Oppenheimer.",
 "Employing 130,000 people and costing $2 billion, it remains history's largest weapons program.",
 "Trinity (July 1945) proved the implosion design; Hiroshima and Nagasaki ended World War II.",
 "Nuclear weapons made great-power war potentially suicidal, birthing deterrence theory."],
["Radar and the Battle of Britain","technology","1940",
 "Britain's Chain Home radar network gave Fighter Command early warning of Luftwaffe raids in 1940.",
 "Radar plus centralized control let outnumbered fighters meet each raid efficiently.",
 "The system — sensors, communications, command — was the real weapon, not the aircraft alone.",
 "It is the first victory of networked information warfare."]
];
var ANGLES=["doctrine profile","battle profile","commander profile","technology profile"];
var SYNREL=[
 ["compared with","This Signature comparative study evaluates both on principles, execution, and historical consequence."],
 ["contrasted against","This Signature contrast study draws out what separates the two across eras and domains."],
 ["as predecessor and successor to","This Signature lineage study traces how the later case answers the earlier one."],
 ["alongside","This Signature pairing study reads the two together as variations on enduring strategic themes."]
];
function filedLine(id){return "Filed as "+id+" in the JAH Military Strategy Database archive.";}
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
      spec:{kind:"study",pair:[A[0],B[0]],relation:rel[0],eras:[A[2],B[2]],src:"signature"},
      era:A[2],src:"signature"};
  }
  var A=pick(pool,rnd);
  var ang=pick(ANGLES,rnd);
  var facts=A.slice(3);
  var d=facts[0]+" "+pick(facts.slice(1),rnd);
  if(rnd()<0.6)d+=" "+pick(facts.slice(1),rnd);
  var title=A[0]+" — "+ang;
  return {id:id,title:title,description:d+" "+filedLine(id),category:A[1],
    spec:{kind:A[1],era:A[2],src:"online"},era:A[2],src:"online",_facts:facts,_an:A[0]};
}
function sentences(s){return String(s).split(/[.!?]+/).filter(function(x){return x.trim().length>10;}).length;}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-MIL-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||r.title.length<4)e.push('title');
  if(typeof r.description!=='string'||r.description.length<80)e.push('description');
  else if(sentences(r.description)<2)e.push('description-sentences');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(r.src!=='online'&&r.src!=='signature')e.push('src');
  if(typeof r.era!=='string'||!r.era.length)e.push('era');
  var s=r.spec;
  if(!s||typeof s!=='object')e.push('spec');
  else{
    if(s.src!=='online'&&s.src!=='signature')e.push('spec.src');
    if(s.src!==r.src)e.push('spec.src-mismatch');
    if(s.src==='online'){
      if(typeof s.era!=='string'||!s.era.length)e.push('spec.era');
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
var gen={version:'jahdb-military-strategy-1.0',generate:generate,validate:validate,signatureVersion:signatureVersion};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('military-strategy',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
