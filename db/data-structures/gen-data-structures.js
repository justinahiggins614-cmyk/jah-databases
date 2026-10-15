(function(){'use strict';
/* JAH The Data Structures Database generator — jahdb-data-structures-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-DS-";
var FIELDS=["structure"];
var TOPICS={
 "structure": [
  "JSON Serializers \u2014 structure",
  "BSON Encoders \u2014 structure",
  "CBOR Encoders \u2014 structure",
  "MessagePack Encoders \u2014 structure",
  "Protocol Buffers \u2014 structure",
  "FlatBuffers \u2014 structure",
  "Cap'n Proto \u2014 structure",
  "Avro Encoders \u2014 structure",
  "Thrift Serializers \u2014 structure",
  "XML Serializers \u2014 structure",
  "YAML Serializers \u2014 structure",
  "TOML Parsers \u2014 structure",
  "INI Parsers \u2014 structure",
  "CSV Parsers \u2014 structure",
  "Parquet Writers \u2014 structure",
  "ORC Writers \u2014 structure",
  "Arrow Tables \u2014 structure",
  "Feather Files \u2014 structure",
  "HDF5 Files \u2014 structure",
  "NetCDF Files \u2014 structure",
  "Zarr Stores \u2014 structure",
  "TileDB Arrays \u2014 structure",
  "LMDB Stores \u2014 structure",
  "RocksDB Stores \u2014 structure",
  "LevelDB Stores \u2014 structure",
  "B-Tree Implementations \u2014 structure",
  "B+Tree Implementations \u2014 structure",
  "LSM Trees \u2014 structure",
  "Fractal Trees \u2014 structure",
  "Trie Implementations \u2014 structure",
  "Radix Trees \u2014 structure",
  "Suffix Trees \u2014 structure",
  "Suffix Arrays \u2014 structure",
  "Bloom Filters \u2014 structure",
  "Cuckoo Filters \u2014 structure",
  "Count-Min Sketches \u2014 structure",
  "HyperLogLog \u2014 structure",
  "Quotient Filters \u2014 structure",
  "Xor Filters \u2014 structure",
  "Ring Buffers \u2014 structure",
  "Lock-Free Queues \u2014 structure",
  "Skip Lists \u2014 structure",
  "Treaps \u2014 structure",
  "Splay Trees \u2014 structure",
  "Red-Black Trees \u2014 structure",
  "AVL Trees \u2014 structure",
  "Bw-Trees \u2014 structure",
  "Hash Tables \u2014 structure",
  "Cuckoo Hashing \u2014 structure",
  "Hopscotch Hashing \u2014 structure",
  "Swiss Tables \u2014 structure",
  "Robin Hood Hashing \u2014 structure",
  "Sparse Matrices \u2014 structure",
  "Compressed Graphs \u2014 structure",
  "Persistent Structures \u2014 structure",
  "Write-Ahead Logs \u2014 structure",
  "SSTables \u2014 structure",
  "Memtables \u2014 structure",
  "Journal Segments \u2014 structure"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Data Structures — "+safe+"\n"
   + "# Field: "+field+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\"}\n"
   + "def summarize(r):\n"
   + "    return r['title'] + ' [' + r['field'] + ']'\n"
   + "print(summarize(record))\n"
   + "print('Sample record — structural sample, not an archive entry.')\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — data structure record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A data structure record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
    _seed:seed
  };
}
function validate(r){
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
var gen={version:'jahdb-data-structures-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('data-structures',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
