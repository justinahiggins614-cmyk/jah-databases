(function(){'use strict';
/* EXPANSION 2026-10-18 group-1: archive-shape branches added. */
/* JAH The Personality Database generator — jahdb-personality-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRSL-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Personality Is - Foundations",
  "Traits, States, and Types - Foundations",
  "The Big Five at a Glance - Foundations",
  "Openness to Experience - Foundations",
  "Conscientiousness: The Big Five Discipline Domain - Foundations",
  "Extraversion: The Big Five Energy Domain - Foundations",
  "Agreeableness: The Big Five Warmth Domain - Foundations",
  "Emotional Stability and Neuroticism - Foundations",
  "The HEXACO Model - Foundations",
  "Honesty-Humility - Foundations",
  "Facets: The Six Faces of Every Domain - Foundations",
  "Self-Reports, Observer Ratings, and Bias - Foundations",
  "Nature, Nurture, and the Sources of Traits - Foundations"
 ],
 "Compounded": [
  "The Sixteen Types of Jung and Myers-Briggs - Compounded",
  "Introversion, Extraversion, and Ambiversion in Daily Life - Compounded",
  "The Enneagram: Nine Motivational Patterns - Compounded",
  "DISC: Four Behavioral Styles - Compounded",
  "The Four Temperaments - Compounded",
  "The Sixteen Personality Factors - Compounded",
  "How Traits Combine: Reading a Full Profile - Compounded",
  "Personality at Work - Compounded",
  "Personality in Relationships - Compounded",
  "Measuring Personality: Reliability and Validity - Compounded",
  "The Person-Situation Debate - Compounded",
  "Team Chemistry: Traits in Groups - Compounded"
 ],
 "Advanced": [
  "Trait Stability and Change Across the Lifespan - Advanced",
  "Personality Development: The Maturity Principle - Advanced",
  "Personality and Decision-Making - Advanced",
  "Reading Others Ethically - Advanced",
  "Personality and Leadership - Advanced",
  "Personality Across Cultures - Advanced",
  "Conflict Styles and Personality - Advanced",
  "Growing on Purpose: Developing Your Traits - Advanced",
  "The Integrated View: One Person, Many Models - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Personality Study — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
/* === EXPANSION 2026-10-18 group-1: Color Personality Playground / Strengths Discovery ===
   Full records in the stored archive schema (id,t,g,name,title,description,how_it_works,
   key_points,requirements,standards,citations,src,ladder_rank,ladder_tier,demo[python]).
   Deterministic by seed. */
function pyDemoProgram(id,title,g,pairs){
  var L=[];
  L.push("#!/usr/bin/env python3");
  L.push('"""'+title+" — working demonstration.");
  L.push("Record "+id+" ["+g+"]. Property of Justin Addam Higgins (JAH).");
  L.push('"""');
  L.push("def main():");
  L.push("    groups = {");
  for(var i=0;i<pairs.length;i++){
    var words=pairs[i][1].map(function(w){return '"'+w+'"';}).join(", ");
    L.push('        "'+pairs[i][0]+'": ['+words+'],');
  }
  L.push("    }");
  L.push("    total = sum(len(v) for v in groups.values())");
  L.push('    print("groups: %d  items: %d" % (len(groups), total))');
  L.push("    for name, items in groups.items():");
  L.push('        print("  %-22s %d items" % (name, len(items)))');
  L.push("    assert total == "+pairs.reduce(function(a,p){return a+p[1].length;},0));
  L.push("    assert len(groups) == "+pairs.length);
  L.push('    print("OK: '+title.replace(/"/g,"'")+' mapped")');
  L.push('if __name__ == "__main__":');
  L.push("    main()");
  return L.join("\n")+"\n";
}
var COLOR_TOPICS=[
{t:"Red Personalities — Energy and Action",g:"Foundations",
 desc:"Red is the color of energy, urgency, and action: this record explores what a preference for red suggests about temperament — boldness, competitiveness, and appetite for stimulation — and how red-preferring people show up at work and in relationships.",
 how:"Color preference works as a soft signal, not a diagnosis. People drawn to red tend to score higher on measures of extraversion and sensation-seeking: they choose the fast lane, speak first in meetings, and recharge through action rather than rest. The signal is probabilistic — plenty of calm people love red — but the pattern is consistent enough to be useful as a conversation starter about temperament.",
 kp:["A red preference correlates with extraversion and sensation-seeking — energy expressed outward.",
     "Red-preferring people tend to decide fast and act first; they are starters more than finishers.",
     "In teams, red energy drives momentum but can overwhelm reflective colleagues — pacing matters.",
     "Red signals urgency to others: use it deliberately in communication, not by default."],
 req:["Treat color preference as a clue about temperament, never a verdict on character.",
      "Separate the cultural meanings of red (luck, danger, passion) from personal preference.",
      "Observe behavior across situations before drawing conclusions from a favorite color."],
 std:["Color-psychology claims follow Elliot & Maier (2014): red effects are context-dependent, not universal laws.",
      "Preference research distinguishes favorite-color choice from color-in-context effects."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120.",
      "Luscher M. The Luscher Color Test. Pan Books; 1969."],
 rank:1,tier:"foundations",
 pairs:[["Energy words",["bold","driven","quick"]],["Action words",["decisive","competitive","direct"]],["Caution words",["impatient","intense","loud"]]]},
{t:"Blue Personalities — Calm and Trust",g:"Foundations",
 desc:"Blue is the world's most popular favorite color, and its fans cluster around steadiness: this record explores the calm-trust profile — reliability, thoughtfulness, and depth — and where blue temperaments thrive.",
 how:"Blue preference signals a temperament tuned for steadiness. People drawn to blue tend to be the reliable ones: they keep confidences, think before speaking, and prefer depth to breadth in relationships. Cross-cultural surveys consistently find blue the most chosen favorite color, which means the blue profile is common — the temperament of the dependable majority. In conflict, blue temperaments de-escalate; under pressure, they stabilize.",
 kp:["Blue preference is the most common worldwide — the calm-trust profile is the human default, not the exception.",
     "Blue temperaments excel at trust-building: consistency over time is their superpower.",
     "The risk of blue is passivity: steadiness can become conflict-avoidance if never examined.",
     "Blue communicates trustworthiness — which is why institutions (banks, hospitals) dress in it."],
 req:["Recognize that blue's popularity means the profile describes many different people — look for the pattern, not the stereotype.",
      "Distinguish genuine calm (regulated) from suppressed feeling (avoidant).",
      "Notice when steadiness serves and when it stalls."],
 std:["Favorite-color surveys reviewed per Elliot & Maier (2014); blue's cross-cultural lead is well replicated.",
      "Trust-signaling by blue follows the color-in-context model, not a universal law."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120."],
 rank:1,tier:"foundations",
 pairs:[["Calm words",["steady","patient","thoughtful"]],["Trust words",["reliable","loyal","honest"]],["Watch words",["passive","reserved","distant"]]]},
{t:"Yellow Personalities — Optimism and Ideas",g:"Foundations",
 desc:"Yellow is the color of sunlight and ideas: this record explores the optimism profile — curiosity, playfulness, and generative thinking — and how yellow temperaments handle the world's seriousness.",
 how:"Yellow preference marks the optimists and the idea-generators. People drawn to yellow tend toward curiosity over certainty: they ask the question nobody asked, find the game in the task, and recover from setbacks faster because their attention moves forward. The research on yellow is thinner than on red and blue, but the association pattern — yellow with cheerfulness, creativity, and mental stimulation — is consistent across preference studies.",
 kp:["Yellow preference signals cognitive optimism — a bias toward possibility over threat.",
     "Yellow temperaments generate options; they need partners who select among them.",
     "The risk of yellow is flightiness: optimism without follow-through disappoints.",
     "Yellow in environments stimulates mental activity — use it in creative spaces, sparingly elsewhere."],
 req:["Separate trait optimism (temperament) from state cheerfulness (mood).",
      "Value idea generation as a real contribution, not a distraction from 'real work.'",
      "Pair yellow temperaments with finishers; do not ask them to become finishers."],
 std:["Yellow associations reviewed per Elliot & Maier (2014); effects are weaker and more context-bound than red/blue.",
      "Optimism as a trait follows the standard personality literature (Scheier & Carver)."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120.",
      "Scheier MF, Carver CS. Optimism, coping, and health. American Psychologist. 1992;47(9):1064-1065."],
 rank:2,tier:"foundations",
 pairs:[["Optimism words",["cheerful","hopeful","bright"]],["Ideas words",["curious","inventive","playful"]],["Watch words",["scattered","naive","restless"]]]},
{t:"Green Personalities — Balance and Growth",g:"Foundations",
 desc:"Green is the color of nature and equilibrium: this record explores the balance profile — harmony-seeking, growth-oriented, quietly persistent people — and how green temperaments anchor groups.",
 how:"Green preference signals the balancers: people who seek harmony without surrendering growth. They are the mediators who actually listen, the friends who remember, the colleagues who keep the project human. Preference research links green to nature-connectedness and to a temperament that values steadiness with an organic, growing quality — less rigid than blue's order, more rooted than yellow's flight.",
 kp:["Green temperaments mediate well because they genuinely value all sides — not as tactics but as temperament.",
     "Growth-orientation means green-preferring people invest in long arcs: relationships, skills, gardens.",
     "The risk of green is over-accommodation: harmony-seeking can mute necessary conflict.",
     "Green environments measurably reduce stress — the preference and the effect reinforce each other."],
 req:["Distinguish healthy mediation (all voices heard) from conflict-avoidance (no voice raised).",
      "Honor the long arc: green temperaments play games measured in years.",
      "Check that harmony-seeking does not silence the green person's own needs."],
 std:["Nature-connectedness and green preference follow the biophilia literature (Kellert & Wilson, 1993).",
      "Stress-reduction effects of green environments are well replicated."],
 cit:["Kellert SR, Wilson EO, editors. The Biophilia Hypothesis. Island Press; 1993.",
      "Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120."],
 rank:2,tier:"foundations",
 pairs:[["Balance words",["harmonious","fair","grounded"]],["Growth words",["nurturing","patient","persistent"]],["Watch words",["avoidant","stubborn","selfless"]]]},
{t:"The Warm-Cool Spectrum",g:"Foundations",
 desc:"Warm colors (red, orange, yellow) advance and energize; cool colors (blue, green, violet) recede and calm. This record teaches the spectrum as a practical tool for reading rooms, moods, and moments.",
 how:"The warm-cool distinction is the most robust finding in color psychology: warm colors increase arousal and a sense of closeness, cool colors decrease arousal and increase a sense of space. It works on rooms (a red wall feels closer), on clothing (warm colors draw the eye), and on temperament readings — a person's position on the warm-cool preference spectrum predicts their arousal baseline better than any single color does.",
 kp:["Warm preference predicts higher baseline arousal and sociability; cool preference predicts lower arousal and reflectiveness.",
     "The spectrum is dimensional — most people sit somewhere in the middle, leaning one way.",
     "Use the spectrum diagnostically: where someone sits predicts what environments recharge them.",
     "Design with the spectrum: warm for energy spaces, cool for recovery spaces."],
 req:["Treat the spectrum as a dimension, not two boxes — the middle is the most populated.",
      "Separate color temperature (the stimulus) from temperament (the person).",
      "Test the reading against behavior, not just self-report."],
 std:["Warm-cool arousal effects follow Elliot & Maier (2014); among the best-replicated color effects.",
      "Arousal-temperament links follow Eysenck's arousal theory of extraversion."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120.",
      "Eysenck HJ. The Biological Basis of Personality. Thomas; 1967."],
 rank:3,tier:"foundations",
 pairs:[["Warm words",["energetic","social","bold"]],["Cool words",["calm","reflective","gentle"]],["Middle words",["adaptable","balanced","versatile"]]]},
{t:"Color and First Impressions",g:"Foundations",
 desc:"People read your colors before they hear your words: this record covers what color choices signal in first meetings — and how to choose deliberately.",
 how:"First impressions form in seconds, and color is among the fastest signals: clothing color shapes judgments of competence, warmth, authority, and creativity before a word is spoken. The effects are documented — dark colors read as authoritative, blue as trustworthy, red as powerful (and, in some contexts, aggressive), black as sophisticated. None of this is destiny, but all of it is data about how the signal lands.",
 kp:["Dress for the impression you intend — color is a signal you send whether you choose it or not.",
     "Context rules: red empowers in competition, alarms in caregiving — match the color to the room.",
     "Consistency beats intensity: a personal color signature is more memorable than loud choices.",
     "The strongest signal is congruence — colors that match your temperament read as authentic."],
 req:["Never judge character from clothing color — the signal is about perception, not worth.",
      "Account for culture: color meanings shift across contexts (white mourns in some cultures, celebrates in others).",
      "Update the reading as you gather real data about the person."],
 std:["Color-in-context effects per Elliot & Maier (2014); first-impression color effects are context-bound.",
      "Cultural variation in color meaning is well documented; no universal dress code exists."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120."],
 rank:3,tier:"foundations",
 pairs:[["Authority colors",["black","navy","charcoal"]],["Warmth colors",["soft blue","green","warm beige"]],["Energy colors",["red","orange","bright yellow"]]]},
{t:"Your Color Comfort Zone",g:"Foundations",
 desc:"Everyone has a color comfort zone — the palette they default to. This record teaches how to map yours and what expanding it does for flexibility.",
 how:"Your color comfort zone is visible in your closet, your home, and your screen themes: the 3-5 colors you return to without thinking. The zone reflects temperament — its breadth reflects flexibility. People with narrow zones tend toward routine and predictability; people with wide zones tend toward novelty-seeking. Neither is better, but knowing your zone lets you stretch it deliberately.",
 kp:["Map your zone: photograph your closet, your living room, your phone theme — the pattern emerges fast.",
     "A narrow zone is a preference, not a prison — but expanding it exercises flexibility.",
     "Try the 'one new color' experiment: wear or use one outside-zone color for a week and note what shifts.",
     "Zones change with life seasons — the palette of grief differs from the palette of new love."],
 req:["No judgment on any palette — the zone is information, not a grade.",
      "Expand by curiosity, not by rule — forced colors teach nothing.",
      "Notice emotional responses to new colors; they are data about your range."],
 std:["Comfort-zone concepts follow the personality literature on openness to experience.",
      "Color preference stability is moderate — zones evolve with life context."],
 cit:["McCrae RR, Costa PT. The five-factor theory of personality. In Handbook of Personality. Guilford; 1999."],
 rank:4,tier:"foundations",
 pairs:[["Narrow-zone words",["consistent","loyal","focused"]],["Wide-zone words",["adventurous","flexible","curious"]],["Stretch words",["brave","open","growing"]]]},
{t:"Colors in Teams",g:"Foundations",
 desc:"Teams have color profiles too: this record shows how to read a group's collective palette — and how to balance warm drivers with cool stabilizers.",
 how:"Map each member's color preference and the team's profile emerges: a team of reds moves fast and burns out; a team of blues deliberates beautifully and ships late; the healthiest teams span the spectrum. The profile predicts the team's failure mode better than its org chart does — and it suggests the fix: not new people, but new balance, achieved by giving each temperament its proper role.",
 kp:["Audit the spectrum: list the team by warm-cool preference and look for the gaps.",
     "Staff to the gaps: a red-heavy team needs a blue anchor; a blue-heavy team needs a yellow spark.",
     "Give each color its arena: reds own launches, blues own reviews, yellows own brainstorms, greens own retrospectives.",
     "Revisit quarterly — teams drift, and the spectrum drifts with them."],
 req:["Never use color profiles for hiring or firing — the tool is for balance, not selection.",
      "Keep it playful: the moment it feels like labeling, it has gone wrong.",
      "Combine with real performance data; color is the garnish, not the meal."],
 std:["Team composition effects follow the standard diversity literature; color is a lens, not a validated instrument.",
      "Use only for development conversations, never personnel decisions."],
 cit:["Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120."],
 rank:4,tier:"foundations",
 pairs:[["Driver colors",["red","orange"]],["Stabilizer colors",["blue","green"]],["Spark colors",["yellow","violet"]]]},
{t:"The Luscher Color Test — A Critical Tour",g:"Foundations",
 desc:"Max Luscher's famous color test claims your color ranking reveals your psyche. This record gives it a fair, critical tour — what it gets right, where it overreaches, and how to use it wisely.",
 how:"The Luscher test asks you to rank color cards by preference, then interprets the order as a personality readout: which needs are satisfied, which are frustrated, where the stress sits. It is genuinely engaging — the ranking feels revealing — and its core insight (that preference order carries information about current state) has some support. Its grander claims (diagnosing pathology from color order) do not survive scrutiny.",
 kp:["What it gets right: color preference reflects current emotional state more than fixed traits — the test is a mood ring with footnotes.",
     "What it overreaches: specific diagnostic claims lack replicated evidence; treat interpretations as hypotheses.",
     "Best use: a conversation starter about how you feel right now, not a psychological assessment.",
     "The meta-lesson: beware any instrument that flatters by seeming to see through you."],
 req:["Never use the Luscher (or any color test) for clinical or employment decisions.",
      "Interpret results as reflections of current state, not verdicts on character.",
      "Hold the interpretations lightly — the value is the reflection they prompt."],
 std:["Projective-test standards apply: reliability and validity evidence is required for consequential use.",
      "Luscher's diagnostic claims lack the replicated validation the standards require."],
 cit:["Luscher M. The Luscher Color Test. Pan Books; 1969.",
      "Elliot AJ, Maier MA. Color psychology: Effects of perceiving color on psychological functioning in humans. Annual Review of Psychology. 2014;65:95-120."],
 rank:4,tier:"foundations",
 pairs:[["Luscher primaries",["blue","green","red","yellow"]],["Luscher auxiliaries",["violet","brown","gray","black"]],["Reading words",["state","stress","desire"]]]},
{t:"Building Your Personal Palette",g:"Foundations",
 desc:"The capstone: assemble a personal palette — 5 colors that express who you are and who you are becoming — and learn to live inside it deliberately.",
 how:"A personal palette is a 5-color set chosen with intention: two anchors (your comfort colors), two aspirations (colors of who you are becoming), one accent (the wild card). The method: review everything this playground taught — your warm-cool position, your comfort zone, the signals you want to send — and choose deliberately. Then live with it for a month: dress it, decorate with it, notice what changes.",
 kp:["Two anchors honor who you are; two aspirations pull you forward; one accent keeps you playful.",
     "Write the why for each color — the palette is a statement of intent, not a decoration scheme.",
     "Revisit seasonally: palettes are living documents, and you are allowed to outgrow them.",
     "Share it: telling someone your palette is telling them something true about you."],
 req:["Choose by resonance, not by rule — the palette must feel like you.",
      "Include at least one color outside your comfort zone — growth needs an edge.",
      "Let it evolve; a palette that never changes is a uniform, not a self."],
 std:["Identity-expression through aesthetic choice follows the personality literature on self-presentation.",
      "No validated instrument; the value is reflective, not diagnostic."],
 cit:["McCrae RR, Costa PT. The five-factor theory of personality. In Handbook of Personality. Guilford; 1999."],
 rank:4,tier:"foundations",
 pairs:[["Anchor words",["home","true","steady"]],["Aspiration words",["becoming","reaching","brave"]],["Accent words",["play","surprise","joy"]]]}
];
var STRENGTHS_TOPICS=[
{t:"The VIA Character Strengths",g:"Compounded",
 desc:"The VIA classification names 24 character strengths in 6 virtues — psychology's map of what is best in people. This record teaches the full framework and how to find your signature strengths.",
 how:"The VIA (Values in Action) framework, built by Peterson and Seligman, classifies 24 measurable strengths — curiosity, bravery, kindness, leadership, gratitude among them — under 6 broad virtues: wisdom, courage, humanity, justice, temperance, transcendence. Your 'signature strengths' are your top 5: the ones that feel most like you, energize rather than drain, and show up across your life. The VIA survey (free, validated) ranks all 24 for you.",
 kp:["Signature strengths are identity-level: using them feels like being yourself, not performing.",
     "The 24 are descriptive, not prescriptive — there are no bad strengths, only misapplied ones.",
     "Strengths are plural: everyone has all 24 in some measure; the ranking is what differs.",
     "The framework is cross-culturally studied — the virtues appear across traditions."],
 req:["Take the actual VIA survey rather than guessing — self-estimates of strengths are unreliable.",
      "Treat the ranking as a starting hypothesis, confirmed by life evidence.",
      "Revisit every few years; strengths develop and the ranking shifts."],
 std:["VIA classification per Peterson & Seligman (2004); the 24-strength structure is the standard.",
      "Signature-strengths research follows the positive-psychology literature on strengths use and well-being."],
 cit:["Peterson C, Seligman MEP. Character Strengths and Virtues: A Handbook and Classification. Oxford University Press; 2004.",
      "Niemiec RM. Character Strengths Interventions. Hogrefe; 2018."],
 rank:5,tier:"compounded",
 pairs:[["Wisdom strengths",["curiosity","creativity","judgment"]],["Courage strengths",["bravery","perseverance","honesty"]],["Humanity strengths",["kindness","love","social intelligence"]]]},
{t:"CliftonStrengths: The 34 Themes",g:"Compounded",
 desc:"Gallup's CliftonStrengths names 34 talent themes in 4 domains — the workplace's most-used strengths language. This record teaches the domains and how to read a 34 report.",
 how:"CliftonStrengths (formerly StrengthsFinder) assesses 34 themes — Achiever, Empathy, Strategic, Learner among them — grouped into 4 domains: Executing (getting things done), Influencing (taking charge), Relationship Building (holding the team together), Strategic Thinking (absorbing and analyzing). Your top 5 themes are your talent signature; the full 34 report shows the whole pattern, including the bottom themes you should manage around rather than fix.",
 kp:["The 4 domains are the quick read: a report's domain balance predicts team role better than any single theme.",
     "Bottom themes are not weaknesses to fix — they are areas to partner around or manage.",
     "Themes are talents, not skills: raw material that investment turns into strength.",
     "The language's power is shared vocabulary — teams that speak themes collaborate better."],
 req:["Take the real assessment — theme-guessing from descriptions is notoriously inaccurate.",
      "Read the full 34, not just the top 5 — the pattern matters more than the peaks.",
      "Apply the 'name it, claim it, aim it' sequence: identify, own, direct."],
 std:["CliftonStrengths per Buckingham & Clifton (2001) and Gallup's technical reports.",
      "Talent-vs-strength distinction (talent x investment = strength) is the framework's core formula."],
 cit:["Buckingham M, Clifton DO. Now, Discover Your Strengths. Free Press; 2001.",
      "Gallup. CliftonStrengths technical documentation. Gallup Press."],
 rank:5,tier:"compounded",
 pairs:[["Executing themes",["Achiever","Arranger","Responsibility"]],["Influencing themes",["Communication","Command","Woo"]],["Thinking themes",["Strategic","Learner","Input"]]]},
{t:"Signature Strengths vs Learned Behaviors",g:"Compounded",
 desc:"Not everything you are good at is a strength: this record teaches the difference between signature strengths (energizing, identity-level) and learned behaviors (competent but draining) — and why the distinction runs your career.",
 how:"The test is energy, not skill. A signature strength leaves you more alive after using it; a learned behavior leaves you competent and tired. Many careers are built on learned behaviors — the accountant who is brilliant with spreadsheets and drained by them, the manager who runs great meetings and dreads them. The distinction matters because decades compound: a career built on strengths energizes for forty years; a career built on learned behaviors burns out in ten.",
 kp:["Audit by energy: list what you do well, then mark each energizing or draining — the pattern is the truth.",
     "Learned behaviors are valuable and billable — the goal is proportion, not purity.",
     "The 70% rule: aim for strengths to dominate your week; learned behaviors fill the gaps.",
     "Transitions (new roles, new decades) are the moments to rebalance toward strengths."],
 req:["Be honest about the drain — competence masks it, even from yourself.",
      "Separate market value (what pays) from energy value (what sustains).",
      "Redesign the role before quitting it — most jobs have strengths-shaped room."],
 std:["Energy-based strengths distinction follows the VIA signature-strengths literature.",
      "Burnout research supports the draining-competence pattern."],
 cit:["Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004.",
      "Maslach C, Leiter MP. Understanding the burnout experience. World Psychiatry. 2016;15(2):103-111."],
 rank:6,tier:"compounded",
 pairs:[["Energy signs",["alive","eager","absorbed"]],["Drain signs",["tired","dreading","heavy"]],["Rebalance moves",["redesign","delegate","transition"]]]},
{t:"Strengths Spotting in Others",g:"Compounded",
 desc:"The most underused strengths skill: seeing strengths in other people — and telling them. This record teaches strengths-spotting as a daily practice.",
 how:"Strengths-spotting is the discipline of naming the strength behind the behavior: not 'good job' but 'that took real bravery — you spoke the uncomfortable truth.' The practice has three steps: observe the behavior, infer the strength, name it specifically. It works because most people cannot see their own strengths — they are too close, and strengths feel ordinary from the inside ('doesn't everyone do that?'). The spotter gives people back their own excellence, labeled.",
 kp:["Be specific: name the strength and the behavior that revealed it — vagueness wastes the gift.",
     "Spot in real time: the closer to the behavior, the more it lands.",
     "Spot the quiet strengths too — the perseverance in the unglamorous work, the kindness in the small gesture.",
     "Receiving spotting well is its own skill: say thank you, write it down, believe it."],
 req:["Accuracy over flattery — mislabeled strengths confuse more than silence.",
      "Spot across the hierarchy: upward spotting (naming a boss's strength) is powerful and rare.",
      "Make it habitual: one spotted strength a day changes a culture in a quarter."],
 std:["Strengths-spotting interventions follow Niemiec (2018); specificity is the active ingredient.",
      "The 'ordinary from the inside' effect is well documented in strengths research."],
 cit:["Niemiec RM. Character Strengths Interventions. Hogrefe; 2018.",
      "Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004."],
 rank:6,tier:"compounded",
 pairs:[["Spotting steps",["observe","infer","name"]],["Spot phrases",["that took courage","your kindness showed","brilliant strategy"]],["Receiver moves",["thank","record","believe"]]]},
{t:"Strengths and Career Fit",g:"Compounded",
 desc:"Careers have strength profiles too: this record teaches how to read a role's demands against your signature strengths — and what to do about the gaps.",
 how:"Every role rewards certain strengths and taxes others: sales rewards persuasion and resilience; research rewards curiosity and perseverance; caregiving rewards kindness and patience. Career fit is the overlap between your signature strengths and the role's daily demands. High overlap predicts engagement and longevity; low overlap predicts the Sunday-night dread. The analysis is straightforward: list the role's top 5 demanded strengths, list yours, compare.",
 kp:["Map before you leap: profile the role's strengths demands through informational interviews, not job ads.",
     "A 3-of-5 overlap is workable; 1-of-5 is a warning; 0-of-5 is a no.",
     "Gaps are manageable if they are small and supported — delegate, systematize, or time-box them.",
     "Roles evolve: the fit you negotiate in year one can be reshaped by year three."],
 req:["Assess the real role, not the title — talk to people doing the work.",
      "Weight daily demands over occasional ones — the Tuesday matters more than the offsite.",
      "Revisit fit at every transition; strengths and roles both change."],
 std:["Person-environment fit literature supports strengths-role alignment predicting satisfaction.",
      "Use validated strengths measures for the self side of the comparison."],
 cit:["Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004.",
      "Buckingham M, Clifton DO. Now, Discover Your Strengths. Free Press; 2001."],
 rank:7,tier:"compounded",
 pairs:[["Fit signals",["engaged","flowing","eager"]],["Misfit signals",["dreading","drained","counting hours"]],["Gap tactics",["delegate","systematize","time-box"]]]},
{t:"The VIA Youth Survey",g:"Compounded",
 desc:"Character strengths in young people: the VIA Youth Survey, what it reveals, and how parents and teachers use strengths language with kids.",
 how:"The VIA Youth Survey adapts the 24 strengths for ages 10-17, with items written for young lives. The results give kids something school rarely provides: a vocabulary for what is right with them. Research links youth strengths-awareness to well-being, academic engagement, and resilience — and the practices are simple: strengths-spotting in the classroom, signature-strengths projects, the language of 'which strength did you use?' replacing 'what did you do wrong?'",
 kp:["Give kids the vocabulary early — named strengths get used; unnamed ones stay invisible.",
     "Spot effort-strengths (perseverance, bravery) as much as talent-strengths.",
     "Let kids lead: their top strengths often surprise adults, and the surprise is the point.",
     "Strengths language de-shames struggle — 'your perseverance is showing' reframes difficulty."],
 req:["Never rank kids against each other — strengths are personal, not competitive.",
      "Use the youth-validated survey, not the adult items.",
      "Involve the kids in interpreting their own results."],
 std:["VIA Youth Survey per Peterson & Seligman; youth strengths research follows the positive youth development literature.",
      "Practices adapted from Niemiec's education interventions."],
 cit:["Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004.",
      "Niemiec RM. Character Strengths Interventions. Hogrefe; 2018."],
 rank:7,tier:"compounded",
 pairs:[["Youth strengths",["curiosity","kindness","bravery"]],["Practices",["spotting","projects","language"]],["Outcomes",["well-being","engagement","resilience"]]]},
{t:"The Strengths-Overuse Trap",g:"Advanced",
 desc:"Every strength has a shadow: overused, a strength becomes a weakness. This record teaches the overuse pattern — and the golden mean for each of your top strengths.",
 how:"The overuse trap is strengths theory's advanced lesson: bravery overused becomes recklessness; kindness overused becomes self-neglect; honesty overused becomes cruelty; perseverance overused becomes stubbornness. The mechanism is context-blindness — applying the strength where a different strength was needed. The correction is not less strength but better aim: the same bravery, deployed with prudence (its temperance partner), becomes courage instead of recklessness.",
 kp:["Learn your overuse signature: the complaint you hear most often points at it ('you're too blunt' = overused honesty).",
     "Pair strengths: every strength has a balancing partner — find yours and practice the pair.",
     "The golden mean is situational — the right amount of a strength depends on the moment, not a formula.",
     "Feedback is the detector: overuse is invisible from the inside, obvious from the outside."],
 req:["Invite the specific feedback — 'tell me when I'm overusing X' — and reward honesty.",
      "Study the virtue families: balance usually lives in a neighboring virtue.",
      "Practice the underused partner strength deliberately."],
 std:["Strengths overuse follows the VIA literature on the 'shadow side' and Aristotle's golden mean framing.",
      "Balancing-strengths interventions per Niemiec (2018)."],
 cit:["Niemiec RM. Character Strengths Interventions. Hogrefe; 2018.",
      "Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004."],
 rank:8,tier:"advanced",
 pairs:[["Overuse pairs",["bravery-reckless","kindness-depleted","honesty-harsh"]],["Balance pairs",["bravery-prudence","kindness-boundaries","honesty-tact"]],["Detectors",["feedback","complaints","friction"]]]},
{t:"Building a Strengths-Based Team",g:"Advanced",
 desc:"From individual strengths to collective power: how to compose, run, and lead a team around its members' signature strengths.",
 how:"A strengths-based team is composed and managed by strengths, not just staffed by skills. The method: map every member's top 5, then design roles around the map — the Strategic thinker owns planning, the Empathy lead owns the client relationship, the Achiever owns the deadline. Meetings run on strengths (brainstorms led by Ideation, reviews by Analytical), and the team's gaps — the strengths nobody has — are named and covered by process or hiring.",
 kp:["Map the whole team visibly — the wall chart of strengths is the team's operating manual.",
     "Design roles to strengths, then let people grow into the stretch.",
     "Name the gaps honestly: 'we have no one high in Deliberative, so we build review steps.'",
     "Run strengths-based retrospectives: which strengths carried us, which were missing?"],
 req:["Get everyone's real assessment — volunteered strengths data only, never mandated.",
      "Use strengths for development, never for selection or stack-ranking.",
      "Revisit the map as the team changes; the operating manual must stay current."],
 std:["Team strengths interventions follow Gallup's strengths-based management research.",
      "Voluntary participation is an ethical requirement, not a preference."],
 cit:["Buckingham M, Clifton DO. Now, Discover Your Strengths. Free Press; 2001.",
      "Gallup. State of the American Manager. Gallup Press; 2015."],
 rank:8,tier:"advanced",
 pairs:[["Map moves",["assess","chart","design"]],["Run moves",["lead by strength","review by strength"]],["Gap moves",["name","cover","hire"]]]},
{t:"Developing a Lesser Strength",g:"Advanced",
 desc:"Can you grow a strength that ranks 20th? Yes — deliberately. This record teaches the protocol for developing a bottom-half strength without fighting your nature.",
 how:"Lesser strengths develop through deliberate, small, structured practice — not through wishing. The protocol: pick one lesser strength that matters to your goals (not all 24 — one), define the smallest daily rep (for prudence: one paused decision a day; for gratitude: one specific thank-you), attach it to an existing habit, and track for 30 days. The mechanism is the same as skill acquisition: reps, feedback, progression. Strengths are not fixed traits; the VIA research shows they develop with practice.",
 kp:["Pick by purpose: develop the lesser strength your goals actually require.",
     "Shrink the rep until it is embarrassingly small — consistency beats intensity.",
     "Borrow scaffolding: pair the new strength with a signature one (use curiosity to fuel perseverance).",
     "Measure behaviorally: count the reps, not the feelings — feelings follow."],
 req:["One strength at a time — divided effort develops nothing.",
      "Distinguish developing (growing capacity) from faking (performing without growth).",
      "Give it 90 days before judging; strengths grow on the slow curve."],
 std:["Strengths development follows the VIA intervention literature (Niemiec, 2018).",
      "Habit-formation mechanics per the behavioral literature on deliberate practice."],
 cit:["Niemiec RM. Character Strengths Interventions. Hogrefe; 2018.",
      "Peterson C, Seligman MEP. Character Strengths and Virtues. Oxford University Press; 2004."],
 rank:9,tier:"advanced",
 pairs:[["Protocol steps",["pick","shrink","attach","track"]],["Scaffolds",["pair","remind","review"]],["Measures",["reps","streaks","outcomes"]]]},
{t:"Strengths in Hard Times",g:"Advanced",
 desc:"The ultimate test: using character strengths under pressure — grief, failure, crisis. This record teaches strengths as resilience equipment.",
 how:"Hard times do not suspend strengths; they reveal and require them. The research on post-traumatic growth finds that people who navigate crisis well tend to lean deliberately on signature strengths: the brave act despite fear, the kind receive as well as give, the grateful find the one intact thing. The practice is pre-loading — knowing your strengths before the crisis, so the crisis does not have to teach you who you are while it is also testing you.",
 kp:["Know your crisis strengths in advance — the top 3 you will lean on when it gets hard.",
     "Let strengths be specific: 'my perseverance means I make the next call' beats 'stay strong.'",
     "Borrow others' strengths: in crisis, teams survive on complementary signatures.",
     "Afterward, narrate with strengths: the story of how you endured becomes part of the strength."],
 req:["Never strengths-shame suffering — strengths support grief, they do not cancel it.",
      "Distinguish resilience (adapting) from endurance (merely lasting).",
      "Seek professional support for trauma — strengths complement care, they do not replace it."],
 std:["Post-traumatic growth literature (Tedeschi & Calhoun) supports strengths-framed recovery.",
      "Strengths-based coping follows the positive-psychology resilience literature."],
 cit:["Tedeschi RG, Calhoun LG. Posttraumatic growth: Conceptual foundations and empirical evidence. Psychological Inquiry. 2004;15(1):1-18.",
      "Niemiec RM. Character Strengths Interventions. Hogrefe; 2018."],
 rank:9,tier:"advanced",
 pairs:[["Crisis strengths",["bravery","perseverance","hope"]],["Practices",["pre-load","specify","borrow"]],["Afterward",["narrate","integrate","grow"]]]}
];


function persRec(seed,cat){
  var pool=cat==='color-personality'?COLOR_TOPICS:STRENGTHS_TOPICS;
  var tp=pool[(seed-1)%pool.length];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,t:tp.t,g:tp.g,name:tp.t,title:tp.t,
    description:tp.desc,how_it_works:tp.how,key_points:tp.kp,requirements:tp.req,
    standards:tp.std,citations:tp.cit,src:'public-harvest',
    ladder_rank:tp.rank,ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:pyDemoProgram(id,tp.t,tp.g,tp.pairs)},
    _seed:seed};
}

function validateArchive(r){
  var e=[];
  if(!new RegExp('^JAH-PRSL-'+'\\d{6}$').test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.g!=='string'||!r.g.length)e.push('g');
  if(typeof r.description!=='string'||r.description.length<40)e.push('description');
  if(typeof r.how_it_works!=='string'||!r.how_it_works.length)e.push('how_it_works');
  if(!Array.isArray(r.key_points)||r.key_points.length<3)e.push('key_points');
  if(!Array.isArray(r.requirements)||r.requirements.length<2)e.push('requirements');
  if(!Array.isArray(r.standards)||!r.standards.length)e.push('standards');
  if(!Array.isArray(r.citations)||!r.citations.length)e.push('citations');
  if(r.src!=='public-harvest'&&r.src!=='signature')e.push('src');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=10))e.push('ladder_rank');
  if(['foundations','compounded','advanced'].indexOf(r.ladder_tier)<0)e.push('ladder_tier');
  if(!r.demo||typeof r.demo.program!=='string'||!r.demo.program.length)e.push('demo');
  return e;
}
function generate(seed,opts,rnd){
  opts=opts||{};
  if(opts.category&&(opts.category==='color-personality'||opts.category==='strengths-discovery'))return persRec(seed,opts.category);

  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — personality record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A personality record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"personality-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
  if(r&&typeof r==='object'&&(r.ladder_rank||r.questions)){
    var ae=validateArchive(r);return {ok:!ae.length,errors:ae};
  }
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate topic+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-personality-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personality',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
