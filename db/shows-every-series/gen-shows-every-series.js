(function(){'use strict';
/* JAH The Shows Database generator — jahdb-shows-every-series-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-TV-";
var FIELDS=["foundations","compounded","advanced"];
var TOPICS={
 "foundations": [
  "Captain Video and His Video Rangers (1949-1955) \u2014 foundations",
  "The Cisco Kid (1950-1956) \u2014 foundations",
  "The Gene Autry Show (1950-1956) \u2014 foundations",
  "You Bet Your Life (1950-1961) \u2014 foundations",
  "Tom Corbett, Space Cadet (1950-1955) \u2014 foundations",
  "Dragnet (1951-1959) \u2014 foundations",
  "The Adventures of Kit Carson (1951-1955) \u2014 foundations",
  "The Roy Rogers Show (1951-1957) \u2014 foundations",
  "Hopalong Cassidy (1952-1954) \u2014 foundations",
  "Sherlock Holmes (1954-1955) \u2014 foundations",
  "Annie Oakley (1954-1957) \u2014 foundations",
  "Flash Gordon (1936) \u2014 foundations"
 ],
 "compounded": [
  "I Love Lucy (1951-1957) \u2014 compounded",
  "The Twilight Zone (1959-1964) \u2014 compounded",
  "The Andy Griffith Show (1960-1968) \u2014 compounded",
  "Star Trek: The Original Series (1966-1969) \u2014 compounded",
  "Mister Rogers' Neighborhood (1968-2001) \u2014 compounded",
  "Sesame Street (1969-present) \u2014 compounded",
  "The Mary Tyler Moore Show (1970-1977) \u2014 compounded",
  "All in the Family (1971-1979) \u2014 compounded",
  "M*A*S*H (1972-1983) \u2014 compounded",
  "Cheers (1982-1993) \u2014 compounded",
  "The Simpsons (1989-present) \u2014 compounded",
  "Seinfeld (1989-1998) \u2014 compounded"
 ],
 "advanced": [
  "The X-Files (1993-2018) \u2014 advanced",
  "Friends (1994-2004) \u2014 advanced",
  "The Sopranos (1999-2007) \u2014 advanced",
  "The Wire (2002-2008) \u2014 advanced",
  "The Office (2005-2013) \u2014 advanced",
  "Planet Earth (2006) \u2014 advanced",
  "Breaking Bad (2008-2013) \u2014 advanced",
  "Game of Thrones (2011-2019) \u2014 advanced",
  "Cosmos: A Spacetime Odyssey (2014) \u2014 advanced",
  "Stranger Things (2016-present) \u2014 advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Series Record Study — "+safe+"\n"
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
    name:topic+' — series record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A series record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"series-record",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-shows-every-series-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('shows-every-series',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
