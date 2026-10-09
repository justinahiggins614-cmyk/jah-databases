/* JAH API Reference Database generator. Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(s,r){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var CATS=['math','dictionary','search','routing','data','media'];
function P(n,t,d){return{name:n,type:t,desc:d};}
var A={
math:[
['calculate','Evaluates a math expression and returns the result.',[P('expression','string','The expression to evaluate, e.g. "2*(3+4)".'),P('precision','integer','Decimal places in the result (default 6).'),P('angle','string','"deg" or "rad" for trig functions (default "deg").')],'`jahdb.math.calculate({expression:"sqrt(144)+2^3"})`','`{"result":20,"precision":6}`',[['E_SYNTAX','The expression could not be parsed.'],['E_DIVZERO','Division by zero encountered.'],['E_DOMAIN','Function argument outside its domain.']]],
['solve_equation','Solves a linear or quadratic equation for x.',[P('equation','string','Equation string, e.g. "2x+3=11" or "x^2-5x+6=0".'),P('form','string','"exact" or "decimal" output (default "decimal").')],'`jahdb.math.solve_equation({equation:"x^2-5x+6=0"})`','`{"solutions":[2,3],"form":"decimal"}`',[['E_SYNTAX','The equation could not be parsed.'],['E_DEGREE','Degree higher than 2 is not supported.'],['E_NOSOL','No real solutions exist.']]],
['convert_units','Converts a value between compatible units.',[P('value','number','The numeric value to convert.'),P('from','string','Source unit, e.g. "km".'),P('to','string','Target unit, e.g. "mi".')],'`jahdb.math.convert_units({value:5,from:"km",to:"mi"})`','`{"result":3.1069,"unit":"mi"}`',[['E_UNIT','Unknown or incompatible unit.'],['E_VALUE','Value is not a finite number.']]],
['factorial','Returns n! for a non-negative integer.',[P('n','integer','Non-negative integer up to 170.'),P('as_string','boolean','Return very large results as a string (default false).')],'`jahdb.math.factorial({n:6})`','`{"result":720}`',[['E_RANGE','n is negative or exceeds 170.'],['E_TYPE','n is not an integer.']]],
['gcd','Greatest common divisor of two integers.',[P('a','integer','First integer.'),P('b','integer','Second integer.')],'`jahdb.math.gcd({a:48,b:18})`','`{"result":6}`',[['E_TYPE','Inputs must be integers.'],['E_RANGE','Inputs out of supported range.']]],
['prime_factors','Prime factorization of a positive integer.',[P('n','integer','Integer from 2 to 10^12.'),P('unique','boolean','Return only unique factors (default false).')],'`jahdb.math.prime_factors({n:84})`','`{"factors":[2,2,3,7]}`',[['E_RANGE','n outside 2..10^12.'],['E_TYPE','n is not an integer.']]],
['mean','Arithmetic mean of a list of numbers.',[P('values','array','Non-empty array of finite numbers.'),P('round','integer','Decimal places in the result (default 6).')],'`jahdb.math.mean({values:[2,4,6]})`','`{"result":4}`',[['E_EMPTY','The values array is empty.'],['E_VALUE','A value is not finite.']]],
['matrix_multiply','Multiplies two matrices.',[P('a','array','First matrix as nested arrays.'),P('b','array','Second matrix as nested arrays.')],'`jahdb.math.matrix_multiply({a:[[1,2]],b:[[3],[4]]})`','`{"result":[[11]]}`',[['E_SHAPE','Inner dimensions do not match.'],['E_TYPE','Inputs must be numeric matrices.']]],
['derivative','Symbolic derivative of a polynomial expression.',[P('expression','string','Polynomial in x, e.g. "3x^2+2x".'),P('at','number','Optional point to evaluate the derivative.')],'`jahdb.math.derivative({expression:"3x^2+2x",at:2})`','`{"derivative":"6x+2","value":14}`',[['E_SYNTAX','Expression is not a polynomial.'],['E_TYPE','Expression must be a string.']]],
['random_int','Deterministic pseudo-random integer in a range.',[P('min','integer','Inclusive lower bound.'),P('max','integer','Inclusive upper bound.'),P('seed','integer','Seed for reproducibility.')],'`jahdb.math.random_int({min:1,max:6,seed:42})`','`{"result":4}`',[['E_RANGE','min is greater than max.'],['E_TYPE','Bounds must be integers.']]]
],
dictionary:[
['define_word','Returns the definition of a dictionary headword.',[P('word','string','The headword to look up.'),P('pos','string','Optional part of speech filter.')],'`jahdb.dict.define_word({word:"serendipity"})`','`{"word":"serendipity","pos":"noun","definition":"...","syllables":5}`',[['E_NOTFOUND','No entry for this headword.'],['E_POS','No entry with that part of speech.']]],
['word_exists','Checks whether a headword exists in the dictionary.',[P('word','string','The headword to check.'),P('fuzzy','boolean','Allow near-matches (default false).')],'`jahdb.dict.word_exists({word:"quixotic"})`','`{"exists":true}`',[['E_TYPE','word must be a string.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['synonyms','Lists synonyms for a headword.',[P('word','string','The headword.'),P('limit','integer','Max synonyms to return (default 10).')],'`jahdb.dict.synonyms({word:"happy",limit:5})`','`{"synonyms":["glad","joyful","cheerful","delighted","content"]}`',[['E_NOTFOUND','No entry for this headword.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['antonyms','Lists antonyms for a headword.',[P('word','string','The headword.'),P('limit','integer','Max antonyms to return (default 10).')],'`jahdb.dict.antonyms({word:"hot",limit:3})`','`{"antonyms":["cold","chilly","freezing"]}`',[['E_NOTFOUND','No entry for this headword.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['pronounce','Returns pronunciation guidance for a word.',[P('word','string','The headword.'),P('dialect','string','"us" or "uk" (default "us").')],'`jahdb.dict.pronounce({word:"data"})`','`{"ipa":"/ˈdeɪtə/","syllables":"da-ta"}`',[['E_NOTFOUND','No entry for this headword.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['word_of_day','Returns today\'s featured dictionary word.',[P('date','string','Optional date YYYY-MM-DD (default today).'),P('locale','string','Locale for the word (default en).')],'`jahdb.dict.word_of_day()`','`{"word":"petrichor","definition":"..."}`',[["E_INTERNAL","Word service unavailable."],["E_DATE","System clock invalid."]]],
['starts_with','Lists headwords beginning with a prefix.',[P('prefix','string','1-4 letter prefix.'),P('limit','integer','Max results (default 25).')],'`jahdb.dict.starts_with({prefix:"br",limit:3})`','`{"words":["brave","bread","break"]}`',[['E_PREFIX','Prefix must be 1-4 letters.'],['E_LIMIT','Limit out of range.']]],
['rhymes','Lists words rhyming with the input.',[P('word','string','The word to rhyme.'),P('limit','integer','Max results (default 20).')],'`jahdb.dict.rhymes({word:"cat",limit:3})`','`{"rhymes":["hat","bat","mat"]}`',[['E_NOTFOUND','No rhymes found.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['etymology','Returns the origin history of a word.',[P('word','string','The headword.'),P('depth','integer','Detail level 1-3 (default 2).')],'`jahdb.dict.etymology({word:"robot"})`','`{"origin":"Czech robota, forced labor"}`',[['E_NOTFOUND','No entry for this headword.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['translate_word','Glosses a word into another language.',[P('word','string','The English headword.'),P('to','string','Target language code, e.g. "es".')],'`jahdb.dict.translate_word({word:"hello",to:"es"})`','`{"translation":"hola"}`',[['E_LANG','Unsupported language code.'],['E_NOTFOUND','No entry for this headword.']]]
],
search:[
['search_archive','Full-text search across one database archive.',[P('query','string','Search text.'),P('database','string','Database slug to search.'),P('limit','integer','Max hits (default 12, max 50).')], '`jahdb.search.search_archive({query:"black hole",database:"knowledge-triples"})`','`{"hits":[{...}],"total":34}`',[['E_DB','Unknown database slug.'],['E_QUERY','Query is empty.']]],
['search_all','Searches every database archive at once.',[P('query','string','Search text.'),P('limit','integer','Max hits per database (default 5).')], '`jahdb.search.search_all({query:"photosynthesis"})`','`{"results":{"summarization-pairs":[...]}}`',[['E_QUERY','Query is empty.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['lookup_id','Fetches a single record by its ID.',[P('id','string','Record ID, e.g. "JAH-KG-000123".'),P('fields','array','Optional field subset to return.')], '`jahdb.search.lookup_id({id:"JAH-KG-000123"})`','`{"record":{...}}`',[['E_NOTFOUND','No record with that ID.'],['E_ID','Malformed record ID.']]],
['suggest','Returns query completions for a prefix.',[P('prefix','string','Partial query text.'),P('limit','integer','Max suggestions (default 8).')], '`jahdb.search.suggest({prefix:"quant"})`','`{"suggestions":["quantum","quantity"]}`',[['E_PREFIX','Prefix is empty.'],['E_DB','Unknown database slug.']]],
['filter_by_category','Lists archive records in one category.',[P('database','string','Database slug.'),P('category','string','Category value.'),P('limit','integer','Max records (default 25).')], '`jahdb.search.filter_by_category({database:"unit-tests",category:"python"})`','`{"records":[{...}]}`',[['E_DB','Unknown database slug.'],['E_CAT','Unknown category for this database.']]],
['count','Returns the stored record count of a database.',[P('database','string','Database slug.'),P('category','string','Optional category to count within.')],'`jahdb.search.count({database:"api-docs"})`','`{"count":10000,"target":1000000}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['random_record','Returns a deterministic record by seed.',[P('database','string','Database slug.'),P('seed','integer','Seed.')],'`jahdb.search.random_record({database:"safety-refusals",seed:7})`','`{"record":{...}}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['recent','Lists the most recently added archive records.',[P('database','string','Database slug.'),P('limit','integer','Max records (default 10).')], '`jahdb.search.recent({database:"embedding-chunks"})`','`{"records":[{...}]}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]]
],
routing:[
['route_site','Routes a user request to the right database.',[P('request','string','The user\'s request text.'),P('confidence','number','Minimum confidence 0-1 (default 0.5).')], '`jahdb.route.route_site({request:"fix my python error"})`','`{"database":"error-fix-pairs","confidence":0.93}`',[['E_REQUEST','Request text is empty.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['list_databases','Lists all databases with status.',[P('status','string','Filter by status, e.g. live.'),P('limit','integer','Max databases to return (default 50).')],'`jahdb.route.list_databases()`','`{"databases":[{...}],"live":8}`',[["E_INTERNAL","Manifest unreadable."],["E_EMPTY","No databases registered."]]],
['describe','Returns a database\'s description and schema.',[P('database','string','Database slug.'),P('example','boolean','Include a sample record (default false).')],'`jahdb.route.describe({database:"api-docs"})`','`{"name":"...","record_kind":"API reference","fields":[...]}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['cross_sample','Samples records from another database.',[P('database','string','Database slug.'),P('n','integer','Sample size (default 5).')], '`jahdb.route.cross_sample({database:"classification-rows",n:3})`','`{"samples":[{...}]}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['ai_route','Asks the archive-aware AI a question.',[P('database','string','Database slug.'),P('question','string','The question.')],'`jahdb.route.ai_route({database:"knowledge-triples",question:"Who discovered radium?"})`','`{"answer":"Marie Curie ..."}`',[['E_DB','Unknown database slug.'],['E_QUESTION','Question is empty.']]],
['manifest','Returns the network manifest.',[P('version','string','Manifest schema version to request.'),P('pretty','boolean','Pretty-print the JSON output.')],'`jahdb.route.manifest()`','`{"databases":[...],"version":"1.0"}`',[['E_INTERNAL','Manifest unreadable.'],['E_VERSION','Manifest version mismatch.']]]
],
data:[
['fetch_chunk','Fetches one archive chunk by number.',[P('database','string','Database slug.'),P('chunk','integer','Chunk number, 1-based.')],'`jahdb.data.fetch_chunk({database:"unit-tests",chunk:3})`','`{"records":[{...}],"chunk":3}`',[['E_DB','Unknown database slug.'],['E_CHUNK','Chunk number out of range.']]],
['fetch_index','Fetches the archive index lines.',[P('database','string','Database slug.'),P('offset','integer','Line offset (default 0).'),P('limit','integer','Max lines (default 100).')], '`jahdb.data.fetch_index({database:"api-docs",limit:2})`','`{"lines":[{...}]}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['validate_record','Validates a record against its schema.',[P('database','string','Database slug.'),P('record','object','The record to validate.')],'`jahdb.data.validate_record({database:"safety-refusals",record:{...}})`','`{"ok":true,"errors":[]}`',[['E_DB','Unknown database slug.'],['E_RECORD','record must be an object.']]],
['generate','Generates a deterministic record by seed.',[P('database','string','Database slug.'),P('seed','integer','Seed.'),P('category','string','Optional category.')],'`jahdb.data.generate({database:"error-fix-pairs",seed:42})`','`{"record":{...},"version":"jahdb-error-fix-pairs-1.0"}`',[['E_DB','Unknown database slug.'],['E_GEN','No generator registered.']]],
['stats','Returns storage stats for a database.',[P('database','string','Database slug.'),P('detail','boolean','Include per-chunk breakdown (default false).')],'`jahdb.data.stats({database:"embedding-chunks"})`','`{"records":10000,"chunks":100,"bytes_gz":2450000}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['export_jsonl','Exports records as JSON lines.',[P('database','string','Database slug.'),P('limit','integer','Max records (default 100).')], '`jahdb.data.export_jsonl({database:"knowledge-triples",limit:2})`','`{"jsonl":"{...}\\n{...}"}`',[['E_DB','Unknown database slug.'],['E_INTERNAL','An unexpected internal error occurred.']]]
],
media:[
['emblem','Generates a deterministic SVG emblem for a record.',[P('label','string','Label text for the emblem.'),P('sub','string','Optional subtitle.')],'`jahdb.media.emblem({label:"JAH-ERR",sub:"JAH-ERR-000001"})`','`{"svg_url":"data:image/svg+xml,..."}`',[['E_LABEL','label is required.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['speak','Reads text aloud with the page TTS voice.',[P('text','string','Text to speak (max 600 chars).'),P('voice','string','"female" or "male" (default "female").')],'`jahdb.media.speak({text:"Hello world"})`','`{"playing":true}`',[['E_TEXT','Text is empty or too long.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['stop_audio','Stops all audio playback on the page.',[P('fade_ms','integer','Fade-out duration in ms (default 0).'),P('session','string','Optional session id to stop.')],'`jahdb.media.stop_audio()`','`{"stopped":true}`',[["E_AUDIO","Audio engine unavailable."],["E_STATE","Nothing is playing."]]],
['chart_bar','Renders a bar chart from label/value pairs.',[P('labels','array','Category labels.'),P('values','array','Numeric values, same length as labels.')],'`jahdb.media.chart_bar({labels:["a","b"],values:[3,5]})`','`{"svg":"<svg>..."}`',[['E_SHAPE','labels and values must match in length.'],['E_INTERNAL','An unexpected internal error occurred.']]],
['qr','Generates a QR code for a URL.',[P('url','string','The URL to encode.'),P('size','integer','Image size in pixels (default 256).')],'`jahdb.media.qr({url:"https://example.com"})`','`{"svg":"<svg>..."}`',[['E_URL','Invalid URL.'],['E_INTERNAL','An unexpected internal error occurred.']]]
]
};
function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var cat=opts.category||pick(rnd,CATS);
  var bank=A[cat]||A.math;
  var a=bank[ri(rnd,0,bank.length-1)];
  var params={};
  a[2].forEach(function(p){params[p.name]={type:p.type,description:p.desc};});
  return {
    id:'JAH-API-'+String(seed).padStart(6,'0'),
    api_id:'JAH-API-'+String(seed).padStart(6,'0'),
    name:a[0],
    description:a[1],
    parameters:params,
    example_call:a[3],
    example_response:a[4],
    error_codes:a[5].map(function(e){return{code:e[0],meaning:e[1]};}),
    category:cat,
    title:a[0]
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return{ok:false,errors:['not an object']};
  ['id','api_id','name','description','parameters','example_call','example_response','error_codes','category','title'].forEach(function(k){if(r[k]===undefined||r[k]===''||r[k]===null)e.push('missing '+k);});
  if(r.id&&!/^JAH-API-\d{6}$/.test(r.id))e.push('bad id');
  if(r.api_id&&r.api_id!==r.id)e.push('api_id != id');
  if(r.parameters&&(typeof r.parameters!=='object'||Array.isArray(r.parameters)))e.push('parameters not object');
  var pn=r.parameters?Object.keys(r.parameters):[];
  if(pn.length<2||pn.length>5)e.push('parameters count '+pn.length);
  pn.forEach(function(k){var p=r.parameters[k];if(!p.type||!p.description)e.push('param '+k+' incomplete');});
  if(!Array.isArray(r.error_codes)||r.error_codes.length<2||r.error_codes.length>3)e.push('error_codes count');
  if(r.category&&CATS.indexOf(r.category)<0)e.push('bad category');
  return{ok:!e.length,errors:e};
}
var gen={version:'jahdb-api-docs-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('api-docs',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
