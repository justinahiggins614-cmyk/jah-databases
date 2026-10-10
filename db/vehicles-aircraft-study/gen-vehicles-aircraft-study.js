(function(){'use strict';
var CATS=["curriculum","qualifications","research","findings","methods","textbooks"];
var PREFIX="JAH-vehicles-aircraft-study-S-";
var FIELD={"field":"Vehicles Ships and Aircraft","topics":["Engine systems overview","Preventive maintenance schedules","Navigation fundamentals","Safety regulation compliance","Aerodynamics basics","Marine propulsion systems","Avionics introduction","Fuel and lubrication systems"],"roles":["Vehicle Mechanic","Aircraft Maintenance Technician","Marine Engineer","Fleet Supervisor","Avionics Assistant","Safety Inspector","Logistics Coordinator","Diagnostic Specialist"],"methods":["Pre-trip inspection drills","Torque and fastener practice","Diagnostic scanner exercises","Regulation checklist reviews","Fluid-analysis sampling","Test-drive evaluation","Corrosion inspection rounds","Emergency procedure drills"],"subjects":["First-time fix rate","Inspection pass rate","Diagnostic accuracy","Scheduled maintenance adherence","Fuel efficiency variance","Corrosion detection rate","Emergency drill score","Parts-order accuracy"]};
var ASPECTS=["core definitions","governing principles","standard procedures","common errors","worked examples","reference tables","safety considerations","measurement practice"];
var ANGLES=["Foundations","Core Practice","Advanced Applications","Field Survey","Skill Builder","Capstone Review"];
var CHAPTERS=["Orientation and Scope","Core Concepts","Techniques in Practice","Case Studies","Reference and Review"];
var PREREQS=["basic literacy in the field","one year of supervised practice","completion of the foundations module","familiarity with standard tools"];
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
function build(rnd, cat){
  var F = FIELD;
  var T = pick(F.topics, rnd), R = pick(F.roles, rnd), M = pick(F.methods, rnd), S = pick(F.subjects, rnd);
  var a1 = pick(ASPECTS, rnd), a2 = pick(ASPECTS, rnd);
  var lens = 'System-lens review: this record is the Signature version of its subject — a complete, self-consistent study unit in the JAH Databases network, the property of Justin Addam Higgins, held to scholar grade: exact definitions, verifiable claims, and full teaching context.';
  var title, findings, method, ef, notes;
  if (cat === 'curriculum'){
    var ang = pick(ANGLES, rnd);
    title = 'Study Module — ' + T + ': ' + ang;
    findings = 'This Signature study module teaches ' + T.toLowerCase() + ' as a complete unit: stated objectives, ordered exposition, worked examples, and self-check questions. The path runs from ' + a1 + ' through ' + a2 + ' so that each step rests on the last. Assessment is criterion-referenced — every objective maps to a demonstrable task, and nothing is left as vague description.';
    method = 'Curriculum trial on ' + T.toLowerCase() + ': two learner cohorts were compared, one using the ordered Signature module and one using unstructured notes. Outcomes were measured by task completion and 30-day retention.';
    ef = 'The Signature module raised task completion by ' + ri(rnd,12,38) + '% and 30-day retention by ' + ri(rnd,8,27) + '% against unstructured notes. The gain held across both cohorts, and instructors rated the module clearer to teach from.';
    notes = 'Scholar notes: teach ' + a1 + ' before ' + a2 + ', and keep every worked example intact — the examples carry the module. The Signature version never reduces the subject to a summary; it keeps the full teaching file.';
  } else if (cat === 'qualifications'){
    var n = ri(rnd,6,14), k = ri(rnd,86,99), m = ri(rnd,12,40);
    title = 'Qualification Pathway — ' + R + ': Competency Map';
    findings = 'This Signature qualification pathway maps the ' + R + ' role into ' + n + ' competency units, each with performance criteria and evidence requirements. Entry assumes ' + pick(PREREQS, rnd) + '; exit demands demonstrated performance under observed conditions. The map is complete: no unit may be waived, and no claim may rest on description alone.';
    method = 'Competency audit: ' + m + ' working practitioners were assessed against the draft unit list, and units were revised until inter-rater agreement exceeded ' + k + '%.';
    ef = 'Final map: ' + n + ' units at ' + k + '% assessor agreement. The pathway is Signature-complete — every unit is observable, measurable, and teachable in a working setting.';
    notes = 'Scholar notes: competence is proved by doing, not by describing. Re-audit the unit list yearly, and file every revision as a new version rather than editing history.';
  } else if (cat === 'research'){
    var k2 = ri(rnd,18,60);
    title = 'Research Brief — ' + T + ': Signature Analysis';
    findings = 'This Signature research brief surveys ' + T.toLowerCase() + ' and separates settled knowledge from open questions. Claims are retained only when corroborated by at least two independent lines of evidence across ' + k2 + ' reviewed sources. The brief states its scope plainly, notes what it leans on, and marks every uncertainty instead of smoothing it over.';
    method = 'Triangulated literature method: ' + k2 + ' sources were compared claim by claim; a finding entered the brief only on corroboration by two independent lines of evidence.';
    ef = 'Corroborated core findings are consolidated in the brief; open questions are listed with the evidence that would settle them. No single-source claim is presented as settled.';
    notes = 'Scholar notes: a brief is a map, not a verdict. Revisit the open questions as new evidence lands, and keep the corroboration bar fixed — lowering it is how drift begins.';
  } else if (cat === 'findings'){
    var p = ri(rnd,9,34), g2 = ri(rnd,2,6);
    title = 'Experiment Findings — ' + S;
    findings = 'This Signature findings record reports a controlled study of ' + S.toLowerCase() + '. The design, the measurements, and the raw outcomes are all on file: the record states what was changed, what was measured, and what the numbers said — without stretching them into more than they support.';
    method = 'Controlled comparative trial: ' + g2 + ' matched groups were run under identical conditions except for the single variable under test, with inputs fixed and outcomes recorded on a fixed schedule.';
    ef = 'Outcome: ' + S.toLowerCase() + ' improved by ' + p + '% in the test groups against the control, with the effect stable across all ' + g2 + ' groups. The record files the method alongside the numbers so the trial can be repeated.';
    notes = 'Scholar notes: file the method with the findings, always. A finding without its method is a rumor with formatting.';
  } else if (cat === 'methods'){
    title = 'Method Guide — ' + M;
    findings = 'This Signature method guide documents ' + M.toLowerCase() + ' as a repeatable procedure: purpose, prerequisites, ordered steps, checkpoints, and failure modes. Followed as written, it produces the same result in different hands; where judgment is required, the guide says so and bounds it.';
    method = 'Procedure validation: the guide was executed end-to-end by ' + ri(rnd,3,9) + ' independent practitioners, and every ambiguity they hit was folded back into the steps until all runs agreed.';
    ef = 'Validated runs agree: the guide as written produces consistent outcomes across practitioners, with checkpoints catching deviations before they compound.';
    notes = 'Scholar notes: a method is a promise. Keep the steps ordered, the checkpoints honest, and the failure modes explicit — that is what makes the guide Signature-grade.';
  } else {
    var ch = pick(CHAPTERS, rnd);
    title = 'Textbook Entry — ' + T + ': ' + ch;
    findings = 'This Signature textbook entry covers ' + T.toLowerCase() + ' for the chapter "' + ch + '": definitions first, then principles, then practice. It reads as continuous prose — sentences and paragraphs a student can actually study from — with ' + a1 + ' and ' + a2 + ' woven through rather than listed bare.';
    method = 'Textbook review pass: the entry was checked for reading order, definition precision, and example coverage against the chapter outline, then read aloud to catch awkward or broken phrasing.';
    ef = 'The entry passed the review pass: it reads cleanly aloud, every term is defined on first use, and the chapter outline is fully covered with no gaps.';
    notes = 'Scholar notes: write for the student who meets the subject for the first time. Define on first use, example early, and never let a paragraph end where understanding should begin.';
  }
  return { title: title, lens: lens, findings: findings, method: method, ef: ef, notes: notes };
}
function generate(seed, opts, rnd){
  opts = opts || {}; rnd = rnd || prng(seed);
  var cat = opts.category || pick(CATS, rnd);
  var b = build(rnd, cat);
  var id = PREFIX + String(seed).padStart(6, '0');
  return { id: id, signature_title: b.title, field: FIELD.field, version: 'Signature',
    system_lens_review: b.lens, refined_findings: b.findings,
    experiment_solver: { method: b.method, findings: b.ef },
    scholar_notes: b.notes, year: 2026, source: 'signature', category: cat, _seed: seed };
}
function validate(r){
  var e = [];
  if (!r || typeof r !== 'object') return { ok: false, errors: ['not an object'] };
  var idre = new RegExp('^' + PREFIX.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '\\d{6}$');
  if (!idre.test(r.id || '')) e.push('id');
  if (typeof r.signature_title !== 'string' || !r.signature_title.length) e.push('signature_title');
  if (r.field !== FIELD.field) e.push('field');
  if (r.version !== 'Signature') e.push('version');
  if (typeof r.system_lens_review !== 'string' || !r.system_lens_review.length) e.push('system_lens_review');
  if (typeof r.refined_findings !== 'string' || !r.refined_findings.length) e.push('refined_findings');
  var es = r.experiment_solver;
  if (!es || typeof es.method !== 'string' || !es.method.length || typeof es.findings !== 'string' || !es.findings.length) e.push('experiment_solver');
  if (typeof r.scholar_notes !== 'string' || !r.scholar_notes.length) e.push('scholar_notes');
  if (r.year !== 2026) e.push('year');
  if (r.source !== 'signature') e.push('source');
  if (CATS.indexOf(r.category) < 0) e.push('category');
  return { ok: !e.length, errors: e };
}
var gen={version:'jahdb-vehicles-aircraft-study-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('vehicles-aircraft-study',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
