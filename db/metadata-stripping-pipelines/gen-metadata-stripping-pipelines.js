(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var CATS=["exif", "documents", "archives", "verification"];
var PREFIX='JAH-METADA-';
var KIND='metadata stripping stage';
var SRC='public-harvest';
var EDITION='public';
var ABILITY='metadata-stripping-pipelines';
var ROWS=[{"n": "EXIF stripping for images", "d": "Photos carry EXIF: GPS coordinates, camera serial, timestamps — enough to locate the photographer. Stripping pipelines remove all EXIF (or keep only orientation/dimensions) before publishing, so shared images don't leak where and when they were taken.", "m": "Parse EXIF; delete all tags (or allowlist safe ones); rewrite the file; verify no GPS remains.", "s": {"remove": "GPS, serial, timestamps", "keep": "orientation (optional)", "tools": "exiftool, MAT2"}, "u": "Strip on upload, not on trust; verify with a checker; keep originals only in the private archive.", "demo": "print('photo.jpg EXIF: GPS 40.7N 74.0W, iPhone 15, 2026-10-20')\nprint('stripped: 0 tags remain -> safe to publish')"}, {"n": "Document metadata scrubbing", "d": "Office documents and PDFs hide author names, edit history, comments, and tracked changes — the classic leak (government reports with redacted text recoverable from metadata). Scrubbers remove author info, revision history, and hidden layers before external sharing.", "m": "Remove author/revision metadata; flatten tracked changes; strip comments and hidden text; verify with a metadata reader.", "s": {"remove": "authors, revisions, comments", "flatten": "tracked changes", "tools": "MAT2, exiftool"}, "u": "Scrub every externally-shared document; verify, don't assume; keep the original internally.", "demo": "print('report.docx: author \"J. Smith\", 14 revisions, 3 comments')\nprint('scrubbed: metadata empty, changes accepted, comments removed')"}, {"n": "MAT2 comprehensive cleaner", "d": "MAT2 (Metadata Anonymisation Toolkit) strips metadata from dozens of formats — images, documents, audio, archives — in one pipeline. It's the standard 'clean everything' tool: point it at a directory before publishing and it handles each format's metadata correctly.", "m": "Run MAT2 over the publish set; it dispatches per-format cleaners; verify output; integrate into the publish pipeline.", "s": {"tool": "MAT2", "formats": "dozens", "use": "pre-publish pipeline"}, "u": "Run MAT2 as a publish gate; update it (new formats, new metadata fields appear).", "demo": "print('MAT2: 142 files processed (jpg, pdf, docx, mp3)')\nprint('metadata removed from 138; 4 already clean')"}, {"n": "Archive and container cleaning", "d": "Zips and tars carry filenames, timestamps, permissions, and sometimes absolute paths — metadata about the build machine and its user. Cleaning normalizes timestamps (SOURCE_DATE_EPOCH), strips paths, and sorts entries, so archives reveal nothing about their origin.", "m": "Normalize timestamps; strip absolute paths; sort entries; remove owner metadata; verify reproducibility.", "s": {"normalize": "timestamps, paths, order", "remove": "owner info", "verify": "reproducible archives"}, "u": "Clean all distributed archives; the archive should be reproducible from source alone.", "demo": "print('release.tar.gz: timestamps -> 1970-01-01, paths relative, sorted')\nprint('origin metadata: none remaining')"}, {"n": "Audio metadata removal", "d": "Audio files carry ID3 tags, encoder strings, and sometimes location or device info. Podcasts and published recordings get their tags scrubbed — keep title/artist if intended, remove everything identifying, and re-encode if the container hides data in padding.", "m": "Strip ID3/all tags; keep only intended fields; check container padding; verify with a tag reader.", "s": {"strip": "ID3, encoder, device tags", "keep": "intended title/artist", "check": "padding areas"}, "u": "Scrub published audio; verify tags after encoding (encoders re-add metadata).", "demo": "print('episode.mp3: encoder \"Lavf\", device tag removed')\nprint('remaining tags: title, artist (intended only)')"}, {"n": "Video metadata and thumbnail scrubbing", "d": "Videos hide metadata in container atoms and embedded thumbnails (which can contain their own EXIF, including GPS). Scrubbing removes container metadata and regenerates or strips thumbnails — the preview image shouldn't leak what the video hides.", "m": "Strip container metadata; handle embedded thumbnails (strip or regenerate); verify with a metadata dump.", "s": {"strip": "container atoms", "thumbnails": "strip/regenerate", "verify": "metadata dump"}, "u": "Scrub published video; check thumbnails specifically — they're the forgotten leak.", "demo": "print('video.mp4: 12 metadata atoms removed; thumbnail EXIF (GPS!) stripped')\nprint('clean: safe to publish')"}, {"n": "Email header minimization", "d": "Email headers trace the message's path: originating IP, mail client, internal hostnames. Minimization strips non-essential headers before external delivery and avoids leaking internal topology — the headers recipients see reveal nothing about the sender's infrastructure.", "m": "Strip internal Received hops and client identifiers; keep required headers; apply at the gateway.", "s": {"strip": "internal hops, client IDs", "keep": "required headers", "apply": "gateway"}, "u": "Configure the gateway once; audit headers on outbound mail periodically.", "demo": "print('outbound headers: 3 internal Received lines removed')\nprint('recipient sees: clean headers, no internal topology')"}, {"n": "PDF redaction verification", "d": "Fake redaction (black boxes over text) is a famous leak — the text remains underneath. Real redaction removes the text and metadata, and verification tries to extract the 'redacted' content to prove it's gone. The pipeline redacts, then attacks its own output.", "m": "Remove redacted text (not just cover it); strip metadata; attempt extraction; require zero recoverable content.", "s": {"remove": "text, not just cover", "attack": "own output", "require": "zero recoverable"}, "u": "Never trust visual redaction; verify by extraction; use proper redaction tools.", "demo": "print('redacted.pdf: black boxes -> text REMOVED underneath')\nprint('extraction attack: 0 recoverable chars -> VERIFIED')"}, {"n": "Steganography screening", "d": "Beyond metadata, files can hide data steganographically (LSB encoding, appended archives). Screening checks for anomalies — unexpected appended data, statistical irregularities — before publishing or ingesting files. It's the deeper clean for high-sensitivity pipelines.", "m": "Scan for appended data and statistical anomalies; quarantine suspicious files; investigate before release.", "s": {"scan": "appended data, anomalies", "quarantine": "suspicious files", "use": "high-sensitivity"}, "u": "Screen inbound files in sensitive pipelines; the check is cheap, the miss is expensive.", "demo": "print('scan: image.jpg has 2MB appended after EOI marker')\nprint('QUARANTINED: hidden payload suspected')"}, {"n": "Publish-pipeline integration", "d": "Stripping works when it's automatic: the publish pipeline runs the cleaners on every artifact, verifies the output, and blocks publication on failure. Manual stripping is forgotten stripping — the pipeline is the policy.", "m": "Cleaners as pipeline stages; verification per artifact; block on failure; log what was removed.", "s": {"stages": "clean + verify", "block": "on failure", "log": "removals"}, "u": "Wire stripping into every publish path; no manual exceptions.", "demo": "print('publish pipeline: 142 artifacts -> cleaned -> verified')\nprint('3 failed verification -> BLOCKED, fixed, re-run')"}];
var IDRE=new RegExp('^'+PREFIX.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'\\d{6}$');
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category||pick(CATS,rnd);
  var row=pick(ROWS,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {id:id,title:row.n,description:row.d,method:row.m,specification:row.s,usage:row.u,
    category:cat,ladder_rank:1+(seed%3),
    demo:{language:'python',code:row.demo,run:'python3 demo.py'},
    provenance:'JAH Databases lane A3 build',src:SRC,edition:EDITION,ability:ABILITY,
    record_kind:KIND,last_verified:'2026-10-21',_seed:seed};
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!IDRE.test(r.id||''))e.push('id');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.description!=='string'||r.description.length<50)e.push('description');
  if(typeof r.method!=='string'||!r.method.length)e.push('method');
  if(!r.specification||typeof r.specification!=='object')e.push('specification');
  if(typeof r.usage!=='string'||!r.usage.length)e.push('usage');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(!(r.ladder_rank>=1&&r.ladder_rank<=3))e.push('ladder_rank');
  if(!r.demo||typeof r.demo.code!=='string'||!r.demo.code.length)e.push('demo');
  if(r.src!==SRC)e.push('src');
  if(r.last_verified!=='2026-10-21')e.push('last_verified');
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var e=[];
  (sample||[]).forEach(function(s){
    if(s&&s.title===rec.title&&s.id!==rec.id)e.push('duplicate-title');
  });
  return {ok:!e.length,errors:e};
}
var gen={version:'jahdb-metadata-stripping-pipelines-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('metadata-stripping-pipelines',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
