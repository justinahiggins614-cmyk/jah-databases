(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function ri(r,a,b){return a+((r()*(b-a+1))|0);}
function pad6(n){return String(n).padStart(6,'0');}

var CATS=['extraction','validation','parsing'];

var BANK=[
 {name:'Email address',use:'validation',
  regex:'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$',
  desc:'Matches a standard email address with a two-or-more-letter top-level domain.',
  pos:['ana@example.com','bob.smith+tag@mail.co.uk','x9@io.dev'],
  neg:['not-an-email','user@domain','@missing.com']},
 {name:'IPv4 address',use:'validation',
  regex:'^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$',
  desc:'Matches a dotted-quad IPv4 address with each octet 0-255.',
  pos:['192.168.0.1','8.8.8.8','255.255.255.255'],
  neg:['999.1.1.1','192.168.1','1.2.3.4.5']},
 {name:'Hex color code',use:'validation',
  regex:'^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$',
  desc:'Matches a CSS hex color: # plus 3 or 6 hex digits.',
  pos:['#fff','#1A2B3C','#000'],
  neg:['#ff','#gggggg','123456']},
 {name:'ISO calendar date',use:'parsing',
  regex:'^\\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$',
  desc:'Parses an ISO-8601 calendar date YYYY-MM-DD with valid month and day ranges.',
  pos:['2026-10-09','1999-01-31','2030-12-01'],
  neg:['2026-13-01','10/09/2026','2026-1-1']},
 {name:'HTTP(S) URL',use:'extraction',
  regex:'^https?:\\/\\/[^\\s/$.?#].[^\\s]*$',
  desc:'Extracts an http or https URL with a non-empty host.',
  pos:['https://example.com','http://a.io/x?y=1','https://sub.domain.org/path'],
  neg:['ftp://x.com','not a url','http://']},
 {name:'Semantic version',use:'parsing',
  regex:'^\\d+\\.\\d+\\.\\d+(?:-[0-9A-Za-z.-]+)?(?:\\+[0-9A-Za-z.-]+)?$',
  desc:'Parses a semantic version MAJOR.MINOR.PATCH with optional pre-release and build parts.',
  pos:['1.2.3','2.0.0-beta','0.0.1+build.5'],
  neg:['1.2','v1.2.3','1.2.3.4']},
 {name:'UUID',use:'extraction',
  regex:'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$',
  desc:'Matches a canonical 36-character UUID with dashes.',
  pos:['123e4567-e89b-12d3-a456-426614174000','AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE'],
  neg:['123e4567-e89b-12d3-a456','xyz']},
 {name:'URL slug',use:'parsing',
  regex:'^[a-z0-9]+(?:-[a-z0-9]+)*$',
  desc:'Matches a lowercase URL slug: groups of letters and digits joined by single dashes.',
  pos:['hello-world','jah-db-123','abc'],
  neg:['Hello-World','-leading','trailing-']},
 {name:'North American phone number',use:'validation',
  regex:'^\\+?1?[-. ]?\\(?[0-9]{3}\\)?[-. ]?[0-9]{3}[-. ]?[0-9]{4}$',
  desc:'Validates a 10-digit North American phone number with common separators.',
  pos:['(555) 123-4567','555-123-4567','+1 555 123 4567'],
  neg:['12345','555-1234-56789','abc-def-ghij']},
 {name:'US dollar amount',use:'extraction',
  regex:'^\\$\\d{1,3}(?:,\\d{3})*(?:\\.\\d{2})?$',
  desc:'Extracts a US dollar amount with comma thousands separators and optional cents.',
  pos:['$1,234.56','$99','$1,000,000.00'],
  neg:['$12.5','12.34','$1,23.45']}
];

function generate(seed,opts,rnd){
  rnd=rnd||prng(seed);
  var pool=BANK;
  if(opts&&opts.category&&CATS.indexOf(opts.category)>=0){
    var f=BANK.filter(function(p){return p.use===opts.category;});
    if(f.length)pool=f;
  }
  var p=pool[ri(rnd,0,pool.length-1)];
  var id='JAH-RX-'+pad6(seed);
  return {id:id,pattern_id:id,name:p.name,regex:p.regex,description:p.desc,
    positive_tests:p.pos.slice(),negative_tests:p.neg.slice(),use:p.use,title:p.name};
}

function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-RX-\d{6}$/.test(r.id))e.push('id');
  if(r.pattern_id!==r.id)e.push('pattern_id');
  if(typeof r.name!=='string'||!r.name.length)e.push('name');
  if(typeof r.regex!=='string'||!r.regex.length||r.regex.length>600)e.push('regex');
  if(typeof r.description!=='string'||!r.description.length||r.description.length>600)e.push('description');
  if(!Array.isArray(r.positive_tests)||r.positive_tests.length<2||r.positive_tests.length>3)e.push('positive_tests');
  if(!Array.isArray(r.negative_tests)||r.negative_tests.length<2||r.negative_tests.length>3)e.push('negative_tests');
  if(CATS.indexOf(r.use)<0)e.push('use');
  if(r.title!==r.name)e.push('title');
  if(!e.length){
    var re;
    try{re=new RegExp(r.regex);}catch(err){e.push('regex does not compile');}
    if(re){
      r.positive_tests.forEach(function(t,i){ if(!re.test(t))e.push('positive_tests['+i+'] fails to match'); });
      r.negative_tests.forEach(function(t,i){ if(re.test(t))e.push('negative_tests['+i+'] unexpectedly matches'); });
    }
  }
  return {ok:!e.length,errors:e};
}

var gen={version:'jahdb-regex-patterns-1.0',generate:generate,validate:validate};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('regex-patterns',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
