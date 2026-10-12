/* JAH Comics Database — full 22-page issue renderer (on-demand).
   Byte-identical with make_comics_full.py: same mulberry32, same pools
   (embedded from pools.json at build time), same draw order.
   Exposes JAHComicsFull.fullRecord(idxRow) -> complete 22-page record. */
(function () {
'use strict';
var POOLS = {"_note": "Single source of truth for the 22-page full-issue expansion. Pools copied verbatim from signature-comics/code/make_comics.py and make_events.py. Beat templates are original Signature inventions.", "seed2": 20261012, "beats": ["cover", "hook", "setup", "inciting", "complication", "debate", "escalation", "setback", "midpoint", "fallout", "strike", "all-is-lost", "dark-night", "rally", "plan", "infiltration", "climax", "final-blow", "aftermath", "denouement", "tag", "next"], "scene_a_beats": ["cover", "hook", "setup", "inciting", "complication", "debate", "escalation", "rally", "plan", "infiltration", "climax", "final-blow", "aftermath", "denouement", "tag", "next"], "dlg_prob": {"cover": 1.0, "hook": 0.8, "setup": 0.8, "inciting": 0.75, "complication": 0.7, "debate": 0.9, "escalation": 0.65, "setback": 0.7, "midpoint": 0.85, "fallout": 0.7, "strike": 0.6, "all-is-lost": 0.8, "dark-night": 0.9, "rally": 0.9, "plan": 0.9, "infiltration": 0.5, "climax": 0.7, "final-blow": 0.8, "aftermath": 0.6, "denouement": 0.8, "tag": 0.9, "next": 0.5}, "speakers": {"cover": ["none"], "midpoint": ["hero", "ally", "villain"], "strike": ["hero", "ally", "villain"], "final-blow": ["hero", "ally", "villain"], "all-is-lost": ["hero", "ally", "villain"]}, "caps": {"cover": ["COVER — {title}: {hero} {bursts|races|soars} across a {adj} {sky} above {place}, {power} blazing.", "COVER — {title}: {hero} and {ally} stand back-to-back as {villain}'s shadow falls over {scene}.", "COVER — {title}: the {artifact} burns {adj} and bright in {hero}'s hand above {place}.", "COVER — {title}: {foe_desc} looms over {place} — and {hero} is already {moving}."], "hook": ["{hero} {races|hurries|streaks} toward {scene}, {power} flaring.", "The call comes at {time}: {scene} needs {hero}.", "{time} over {place} — and {hero} is already {moving}.", "{ally} spots it first: {signs}, at the edge of {scene}."], "setup": ["{hero} and {ally} {walk|patrol|drift} the length of {scene}, {power2} and {power3} at the ready.", "In {place}, the {nouns} are {restless|quiet|wrong} tonight — {ally} can feel it.", "{hero} checks the {artifact}: {num2} {nouns} and counting, all wrong.", "Old {reveal} in hand, {ally} {traces|reads|follows} the signs back toward {scene}."], "inciting": ["It starts with {signs} — then {scene} goes {silent|dark|still}.", "{foe_desc} steps out of the {nouns} — {villain} has come to {place}.", "The {artifact} {shatters|cracks|dims} in {hero}'s grip. That has never happened before.", "{ally}'s {power3} flares on its own: something vast is {moving} beneath {scene}."], "complication": ["The way to {scene} is {blocked|gone|wrong} — {villain}'s work, plain as {signs}.", "{hero}'s {power} {flickers|falters|stutters} at the worst possible moment.", "{ally} finds the {reveal}: a message, {num2} {years} old, addressed to {hero}.", "Half the {nouns} of {place} are already {gone|dark|silent}. The rest are {waiting|afraid|next}."], "debate": ["{hero} {paces|stalls|hesitates} — the cost of facing {villain} is written in {signs}.", "{ally} lays it out: {place} {burns|falls|suffers}, or they {risk|spend|burn} everything on one {throw|play|shot}.", "The {artifact} shows two futures. {hero} {hates|fears|loves} them both.", "{time} is {running|bleeding|gone}. {villain} is not waiting for an answer."], "escalation": ["{hero} {pushes|digs deep|rallies}, {power2} answering the call across {scene}.", "{ally} {meets|matches|outruns} the {foe_desc} {blow|rush|trick} for {blow|rush|trick}.", "The {sky} over {place} {burns|shakes|sings} as {power4} collides with {power}.", "{villain}'s {nouns} {pour|march|crawl} through {scene} — too many to count."], "setback": ["The {artifact} goes {dark|cold|silent} in {hero}'s hand. {signs} everywhere.", "{ally} goes down under the {foe_desc}'s {weight} — {hero} {catches|reaches|dives}, too slow.", "{villain} {takes|claims|steals} the {noun2} — {place} {dims|shudders|weeps}.", "Across {scene}, the {nouns} {turn|fall|break}. This is the part where heroes lose."], "midpoint": ["A {reveal} changes everything {hero} believed about {place}.", "\"{truth}\" — {villain}'s words land like {weight}.", "The {artifact} was never the prize. {hero} understands at last.", "{ally} sees it too: {villain} isn't {attacking|invading|stealing} — {villain} is {running|hiding|mourning}."], "fallout": ["{hero} {reels|stumbles|falls} back — the {truth} still {ringing|burning|echoing}.", "{scene} looks {different|smaller|wrong} now. {ally} won't meet {hero}'s eyes.", "The {artifact} {pulses|dims|shatters} with new meaning. {num2} {nouns}, all {wrong|right|different}.", "{villain} is gone — {vanished|withdrawn|waiting} — and {place} holds its breath."], "strike": ["{villain} {strikes|returns|answers} at {time} — {scene} {burns|shakes|sings}.", "The {foe_desc} {takes|seizes|shatters} the {artifact} and {turns|aims|levels} it at {place}.", "{ally}'s warning comes too late: {signs}, then {darkness|silence|static}.", "{hero} {takes|catches|blocks} the blow meant for {ally} — {power} {screaming|flaring|breaking}."], "all-is-lost": ["{hero} is down. The {artifact} is {gone|dark|broken}. {scene} is {villain}'s now.", "{ally} {drags|carries|shields} {hero} through the {nouns}, {power3} barely a {spark|whisper|ember}.", "Over {place}, the {sky} goes {dark|still|wrong}. {years} of {light|hope|work}, {gone|spent|lost}.", "{villain} stands over the {noun2}, {victorious|patient|waiting} — and {monologuing|laughing|silent}."], "dark-night": ["In the {quiet|dark|still} after, {ally} {binds|mends|wakes} {hero}'s {power} with {power3}.", "{hero} remembers the {reveal} — and {truth} — and something {shifts|clicks|ignites}.", "Beneath {scene}, the old {nouns} {stir|wake|listen}. {place} is not done yet.", "{time} passes. {hero} {sleeps|dreams|burns}, and {ally} keeps watch over {place}."], "rally": ["{hero} rises — {power} {steadier|brighter|truer} than before — and {ally} {grins|nods|laughs}.", "\"{closer}\" {hero} says, and {scene} itself seems to {listen|lean|answer}.", "The {artifact} {reignites|remakes|returns}, {num2} {nouns} {singing|burning|aligned}.", "Across {place}, the {nouns} {rise|turn|gather}. Hope is {contagious|loud|stubborn}."], "plan": ["{ally} sketches it in {light|dust|signal}: {hero} {takes|draws|holds} {villain}'s {eye|ire|focus} while {ally} {takes|finds|frees} the {noun2}.", "The {artifact} needs {num2} {seconds|heartbeats|breaths} to {charge|wake|sing}. {hero} will buy them.", "{power} plus {power3}, {braided|stacked|woven} through the {artifact} — {ally}'s {math|hunch|plan} is {mad|perfect|both}.", "{scene} mapped, {signs} marked, {villain}'s {pattern|habit|tell} {found|learned|known}. Go."], "infiltration": ["{hero} {ghosts|slips|strides} through {scene}, {power} {low|quiet|coiled}.", "{ally} {takes|finds|opens} the {back|side|third} way — {signs} {covered|dodged|ignored}.", "The {foe_desc} {passes|sleeps|waits} {inches|heartbeats|breaths} away. Nobody breathes.", "{num2} {steps|locks|wards} to the {noun2}. {num2} {steps|locks|wards} too many."], "climax": ["{hero} and {ally} stand together as {scene} {burns|shakes|sings}.", "One final {exchange|charge|stand}: {power} against {power4}, and the {sky} holds its breath.", "{villain} {unleashes|becomes|reveals} the {foe_desc}'s full {might|truth|hunger}.", "The {artifact} {screams|sings|blazes} — {num2} {nouns} of pure {power}."], "final-blow": ["{hero} {leaps|dives|charges} — for {place}, for {ally}, for everything.", "{power} and {power3} {strike|land|connect} as one. {villain} {staggers|breaks|falls}.", "The {noun2} {flares|shatters|opens} — {light|truth|dawn} {pours|floods|breaks} over {scene}.", "{villain}'s last word is {truth} — then {silence|light|stillness}."], "aftermath": ["{scene} {smolders|settles|glows} — {hero} {counts|checks|finds} {ally} first, always.", "The {artifact} is {quiet|warm|changed}. {num2} {nouns} will tell this story.", "{place} {picks|dusts|pulls} itself up. {signs} of {villain}, {fading|gone|scattered}.", "{ally} {laughs|cries|sits} — the {loud|quiet|shaky} kind that means {alive|done|home}."], "denouement": ["Quiet, after. {scene} {heals|settles|glows} in the aftermath.", "{hero} looks to the {horizon}: \"{closer}\"", "In {place}, they will tell this story for {years}.", "The {artifact} {rests|waits|dreams} — until {place} needs it again."], "tag": ["{ally} finds one last {reveal} in the {rubble|quiet|signal} — {addressed|marked|meant} for {hero}.", "Far from {place}, {signs} — {villain}'s {nouns} are {moving|gathering|wrong} again.", "{hero} {pockets|keeps|hides} the {reveal}. Some {nouns} can wait.", "The {horizon} {darkens|brightens|shifts}. {time} will tell."], "next": ["NEXT: {adj} {nouns} over {place} — {hero} returns!", "NEXT: {villain}'s {nouns} {gather|stir|rise} — and {place} {burns|calls|waits}!", "NEXT: the {artifact} {chooses|calls|warns} — {ally}'s {noun2}, {hero}'s {burden|promise|fight}!", "NEXT: {num2} {nouns}. One {reveal}. Zero {mercy|sleep|second chances}."]}, "dlgs": {"cover": ["\"{quips}\"", "\"{truth}.\"", "\"Every {noun2} has its {nouns}. This one is ours.\"", "\"{place} {burns|shakes|sings} — and so do we.\""], "hook": ["\"{quips}\"", "\"{place} first. Everything else later.\"", "\"Did you feel that? The {artifact} just {pulsed|dimmed|sang}.\"", "\"{villain} can't have gone far. Look for {signs}.\""], "setup": ["\"Remind me why we {volunteered|drew the short straw|always say yes}.\"", "\"{place} is counting on us. No pressure.\"", "\"You brought the {artifact}? Good. We'll need it.\"", "\"Stay sharp. {villain} {loves|adores|collects} quiet {time}s like this.\""], "inciting": ["\"That is new. That is definitely new.\"", "\"{hero} — the {scene}! Now!\"", "\"Everybody in {place} just felt that. We don't have long.\"", "\"{villain}. Of course it's {villain}.\""], "complication": ["\"Forget the {nouns} we drew up. New plan.\"", "\"We go {over|under|through}. Pick one fast.\"", "\"{villain} knew we'd come. {villain} always knows.\"", "\"Then we do it the loud way.\""], "debate": ["\"We can't. We have to. Pick one, {hero}.\"", "\"{truth}. You know I'm right.\"", "\"{place} first. Everything else later — including our doubts.\"", "\"On three. One... two...\""], "escalation": ["\"Is that all? I've {seen|eaten|outrun} worse {time}s!\"", "\"{ally}, the {artifact} — throw it!\"", "\"They just keep coming!\"", "\"{quips}\""], "setback": ["\"{ally}! Talk to me!\"", "\"No no no — not the {noun2}!\"", "\"Fall back! Everybody fall back!\"", "\"That... that actually hurt.\""], "midpoint": ["\"You still don't see it, do you? {truth}.\"", "\"{hero}. {ally}. {place} was never yours to save.\"", "\"Look at the {artifact}. Really look.\"", "\"We were never the {nouns} you feared. We were the {warning|message|answer}.\""], "fallout": ["\"Tell me we misheard. Somebody tell me we misheard.\"", "\"Everything we knew about {place}... was {backwards|incomplete|a lie}.\"", "\"So what do we do now?\"", "\"We finish it. Differently.\""], "strike": ["\"You should have {run|hidden|listened}, little {nouns}.\"", "\"{place} {burns|falls|breaks} tonight!\"", "\"The {noun2} is MINE.\"", "\"{hero}! Behind you!\""], "all-is-lost": ["\"Get up. GET UP. {place} needs you.\"", "\"It's over, {hero}. It's over.\"", "\"{closer}\"", "\"One more {push|try|breath}. For {place}.\""], "dark-night": ["\"{truth}. That is the answer. That has always been the answer.\"", "\"The {artifact} isn't {gone|dead|lost}. It's {waiting|hiding|choosing}.\"", "\"{villain} {took|broke|stole} everything except the one thing that matters.\"", "\"{quips}\""], "rally": ["\"{closer}\"", "\"{villain} took our {noun2}. Let's go take it back.\"", "\"{place} first. Everything else later. Starting now.\"", "\"Try keeping up.\""], "plan": ["\"You sure about the {math|timing|part where I almost die}?\"", "\"{Sixty|Seventy} percent. Don't ask about the rest.\"", "\"On my mark. Not before.\"", "\"{hero} — whatever happens — {place} first.\""], "infiltration": ["\"...almost...\"", "\"Eyes up. {villain}'s {nouns} are {everywhere|restless|close}.\"", "\"The {artifact}'s {awake|warm|ready}.\"", "\"Quiet. {signs}, {inches|breaths} away.\""], "climax": ["\"{place} is OURS, {villain}!\"", "\"Now, {ally}! NOW!\"", "\"{quips}\"", "\"For {place}! For every {noun2}!\""], "final-blow": ["\"{truth}!\"", "\"This ends {tonight|now|here}, {villain}!\"", "\"...{closer}...\"", "\"Got you.\""], "aftermath": ["\"We {did|made|kept} it.\"", "\"{place} first. {place} always.\"", "\"Don't ever {scare|do that to|leave} me like that again.\"", "\"{quips}\""], "denouement": ["\"{closer}\"", "\"Same time tomorrow?\"", "\"The {light|signal|tide} holds.\"", "\"Tell it true.\""], "tag": ["\"You should see this.\"", "\"{hero}... we need to talk.\"", "\"It's {starting|not over|bigger} — isn't it?\"", "\"{quips}\""], "next": ["\"You thought THIS was the {fight|storm|story}?\"", "\"{place} isn't done with us yet.\"", "\"To be continued...\"", "\"{quips}\""]}, "settings": {"signal": ["the Signal Spire", "orbit above Velnara", "the Quiet Array", "the Shattered Relay", "deep orbit", "the Beacon Fields"], "ember": ["the Ashen Vale", "Cinderhold Keep", "the Frostpine Reach", "the Ember Road", "the Hollow Mountain", "Duskwater Fen"], "circuit": ["Neon Row", "the Undergrid", "Sector Nine rooftops", "the Data Docks", "Chrome Alley", "the Quiet Server"], "tide": ["the Coral Steps", "open water past Gullrest", "the Sunken Bell", "Tidewater Market", "the Drowned Library", "Skerry Light"], "gloam": ["Lantern Row", "the Fog Docks", "Blackbrick Lane", "the Gloaming Stair", "Hollow Square", "the Night Market"], "starlog": ["the helm of the Wayfarer", "orbit of the Pale Twins", "the Drift", "a nameless moon", "the Long Dark", "the Cartographer's Reef"], "clockwork": ["Gearheart Plaza", "the Brass Works", "Cogsworth Lane", "the Sky Dock", "the Tinker's Market", "Furnace Row"], "junior": ["Maple Street", "the Old Treehouse", "Sunnybrook Park", "the Library Steps", "Clover Field", "the Corner Store"]}, "places": {"signal": ["Velnara Prime", "the Accord", "Relay Nine"], "ember": ["Cinderhold", "the Vale Compact", "Frostpine"], "circuit": ["the Sprawl", "the Grid Council", "Sector Nine"], "tide": ["Gullrest", "the Harbor Compact", "Skerry Light"], "gloam": ["Gloam City", "the Lantern Guild", "Hollow Ward"], "starlog": ["the Wayfarer", "the Far Cartography", "Pale Twins"], "clockwork": ["Cogsworth", "the Brass Guild", "Gearheart"], "junior": ["Maple Street", "Sunnybrook", "the Treehouse Club"]}, "powers": {"signal": ["signal-jumping", "light-bending", "gravity anchoring", "echo-location pulses", "memory weaving", "star charting"], "ember": ["ember shaping", "flame warding", "stone singing", "beast speaking", "frost tracing", "wind riding"], "circuit": ["circuit diving", "hologram casting", "signal splicing", "machine listening", "ghost frequency tuning", "data weaving"], "tide": ["tide reading", "current riding", "deep listening", "storm weathering", "pearl diving", "whale singing"], "gloam": ["shadow listening", "thought sketching", "dust reading", "lantern guiding", "echo tracing", "fog walking"], "starlog": ["star charting", "void navigating", "signal decoding", "gravity slinging", "comet riding", "nebula mapping"], "clockwork": ["clockwork mending", "gear reading", "steam shaping", "brass singing", "automaton waking", "timepiece tuning"], "junior": ["bubble shielding", "giggle sparks", "puddle jumping", "kite riding", "marble rolling", "firefly guiding"]}, "cosmic_powers": ["automaton waking", "beast speaking", "brass singing", "bubble shielding", "circuit diving", "clockwork mending", "comet riding", "current riding", "data weaving", "deep listening", "dust reading", "echo tracing", "echo-location pulses", "ember shaping", "firefly guiding", "flame warding", "fog walking", "frost tracing", "gear reading", "ghost frequency tuning", "giggle sparks", "gravity anchoring", "gravity slinging", "hologram casting", "kite riding", "lantern guiding", "light-bending", "machine listening", "marble rolling", "memory weaving", "nebula mapping", "pearl diving", "puddle jumping", "shadow listening", "signal decoding", "signal splicing", "signal-jumping", "star charting", "steam shaping", "stone singing", "storm weathering", "thought sketching", "tide reading", "timepiece tuning", "void navigating", "whale singing", "wind riding"], "villains": ["the Quiet", "the Hollow King", "Madame Static", "the Rust Choir", "Captain Undertow", "the Pale Cartographer", "the Gear Thief", "Old Murk", "the Signal Eater", "the Brass Widow"], "foe_desc": ["a rusted automaton with one lit eye", "three figures in fog-grey coats", "a hollow signal wearing a person's voice", "a tide-beast tangled in chain", "a courier gone quiet, eyes like static", "the Brass Widow's clockwork crows"], "signs": ["scorch marks in a perfect ring", "footprints that stop mid-step", "a lantern burning cold blue", "gears laid out like a message", "silence where gulls should be", "frost on the inside of glass"], "quips": ["Try keeping up.", "The night is young.", "I brought the loud one.", "You rang?", "Maps are just suggestions.", "Hold my lantern."], "truths": ["We were the storm all along", "The beacon was calling us home", "The map was drawn backwards", "The enemy kept our summers", "Every ending is a relay", "The quiet ones were listening"], "closers": ["Same time tomorrow.", "The light holds.", "Tell it true.", "Keep the signal lit.", "The tide always returns.", "Wind it tight."], "reveals": ["old map", "cracked lens", "folded letter", "rusted key", "tide-worn coin", "brass feather"], "weights": ["a dropped anchor", "a closing door", "a struck bell", "a snapped string"], "times": ["first light", "the blue hour", "midnight", "low tide", "shift change"], "moving": ["mid-stride", "already moving", "laughing into the wind", "three steps ahead", "exactly on time"], "adj": ["Silent", "Burning", "Hollow", "Bright", "Long", "Last", "First", "Hidden", "Wild", "Gentle", "Iron", "Paper", "Copper", "Velvet", "Amber", "Indigo", "Crimson", "Pale", "Restless", "Patient"], "nouns": ["Embers", "Tides", "Gears", "Signals", "Lanterns", "Echoes", "Storms", "Keys", "Maps", "Bells", "Bridges", "Stars"], "noun2": ["Beacon", "Oath", "Key", "Map", "Bell", "Engine", "Lantern", "Compass", "Signal", "Bridge", "Chart", "Relay"], "skies": ["sky", "sea", "city", "vale"], "horizons": ["horizon", "tide line", "rooftops", "treeline", "stars"], "years": ["a hundred years", "seven winters", "a generation", "a long age"], "artifacts": ["ember-lantern", "signal relay", "brass compass", "tide bell", "ghost tuner", "star chart", "cog heart", "fog lantern", "relay coil", "wayfinder's lens"], "series_flavor": {"signal": "A team of cosmic guardians keeps the beacon-network of the far colonies lit — and something out in the dark keeps trying to snuff it.", "ember": "In a valley of ash and frost, young wardens carry living ember-flames between the last warm holds of the Vale.", "circuit": "Neon-row couriers who dive the city's ghost frequencies discover a signal that was never meant to be heard.", "tide": "Harbor kids and old sailors bound by tide-oaths guard the sea-roads between Gullrest and the drowned places.", "gloam": "Lantern-keepers patrol the fog city after dark, solving the small strange mysteries the daylight misses.", "starlog": "An anthology of voyages: the survey ship Wayfarer charts the far dark, one strange world per issue.", "clockwork": "Tinkerers and their brass automatons keep the gear-city wound — and someone keeps loosening the springs.", "junior": "The Maple Street kids and their treehouse club: small heroes, big heart, everyday wonders."}, "series_names": {"signal": "THE SIGNALBEARERS", "ember": "EMBERFALL", "circuit": "THE HOLLOW CIRCUIT", "tide": "TIDEBOUND", "gloam": "THE GLOAMING WATCH", "starlog": "STARFARER'S LOG", "clockwork": "THE CLOCKWORK MENAGERIE", "junior": "JUNIOR SIGNALS"}, "events": [{"key": "amalthea", "name": "SIEGE OF AMALTHEA", "desc": "The Unmaking comes for Jupiter's first moon — and every hero answers.", "villain": "THE UNMAKING", "foe": "an entropy storm wearing a crown of dead stars", "scenes": ["the rust-red plains of Amalthea", "beneath Jupiter's looming eye", "the crater of First Landing", "the ice caves of Amalthea", "the shattered muster-field", "the long shadow of the gas giant"], "places": ["Amalthea", "the Jovian muster", "First Landing"]}, {"key": "saurian", "name": "WAR IN THE SAURIAN DAWN", "desc": "The Maw of Eons hunts through deep time — the heroes follow it down.", "villain": "THE MAW OF EONS", "foe": "a devourer of eras with teeth like epochs", "scenes": ["the fern-choked valleys", "beneath the thunder-lizards' feet", "the tar-seep flats", "the nesting grounds", "the ash-fall ridges", "the inland sea at dusk"], "places": ["the Saurian Dawn", "Old Pangaea", "the Nesting Grounds"]}, {"key": "farfallen", "name": "THE FARFALLEN CENTURY", "desc": "In the 31st century, the Pale Extinction returns — and legends wake.", "villain": "THE PALE EXTINCTION", "foe": "a white silence that unmakes memory itself", "scenes": ["the spire-cities of the 31st century", "the rust deserts of old Earth", "orbit above the museum-world", "the last library satellite", "the memorial fields", "the dawn vaults"], "places": ["the 31st century", "Museum-Earth", "the Last Library"]}, {"key": "collapse", "name": "WHEN TIMELINES COLLAPSE", "desc": "Every when is falling into every other when — the Null-King reigns the wreckage.", "villain": "THE NULL-KING", "foe": "a king of the collapsed timeline, crowned in stopped clocks", "scenes": ["the shattering timestream", "between the seconds", "the crossroads of eras", "the unraveling now", "the museum of lost tomorrows", "the still point"], "places": ["the Timestream", "the Crossroads", "everywhen"]}], "gen_note": "An original generated comic created by the Signature system. All characters, places, and events are invented."};
var SEED2 = POOLS.seed2, BEATS = POOLS.beats, GEN_NOTE = POOLS.gen_note;
var EMDASH = '—';

function m32(seed) {
  var a = seed | 0;
  return function () {
    a = a + 0x6D2B79F5 | 0;
    var t = Math.imul(a ^ a >>> 15, 1 | a);
    t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
    return ((t ^ t >>> 14) >>> 0) / 4294967296;
  };
}
function pick(rnd, arr) { return arr[Math.floor(rnd() * arr.length)]; }
function num(rnd, a, b) { return a + Math.floor(rnd() * (b - a + 1)); }
function wordCount(s) { return s.trim() === '' ? 0 : s.trim().split(/\s+/).length; }

function fill(rnd, tpl, ctx) {
  var t = tpl.replace(/\{([^{}]*\|[^{}]*)\}/g, function (m, g) {
    return pick(rnd, g.split('|'));
  });
  t = t.replace(/\{([A-Za-z0-9_]+)\}/g, function (m, k) {
    return (k in ctx) ? String(ctx[k]) : m;
  });
  t = t.split('The the ').join('The ').split('the the ').join('the ');
  return t;
}

function evByKey(key) {
  for (var i = 0; i < POOLS.events.length; i++)
    if (POOLS.events[i].key === key) return POOLS.events[i];
  throw new Error('unknown event key: ' + key);
}

function expandIssue(i, skey, hero, ally, title, evKey) {
  var rnd = m32(SEED2 + i);
  var isEvent = (skey === 'event');
  var ev = isEvent ? evByKey(evKey) : null;
  var settings = isEvent ? ev.scenes : POOLS.settings[skey];
  var places = isEvent ? ev.places : POOLS.places[skey];
  var powersPool = isEvent ? POOLS.cosmic_powers : POOLS.powers[skey];

  /* upfront ctx draws: FIXED ORDER (mirrors Python) */
  var sceneA = pick(rnd, settings);
  var sceneB = pick(rnd, settings);
  var place = pick(rnd, places);
  var villain = isEvent ? ev.villain : pick(rnd, POOLS.villains);
  var foe = isEvent ? ev.foe : pick(rnd, POOLS.foe_desc);
  var artifact = pick(rnd, POOLS.artifacts);
  var signs = pick(rnd, POOLS.signs);
  var quips = pick(rnd, POOLS.quips);
  var truth = pick(rnd, POOLS.truths);
  var closer = pick(rnd, POOLS.closers);
  var reveal = pick(rnd, POOLS.reveals);
  var weight = pick(rnd, POOLS.weights);
  var time = pick(rnd, POOLS.times);
  var moving = pick(rnd, POOLS.moving);
  var adj = pick(rnd, POOLS.adj);
  var nouns = pick(rnd, POOLS.nouns);
  var noun2 = pick(rnd, POOLS.noun2);
  var sky = pick(rnd, POOLS.skies);
  var horizon = pick(rnd, POOLS.horizons);
  var years = pick(rnd, POOLS.years);
  var num2 = String(num(rnd, 100, 999));
  var power4 = pick(rnd, powersPool);

  var sceneASet = {};
  POOLS.scene_a_beats.forEach(function (b) { sceneASet[b] = 1; });
  var pages = [];
  for (var bi = 0; bi < BEATS.length; bi++) {
    var beat = BEATS[bi];
    var scene = sceneASet[beat] ? sceneA : sceneB;
    var ctx = {
      hero: hero.code, ally: ally.code, villain: villain,
      scene: scene, place: place,
      power: hero.power, power2: hero.power,
      power3: ally.power, power4: power4,
      artifact: artifact, foe_desc: foe,
      signs: signs, quips: quips, truth: truth,
      closer: closer, reveal: reveal, weight: weight,
      time: time, moving: moving, adj: adj, nouns: nouns,
      noun2: noun2, sky: sky, horizon: horizon,
      years: years, num2: num2, title: title,
      evname: isEvent ? ev.name : ''
    };
    var cap = fill(rnd, pick(rnd, POOLS.caps[beat]), ctx);
    var dlg = '', who = '';
    if (rnd() < POOLS.dlg_prob[beat]) {
      var speakers = POOLS.speakers[beat] || ['hero', 'ally'];
      var sp = pick(rnd, speakers);
      if (sp === 'none') who = '';
      else if (sp === 'villain') who = villain;
      else if (sp === 'ally') who = ally.code;
      else who = hero.code;
      dlg = fill(rnd, pick(rnd, POOLS.dlgs[beat]), ctx);
    }
    pages.push({ cap: cap, dlg: dlg, who: who, scene: scene, beat: beat });
  }
  return pages;
}

function starring(chars) {
  return chars.map(function (c) { return c.code + ' (' + c.name + ')'; }).join(', ');
}

function buildDesc(skey, series, num, title, chars, hookCap, evKey) {
  var star = starring(chars);
  if (skey === 'event') {
    var ev = evByKey(evKey);
    var part = (num - 1) % 6 + 1;
    return ev.name + ' ' + EMDASH + ' Part ' + part + ' of ' + ev.name + '. ' +
           ev.desc + ' Starring ' + star + '. ' + hookCap;
  }
  return series + ' #' + num + ' ' + EMDASH + ' ' + title + '. ' + hookCap +
         ' Starring ' + star + '. ' + POOLS.series_flavor[skey];
}

/* Build the complete 22-page record from a compact idx row (on-demand path). */
function fullRecord(r) {
  var i = parseInt(String(r.id).slice(10), 10);
  var chars = r.ch.map(function (c) { return { name: c.name, code: c.code, power: c.power }; });
  var hero = chars[0], ally = chars.length > 1 ? chars[1] : chars[0];
  var pages = expandIssue(i, r.sk, hero, ally, r.t, r.ev || null);
  var desc = buildDesc(r.sk, r.s, r.n, r.t, chars, pages[1].cap, r.ev || null);
  var words = 0, k;
  for (k = 0; k < pages.length; k++)
    words += wordCount(pages[k].cap) + wordCount(pages[k].dlg);
  var rec = {
    id: r.id, series: r.s, skey: r.sk, num: r.n, title: r.t,
    chars: chars, desc: desc, pages: pages, words: words,
    note: GEN_NOTE + (r.sk === 'event' ? ' Cosmic crossover event issue.' : ''),
    creation_mode: 'GENERATED', src: 'signature'
  };
  if (r.ev) rec.event = r.ev;
  return rec;
}

var api = { expandIssue: expandIssue, buildDesc: buildDesc, fullRecord: fullRecord, m32: m32 };
if (typeof module !== 'undefined' && module.exports) module.exports = api;
if (typeof window !== 'undefined') window.JAHComicsFull = api;
})();
