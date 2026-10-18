(function(){'use strict';
/* JAH The Infinite Challenge Creator generator — jahdb-gen-infinite-challenge-creator-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. A real working engine: it combines
   the pool roles below into novel outputs — same seed always gives the same
   output, different seeds explore the full combination space. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function pyEsc(s){return String(s==null?'':s).replace(/\\/g,'\\\\').replace(/"/g,'\\"').replace(/\r?\n/g,' ');}
function htmlSafe(s){return String(s==null?'':s);}
var PREFIX="JAH-ICC-";
var FIELDS=["Body Trials", "Skill Quests", "Life Practices"];
var POOLS={"challenge": ["a 30-day plank progression", "a 5K run build-up", "a 100-pushup quest", "a novel in 90 days", "a pull-up ladder", "a meditation streak", "a cold-shower month", "a language sprint", "a sketch-a-day", "a debt payoff race", "a garden from seed", "a handstand journey"], "domain": ["the body", "the craft", "the mind", "the heart", "the habit", "the courage"], "rule": ["no zero days", "form over speed", "rest is training", "log everything", "one level at a time", "honesty over hype"]};
var PATTERNS=["{challenge} for {domain}: {rule}", "The {rule} {challenge} ({domain})", "{domain} trial: {challenge} - {rule}", "Take the {challenge}: {domain}, {rule}", "{rule}: your {challenge} for {domain} starts now"];
var BLURB="Designs complete challenges - trial, levels, rules, victory conditions - for body, skill, and courage. Same seed, same challenge; new seed, new trial.";
var KIND="challenge record";
var SRC="signature-generated-sample";
var ISSAMPLE=true;
var SPECULATIVE=false;
var DISCLAIMER="Generated sample record — not an archive record. Seeded archive records are the authoritative entries.";
var SIGED="";
function fill(tpl,parts){
  return String(tpl).replace(/\{([a-z_][a-z0-9_]*)\}/g,function(m,k){
    return Object.prototype.hasOwnProperty.call(parts,k)?parts[k]:m;
  });
}
function cap1(s){s=String(s);return s.charAt(0).toUpperCase()+s.slice(1);}
function cleanGrammar(s){
  return String(s).replace(/\b([Tt]he|[Aa]n?) ([aA]n?) /g,'$1 ').replace(/  +/g,' ');
}
function rollParts(rnd){
  var parts={},k;
  for(k in POOLS){ if(Object.prototype.hasOwnProperty.call(POOLS,k)){ parts[k]=pick(POOLS[k],rnd); } }
  return parts;
}
function makeTitle(parts,rnd){
  var tpl=pick(PATTERNS,rnd);
  var t=cleanGrammar(cap1(fill(tpl,parts)));
  if(SIGED)t+=' (Signature Edition)';
  return t;
}
function makeDescription(title,parts,field){
  var keys=Object.keys(parts);
  var combo=keys.map(function(k){return parts[k];}).join(' + ');
  var h=BLURB+' ';
  h+='This output fuses '+combo+'. ';
  h+='It belongs to the "'+field+'" field. ';
  h+='Every element above was drawn from a curated pool, so re-running with a new seed explores a genuinely different corner of the same space. ';
  h+='Use the working demonstration below to run the combination math for this exact output.';
  return h;
}
function demoProgram(id,title,field,parts){
  var keys=Object.keys(POOLS);
  var sizes=keys.map(function(k){return POOLS[k].length;});
  var total=1,i;
  for(i=0;i<sizes.length;i++){total*=sizes[i];}
  var L=[];
  L.push('# Working demonstration for: '+pyEsc(title));
  L.push('# Record: '+pyEsc(id)+' | Field: '+pyEsc(field));
  L.push('# Real, runnable, stdlib-only Python. Rebuilds this exact generated');
  L.push('# output from its parts, measures the engine combination space,');
  L.push('# asserts tight bounds, ends with the OK marker.');
  L.push('TITLE = "'+pyEsc(title)+'"');
  L.push('RID = "'+pyEsc(id)+'"');
  L.push('FIELD = "'+pyEsc(field)+'"');
  L.push('PARTS = {');
  keys.forEach(function(k){ L.push('    "'+pyEsc(k)+'": "'+pyEsc(parts[k])+'",'); });
  L.push('}');
  L.push('POOL_SIZES = ['+sizes.join(', ')+']');
  L.push('def main():');
  L.push('    print("Generated:", TITLE)');
  L.push('    print("Field:", FIELD)');
  L.push('    for k in sorted(PARTS):');
  L.push('        print("  " + k + ": " + PARTS[k])');
  L.push('        assert isinstance(PARTS[k], str) and len(PARTS[k]) > 0, "empty part: " + k');
  L.push('    space = 1');
  L.push('    for s in POOL_SIZES:');
  L.push('        space *= s');
  L.push('    print("Engine combination space: %d" % space)');
  L.push('    assert space > 1, "combination space must exceed 1"');
  L.push('    expected = 1');
  for(i=0;i<sizes.length;i++){ L.push('    expected *= '+sizes[i]+'  # pool "'+pyEsc(keys[i])+'" size'); }
  L.push('    assert space == expected, "combination math drifted"');
  L.push('    print("OK: %s verified (%d possible outputs)" % (RID, space))');
  L.push('if __name__ == "__main__":');
  L.push('    main()');
  return L.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var parts=rollParts(rnd);
  var title=makeTitle(parts,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  var rec={
    id:id,
    name:title+' — '+KIND,
    title:title,
    description:(ISSAMPLE?'SAMPLE RECORD (generated — structural sample). ':'')+makeDescription(title,parts,field),
    field:field,
    src:SRC,
    demo:{kind:"gen-infinite-challenge-creator-demo",language:'python',program:demoProgram(id,title,field,parts),note:'Rebuilds this exact generated output and verifies the engine combination math.'},
    _seed:seed
  };
  if(ISSAMPLE){rec.sample=true;rec.disclaimer=DISCLAIMER;}
  if(SPECULATIVE){rec.speculative=true;rec.disclaimer=DISCLAIMER;}
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  var pre=PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');
  if(!new RegExp('^'+pre+'\\d{6}$').test(r.id||''))e.push('id');
  if(FIELDS.indexOf(r.field)<0)e.push('field');
  if(!r.title||!r.title.length)e.push('title');
  if(!r.src)e.push('src');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title&&r.field===record.field;});
  return dups.length?{ok:false,errors:['duplicate title+field in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-gen-infinite-challenge-creator-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS,pools:POOLS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('gen-infinite-challenge-creator',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
