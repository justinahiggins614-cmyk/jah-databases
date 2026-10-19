(function(){'use strict';
/* EXPANSION 2026-10-18 group-1: archive-shape branches added. */
/* JAH The Personality Signature Database generator — jahdb-personality-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-PRSLS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Personality Is (Signature Edition) - Foundations",
  "Traits, States, and Types (Signature Edition) - Foundations",
  "The Big Five at a Glance (Signature Edition) - Foundations",
  "Openness to Experience (Signature Edition) - Foundations",
  "Conscientiousness: The Big Five Discipline Domain (Signature Edition) - Foundations",
  "Extraversion: The Big Five Energy Domain (Signature Edition) - Foundations",
  "Agreeableness: The Big Five Warmth Domain (Signature Edition) - Foundations",
  "Emotional Stability and Neuroticism (Signature Edition) - Foundations",
  "The HEXACO Model (Signature Edition) - Foundations",
  "Honesty-Humility (Signature Edition) - Foundations",
  "Facets: The Six Faces of Every Domain (Signature Edition) - Foundations",
  "Self-Reports, Observer Ratings, and Bias (Signature Edition) - Foundations",
  "Nature, Nurture, and the Sources of Traits (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "The Sixteen Types of Jung and Myers-Briggs (Signature Edition) - Compounded",
  "Introversion, Extraversion, and Ambiversion in Daily Life (Signature Edition) - Compounded",
  "The Enneagram: Nine Motivational Patterns (Signature Edition) - Compounded",
  "DISC: Four Behavioral Styles (Signature Edition) - Compounded",
  "The Four Temperaments (Signature Edition) - Compounded",
  "The Sixteen Personality Factors (Signature Edition) - Compounded",
  "How Traits Combine: Reading a Full Profile (Signature Edition) - Compounded",
  "Personality at Work (Signature Edition) - Compounded",
  "Personality in Relationships (Signature Edition) - Compounded",
  "Measuring Personality: Reliability and Validity (Signature Edition) - Compounded",
  "The Person-Situation Debate (Signature Edition) - Compounded",
  "Team Chemistry: Traits in Groups (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Trait Stability and Change Across the Lifespan (Signature Edition) - Advanced",
  "Personality Development: The Maturity Principle (Signature Edition) - Advanced",
  "Personality and Decision-Making (Signature Edition) - Advanced",
  "Reading Others Ethically (Signature Edition) - Advanced",
  "Personality and Leadership (Signature Edition) - Advanced",
  "Personality Across Cultures (Signature Edition) - Advanced",
  "Conflict Styles and Personality (Signature Edition) - Advanced",
  "Growing on Purpose: Developing Your Traits (Signature Edition) - Advanced",
  "The Integrated View: One Person, Many Models (Signature Edition) - Advanced"
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
/* === EXPANSION 2026-10-18 group-1: Adventurer Profile Database ===
   Signature-original adventurer profiles in the stored archive schema
   (id,t,g,name,title,description,how_it_works,key_points,requirements,standards,
   citations,src,ladder_rank,ladder_tier,demo[python]). Deterministic by seed. */
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
var ADVENTURER_TOPICS=[
{t:"The Trailblazer Adventurer",g:"Compounded",
 desc:"Signature original interpretation. The Trailblazer is the adventurer who goes first — not because they fear nothing, but because their curiosity outweighs their caution. This profile maps the trailblazer's temperament: high openness, high tolerance for ambiguity, and a relationship with uncertainty that reads as courage.",
 how:"The Signature reading hears the Trailblazer as the expedition's compass: they point, and the group follows — not from authority but from the visible joy they take in the unknown. Trailblazers thrive where the map ends; they wither in routine. Their growth edge is the return journey: learning to come back, report, and let others go next.",
 kp:["Trailblazers lead by enthusiasm, not by rank — followership is voluntary and total.",
     "Their gift is the first step; their discipline is the debrief — both matter.",
     "Under stress, trailblazers accelerate — the team must build brakes they will actually use.",
     "Pair trailblazers with anchors: someone must mind the base camp."],
 req:["Distinguish trailblazing (exploring for the group) from thrill-seeking (risk for the rush).",
      "Give trailblazers genuine unknowns — manufactured adventure insults them.",
      "Require the return: the expedition is not complete until the knowledge is shared."],
 std:["Adventure temperament framed per the sensation-seeking literature (Zuckerman, 1994).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Zuckerman M. Behavioral Expressions and Biosocial Bases of Sensation Seeking. Cambridge University Press; 1994."],
 rank:3,tier:"compounded",
 pairs:[["Trail signs",["curious","bold","restless"]],["Gifts",["first steps","morale","discovery"]],["Edges",["impatience","overcommitment","solo runs"]]]},
{t:"The Navigator Adventurer",g:"Compounded",
 desc:"Signature original interpretation. The Navigator is the adventurer who reads the world — maps, stars, weather, people. Where the Trailblazer charges, the Navigator charts: their adventure is understanding, and their courage is the patience to get it right.",
 how:"The Signature reading hears the Navigator as the expedition's memory: they hold the route, the contingencies, the way home. Navigators find adventure in precision — the perfect line through the rapids, the exact bearing at dawn. Their joy is quiet and total: the world, correctly read. Their growth edge is improvisation — trusting the reading when the map runs out.",
 kp:["Navigators reduce risk for everyone — their preparation is the team's safety margin.",
     "Their adventure is mastery: the same river, run better, is a new adventure.",
     "Under stress, navigators over-plan — the team must sometimes take the map away.",
     "Pair navigators with trailblazers: the chart and the charge, together."],
 req:["Respect the preparation — questioning the plan is fine; dismissing it is not.",
      "Give navigators real responsibility for outcomes, not just advice.",
      "Practice the unplanned: deliberately take the Navigator somewhere unmapped."],
 std:["Mastery-oriented temperament per the expertise literature (Ericsson).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Ericsson KA, et al. The Cambridge Handbook of Expertise and Expert Performance. Cambridge University Press; 2006."],
 rank:4,tier:"compounded",
 pairs:[["Navigator signs",["precise","patient","observant"]],["Gifts",["safety","routes","calm"]],["Edges",["rigidity","overplanning","hesitation"]]]},
{t:"The Guardian Adventurer",g:"Compounded",
 desc:"Signature original interpretation. The Guardian adventures for others — the guide, the medic, the one who carries the extra water. Their thrill is not the summit but the team's safe return: adventure as service, courage as care.",
 how:"The Signature reading hears the Guardian as the expedition's conscience: they count heads, check knots, and turn back when pride says go. Guardians find their adventure in responsibility — the harder the conditions, the more their care matters. Their growth edge is receiving: guardians who never let themselves be helped burn out guarding.",
 kp:["Guardians make adventure possible for everyone else — they are the infrastructure of daring.",
     "Their courage is quiet: the decision to turn the team back takes more guts than the summit push.",
     "Under stress, guardians over-function — the team must order them to rest.",
     "Pair guardians with trailblazers: the charge needs its conscience."],
 req:["Do not mistake service for servitude — guardians choose this; honor the choice.",
      "Rotate the guardian role: everyone should carry the responsibility sometimes.",
      "Watch for guardian burnout — the caregivers need care too."],
 std:["Prosocial risk-taking framed per the altruism literature (Batson).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Batson CD. Altruism in Humans. Oxford University Press; 2011."],
 rank:4,tier:"compounded",
 pairs:[["Guardian signs",["responsible","attentive","steady"]],["Gifts",["safety","trust","care"]],["Edges",["overfunctioning","self-neglect","control"]]]},
{t:"The Solo Adventurer",g:"Advanced",
 desc:"Signature original interpretation. The Solo goes alone — not from misanthropy but from a need to meet the world unmediated. Their adventure is the conversation between one person and the wild, with no translation.",
 how:"The Signature reading hears the Solo as the expedition's purist: no team dynamics, no shared decisions, just the individual's full attention on the world. Solos develop extraordinary self-reliance — they are their own navigator, guardian, and trailblazer. Their growth edge is the return: solos who cannot share what they found keep the adventure but lose its meaning, which is connection.",
 kp:["Solo adventure builds self-knowledge faster than any other form — the mirror has no distractions.",
     "The risks are real and unshared: solos must be the most skilled, not the least.",
     "Under stress, solos have no team to catch the error — redundancy must be built into the plan.",
     "The solo's story, well told, becomes everyone's adventure — telling it is the final skill."],
 req:["Never solo beyond your skill — the margin for error is zero.",
      "File the plan: someone must know where you are and when to worry.",
      "Distinguish solitude (chosen, restorative) from isolation (imposed, corrosive)."],
 std:["Solitude benefits framed per the positive-solitude literature (Long & Averill).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Long CR, Averill JR. Solitude: An exploration of benefits of being alone. Journal for the Theory of Social Behaviour. 2003;33(1):21-44."],
 rank:8,tier:"advanced",
 pairs:[["Solo signs",["self-reliant","reflective","disciplined"]],["Gifts",["depth","freedom","clarity"]],["Edges",["risk","isolation","unshared joy"]]]},
{t:"The Storyteller Adventurer",g:"Compounded",
 desc:"Signature original interpretation. The Storyteller's adventure is the telling — they go so they can bring it back. Every expedition is material; every hardship is a chapter. Their courage is narrative: they endure because the story demands it.",
 how:"The Signature reading hears the Storyteller as the expedition's meaning-maker: while others climb, the Storyteller is already composing the account — and the composing changes the climbing, making it braver, funnier, more human. Storytellers preserve adventures that would otherwise vanish; they are the reason we know the great expeditions at all. Their growth edge is presence: sometimes the story must wait while the moment is lived.",
 kp:["Storytellers give adventures their afterlife — the telling is half the expedition.",
     "Their narrative drive sustains teams through the miserable middle miles.",
     "Under stress, storytellers narrate instead of acting — the team must pull them into the present.",
     "The best adventure stories are true and well-told — the Storyteller serves both masters."],
 req:["Tell it true — embellishment compounds, and the story outlives the teller.",
      "Get consent: not every teammate wants to be a character.",
      "Live first, narrate second — the moment outranks the material."],
 std:["Narrative identity framed per McAdams' life-story model of identity.",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["McAdams DP. The Stories We Live By. Guilford; 1993."],
 rank:5,tier:"compounded",
 pairs:[["Storyteller signs",["expressive","observant","dramatic"]],["Gifts",["memory","morale","meaning"]],["Edges",["embellishment","detachment","spotlight"]]]},
{t:"The Endurance Adventurer",g:"Advanced",
 desc:"Signature original interpretation. The Endurance adventurer seeks the long suffering — the thru-hike, the ocean row, the desert crossing. Their adventure is measured in days and blisters: they find out who they are by outlasting who they were.",
 how:"The Signature reading hears the Endurance as the expedition's engine: when talent fades and luck runs out, the Endurance keeps moving — one foot, one stroke, one dune at a time. Their temperament is built for the long middle where most adventures are actually lived. Their gift is pace: they know the speed they can hold forever, and they hold it. Their growth edge is stopping: endurance without a finish line is just suffering.",
 kp:["Endurance is a skill, not just a trait — it is built in training, proven in the event.",
     "The Endurance's pace discipline is the team's metronome — follow it and everyone finishes.",
     "Under stress, the Endurance grinds — the team must check whether grinding is still wise.",
     "Recovery is part of endurance: the great ones rest as deliberately as they push."],
 req:["Build the base before the event — endurance cannot be improvised.",
      "Know the difference between productive suffering and injury.",
      "Have a finish line: the endeavor needs an end to be an adventure."],
 std:["Endurance performance framed per the sports-psychology literature on pacing and perseverance.",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Duckworth AL. Grit: The Power of Passion and Perseverance. Scribner; 2016."],
 rank:8,tier:"advanced",
 pairs:[["Endurance signs",["patient","tough","steady"]],["Gifts",["pace","reliability","grit"]],["Edges",["grinding","ignoring signals","no finish"]]]},
{t:"The Trickster Adventurer",g:"Compounded",
 desc:"Signature original interpretation. The Trickster adventures sideways — finding the unofficial route, the loophole, the way nobody thought of. Their courage is creative: they risk looking foolish to find the brilliant path.",
 how:"The Signature reading hears the Trickster as the expedition's wild card: when the plan fails, the Trickster was already trying something else — and half the time it works. Tricksters see the adventure as a puzzle, not an ordeal: the mountain is a problem to be solved cleverly, not merely endured. Their growth edge is commitment: the clever path is not always the right one, and sometimes the mountain just needs climbing.",
 kp:["Tricksters generate options when options run out — the team's creativity reserve.",
     "Their lateral thinking finds the route the map hid — and the shortcut that wasn't.",
     "Under stress, tricksters joke — the humor defuses, but the team must hear the plan inside it.",
     "The trickster's best move is sometimes the straightforward one — surprise everyone."],
 req:["Distinguish cleverness (solving the problem) from showing off (solving the audience).",
      "Test the clever path before committing the team to it.",
      "Honor the times the straightforward path is the wise one."],
 std:["Creative problem-solving framed per the creativity literature (Amabile).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Amabile TM. Creativity in Context. Westview Press; 1996."],
 rank:6,tier:"compounded",
 pairs:[["Trickster signs",["clever","playful","unconventional"]],["Gifts",["options","humor","surprise"]],["Edges",["unreliability","showing off","overcomplicating"]]]},
{t:"The Pilgrim Adventurer",g:"Advanced",
 desc:"Signature original interpretation. The Pilgrim's adventure is inward — the outer journey serves the inner one. They walk the ancient routes, climb the sacred peaks, and return changed: adventure as transformation, not conquest.",
 how:"The Signature reading hears the Pilgrim as the expedition's soul: while others measure miles, the Pilgrim measures meaning — and the meaning, honestly sought, changes the measurer. Pilgrims choose routes with history, walk them with intention, and let the journey work on them. Their growth edge is the ordinary: the pilgrimage ends, and the transformation must survive the return to Tuesday.",
 kp:["Pilgrims remind the team why anyone bothers — the meaning beneath the miles.",
     "Their intentionality deepens any expedition — even a casual trip gains gravity.",
     "Under stress, pilgrims spiritualize — the team must keep them practical too.",
     "The return is the real pilgrimage: bringing the mountain home."],
 req:["Respect the sacred — pilgrim routes are holy to someone; act like it.",
      "Do not perform piety — the inner journey is private until shared.",
      "Plan the re-entry: transformation needs a landing pad."],
 std:["Pilgrimage psychology framed per the ritual and transformation literature (Turner).",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Turner V. The Ritual Process. Aldine; 1969."],
 rank:9,tier:"advanced",
 pairs:[["Pilgrim signs",["reflective","intentional","reverent"]],["Gifts",["meaning","depth","perspective"]],["Edges",["escapism","preaching","impracticality"]]]},
{t:"The Mentor Adventurer",g:"Advanced",
 desc:"Signature original interpretation. The Mentor has had their adventures and now adventures through others — guiding, teaching, witnessing. Their courage is generativity: risking their heart on someone else's summit.",
 how:"The Signature reading hears the Mentor as the expedition's elder: they have seen the mountain in all weathers, and their adventure now is the novice's first view of it. Mentors find fresh wonder secondhand — and it is real wonder, not nostalgia. Their growth edge is letting go: the mentee's adventure belongs to the mentee, including the mistakes the mentor could have prevented.",
 kp:["Mentors multiply adventure — every mentee's expedition is partly theirs.",
     "Their experience is the team's library: consult it, especially when confident.",
     "Under stress, mentors take over — the team must remind them to advise, not command.",
     "The mentor's final adventure is retirement from the sharp end — and finding the next one."],
 req:["Advise, do not command — the mentee's judgment must develop.",
      "Let them fail safely: the preventable mistake is sometimes the necessary lesson.",
      "Keep your own adventure alive — the mentor who stops going stops relating."],
 std:["Generativity framed per Erikson's developmental stages.",
      "Signature-original profile: an interpretation, not a clinical assessment."],
 cit:["Erikson EH. Childhood and Society. Norton; 1950."],
 rank:9,tier:"advanced",
 pairs:[["Mentor signs",["wise","generous","patient"]],["Gifts",["guidance","perspective","legacy"]],["Edges",["takeover","nostalgia","overprotection"]]]},
{t:"The Adventurer's Code — Capstone",g:"Advanced",
 desc:"Signature original interpretation. The capstone profile: what all adventurers share — the code beneath the types. Curiosity over comfort, preparation over luck, the team over the ego, and the return over the summit.",
 how:"The Signature reading gathers the nine profiles into one code. The Trailblazer brings the first step; the Navigator, the way; the Guardian, the care; the Solo, the depth; the Storyteller, the meaning; the Endurance, the pace; the Trickster, the options; the Pilgrim, the soul; the Mentor, the legacy. No adventurer is one type — the profiles are instruments, and the complete adventurer plays them all, louder or softer as the expedition demands.",
 kp:["Know your primary instrument — and practice the other eight.",
     "The code: curiosity over comfort, preparation over luck, team over ego, return over summit.",
     "Every expedition needs all nine voices — in nine people or in one.",
     "The final profile is yours: write it by adventuring."],
 req:["Do not type yourself permanently — the profiles describe moments, not destinies.",
      "Earn each profile: the only credential is the expedition.",
      "Teach the code by living it — the next adventurer is watching."],
 std:["Integrative profile per the Signature interpretation framework.",
      "Signature-original: a synthesis, not a clinical assessment."],
 cit:["Zuckerman M. Behavioral Expressions and Biosocial Bases of Sensation Seeking. Cambridge University Press; 1994."],
 rank:10,tier:"advanced",
 pairs:[["The code",["curiosity","preparation","team","return"]],["The nine",["trailblazer","navigator","guardian"]],["Your move",["go","learn","become"]]]}
];


function prslsRec(seed,cat){
  var tp=ADVENTURER_TOPICS[(seed-1)%ADVENTURER_TOPICS.length];
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,t:tp.t,g:tp.g,name:tp.t,title:tp.t,
    description:tp.desc,how_it_works:tp.how,key_points:tp.kp,requirements:tp.req,
    standards:tp.std,citations:tp.cit,src:'signature',
    ladder_rank:tp.rank,ladder_tier:tp.tier,
    demo:{kind:"python",language:"python",program:pyDemoProgram(id,tp.t,tp.g,tp.pairs)},
    _seed:seed};
}

function validateArchive(r){
  var e=[];
  if(!new RegExp('^JAH-PRSLS-'+'\\d{6}$').test(r.id||''))e.push('id');
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
  if(opts.category==='adventurer-profiles')return prslsRec(seed,opts.category);

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
var gen={version:'jahdb-personality-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('personality-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
