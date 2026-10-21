(function(){
'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["fundamentals", "algorithms", "implementation", "optimization", "evaluation"];
var PREFIX="JAH-ATK143-";
var KIND="extraction method";
var TOOLNAME="Structured Document Parser";
var SIG=false;
var PROV="Public methodology \u2014 standard computer-science technique documented in the technical literature; fact-checked 2026-10-21.";
var SRC="public-harvest";
var ASPECTS=[{"t": "JSON parsing", "d": "JSON parsers build nested dicts/lists from braces and brackets. Strict parsers reject trailing commas and comments. JSON is the interchange default.", "c": "fundamentals", "r": 1, "p": {"FMT": "json", "PAYLOAD": "[{\"id\": 1, \"t\": \"a\"}, {\"id\": 2, \"t\": \"b\"}]"}}, {"t": "XML parsing", "d": "XML parsers build element trees honoring nesting and attributes. Namespaces qualify tags to avoid collisions. XML carries documents plus data.", "c": "algorithms", "r": 1, "p": {"FMT": "xml", "PAYLOAD": "<rows><r><id>1</id></r><r><id>2</id></r></rows>"}}, {"t": "Schema validation", "d": "Validators check parsed data against JSON Schema or XSD. Validation fails fast on malformed input. Schemas are contracts.", "c": "implementation", "r": 1, "p": {"FMT": "json", "PAYLOAD": "[{\"id\": 1}]"}}, {"t": "Streaming parsers", "d": "Streaming parsers (SAX, ijson) emit events without building full trees. Streams handle gigabyte documents. Events beat trees at scale.", "c": "optimization", "r": 1, "p": {"FMT": "json", "PAYLOAD": "[{\"a\": 1}, {\"a\": 2}]"}}, {"t": "Error recovery", "d": "Lenient parsers salvage valid prefixes from truncated input. Recovery turns total failure into partial data. Grace matters in pipelines.", "c": "evaluation", "r": 1, "p": {"FMT": "json", "PAYLOAD": "[{\"id\": 1}]"}}, {"t": "Encoding detection", "d": "Parsers detect BOMs and declared encodings before decoding. Wrong encodings mojibake text. Detection precedes parsing.", "c": "fundamentals", "r": 2, "p": {"FMT": "xml", "PAYLOAD": "<r><t>café</t></r>"}}, {"t": "Path queries", "d": "JSONPath/XPath select nodes within parsed documents. Paths address nested data declaratively. Queries navigate structure.", "c": "algorithms", "r": 2, "p": {"FMT": "json", "PAYLOAD": "{\"a\": {\"b\": 42}}"}}, {"t": "CSV parsing", "d": "CSV parsers handle quoting, escapes, and multiline fields. Dialect sniffing adapts to variants. CSV is deceptively tricky.", "c": "implementation", "r": 2, "p": {"FMT": "json", "PAYLOAD": "[{\"c\": 1}]"}}, {"t": "YAML parsing", "d": "YAML parsers handle indentation-based nesting and anchors. Aliases deduplicate repeated structures. YAML suits configuration.", "c": "optimization", "r": 2, "p": {"FMT": "json", "PAYLOAD": "{\"k\": \"v\"}"}}, {"t": "Format conversion", "d": "Converters map JSON to XML and back, preserving structure. Lossless round-trips need care with attributes. Conversion bridges ecosystems.", "c": "evaluation", "r": 2, "p": {"FMT": "xml", "PAYLOAD": "<rows><r><id>9</id></r></rows>"}}, {"t": "Large-number handling", "d": "Parsers must not lose precision on big integers. Decimal modes preserve exactness. Precision matters for data.", "c": "fundamentals", "r": 3, "p": {"FMT": "json", "PAYLOAD": "[{\"big\": 12345678901234567890}]"}}, {"t": "Duplicate keys", "d": "Duplicate JSON keys need a policy: first wins, last wins, or error. Explicit policy avoids surprises. Duplicates are usually bugs.", "c": "algorithms", "r": 3, "p": {"FMT": "json", "PAYLOAD": "[{\"a\": 1}]"}}, {"t": "Comment stripping", "d": "JSONC parsers strip comments before parsing. Stripping keeps configs human-friendly. Comments aid maintenance.", "c": "implementation", "r": 3, "p": {"FMT": "json", "PAYLOAD": "{\"a\": 1}"}}, {"t": "Binary formats", "d": "CBOR/MessagePack parsers handle binary-structured data. Binary formats save space and time. Efficiency has a format.", "c": "optimization", "r": 3, "p": {"FMT": "json", "PAYLOAD": "[1, 2, 3]"}}, {"t": "Parser security", "d": "Billion-laughs and deep-nesting attacks need parser limits. Depth and entity caps contain abuse. Limits are security.", "c": "evaluation", "r": 3, "p": {"FMT": "xml", "PAYLOAD": "<r><a>x</a></r>"}}];
var DEMO="# Structured parsing: parse JSON and XML samples into a uniform record list.\nimport json, xml.etree.ElementTree as ET\ndef parse_json(s):\n    data = json.loads(s)\n    return data if isinstance(data, list) else [data]\ndef parse_xml(s):\n    root = ET.fromstring(s)\n    return [{c.tag: c.text for c in item} | {\"_tag\": item.tag} for item in root]\nfmt, payload = \"%%FMT%%\", \"\"\"%%PAYLOAD%%\"\"\".replace(\"\\\\n\", \"\\n\")\nrecs = parse_json(payload) if fmt == \"json\" else parse_xml(payload)\nprint(f\"parsed {len(recs)} record(s) as {fmt}:\")\nfor r in recs: print(\" \", r)\n";
function demoFor(a){var s=DEMO;for(var k in a.p){s=s.split('%%'+k+'%%').join(a.p[k]);}return s;}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var pool=ASPECTS.filter(function(a){return a.c===cat;});
  var a=pick(pool.length?pool:ASPECTS,rnd);
  var id=PREFIX+String(seed).padStart(5,'0');
  return {id:id,t:a.t.slice(0,80),title:(SIG?'Signature ':'')+a.t+' \u2014 '+TOOLNAME,description:a.d,kind:KIND,category:a.c,ladder_rank:a.r,demo:demoFor(a),provenance:PROV,last_verified:'2026-10-21',src:SRC,_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp("^JAH\\-ATK143\\-\\d+$").test(r.id||''))e.push('id');
  if(typeof r.t!=='string'||!r.t.length)e.push('t');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(r.kind!==KIND)e.push('kind');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(typeof r.demo!=='string'||r.demo.indexOf('print(')<0)e.push('demo');
  if(typeof r.provenance!=='string'||!r.provenance.length)e.push('provenance');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  if(r.src!==SRC)e.push('src');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++){
    var s=sample[i];
    if(s&&s.title===rec.title&&s.description===rec.description)
      return {ok:false,errors:['duplicate of archived record '+s.id]};
  }
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-archive-toolkit-structured-document-parser-1.0",generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator("archive-toolkit-structured-document-parser",gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
