(function(){'use strict';
/* JAH Self-Upgrade Programs Database generator — jahdb-self-upgrade-programs-1.0.
   Property of Justin Addam Higgins (JAH).
   Generates REAL working self-upgrade programs: every record carries runnable
   code that upgrades itself (patch / extend / repair / optimize / version-bump).
   Deterministic: same seed, same program. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-SUP-';
var SYSTEMS=[['jah-system','JAH Signature System'],['phibes-pc','Phibes PC'],['general-pc','General PC (Windows/Linux)'],['web','Web / Browser']];
var SYS_SHORT={'jah-system':'JAH','phibes-pc':'Phibes PC','general-pc':'PC','web':'Web'};
var UTYPES=[['self-patch','Self-Patch'],['self-extend','Self-Extend'],['self-repair','Self-Repair'],['self-optimize','Self-Optimize'],['version-bump','Version Bump']];
var UTYPE_LABEL={};UTYPES.forEach(function(u){UTYPE_LABEL[u[0]]=u[1];});
var NAMES={
 'self-patch':['Self-Patcher','Auto-Patch Engine','Hotfix Applier','Patch Runner'],
 'self-extend':['Plugin Loader','Capability Extender','Module Hot-Swapper','Feature Grafter'],
 'self-repair':['Self-Healer','Config Doctor','Integrity Restorer','Auto-Fixer'],
 'self-optimize':['Self-Tuner','Performance Optimizer','Adaptive Cache','Efficiency Engine'],
 'version-bump':['Version Bumper','Release Stepper','Build Incrementer','Tag Advancer']};
var WHAT={
 'self-patch':'its own source code by applying patch hunks from a manifest, then rewrites itself with the new version',
 'self-extend':'its own capabilities by hot-loading new plugins or swapping function implementations at runtime without restart',
 'self-repair':'its own configuration and state by detecting corruption and restoring verified defaults',
 'self-optimize':'its own performance parameters by measuring its hit rate and resizing itself toward the optimum',
 'version-bump':'its own version constant by incrementing it and re-saving its own file'};
var HOW={
 'self-patch':'Reads a patch manifest, verifies each hunk exists in its own source, applies replacements, bumps the VERSION constant, and writes the file back to disk. Aborts safely if any hunk is missing.',
 'self-extend':'Scans a plugin directory (or function registry), loads new code into the running process, and registers it — new behavior is live immediately with no restart.',
 'self-repair':'Loads its config inside a guarded try block, validates every required key, and on any failure rewrites the file with known-good defaults before continuing.',
 'self-optimize':'Tracks hits and misses over a window, computes the hit rate, and applies a grow/shrink rule to its own capacity, then resets the counters for the next window.',
 'version-bump':'Parses its own VERSION constant with a regex, increments the patch number, replaces the constant in its own source text, and saves the file.'};
var RUN={
 'python':'Run: python3 program.py — needs no dependencies. Watch it modify/repair/tune itself and print what changed.',
 'javascript':'Run: node program.js — or paste into a browser console. Call the upgrade functions shown in the demo comments.',
 'shell':'Run: chmod +x program.sh && ./program.sh — point UPDATE_URL at a folder containing VERSION and program.sh to see a live upgrade.',
 'batch':'Run on Phibes PC / Windows: program.bat — place a VERSION file and program.bat update in the manifest folder to see a live upgrade.'};
var MANIFEST={'python':'patches/','javascript':'registry/','shell':'https://updates.example.com','batch':'updates'};
var TPL_META=[
 ['py_self_patch','self-patch','python'],
 ['js_hotswap','self-extend','javascript'],
 ['sh_self_update','self-patch','shell'],
 ['py_self_repair','self-repair','python'],
 ['py_version_bump','version-bump','python'],
 ['py_plugin_loader','self-extend','python'],
 ['py_self_tune','self-optimize','python'],
 ['bat_self_update','self-patch','batch']];
function codeFor(tpl,ver,manifest){
var T={
py_self_patch:'#!/usr/bin/env python3\n"""Self-Patcher v'+ver+' — patches its own code from a patch manifest, then bumps its version."""\nimport json, os\n\nVERSION = "'+ver+'"\nPATCH_MANIFEST = "'+manifest+'"\n\ndef fetch_patch(path):\n    if not os.path.exists(path):\n        return None\n    with open(path) as f:\n        return json.load(f)\n\ndef apply_patch(patch):\n    self_path = os.path.abspath(__file__)\n    with open(self_path) as f:\n        src = f.read()\n    for rep in patch.get("replacements", []):\n        if rep["old"] not in src:\n            print("patch hunk not found - aborting safely")\n            return False\n        src = src.replace(rep["old"], rep["new"], 1)\n    src = src.replace(\'VERSION = "%s"\' % VERSION, \'VERSION = "%s"\' % patch["version"], 1)\n    with open(self_path, "w") as f:\n        f.write(src)\n    print("self-upgraded %s -> %s" % (VERSION, patch["version"]))\n    return True\n\ndef main():\n    patch = fetch_patch(PATCH_MANIFEST)\n    if not patch:\n        print("no patch manifest found - v%s is current" % VERSION)\n        return\n    if patch.get("version") == VERSION:\n        print("already at latest version")\n        return\n    apply_patch(patch)\n\nif __name__ == "__main__":\n    main()\n',
js_hotswap:'// Self-Upgrading Module v'+ver+' - hot-swaps its own functions at runtime.\nvar SelfUpgrade = {\n  version: "'+ver+'",\n  registry: {},\n  upgrade: function(name, fnBody, argNames) {\n    var args = (argNames || "a,b").split(",");\n    var Ctor = Function.bind.apply(Function, [null].concat(args.concat([fnBody])));\n    var fn = new Ctor();\n    this[name] = fn;\n    this.registry[name] = fnBody;\n    console.log("self-upgraded function: " + name);\n  },\n  add: function(a, b) { return a + b; }\n};\n// demo: SelfUpgrade.upgrade("add", "return a * b;"); // add() now multiplies\nif (typeof module !== "undefined") module.exports = SelfUpgrade;\n',
sh_self_update:'#!/bin/bash\n# Self-Upgrading Script v'+ver+'\nVERSION="'+ver+'"\nUPDATE_URL="'+manifest+'"\nSELF="$(readlink -f "$0" 2>/dev/null || realpath "$0")"\nREMOTE_VER="$(curl -s "$UPDATE_URL/VERSION" 2>/dev/null | tr -d \' \\r\\n\')"\nif [ -z "$REMOTE_VER" ]; then\n  echo "no update server reached - staying at v$VERSION"\n  exit 0\nfi\nif [ "$REMOTE_VER" = "$VERSION" ]; then\n  echo "already current (v$VERSION)"\n  exit 0\nfi\necho "self-upgrading v$VERSION -> v$REMOTE_VER"\ncurl -s "$UPDATE_URL/program.sh" -o "$SELF.new" || { echo "download failed"; exit 1; }\nmv "$SELF.new" "$SELF" && chmod +x "$SELF"\necho "done - re-run to use v$REMOTE_VER"\n',
py_self_repair:'#!/usr/bin/env python3\n"""Self-Repairing Config v'+ver+' - detects corruption and restores its own defaults."""\nimport json, os\n\nCONFIG = "'+manifest+'"\nDEFAULTS = {"version": "'+ver+'", "mode": "auto", "retries": 3, "log": True}\n\ndef load():\n    try:\n        with open(CONFIG) as f:\n            cfg = json.load(f)\n        for key in DEFAULTS:\n            if key not in cfg:\n                raise ValueError("missing key: %s" % key)\n        return cfg\n    except Exception as exc:\n        print("config corrupted (%s) - self-repairing with defaults" % exc)\n        with open(CONFIG, "w") as f:\n            json.dump(DEFAULTS, f, indent=2)\n        return dict(DEFAULTS)\n\ndef self_check():\n    cfg = load()\n    print("config OK: v%s mode=%s" % (cfg["version"], cfg["mode"]))\n    return cfg\n\nif __name__ == "__main__":\n    self_check()\n',
py_version_bump:'#!/usr/bin/env python3\n"""Version-Bump v'+ver+' - increments its own version constant and re-saves itself."""\nimport os, re\n\nVERSION = "'+ver+'"\n\ndef bump():\n    path = os.path.abspath(__file__)\n    with open(path) as f:\n        src = f.read()\n    m = re.search(r\'VERSION = "(\\\\d+)\\\\.(\\\\d+)\\\\.(\\\\d+)"\', src)\n    if not m:\n        print("version line not found - cannot self-bump")\n        return\n    new = "%d.%d.%d" % (int(m.group(1)), int(m.group(2)), int(m.group(3)) + 1)\n    src = src.replace(\'VERSION = "%s"\' % VERSION, \'VERSION = "%s"\' % new, 1)\n    with open(path, "w") as f:\n        f.write(src)\n    print("self-bumped %s -> %s" % (VERSION, new))\n\nif __name__ == "__main__":\n    bump()\n',
py_plugin_loader:'#!/usr/bin/env python3\n"""Self-Extending Plugin Loader v'+ver+' - hot-loads new plugins without restart."""\nimport importlib.util, os\n\nPLUGIN_DIR = "'+manifest+'"\nVERSION = "'+ver+'"\n\ndef load_plugins():\n    loaded = {}\n    os.makedirs(PLUGIN_DIR, exist_ok=True)\n    for fn in sorted(os.listdir(PLUGIN_DIR)):\n        if not fn.endswith(".py") or fn.startswith("_"):\n            continue\n        name = fn[:-3]\n        if name in loaded:\n            continue\n        spec = importlib.util.spec_from_file_location(name, os.path.join(PLUGIN_DIR, fn))\n        mod = importlib.util.module_from_spec(spec)\n        spec.loader.exec_module(mod)\n        loaded[name] = mod\n        print("self-extended: loaded plugin \'%s\'" % name)\n    return loaded\n\ndef upgrade():\n    return load_plugins()\n\nif __name__ == "__main__":\n    plugins = load_plugins()\n    print("v%s: %d plugin(s) active" % (VERSION, len(plugins)))\n',
py_self_tune:'#!/usr/bin/env python3\n"""Self-Optimizing Cache v'+ver+' - tunes its own capacity from its hit rate."""\nVERSION = "'+ver+'"\n\nclass SelfTuningCache:\n    def __init__(self, size=100):\n        self.size = size\n        self.data = {}\n        self.hits = 0\n        self.misses = 0\n\n    def get(self, key):\n        if key in self.data:\n            self.hits += 1\n            return self.data[key]\n        self.misses += 1\n        return None\n\n    def put(self, key, value):\n        if len(self.data) >= self.size:\n            self.data.pop(next(iter(self.data)))\n        self.data[key] = value\n\n    def self_tune(self):\n        total = self.hits + self.misses\n        if not total:\n            return self.size\n        rate = self.hits / total\n        old = self.size\n        if rate > 0.90 and self.size < 10000:\n            self.size = int(self.size * 1.5)\n        elif rate < 0.50 and self.size > 10:\n            self.size = max(10, int(self.size * 0.75))\n        self.hits = self.misses = 0\n        print("self-tuned cache %d -> %d (hit rate %.1f%%)" % (old, self.size, rate * 100))\n        return self.size\n\nif __name__ == "__main__":\n    c = SelfTuningCache(100)\n    for i in range(200):\n        c.put("k%d" % i, i)\n    for i in range(200):\n        c.get("k%d" % (i % 50))\n    c.self_tune()\n',
bat_self_update:'@echo off\nREM Phibes PC Self-Updater v'+ver+'\nset VERSION='+ver+'\nset SELF=%~f0\necho [Phibes PC] checking for updates (current v%VERSION%)...\nif not exist "'+manifest+'\\VERSION" (\n  echo No update manifest found - staying at v%VERSION%.\n  exit /b 0\n)\nset /p REMOTE_VER=<"'+manifest+'\\VERSION"\nif "%REMOTE_VER%"=="%VERSION%" (\n  echo Already current (v%VERSION%).\n  exit /b 0\n)\necho Self-upgrading v%VERSION% to v%REMOTE_VER%...\ncopy /y "'+manifest+'\\program.bat" "%SELF%.new" >nul\nif errorlevel 1 (\n  echo Download failed - aborting safely.\n  exit /b 1\n)\nmove /y "%SELF%.new" "%SELF%" >nul\necho Done - re-run for v%REMOTE_VER%.\n'};
return T[tpl]||'';
}
function generate(seed,opts){
  opts=opts||{};var s=prng(seed);
  var ti=(s()*TPL_META.length)|0;
  var meta=TPL_META[ti],tpl=meta[0],utype=meta[1],lang=meta[2];
  if(opts.upgrade_type&&UTYPE_LABEL[opts.upgrade_type]){
    var cand=TPL_META.filter(function(m){return m[1]===opts.upgrade_type;});
    if(cand.length){var c=cand[(s()*cand.length)|0];tpl=c[0];utype=c[1];lang=c[2];}
  }
  var sys=pick(SYSTEMS,s);
  if(opts.target_system){var f=SYSTEMS.filter(function(x){return x[0]===opts.target_system;});if(f.length)sys=f[0];}
  var ver='1.'+((s()*9)|0)+'.'+((s()*20)|0);
  var code=codeFor(tpl,ver,MANIFEST[lang]);
  var pname=pick(NAMES[utype],s);
  var name=SYS_SHORT[sys[0]]+' '+pname;
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,name:name,
    title:name+' — '+UTYPE_LABEL[utype]+' for '+sys[1],
    description:'A '+lang+' program for '+sys[1]+' that upgrades '+WHAT[utype]+'. '+HOW[utype],
    program_name:pname,target_system:sys[0],system_label:sys[1],
    upgrade_type:utype,type_label:UTYPE_LABEL[utype],language:lang,
    what_it_upgrades:WHAT[utype],how_it_works:HOW[utype],
    code:code,run_instructions:RUN[lang],
    demo:{kind:'run-code',program:RUN[lang],note:'Save the code block as a file and run it — it upgrades itself and prints proof.'},
    src:'signature',year:2026,g:sys[0],_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  if(!/^JAH-SUP-\d{6}$/.test(r.id||''))e.push('id');
  if(typeof r.name!=='string'||r.name.length<3)e.push('name');
  if(SYSTEMS.map(function(x){return x[0];}).indexOf(r.target_system)<0)e.push('target_system');
  if(!UTYPE_LABEL[r.upgrade_type])e.push('upgrade_type');
  if(['python','javascript','shell','batch'].indexOf(r.language)<0)e.push('language');
  if(typeof r.code!=='string'||r.code.length<100)e.push('code');
  if(!r.src)e.push('src');
  return{ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.name===record.name&&r.target_system===record.target_system;});
  return dups.length?{ok:false,errors:['duplicate name+system in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-self-upgrade-programs-1.0',generate:generate,validate:validate,driftCheck:driftCheck,
  systems:SYSTEMS.map(function(x){return x[0];}),upgradeTypes:UTYPES.map(function(x){return x[0];})};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('self-upgrade-programs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
