/* Group B page stamper: builds db/<slug>/index.html from page-template.html */
var fs = require('fs'), path = require('path');
var base = '/home/hatch/workspace/jah-databases-new18';
var tpl = fs.readFileSync(path.join(base, 'data/paleontology/page-template.html'), 'utf8');
var NET = 'Part of the JAH Data Bases network (77 live databases plus this 18-database expansion), I can also describe boundless new __KIND__ records in archive style.';
var DBS = [
{slug:'paleontology',name:'JAH Paleontology Database',tagline:'Fossils, extinct species, eras, and dig sites.',ai:'JAH Paleontology Creator',kind:'fossil entry',prefix:'JAH-PAL-',genver:'jahdb-paleontology-1.0',
 cats:['dinosaur','marine-reptile','flying-reptile','prehistoric-mammal','invertebrate','plant','ancient-reptile','dig-site','era','field-note','hypothetical'],
 desc:'Fossils, extinct species, geologic eras, and dig sites — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s fossil archive (JAH-PAL- records) \u2014 dinosaurs, marine reptiles, flying reptiles, prehistoric mammals, invertebrates, plants, dig sites, and geologic eras \u2014 preserved as structured, searchable data.',
 prov:'Every record carries provenance: \u201Csourced\u201D for facts drawn from the curated real-taxon dataset, \u201Csignature\u201D for homegrown Signature-generator study material and boundless speculation. Headline facts were spot-checked against public science reporting.',
 greet:'I\u2019m the JAH Paleontology Creator. I know this archive\u2019s 10,000 fossil entries \u2014 dinosaurs, marine reptiles, prehistoric mammals, dig sites, and eras. Ask me to find one, explain one, or generate boundless new entries in archive style.'},
{slug:'sociology',name:'JAH Sociology Database',tagline:'Social theories, institutions, movements, and demographic patterns.',ai:'JAH Sociology Creator',kind:'sociology entry',prefix:'JAH-SOC-',genver:'jahdb-sociology-1.0',
 cats:['theory','thinker','institution','movement','demographic','method','concept','signature-study'],
 desc:'Social theories, thinkers, institutions, movements, and demographic patterns — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s sociology archive (JAH-SOC- records) \u2014 theories, thinkers, institutions, movements, demographics, methods, and concepts \u2014 preserved as structured, searchable data.',
 prov:'Every record carries provenance: \u201Csourced\u201D for facts drawn from the curated sociological dataset, \u201Csignature\u201D for homegrown Signature-generator study exercises.',
 greet:'I\u2019m the JAH Sociology Creator. I know this archive\u2019s 10,000 sociology entries \u2014 theories, thinkers, institutions, movements, and methods. Ask me to find one, explain one, or generate boundless new entries in archive style.'},
{slug:'parenting',name:'JAH Parenting Database',tagline:'Child development stages, parenting methods, and family guidance.',ai:'JAH Parenting Creator',kind:'parenting guide',prefix:'JAH-PAR-',genver:'jahdb-parenting-1.0',
 cats:['development-stage','method','health','nutrition','safety','education','behavior','family','daily-plan','qa'],
 desc:'Child development stages, parenting methods, and family guidance — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s parenting archive (JAH-PAR- records) \u2014 developmental stages, parenting methods, health, nutrition, safety, education, behavior, and family topics \u2014 preserved as structured, searchable data. General information only.',
 prov:'Every record carries provenance: \u201Csourced\u201D for standard milestones, established methods, and widely shared guidance, \u201Csignature\u201D for homegrown Signature-generator planning material. General information only, never medical advice.',
 greet:'I\u2019m the JAH Parenting Creator. I know this archive\u2019s 10,000 parenting guides \u2014 development stages, methods, health, nutrition, safety, and family topics. Ask me to find one, explain one, or generate boundless new guides in archive style.'},
{slug:'pets',name:'JAH Pet Care Database',tagline:'Pet breeds, care guides, health, nutrition, and training.',ai:'JAH Pet Creator',kind:'pet care entry',prefix:'JAH-PET-',genver:'jahdb-pets-1.0',
 cats:['dog-breed','cat-breed','bird','fish','reptile','small-mammal','care-guide','health-note','training-tip','new-owner-checklist'],
 desc:'Pet breeds, care guides, health, nutrition, and training — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s pet care archive (JAH-PET- records) \u2014 dog and cat breeds, birds, fish, reptiles, small mammals, care guides, health notes, and training tips \u2014 preserved as structured, searchable data.',
 prov:'Every record carries provenance: \u201Csourced\u201D for facts drawn from the curated breed and species dataset (spot-checked against public breed references), \u201Csignature\u201D for homegrown Signature-generator checklists. Health notes are general information; see a veterinarian.',
 greet:'I\u2019m the JAH Pet Creator. I know this archive\u2019s 10,000 pet care entries \u2014 breeds, care guides, health notes, and training tips. Ask me to find one, explain one, or generate boundless new entries in archive style.'},
{slug:'photography',name:'JAH Photography Database',tagline:'Cameras, lenses, techniques, composition, and lighting.',ai:'JAH Photography Creator',kind:'photography entry',prefix:'JAH-PHO-',genver:'jahdb-photography-1.0',
 cats:['camera','lens','technique','composition','lighting','film','genre','accessory','shoot-plan'],
 desc:'Cameras, lenses, techniques, composition, and lighting — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s photography archive (JAH-PHO- records) \u2014 cameras, lenses, techniques, composition, lighting, film stocks, genres, and accessories \u2014 preserved as structured, searchable data.',
 prov:'Every record carries provenance: \u201Csourced\u201D for facts drawn from the curated photographic dataset, \u201Csignature\u201D for homegrown Signature-generator shoot plans.',
 greet:'I\u2019m the JAH Photography Creator. I know this archive\u2019s 10,000 photography entries \u2014 cameras, lenses, techniques, composition, and lighting. Ask me to find one, explain one, or generate boundless new entries in archive style.'},
{slug:'publishing',name:'JAH Publishing Database',tagline:'Publishing processes, formats, genres, and industry records.',ai:'JAH Publishing Creator',kind:'publishing entry',prefix:'JAH-PUB2-',genver:'jahdb-publishing-1.0',
 cats:['process','format','genre','role','history','industry-record','publishing-plan'],
 desc:'Publishing processes, formats, genres, and industry records — a permanent archive, a boundless generator, and an archive-aware AI.',
 about:'This database\u2019s publishing archive (JAH-PUB2- records) \u2014 processes, formats, genres, roles, history, and industry records \u2014 preserved as structured, searchable data.',
 prov:'Every record carries provenance: \u201Csourced\u201D for facts drawn from the curated publishing dataset, \u201Csignature\u201D for homegrown Signature-generator publishing plans.',
 greet:'I\u2019m the JAH Publishing Creator. I know this archive\u2019s 10,000 publishing entries \u2014 processes, formats, genres, roles, and history. Ask me to find one, explain one, or generate boundless new entries in archive style.'}
];
function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;');}
DBS.forEach(function(d){
  var h = tpl;
  var catsJS = JSON.stringify(d.cats);
  var opts = d.cats.map(function(c){return '<option value="'+c+'">'+c.replace(/-/g,' ')+'</option>';}).join('');
  var ctx = 'Archive holds 10,000 '+d.kind+' records across categories: '+d.cats.join(', ')+'. '+NET.replace(/__KIND__/g,d.kind);
  var schema = 'id \u00B7 title \u00B7 category \u00B7 record_kind \u00B7 summary \u00B7 details{\u2026} \u00B7 provenance \u00B7 source';
  var rep = {
    '__SLUG__': d.slug, '__NAME__': d.name, '__TAGLINE__': d.tagline,
    '__AI_NAME__': d.ai, '__KIND__': d.kind, '__PREFIX__': d.prefix,
    '__GENVER__': d.genver, '__DESC__': d.desc, '__ABOUT_ARCHIVE__': d.about,
    '__PROV_NOTE__': d.prov, '__GREET__': d.greet, '__CTX__': ctx,
    '__SCHEMA__': schema, '__CATS_JS__': catsJS, '__CAT_OPTS__': opts
  };
  Object.keys(rep).forEach(function(k){
    h = h.split(k).join(rep[k]);
  });
  if (/__[A-Z_]+__/.test(h)) { console.log('UNREPLACED PLACEHOLDER in ' + d.slug); process.exit(1); }
  var out = path.join(base, 'db', d.slug, 'index.html');
  fs.mkdirSync(path.dirname(out), {recursive: true});
  fs.writeFileSync(out, h);
  console.log('wrote ' + out + ' (' + h.length + ' bytes)');
});
