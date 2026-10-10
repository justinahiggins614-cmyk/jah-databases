// C6 full-file completeness auditor for jah-databases slice (indices 57-76).
// Usage: node audit-slice.js
// Per DB: samples 20 records from data/<slug>/chunks/*.jsonl.gz, runs the
// generator's own validate() on each, plus extra stub/generic-body checks,
// key-set drift vs a fresh generate(), and runs generate() for 5 seeds.
(function(){
'use strict';
const fs = require('fs');
const path = require('path');
const ROOT = path.resolve(__dirname, '..');
const zlib = require('zlib');

const SLUGS = ['pharma-drugs','preference-pairs','prompt-collection','rag-qa','real-estate',
'reasoning-traces','redteam-probes','regex-patterns','repair-recovery','research-papers',
'safety-refusals','sports-stats','startup-funding','stock-timeseries','summarization-pairs',
'threat-intel','tool-trajectories','unit-tests','weather-climate','web-browsing-tasks'];

const SEEDS = [1, 7, 42, 999, 12345];

function prng(seed){ var a=(seed>>>0)||1; return function(){ a|=0; a=(a+0x6D2B79F5)|0; var t=Math.imul(a^(a>>>15),1|a); t=(t+Math.imul(t^(t>>>7),61|t))^t; return ((t^(t>>>14))>>>0)/4294967296; }; }

function readChunks(slug){
  const dir = path.join(ROOT, 'data', slug, 'chunks');
  const files = fs.readdirSync(dir).filter(f=>f.endsWith('.jsonl.gz')).sort();
  const recs = [];
  for(const f of files){
    const raw = zlib.gunzipSync(fs.readFileSync(path.join(dir,f))).toString('utf8');
    for(const line of raw.split('\n')){
      if(line.trim()) recs.push(line);
    }
  }
  return {files: files.length, lines: recs};
}

function sampleLines(lines, n){
  // deterministic evenly-spread sample
  if(lines.length <= n) return lines.map((l,i)=>({idx:i,line:l}));
  const out=[]; const step=lines.length/n;
  const r=prng(20261009);
  for(let i=0;i<n;i++){
    const idx=Math.min(lines.length-1, Math.floor(i*step + r()*step));
    out.push({idx, line: lines[idx]});
  }
  return out;
}

const BODY_FIELDS = ['description','body','content','text','transcript','summary','abstract','article','report','record','entry','detail','details','narrative','dossier','message','answer','response','explanation','reasoning','trace'];
const PLACEHOLDER_RE = /lorem ipsum|\bTBD\b|\bTODO\b|placeholder|sample text|insert .* here|\[.*\]|\.\.\.$/i;

function stubCheck(rec){
  // find "title-like" and "body-like" fields heuristically
  const keys = Object.keys(rec);
  const titleKey = keys.find(k=>/title|name|subject|headline|label/i.test(k));
  const bodyKeys = keys.filter(k=>BODY_FIELDS.some(b=>k.toLowerCase().includes(b)));
  const issues = [];
  for(const bk of bodyKeys){
    const v = rec[bk];
    if(typeof v === 'string'){
      if(!v.trim()) issues.push(bk+':empty-string');
      else if(v.length < 20) issues.push(bk+':suspiciously-short('+v.length+' chars)');
      else if(PLACEHOLDER_RE.test(v.slice(0,400))) issues.push(bk+':looks-like-placeholder');
    } else if(Array.isArray(v)){
      if(!v.length) issues.push(bk+':empty-array');
    }
  }
  // empty-string scan across ALL string fields
  for(const k of keys){
    const v = rec[k];
    if(typeof v === 'string' && !v.trim()) issues.push(k+':empty-string');
  }
  return issues;
}

function idPrefix(slug){
  // derive expected id prefix from a fresh generate
  return null;
}

const report = [];
for(const slug of SLUGS){
  const entry = {slug, sample_size: 0, total_records: 0, chunks: 0,
    gen_seeds_ok: 0, gen_seed_errors: [], validate_defects: [], stub_defects: [],
    key_drift: [], id_mismatch: [], count_note: ''};
  try{
    const gen = require(path.join(ROOT, 'db', slug, 'gen-'+slug+'.js'));
    // 1) generator: 5 seeds
    const fresh = [];
    for(const s of SEEDS){
      try{
        const r = gen.generate(s);
        fresh.push(r);
        const v = gen.validate(r);
        if(v && v.ok) entry.gen_seeds_ok++;
        else entry.gen_seed_errors.push({seed:s, errors:(v&&v.errors)||['validate returned falsy']});
      }catch(e){ entry.gen_seed_errors.push({seed:s, errors:['generate threw: '+e.message.slice(0,200)]}); }
    }
    const freshKeys = fresh.length ? Object.keys(fresh[0]).sort() : [];
    const freshId = fresh.length ? fresh[0].id : null;

    // 2) data sample
    const {files, lines} = readChunks(slug);
    entry.chunks = files; entry.total_records = lines.length;
    const sampled = sampleLines(lines, 20);
    entry.sample_size = sampled.length;
    const seenIds = new Set();
    for(const {idx, line} of sampled){
      let rec;
      try{ rec = JSON.parse(line); }catch(e){ entry.validate_defects.push({line:idx, error:'JSON parse failed'}); continue; }
      const v = gen.validate(rec);
      if(!(v && v.ok)) entry.validate_defects.push({id: rec.id||('line '+idx), errors: v&&v.errors});
      const sk = stubCheck(rec);
      if(sk.length) entry.stub_defects.push({id: rec.id||('line '+idx), issues: sk});
      const rk = Object.keys(rec).sort();
      const missing = freshKeys.filter(k=>rk.indexOf(k)<0);
      const extra = rk.filter(k=>freshKeys.indexOf(k)<0);
      if(missing.length||extra.length) entry.key_drift.push({id: rec.id, missing, extra});
      if(rec.id){ if(seenIds.has(rec.id)) entry.id_mismatch.push('duplicate id in sample: '+rec.id); seenIds.add(rec.id); }
      // id should embed the numeric seed per generator convention: check prefix pattern
      if(freshId && rec.id){
        const fp = freshId.replace(/\d+$/,'');
        if(!rec.id.startsWith(fp)) entry.id_mismatch.push('id '+rec.id+' does not share prefix '+fp);
      }
    }
  }catch(e){
    entry.fatal = e.message.slice(0,300);
  }
  report.push(entry);
}

console.log(JSON.stringify(report, null, 1));
})();
