/* JAH Parenting Database generator — jahdb-parenting-1.0
   Deterministic (mulberry32). Seed -> full parenting guide.
   Sourced records draw every fact from the curated dataset below
   (standard developmental milestones, established parenting methods, and
   widely shared family guidance). Medical topics always advise consulting
   your pediatrician. Signature records are homegrown planning material,
   always labeled as such. General information only, never medical advice.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-PAR-';
var KIND='parenting guide';
var CATS=['development-stage','method','health','nutrition','safety','education','behavior','family','daily-plan','qa'];
/* [name, ages, milestones] */
var STAGES=[
["Newborn","0-1 month","Lifts head briefly during tummy time; startles at loud sounds; focuses on faces 8 to 12 inches away."],
["Young infant","1-4 months","Smiles socially; coos and gurgles; holds head steady; reaches for toys."],
["Older infant","4-8 months","Rolls both ways; sits with support; babbles with consonant sounds."],
["Late infancy","8-12 months","Sits without support; pulls to stand; says mama and dada; waves bye-bye."],
["Young toddler","12-18 months","Walks independently; says several single words; follows one-step directions."],
["Toddler","18-24 months","Runs; builds towers of blocks; speaks in short two-word phrases."],
["Older toddler","2-3 years","Kicks a ball; speaks in short sentences; begins toilet learning."],
["Preschooler","3-4 years","Pedals a tricycle; speaks clearly in sentences; plays cooperatively with others."],
["Pre-kindergartner","4-5 years","Counts to 10; prints some letters; takes turns and shares."],
["School age","6-12 years","Reads independently; understands rules and fairness; forms close friendships."]
];
/* [name, description] */
var METHODS=[
["Authoritative parenting","High warmth plus clear limits; explains reasons and listens to the child."],
["Authoritarian parenting","High control with low warmth; an obedience-first approach."],
["Permissive parenting","High warmth with few limits; avoids confrontation."],
["Uninvolved parenting","Low warmth and low control; minimal engagement with the child."],
["Attachment parenting","Emphasizes close physical and emotional bonds, responsiveness, and gentle guidance."],
["Positive discipline","Teaches skills through encouragement, routines, and respectful problem-solving."],
["Gentle parenting","No punishment; focuses on empathy, firm boundaries, and connection."],
["Montessori at home","A prepared environment, independence, and hands-on learning at the child's pace."],
["RIE","Resources for Infant Educarers: respectful, observant care that treats babies as competent people."],
["Conscious discipline","Adults manage their own emotional state first, then coach children through conflict."],
["Free-range parenting","Gives children age-appropriate independence to build confidence and competence."],
["Collaborative problem solving","Parent and child brainstorm solutions together, sharing power respectfully."]
];
/* [name, category, guidance] */
var TOPICS=[
["Well-child visits","health","Keep the recommended checkup schedule with your pediatrician; visits track growth and development."],
["Fever basics","health","A fever is the body fighting infection; call your pediatrician for guidance, especially for babies under 3 months."],
["Vaccinations","health","Follow your pediatrician's recommended immunization schedule and ask questions at every visit."],
["Common colds","health","Rest, fluids, and comfort help; call the doctor if breathing is difficult or symptoms worsen."],
["Ear infections","health","Ear tugging with fever may signal infection; your pediatrician can diagnose and advise."],
["Stomach bugs","health","Small sips of fluids and rest; watch for signs of dehydration and call your doctor if worried."],
["Allergies","health","Introduce common allergens as your pediatrician advises; watch for reactions with new foods."],
["Asthma basics","health","Follow the action plan from your doctor and keep quick-relief medicine as prescribed."],
["Eczema care","health","Gentle moisturizers and short lukewarm baths help; ask your pediatrician about flares."],
["Dental care","health","First dental visit around the first birthday; brush twice daily as your dentist advises."],
["Eye exams","health","Vision screening happens at well-child visits; mention squinting or frequent headaches."],
["Hearing screening","health","Newborn screening plus checks at well visits; mention any concern promptly."],
["Breastfeeding basics","nutrition","Feed on demand in the early weeks; a lactation consultant can help with latch concerns."],
["Formula feeding","nutrition","Prepare exactly as the label directs; never dilute or concentrate formula."],
["Introducing solids","nutrition","Around 6 months as your pediatrician advises; start with single-ingredient foods."],
["Picky eating","nutrition","Offer variety without pressure; it can take many exposures before a child accepts a food."],
["Family meals","nutrition","Eating together builds healthy habits and connection; aim for regular shared meals."],
["Healthy snacks","nutrition","Fruits, vegetables, and whole grains give steadier energy than sugary snacks."],
["Hydration","nutrition","Water is the best everyday drink; limit juice and avoid sugary drinks."],
["Food allergies","nutrition","Introduce allergens one at a time as advised; learn the signs of a reaction."],
["Bottle weaning","nutrition","Transition to a cup around 12 to 18 months to protect developing teeth."],
["Choking hazards","nutrition","Cut grapes, hot dogs, and hard foods small; always supervise eating closely."],
["Safe sleep","safety","Back to sleep on a firm, bare mattress; keep blankets, pillows, and bumpers out of the crib."],
["Car seat safety","safety","Stay rear-facing as long as the seat allows; follow the seat manual and your pediatrician."],
["Baby-proofing","safety","Cover outlets, secure furniture, and lock cabinets before your baby is mobile."],
["Water safety","safety","Never leave children alone near water; swim lessons add one more layer of protection."],
["Bath safety","safety","Never leave a child alone in the bath, not even for a moment."],
["Sun protection","safety","Shade, hats, and sunscreen for babies over 6 months; avoid the midday sun."],
["Choking prevention","safety","Keep small objects out of reach and learn infant and child CPR."],
["Fire safety","safety","Keep working smoke alarms on every level and practice an escape plan."],
["Emergency numbers","safety","Teach children when and how to call for help as they grow old enough."],
["Stranger safety","safety","Teach body-safety rules early, in simple and calm language."],
["Device safety","safety","Keep devices in shared spaces; use parental controls and talk about online kindness."],
["Pet introductions","safety","Supervise every child-pet interaction and teach gentle handling."],
["Reading aloud","education","Read together daily from birth; it builds vocabulary, attention, and bonding."],
["Language development","education","Talk, sing, and narrate your day; respond to babbles as if they are conversation."],
["Bilingual households","education","Consistency helps; one-parent-one-language or one-context-one-language both work."],
["Preschool readiness","education","Social skills and independence matter more than academics at this age."],
["Kindergarten readiness","education","Following directions, taking turns, and basic self-care smooth the transition."],
["Homework routines","education","A consistent time and quiet place beats long battles; stay nearby for young kids."],
["Choosing childcare","education","Visit, observe, ask about ratios and staff turnover, and trust your instincts."],
["Teacher conferences","education","Arrive with questions and listen; partner with the teacher on goals."],
["Library use","education","Free books, story times, and summer programs make the library a parent's ally."],
["Play-based learning","education","Play is the work of childhood; protect unscheduled time for it."],
["Tantrums","behavior","Stay calm, keep everyone safe, and wait it out; connect before you correct."],
["Time-outs","behavior","Brief, calm, and consistent; one minute per year of age is a common guide."],
["Natural consequences","behavior","When it is safe, let natural outcomes do the teaching."],
["Praise that works","behavior","Praise effort and specific actions rather than just being smart."],
["Setting limits","behavior","Clear, few, and consistent rules beat many shifting ones."],
["Sibling rivalry","behavior","Avoid comparisons and give each child individual time with you."],
["Biting","behavior","Stay calm, state the rule briefly, and redirect; the phase usually passes."],
["Sharing","behavior","Forcing sharing backfires; model turn-taking instead."],
["Morning routines","behavior","Visual charts and preparing the night before smooth chaotic mornings."],
["Bedtime battles","behavior","A consistent wind-down routine beats negotiation every single night."],
["Family meetings","family","A weekly check-in gives everyone a voice, including the kids."],
["Co-parenting","family","Keep adult disagreements away from children and present a united front."],
["Single parenting","family","Build your village; steady routines and self-care keep you going."],
["Blended families","family","Go slow and let relationships form naturally without forcing closeness."],
["Grandparent boundaries","family","Share your rules kindly and clearly, and thank them for their help."],
["New baby adjustment","family","Give the older child a role and protect one-on-one time together."],
["Work-life balance","family","Boundaries protect family time; be fully present when you are home."],
["Parental self-care","family","You cannot pour from an empty cup; rest is part of good parenting."],
["Parental burnout","family","Exhaustion, detachment, and irritability signal you need support; ask for help."],
["Family traditions","family","Small repeated rituals build belonging more than big occasional events."],
["Divorce and children","family","Reassure them it is not their fault and keep daily routines stable."],
["Grief and children","family","Answer honestly at their level and let them see healthy grieving."]
];
var ANGLES=[
["","", ""],
["for new parents"," \u2014 for new parents"," If this is your first time, start small and give yourself grace."],
["quick reference"," \u2014 quick reference"," Keep this one bookmarked for busy days."],
["deep dive"," \u2014 deep dive"," Worth a longer read when you have a quiet moment."],
["grandparents"," \u2014 for grandparents"," A helpful share for grandparents and caregivers."],
["cheat sheet"," \u2014 cheat sheet",""]
];
function comboGen(j,nE,nA,nG){
  var per=nA*nG;
  var e=j%nE, c=Math.floor(j/nE)%per, part=Math.floor(j/(nE*per));
  return {e:e,a:Math.floor(c/nG),g:c%nG,part:part};
}
var SRC="JAH Parenting curated dataset v1 \u2014 standard developmental milestones, established methods, and widely shared family guidance. General information only.";
var SIGSRC="JAH Signature generator \u2014 homegrown planning material, clearly labeled as generated. General information only, not professional advice.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" Talk to your pediatrician with any personal concern.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
var STAGE_ASPECTS=[
["overview",function(x){return x[0]+" ("+x[1]+"): "+x[2];}],
["milestones",function(x){return "Watch for: "+x[2];}],
["play ideas",function(x){return "Simple floor play, talking, and reading suit this stage well.";}],
["sleep notes",function(x){return "Steady routines and a calm sleep space help at this age.";}],
["safety notes",function(x){return "Match your childproofing to new mobility at this stage.";}],
["doctor visits",function(x){return "Mention any concern at well-child visits; your pediatrician tracks development.";}],
["for parents",function(x){return "This stage passes quickly; routines and patience carry you through.";}],
["quick tips",function(x){return "Talk, read, play, and keep routines predictable.";}]
];
var METHOD_ASPECTS=[
["overview",function(x){return x[0]+": "+x[1];}],
["in practice",function(x){return "In daily life this looks like calm consistency plus genuine listening.";}],
["strengths",function(x){return "Families choose it for its clarity and respect.";}],
["watch-outs",function(x){return "Like any method, it works best applied flexibly, not rigidly.";}],
["combining",function(x){return "Many parents blend methods; take what fits your family.";}],
["quick tips",function(x){return "Start with one small change and build from there.";}]
];
var TOPIC_ASPECTS=[
["overview",function(x){return x[0]+": "+x[2];}],
["why it matters",function(x){return "Getting this right pays off in health, safety, and family calm.";}],
["how to start",function(x){return "Begin with one small step this week: "+x[2];}],
["common mistakes",function(x){return "The usual pitfall is inconsistency; pick a plan the whole household can keep.";}],
["when to get help",function(x){return "Call your pediatrician promptly with any worry; trust your instincts.";}],
["quick tips",function(x){return "Keep it simple, stay consistent, and adjust as your child grows.";}]
];
function stageRec(seed,j){
  var cb=comboGen(j,STAGES.length,STAGE_ASPECTS.length,ANGLES.length);
  var x=STAGES[cb.e],a=STAGE_ASPECTS[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary="Developmental stage "+x[0]+" ("+x[1]+"). "+a[1](x)+g[2]+" Every child develops at their own pace; milestones are guides, not deadlines.";
  return mkRec(seed,"development-stage",title,summary,{stage:x[0],ages:x[1],milestones:x[2],aspect:a[0]},"sourced",SRC);
}
function methodRec(seed,j){
  var cb=comboGen(j,METHODS.length,METHOD_ASPECTS.length,ANGLES.length);
  var x=METHODS[cb.e],a=METHOD_ASPECTS[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary="Parenting method: "+x[0]+". "+x[1]+" "+a[1](x)+g[2];
  return mkRec(seed,"method",title,summary,{method:x[0],description:x[1],aspect:a[0]},"sourced",SRC);
}
function topicRec(seed,j){
  var cb=comboGen(j,TOPICS.length,TOPIC_ASPECTS.length,ANGLES.length);
  var x=TOPICS[cb.e],a=TOPIC_ASPECTS[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var summary=x[0]+". "+x[2]+" "+a[1](x)+g[2];
  return mkRec(seed,x[1],title,summary,{topic:x[0],guidance:x[2],aspect:a[0]},"sourced",SRC);
}
var DAY_BANDS=[
["newborn days","Feed every 2-3 hours around the clock; sleep in short stretches; one calm walk outdoors."],
["infant days","Morning feed, play, and nap cycles; afternoon outing; early bedtime routine."],
["toddler days","Breakfast, outdoor play, morning nap, lunch, quiet play, afternoon outing, dinner, bath, bed."],
["preschool days","Morning learning play, park time, lunch, rest time, creative play, dinner, stories, bed."],
["school-age days","School, snack and outdoor play, homework block, dinner, family time, reading, bed."],
["weekend family days","Slow breakfast, one outing, free play, shared meal, and an early wind-down."]
];
function planRec(seed,j){
  var b=DAY_BANDS[j%DAY_BANDS.length];
  var v=Math.floor(j/DAY_BANDS.length);
  var title="Sample day: "+b[0]+(v>0?" (v"+(v+1)+")":"");
  var summary="Signature-generated daily rhythm \u2014 a starting template to adapt, not a prescription. "+b[0]+": "+b[1]+" Adjust times to your child's cues and your family's life.";
  return mkRec(seed,"daily-plan",title,summary,{band:b[0],rhythm:b[1],variant:v+1,note:"Template only; adapt freely."},"signature",SIGSRC);
}
var QA_Q=[
["How do I handle bedtime resistance?","Hold the routine steady and stay boring after lights-out; consistency wins within days."],
["When should my child drop naps?","Most children drop naps between ages 3 and 5; quiet rest time can replace the nap."],
["What if my child will not eat vegetables?","Keep offering without pressure alongside foods they like; repeated calm exposure works."],
["How much screen time is okay?","Keep it limited, choose quality content, and co-view when you can; protect sleep and play first."],
["My toddler hits. What do I do?","Stay calm, stop the behavior kindly, and teach words for big feelings; it is a phase for most."],
["How do I prepare my child for a new sibling?","Talk about the baby, give the older child a helper role, and protect one-on-one time."],
["When do I call the pediatrician?","Call with any worry, especially for young infants; trust your instincts over any list."],
["How can we smooth school mornings?","Prepare clothes and bags the night before and use a visual chart; leave buffer time."],
["What helps with sibling fighting?","Separate, cool down, then problem-solve together; avoid declaring a winner."],
["How do I talk about difficult news?","Answer honestly at their level, keep it brief, and reassure them of their safety."]
];
function qaRec(seed,j){
  var q=QA_Q[j%QA_Q.length];
  var v=Math.floor(j/QA_Q.length);
  var title="Q&A: "+q[0]+(v>0?" (v"+(v+1)+")":"");
  var summary="Signature-generated parenting Q&A \u2014 general information only, not medical or professional advice. "+
    q[0]+" "+q[1]+(v>0?" A fresh pass over a common question.":"")+" For personal concerns, talk to your pediatrician or a trusted professional.";
  return mkRec(seed,"qa",title,summary,{question:q[0],answer:q[1],variant:v+1,disclaimer:"General information only."},"signature",SIGSRC);
}
/* Parenting expansion: foster-care, adoption, child-protection process guides.
   Each entry: [category, title, summary, details]. General information only. */
var NEW_CATS=['foster-care','adoption','child-protection'];
var EXPAND_AFTER=10000;
var NEW_WELFARE=[
['foster-care','Becoming a foster parent: the licensing path','Foster licensing prepares and approves families to care for children in state custody. Typical steps include an application, background checks, a home study with interviews and safety review, and pre-service training. Timelines vary by agency. General information only; contact your local child welfare agency for requirements.',
 {steps:['Submit application to agency','Complete background checks','Home study interviews and safety review','Pre-service training','Licensing approval'],note:'Requirements vary by state and agency.',disclaimer:'General information only.'}],
['foster-care','What foster parents provide day to day','Foster parents provide a safe home, meals, school support, medical care coordination, and emotional steadiness. They document behaviors, attend court-related meetings, and work with caseworkers toward the child\u2019s permanency plan. General information only.',
 {provides:['Safe housing and meals','School enrollment support','Medical and therapy appointments','Caseworker collaboration','Court hearing attendance'],disclaimer:'General information only.'}],
['foster-care','Supporting a foster child\u2019s first week','The first week in foster care is disorienting. Keep routines predictable, explain house rules kindly, allow contact with siblings and safe family where permitted, and watch for signs of distress to report to the caseworker. Patience matters more than perfection. General information only.',
 {tips:['Keep routines predictable','Explain rules kindly','Support permitted family contact','Report distress signs','Be patient'],disclaimer:'General information only.'}],
['foster-care','Foster care and school stability','School stability helps foster children learn. Caregivers usually enroll the child promptly, share records with the new school, request support services, and advocate at meetings. Many places prioritize keeping the child in their school of origin when possible. General information only.',
 {actions:['Enroll promptly','Transfer records','Request support services','Advocate at school meetings'],disclaimer:'General information only.'}],
['foster-care','Working with your caseworker','Caseworkers coordinate the foster care team. Foster parents do best when they communicate regularly, document concerns in writing, attend scheduled visits, and ask questions about the permanency plan. Respectful partnership serves the child. General information only.',
 {practices:['Communicate regularly','Document in writing','Attend scheduled visits','Ask about the permanency plan'],disclaimer:'General information only.'}],
['foster-care','Foster care payments and reimbursements','Foster families typically receive a monthly maintenance payment covering the child\u2019s food, clothing, and daily needs, sometimes plus clothing allowances and reimbursed expenses. Rates and policies differ by state. Keep receipts and submit claims on time. General information only.',
 {items:['Monthly maintenance payment','Clothing allowances','Reimbursed approved expenses','Receipt keeping'],disclaimer:'General information only.'}],
['foster-care','When a foster placement ends','Placements end through reunification, adoption, guardianship, or moves. Prepare the child with honest age-appropriate goodbyes, pass along routines and preferences to the next caregiver, and allow yourself to grieve. Your care mattered regardless of length. General information only.',
 {steps:['Prepare honest goodbyes','Share routines with next caregiver','Document the child\u2019s needs','Allow time to grieve'],disclaimer:'General information only.'}],
['foster-care','Kinship care: relatives stepping in','Kinship caregivers \u2014 grandparents, aunts, uncles, family friends \u2014 care for children when parents cannot. They often face expedited licensing, need legal custody clarity, and benefit from support groups and respite care. The existing bond is a powerful asset. General information only.',
 {points:['Often expedited licensing','Clarify legal custody','Seek support groups','Use respite care','Lean on the existing bond'],disclaimer:'General information only.'}],
['adoption','Adoption paths: an overview','Families adopt through public agencies (often foster-to-adopt), private domestic agencies, or intercountry programs. Each path has different timelines, costs, and requirements. Research all three before choosing, and verify any agency\u2019s license and track record. General information only.',
 {paths:['Public agency / foster-to-adopt','Private domestic agency','Intercountry adoption'],tip:'Verify agency licensing.',disclaimer:'General information only.'}],
['adoption','The home study for adoption','The home study assesses readiness to adopt: interviews, background checks, financial review, home safety check, and references. It also prepares parents through education. Be honest and thorough; the process protects children. General information only.',
 {includes:['Interviews','Background checks','Financial review','Home safety check','References','Parent education'],disclaimer:'General information only.'}],
['adoption','Adoption costs and financial help','Adoption costs range from minimal (public agency) to substantial (private/intercountry). Families use employer benefits, tax credits, grants, and loans. Get every fee in writing and beware of guarantees no agency can honestly make. General information only.',
 {costs:['Public agency: often low','Private: varies widely','Intercountry: travel plus fees'],helps:['Employer benefits','Tax credits','Grants'],disclaimer:'General information only.'}],
['adoption','Open adoption: contact agreements','In open adoptions, birth and adoptive families agree on contact \u2014 letters, calls, or visits. Clear written agreements, respectful boundaries, and child-centered flexibility make openness work. Laws on enforceability vary. General information only.',
 {elements:['Written contact agreement','Respectful boundaries','Child-centered flexibility','Legal review'],disclaimer:'General information only.'}],
['adoption','Talking to your child about adoption','Tell the adoption story early, honestly, and warmly, in age-appropriate layers. Affirm that adoption was a loving plan, welcome questions, and never frame birth parents as villains. Books and support groups help the whole family. General information only.',
 {guidance:['Start the story early','Be honest and warm','Welcome questions','Avoid villain narratives'],disclaimer:'General information only.'}],
['adoption','Transracial adoption considerations','Transracial adoptive parents commit to their child\u2019s racial and cultural identity: diverse community, honest talk about racism, cultural education, and mentors who share the child\u2019s background. Love is the start, not the whole job. General information only.',
 {commitments:['Diverse community ties','Honest talk about racism','Cultural education','Same-background mentors'],disclaimer:'General information only.'}],
['adoption','Adoption disruption and support','Some adoptions struggle. Early intervention \u2014 therapy, respite, parent coaching \u2014 prevents disruption. If a placement cannot continue, agencies must plan responsibly for the child. Seeking help is strength, not failure. General information only.',
 {supports:['Early therapy','Respite care','Parent coaching','Agency planning if needed'],disclaimer:'General information only.'}],
['adoption','Stepparent and relative adoption','Stepparents and relatives adopt through a streamlined court process, often with home study waivers and consent requirements. Legal counsel familiar with local family court is essential. The child\u2019s best interest governs every decision. General information only.',
 {notes:['Often streamlined process','Consent requirements apply','Local family counsel essential','Best-interest standard'],disclaimer:'General information only.'}],
['child-protection','Recognizing signs of child maltreatment','Warning signs include unexplained injuries, extreme behavior changes, fear of caregivers, poor hygiene, and age-inappropriate knowledge. No single sign proves abuse, but patterns warrant a report to child protective services. Trust careful observation. General information only.',
 {signs:['Unexplained injuries','Extreme behavior changes','Fear of caregivers','Neglect indicators'],action:'Report patterns to child protective services.',disclaimer:'General information only.'}],
['child-protection','How to report suspected child abuse','Reports go to child protective services or law enforcement hotlines, many 24/7. Give the child\u2019s information, what you observed, and when. Reporters can often remain anonymous, and good-faith reports are protected by law. General information only.',
 {steps:['Call CPS or law enforcement hotline','Give facts observed','Note dates and details','Good-faith reports are protected'],disclaimer:'General information only.'}],
['child-protection','Mandatory reporters: who must report','Teachers, doctors, social workers, and childcare providers are typically mandatory reporters who must alert authorities to suspected maltreatment. Training covers recognition and reporting duties. Know your state\u2019s list and timeline. General information only.',
 {who:['Teachers and school staff','Medical professionals','Social workers','Childcare providers'],duty:'Know your state\u2019s requirements.',disclaimer:'General information only.'}],
['child-protection','What happens after a CPS report','After a report, CPS screens it in or out, may investigate with interviews and home visits, and decides on services, safety plans, or court action. Reporters are rarely told outcomes due to privacy laws. The process aims at child safety. General information only.',
 {stages:['Screening decision','Investigation','Safety planning or services','Possible court action'],note:'Outcomes are usually confidential.',disclaimer:'General information only.'}],
['child-protection','Safety planning for families','Safety plans set concrete steps to keep children safe during CPS involvement: supervision arrangements, hazard removal, service attendance, and check-in schedules. Families who engage honestly with plans do better. General information only.',
 {elements:['Supervision arrangements','Hazard removal','Service attendance','Check-in schedule'],disclaimer:'General information only.'}],
['child-protection','Preventing child maltreatment','Prevention works: home visiting programs, parenting support, concrete help with food and housing, and community connections reduce risk. Stressed caregivers should seek help early \u2014 support lines exist in every state. General information only.',
 {strategies:['Home visiting programs','Parenting support','Concrete economic help','Community connections'],encouragement:'Seek help early.',disclaimer:'General information only.'}],
['child-protection','Supporting a child who discloses abuse','When a child discloses abuse: stay calm, believe them, avoid leading questions, reassure them it is not their fault, and report promptly. Do not confront the alleged abuser. Write down what the child said verbatim. General information only.',
 {response:['Stay calm and believe','Avoid leading questions','Reassure: not their fault','Report promptly','Document verbatim'],disclaimer:'General information only.'}],
['child-protection','The role of the guardian ad litem','Courts appoint guardians ad litem or CASAs to speak for the child\u2019s best interest in dependency cases. They visit, review records, and recommend placements and services to the judge. Their independent voice centers the child. General information only.',
 {role:['Independent best-interest advocate','Visits and record review','Recommendations to the judge'],disclaimer:'General information only.'}]
];
function genExpansion(seed,opts){
  var i=(seed-EXPAND_AFTER-1)%NEW_WELFARE.length;
  var e=NEW_WELFARE[i];
  if(opts&&opts.category&&NEW_CATS.indexOf(opts.category)>=0){
    var pool=NEW_WELFARE.filter(function(x){return x[0]===opts.category;});
    e=pool[i%pool.length];
  }
  return mkRec(seed,e[0],e[1],e[2],e[3],'signature',SIGSRC);
}

function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  if(seed>EXPAND_AFTER)return genExpansion(seed,opts);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=2000)cat="development-stage";
    else if(s<=3500)cat="method";
    else if(s<=8000)cat="topic";
    else if(s<=9000)cat="daily-plan";
    else cat="qa";
  }
  function ord(base){return explicit?(s-1):(s-base);}
  var topicCats=["health","nutrition","safety","education","behavior","family"];
  if(cat==="development-stage")return stageRec(seed,ord(1));
  if(cat==="method")return methodRec(seed,ord(2001));
  if(cat==="topic")return topicRec(seed,ord(3501));
  if(topicCats.indexOf(cat)>=0)return topicRec(seed,ord(3501));
  if(cat==="daily-plan")return planRec(seed,ord(8001));
  if(cat==="qa")return qaRec(seed,ord(9001));
  return stageRec(seed,ord(1));
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-PAR-\d{6,7}$/.test(r.id||""))e.push("id");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if((CATS.concat(NEW_CATS)).indexOf(r.category)<0)e.push("category");
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
var gen={version:"jahdb-parenting-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("parenting",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
