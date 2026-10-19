(function(){'use strict';
/* JAH The Wi-Fi Configuration Support Database generator — jahdb-wi-fi-configuration-support-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-WCS-";
var FIELDS=["router-setup","coverage-and-speed","wifi-security"];
var TOPICS={"router-setup":["Router Placement \u2014 router-setup","Guest Network Setup \u2014 router-setup","Mesh Systems \u2014 router-setup","ISP Modem vs Router \u2014 router-setup","QoS (Quality of Service) \u2014 router-setup","VPN on Router \u2014 router-setup","Smart Home Wi-Fi \u2014 router-setup","When to Replace Router \u2014 router-setup","Interference Sources \u2014 router-setup","Sharing Wi-Fi Safely \u2014 router-setup","Upgrading Internet Plan \u2014 router-setup","Wi-Fi Heat Mapping \u2014 router-setup"],"coverage-and-speed":["2.4GHz vs 5GHz vs 6GHz \u2014 coverage-and-speed","Speed Test Interpretation \u2014 coverage-and-speed","Channel Selection \u2014 coverage-and-speed","Slow Wi-Fi Diagnosis \u2014 coverage-and-speed","Port Forwarding Basics \u2014 coverage-and-speed","Public Wi-Fi Safety \u2014 coverage-and-speed","Parental Controls (Router) \u2014 coverage-and-speed","Extender vs AP vs Mesh \u2014 coverage-and-speed","Wired Beats Wireless \u2014 coverage-and-speed","Troubleshooting Flowchart \u2014 coverage-and-speed","The Home Network Map \u2014 coverage-and-speed"],"wifi-security":["Changing Wi-Fi Password \u2014 wifi-security","Dead Zone Fixes \u2014 wifi-security","Router Firmware Updates \u2014 wifi-security","Too Many Devices \u2014 wifi-security","DNS Settings \u2014 wifi-security","Wi-Fi Calling Setup \u2014 wifi-security","Finding Router Admin \u2014 wifi-security","Wi-Fi 6/6E/7 Basics \u2014 wifi-security","Network Security Audit \u2014 wifi-security","ISP Outage Checks \u2014 wifi-security","Wi-Fi for Renters \u2014 wifi-security"]};
var KINDS="software and IT-support record";
function demoProgram(topic,field,seed){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# The Wi-Fi Configuration Support Database — generated study\n"
   + "# Topic: "+safe+"\n"
   + "# Field: "+field+" | seed "+seed+"\n"
   + "record = {'title': \""+safe+"\", 'field': \""+field+"\", 'seed': "+seed+"}\n"
   + "CHECKS = ['topic_set','field_set','seed_set']\n"
   + "def validate(r):\n"
   + "    missing = [c for c in CHECKS if not r.get(c.replace('_set','')) and c!='seed_set']\n"
   + "    assert r['title'] and r['field'], 'record incomplete'\n"
   + "    return True\n"
   + "def main():\n"
   + "    assert validate(record)\n"
   + "    print('study: '+record['title'])\n"
   + "    print('field: '+record['field'])\n"
   + "    print('kind: software and IT-support record')\n"
   + "    print('Sample record — structural sample, not an archive entry.')\n"
   + "if __name__ == '__main__':\n"
   + "    main()\n";
}
function generate(seed,opts,rnd){
  opts=opts||{}; rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var pool=TOPICS[field]||["General Study"];
  var topic=pick(pool,rnd);
  var id=PREFIX+String(seed).padStart(6,'0');
  return {
    id:id,
    name:topic+' — generated sample',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A structural sample study of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    how_it_works:'Generated sample: apply the steps named in the archive records of the same field, then verify with the field check.',
    key_points:['structural sample','field: '+field,'see archive records for the authoritative method'],
    requirements:'An archive record of the same field for the real method.',
    standards:['software and IT-support record sample standard'],
    citations:'Generated sample — no citation.',
    src:'signature-generated-sample',
    sample:true,
    provenance:'Generated structural sample for the The Wi-Fi Configuration Support Database.',
    last_verified:'2026-10-18',
    ladder_rank:1, ladder_tier:'Foundations',
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"python",language:'python',program:demoProgram(topic,field,seed),note:'Structural sample demo.'},
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
var gen={version:'jahdb-wi-fi-configuration-support-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('wi-fi-configuration-support',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
