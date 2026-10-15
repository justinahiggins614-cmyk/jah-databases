(function(){'use strict';
/* JAH Country Calling Code Database generator — jahdb-public-country-calling-codes-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-CC-";
var FIELDS=["Europe","Asia","Africa","North America","South America","Oceania","Caribbean","Middle East","Central America","Polar & special","Other & special"];
var TOPICS={
 "Europe": [
  "+7 \u2014 Russia and Kazakhstan",
  "+30 \u2014 Greece",
  "+31 \u2014 Netherlands",
  "+32 \u2014 Belgium",
  "+33 \u2014 France",
  "+34 \u2014 Spain",
  "+36 \u2014 Hungary",
  "+39 \u2014 Italy",
  "+40 \u2014 Romania",
  "+41 \u2014 Switzerland",
  "+43 \u2014 Austria",
  "+44 \u2014 United Kingdom",
  "+45 \u2014 Denmark",
  "+46 \u2014 Sweden",
  "+47 \u2014 Norway",
  "+48 \u2014 Poland",
  "+49 \u2014 Germany",
  "+298 \u2014 Faroe Islands",
  "+350 \u2014 Gibraltar",
  "+351 \u2014 Portugal",
  "+352 \u2014 Luxembourg",
  "+353 \u2014 Ireland",
  "+354 \u2014 Iceland",
  "+355 \u2014 Albania",
  "+356 \u2014 Malta",
  "+357 \u2014 Cyprus",
  "+358 \u2014 Finland",
  "+359 \u2014 Bulgaria",
  "+370 \u2014 Lithuania",
  "+371 \u2014 Latvia",
  "+372 \u2014 Estonia",
  "+373 \u2014 Moldova",
  "+375 \u2014 Belarus",
  "+376 \u2014 Andorra",
  "+377 \u2014 Monaco",
  "+378 \u2014 San Marino",
  "+379 \u2014 Vatican City",
  "+380 \u2014 Ukraine",
  "+381 \u2014 Serbia",
  "+382 \u2014 Montenegro",
  "+383 \u2014 Kosovo",
  "+385 \u2014 Croatia",
  "+386 \u2014 Slovenia",
  "+387 \u2014 Bosnia and Herzegovina",
  "+389 \u2014 North Macedonia",
  "+420 \u2014 Czech Republic",
  "+421 \u2014 Slovakia",
  "+423 \u2014 Liechtenstein"
 ],
 "Asia": [
  "+60 \u2014 Malaysia",
  "+62 \u2014 Indonesia",
  "+63 \u2014 Philippines",
  "+65 \u2014 Singapore",
  "+66 \u2014 Thailand",
  "+81 \u2014 Japan",
  "+82 \u2014 South Korea",
  "+84 \u2014 Vietnam",
  "+86 \u2014 China",
  "+90 \u2014 Turkey",
  "+91 \u2014 India",
  "+92 \u2014 Pakistan",
  "+93 \u2014 Afghanistan",
  "+94 \u2014 Sri Lanka",
  "+95 \u2014 Myanmar",
  "+98 \u2014 Iran",
  "+374 \u2014 Armenia",
  "+670 \u2014 East Timor",
  "+673 \u2014 Brunei",
  "+850 \u2014 North Korea",
  "+852 \u2014 Hong Kong",
  "+853 \u2014 Macau",
  "+855 \u2014 Cambodia",
  "+856 \u2014 Laos",
  "+880 \u2014 Bangladesh",
  "+886 \u2014 Taiwan",
  "+960 \u2014 Maldives",
  "+961 \u2014 Lebanon",
  "+962 \u2014 Jordan",
  "+963 \u2014 Syria",
  "+964 \u2014 Iraq",
  "+965 \u2014 Kuwait",
  "+966 \u2014 Saudi Arabia",
  "+967 \u2014 Yemen",
  "+968 \u2014 Oman",
  "+970 \u2014 Palestine",
  "+971 \u2014 United Arab Emirates",
  "+972 \u2014 Israel",
  "+973 \u2014 Bahrain",
  "+974 \u2014 Qatar",
  "+975 \u2014 Bhutan",
  "+976 \u2014 Mongolia",
  "+977 \u2014 Nepal",
  "+992 \u2014 Tajikistan",
  "+993 \u2014 Turkmenistan",
  "+994 \u2014 Azerbaijan",
  "+995 \u2014 Georgia",
  "+996 \u2014 Kyrgyzstan",
  "+998 \u2014 Uzbekistan"
 ],
 "Africa": [
  "+20 \u2014 Egypt",
  "+27 \u2014 South Africa",
  "+211 \u2014 South Sudan",
  "+212 \u2014 Morocco",
  "+213 \u2014 Algeria",
  "+216 \u2014 Tunisia",
  "+218 \u2014 Libya",
  "+220 \u2014 Gambia",
  "+221 \u2014 Senegal",
  "+222 \u2014 Mauritania",
  "+223 \u2014 Mali",
  "+224 \u2014 Guinea",
  "+225 \u2014 Ivory Coast",
  "+226 \u2014 Burkina Faso",
  "+227 \u2014 Niger",
  "+228 \u2014 Togo",
  "+229 \u2014 Benin",
  "+230 \u2014 Mauritius",
  "+231 \u2014 Liberia",
  "+232 \u2014 Sierra Leone",
  "+233 \u2014 Ghana",
  "+234 \u2014 Nigeria",
  "+235 \u2014 Chad",
  "+236 \u2014 Central African Republic",
  "+237 \u2014 Cameroon",
  "+238 \u2014 Cape Verde",
  "+239 \u2014 Sao Tome and Principe",
  "+240 \u2014 Equatorial Guinea",
  "+241 \u2014 Gabon",
  "+242 \u2014 Republic of the Congo",
  "+243 \u2014 Democratic Republic of the Congo",
  "+244 \u2014 Angola",
  "+245 \u2014 Guinea-Bissau",
  "+246 \u2014 British Indian Ocean Territory",
  "+247 \u2014 Ascension Island",
  "+248 \u2014 Seychelles",
  "+249 \u2014 Sudan",
  "+250 \u2014 Rwanda",
  "+251 \u2014 Ethiopia",
  "+252 \u2014 Somalia",
  "+253 \u2014 Djibouti",
  "+254 \u2014 Kenya",
  "+255 \u2014 Tanzania",
  "+256 \u2014 Uganda",
  "+257 \u2014 Burundi",
  "+258 \u2014 Mozambique",
  "+260 \u2014 Zambia",
  "+261 \u2014 Madagascar",
  "+262 \u2014 Reunion and Mayotte",
  "+263 \u2014 Zimbabwe",
  "+264 \u2014 Namibia",
  "+265 \u2014 Malawi",
  "+266 \u2014 Lesotho",
  "+267 \u2014 Botswana",
  "+268 \u2014 Eswatini",
  "+269 \u2014 Comoros",
  "+290 \u2014 Saint Helena",
  "+291 \u2014 Eritrea"
 ],
 "North America": [
  "+1 \u2014 North American Numbering Plan",
  "+52 \u2014 Mexico",
  "+299 \u2014 Greenland",
  "+508 \u2014 Saint Pierre and Miquelon"
 ],
 "South America": [
  "+51 \u2014 Peru",
  "+54 \u2014 Argentina",
  "+55 \u2014 Brazil",
  "+56 \u2014 Chile",
  "+57 \u2014 Colombia",
  "+58 \u2014 Venezuela",
  "+500 \u2014 Falkland Islands",
  "+591 \u2014 Bolivia",
  "+592 \u2014 Guyana",
  "+593 \u2014 Ecuador",
  "+594 \u2014 French Guiana",
  "+595 \u2014 Paraguay",
  "+597 \u2014 Suriname",
  "+598 \u2014 Uruguay"
 ],
 "Oceania": [
  "+61 \u2014 Australia",
  "+64 \u2014 New Zealand",
  "+672 \u2014 Australian External Territories",
  "+674 \u2014 Nauru",
  "+675 \u2014 Papua New Guinea",
  "+676 \u2014 Tonga",
  "+677 \u2014 Solomon Islands",
  "+678 \u2014 Vanuatu",
  "+679 \u2014 Fiji",
  "+680 \u2014 Palau",
  "+681 \u2014 Wallis and Futuna",
  "+682 \u2014 Cook Islands",
  "+683 \u2014 Niue",
  "+685 \u2014 Samoa",
  "+686 \u2014 Kiribati",
  "+687 \u2014 New Caledonia",
  "+688 \u2014 Tuvalu",
  "+689 \u2014 French Polynesia",
  "+690 \u2014 Tokelau",
  "+691 \u2014 Micronesia",
  "+692 \u2014 Marshall Islands"
 ],
 "Caribbean": [
  "+53 \u2014 Cuba",
  "+297 \u2014 Aruba",
  "+509 \u2014 Haiti",
  "+590 \u2014 Guadeloupe",
  "+596 \u2014 Martinique",
  "+599 \u2014 Curacao and Caribbean Netherlands"
 ],
 "Middle East": [

 ],
 "Central America": [
  "+501 \u2014 Belize",
  "+502 \u2014 Guatemala",
  "+503 \u2014 El Salvador",
  "+504 \u2014 Honduras",
  "+505 \u2014 Nicaragua",
  "+506 \u2014 Costa Rica",
  "+507 \u2014 Panama"
 ],
 "Polar & special": [

 ],
 "Other & special": [
  "+800 \u2014 Universal International Freephone",
  "+808 \u2014 Universal International Shared Cost",
  "+878 \u2014 Universal Personal Telecommunications",
  "+881 \u2014 Global Mobile Satellite System",
  "+882 \u2014 International Networks",
  "+883 \u2014 International Networks",
  "+888 \u2014 United Nations OCHA",
  "+979 \u2014 Universal International Premium Rate"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Country Code Study — "+safe+"\n"
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
    name:topic+' — country calling code record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A country calling code record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"country-code-dialer",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-public-country-calling-codes-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('public-country-calling-codes',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
