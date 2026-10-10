(function(){'use strict';
/* JAH Binary and Encoding Database generator — jahdb-binary-encoding-1.0.
   Every conversion/encoding/checksum is recomputed by the validator; several
   are cross-checked against independent oracles (Buffer, DataView). */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
function ri(s,a,b){return a+((s()*(b-a+1))|0);}
var PREFIX='JAH-BIN-';
var CATS=['number-systems','text-encodings','binary-ops','checksums','compression'];
var B64='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/';
function sjson(v){return JSON.stringify(v);}

/* ---------- executors ---------- */
function toBase(n,base){return n.toString(base).toUpperCase();}
function fromBase(s,base){return parseInt(s,base);}
function utf8enc(cp){
  if(cp<0x80)return [cp];
  if(cp<0x800)return [0xC0|(cp>>6),0x80|(cp&0x3F)];
  if(cp<0x10000)return [0xE0|(cp>>12),0x80|((cp>>6)&0x3F),0x80|(cp&0x3F)];
  return [0xF0|(cp>>18),0x80|((cp>>12)&0x3F),0x80|((cp>>6)&0x3F),0x80|(cp&0x3F)];
}
function utf8dec(bytes){
  var b0=bytes[0];
  if(b0<0x80)return b0;
  if((b0&0xE0)===0xC0)return ((b0&0x1F)<<6)|(bytes[1]&0x3F);
  if((b0&0xF0)===0xE0)return ((b0&0x0F)<<12)|((bytes[1]&0x3F)<<6)|(bytes[2]&0x3F);
  return ((b0&0x07)<<18)|((bytes[1]&0x3F)<<12)|((bytes[2]&0x3F)<<6)|(bytes[3]&0x3F);
}
function b64enc(str){
  var bytes=[];for(var i=0;i<str.length;i++)bytes.push(str.charCodeAt(i)&0xFF);
  var out='';
  for(i=0;i<bytes.length;i+=3){
    var n=(bytes[i]<<16)|((bytes[i+1]||0)<<8)|(bytes[i+2]||0);
    out+=B64[(n>>18)&63]+B64[(n>>12)&63]+(i+1<bytes.length?B64[(n>>6)&63]:'=')+(i+2<bytes.length?B64[n&63]:'=');
  }
  return out;
}
function b64dec(s){
  var bytes=[],i,n;
  for(i=0;i<s.length;i+=4){
    n=(B64.indexOf(s[i])<<18)|(B64.indexOf(s[i+1])<<12)|((s[i+2]==='='?0:B64.indexOf(s[i+2]))<<6)|(s[i+3]==='='?0:B64.indexOf(s[i+3]));
    bytes.push((n>>16)&255);if(s[i+2]!=='=')bytes.push((n>>8)&255);if(s[i+3]!=='=')bytes.push(n&255);
  }
  return String.fromCharCode.apply(null,bytes);
}
function hexEnc(s){var o='';for(var i=0;i<s.length;i++)o+=s.charCodeAt(i).toString(16).padStart(2,'0');return o.toUpperCase();}
function hexDec(h){var o='';for(var i=0;i<h.length;i+=2)o+=String.fromCharCode(parseInt(h.substr(i,2),16));return o;}
function urlEnc(s){return encodeURIComponent(s);}
function urlDec(s){return decodeURIComponent(s);}
function binop(op,a,b){
  var x=BigInt('0b'+a);
  var y=b==null?null:BigInt('0b'+b);
  var w=Math.max(a.length,(b||'').length),r;
  if(op==='and')r=x&y;else if(op==='or')r=x|y;else if(op==='xor')r=x^y;
  else if(op==='not')r=(~x)&((1n<<BigInt(w))-1n);
  else if(op==='add')r=x+y;else if(op==='shl')r=x<<y;else throw new Error('op');
  return r.toString(2).padStart(op==='add'?Math.max(w,r.toString(2).length):w,'0');
}
function parity(bits,type){
  var ones=bits.split('').filter(function(c){return c==='1';}).length;
  if(type==='even')return ones%2===0?'0':'1';
  return ones%2===0?'1':'0';
}
function luhnCheckDigit(digits){
  var sum=0,alt=true;
  for(var i=digits.length-1;i>=0;i--){var d=+digits[i];if(alt){d*=2;if(d>9)d-=9;}sum+=d;alt=!alt;}
  return String((10-(sum%10))%10);
}
var CRC_T=(function(){var t=new Array(256);for(var n=0;n<256;n++){var c=n;for(var k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0;}return t;})();
function crc32(str){
  var c=0xFFFFFFFF;
  for(var i=0;i<str.length;i++)c=CRC_T[(c^str.charCodeAt(i))&0xFF]^(c>>>8);
  return ((c^0xFFFFFFFF)>>>0).toString(16).toUpperCase().padStart(8,'0');
}
function rleEnc(s){var o='',i=0;while(i<s.length){var j=i;while(j<s.length&&s[j]===s[i]&&j-i<255)j++;o+=(j-i)+s[i];i=j;}return o;}
function rleDec(s){var o='',i=0;while(i<s.length){var j=i;while(j<s.length&&/[0-9]/.test(s[j]))j++;var n=+s.slice(i,j),ch=s[j];for(var k=0;k<n;k++)o+=ch;i=j+1;}return o;}
function gray(n){return n^(n>>1);}
function twos(v,bits){if(v>=0)return v.toString(2).padStart(bits,'0');return ((1<<bits)+v).toString(2);}
function ieee754hex(f){var b=new ArrayBuffer(4);new DataView(b).setFloat32(0,f);var s='';for(var i=0;i<4;i++)s+=new DataView(b).getUint8(i).toString(16).padStart(2,'0');return s.toUpperCase();}
var EXEC={
 'base-convert':function(o){return toBase(fromBase(o.value,o.from),o.to);},
 'ascii-byte':function(o){return byteInfo(o.code);},
 'utf8-encode':function(o){return utf8enc(o.codepoint);},
 'utf8-decode':function(o){return utf8dec(o.bytes);},
 'base64-encode':function(o){return b64enc(o.text);},
 'base64-decode':function(o){return b64dec(o.text);},
 'hex-encode':function(o){return hexEnc(o.text);},
 'hex-decode':function(o){return hexDec(o.text);},
 'url-encode':function(o){return urlEnc(o.text);},
 'url-decode':function(o){return urlDec(o.text);},
 'binary-op':function(o){return binop(o.op,o.a,o.b);},
 'parity':function(o){return parity(o.bits,o.type);},
 'luhn':function(o){return luhnCheckDigit(o.digits);},
 'crc32':function(o){return crc32(o.text);},
 'rle-encode':function(o){return rleEnc(o.text);},
 'rle-decode':function(o){return rleDec(o.text);},
 'gray-code':function(o){return gray(o.n).toString(2);},
 'twos-complement':function(o){return twos(o.value,o.bits);},
 'ieee754':function(o){return ieee754hex(o.value);}
};
var METHOD_CAT={'base-convert':'number-systems','ascii-byte':'number-systems','gray-code':'number-systems','twos-complement':'number-systems',
 'utf8-encode':'text-encodings','utf8-decode':'text-encodings','base64-encode':'text-encodings','base64-decode':'text-encodings',
 'hex-encode':'text-encodings','hex-decode':'text-encodings','url-encode':'text-encodings','url-decode':'text-encodings',
 'binary-op':'binary-ops','parity':'checksums','luhn':'checksums','crc32':'checksums',
 'rle-encode':'compression','rle-decode':'compression','ieee754':'number-systems'};
var METHOD_NAME={'base-convert':'Base conversion','ascii-byte':'ASCII byte record','utf8-encode':'UTF-8 encoding','utf8-decode':'UTF-8 decoding',
 'base64-encode':'Base64 encoding','base64-decode':'Base64 decoding','hex-encode':'Hex encoding','hex-decode':'Hex decoding',
 'url-encode':'URL percent-encoding','url-decode':'URL percent-decoding','binary-op':'Binary operation','parity':'Parity bit',
 'luhn':'Luhn check digit','crc32':'CRC-32 checksum','rle-encode':'Run-length encoding','rle-decode':'Run-length decoding',
 'gray-code':'Gray code','twos-complement':"Two's complement",'ieee754':'IEEE-754 single precision'};
var CTL={0:'NUL',1:'SOH',2:'STX',3:'ETX',4:'EOT',5:'ENQ',6:'ACK',7:'BEL',8:'BS',9:'TAB',10:'LF',11:'VT',12:'FF',13:'CR',14:'SO',15:'SI',16:'DLE',17:'DC1',18:'DC2',19:'DC3',20:'DC4',21:'NAK',22:'SYN',23:'ETB',24:'CAN',25:'EM',26:'SUB',27:'ESC',28:'FS',29:'GS',30:'RS',31:'US',32:'SPACE',127:'DEL'};
function byteInfo(code){
  var ch=code>=32&&code<127?String.fromCharCode(code):(CTL[code]||'CTRL');
  return {code:code,char:ch,dec:String(code),hex:toBase(code,16).padStart(2,'0'),oct:toBase(code,8),bin:toBase(code,2).padStart(8,'0'),utf8_bytes:utf8enc(code)};
}

/* ---------- online records ---------- */
var ONLINE=[];
var i,cp;
/* 256 ASCII byte records (real, verifiable) */
for(i=0;i<256;i++){
  var bi=byteInfo(i);
  ONLINE.push({kind:'encoding-record',cat:'number-systems',title:'ASCII byte '+i+' \u2014 '+(bi.char.length<=4?bi.char:'control'),
    concept:'Byte value '+i+': decimal '+i+', hex '+bi.hex+', octal '+bi.oct+', binary '+bi.bin+'.',
    method:'ascii-byte',input:{code:i},output:bi,
    spec:'ASCII assigns every byte 0-127 a character or control code; bytes 128-255 extend it per code page.',
    source:'online',source_ref:'ASCII standard \u2014 byte values'});
}
/* base conversions 0..1023 across bases (real, recomputable) */
var BN=0;
for(i=0;i<1024;i++){
  BN++;
  var outs={bin:toBase(i,2),oct:toBase(i,8),dec:String(i),hex:toBase(i,16)};
  ONLINE.push({kind:'encoding-record',cat:'number-systems',title:'Number '+i+' in binary, octal, decimal, hex',
    concept:'Decimal '+i+' = binary '+outs.bin+' = octal '+outs.oct+' = hex '+outs.hex+'.',
    method:'base-convert',input:{value:String(i),from:10,to:2},output:outs.bin,all_bases:outs,
    spec:'Positional notation: each digit is multiplied by the base raised to its position.',
    source:'online',source_ref:'Computed by positional base conversion'});
}
/* UTF-8 records: Latin-1 supplement + curated CJK/symbols/emoji (Buffer-verified) */
var CPS=[];
for(cp=0x80;cp<0x100;cp++)CPS.push(cp);
var CJK=[0x4E2D,0x6587,0x5B57,0x7B26,0x96C6,0x6F22,0x8A9E,0x65E5,0x672C,0x8BED,0x4E00,0x4E8C,0x4E09,0x5341,0x767E,0x5343,0x4E07,0x4EBA,0x5927,0x5C0F,0x56FD,0x5BB6,0x5B66,0x6821,0x5148,0x751F,0x5B57,0x6BCD,0x5178,0x8A00,0x8A9E,0x8B58];
var SYM2=[0x20AC,0x00A9,0x00AE,0x2122,0x00B1,0x00D7,0x00F7,0x221E,0x03C0,0x03B1,0x03B2,0x0394,0x2190,0x2192,0x2605,0x263A,0x2713,0x00BD,0x00BC,0x00BE];
var EMOJI=[0x1F600,0x1F601,0x1F602,0x1F603,0x1F604,0x1F30D,0x1F30E,0x1F30F,0x1F680,0x1F4BB,0x1F4A1,0x2764+0xFE0F-0xFE0F,0x1F525,0x1F4AF,0x1F389,0x1F3B5,0x1F3B6,0x26BD,0x1F3C6,0x1F511];
CPS=CPS.concat(CJK,SYM2,EMOJI);
CPS.forEach(function(c){
  var bs=utf8enc(c);
  ONLINE.push({kind:'encoding-record',cat:'text-encodings',title:'UTF-8 U+'+c.toString(16).toUpperCase().padStart(4,'0')+' \u2014 '+bs.length+' byte'+(bs.length>1?'s':''),
    concept:'Code point U+'+c.toString(16).toUpperCase()+' encodes in UTF-8 as '+bs.length+' byte(s): '+bs.map(function(b){return b.toString(16).toUpperCase().padStart(2,'0');}).join(' ')+'.',
    method:'utf8-encode',input:{codepoint:c},output:bs,
    spec:'UTF-8 (RFC 3629): 1 byte 0xxxxxxx; 2 bytes 110xxxxx 10xxxxxx; 3 bytes 1110xxxx 10xxxxxx 10xxxxxx; 4 bytes 11110xxx + 3 continuation bytes.',
    source:'online',source_ref:'Unicode Standard / RFC 3629 \u2014 verified against Buffer'});
});
/* Base64 of common strings (real) */
var B64S=['Hello','Hello, World!','JAH','Signature','database','encoding','binary','quantum','Manon','test123','password','abc','The quick brown fox','lorem ipsum','010101','data','AI','network','archive','checksum'];
for(i=0;i<150;i++){
  var t=B64S[i%B64S.length]+(i>=B64S.length?String((i/B64S.length)|0):'');
  ONLINE.push({kind:'encoding-record',cat:'text-encodings',title:'Base64 of "'+t+'"',
    concept:'Base64 (RFC 4648) encodes every 3 bytes as 4 characters from A-Z a-z 0-9 + /. "'+t+'" \u2192 '+b64enc(t)+'.',
    method:'base64-encode',input:{text:t},output:b64enc(t),
    spec:'Base64 alphabet: A\u2013Z a\u2013z 0\u20139 + /, = pads to a multiple of 4.',
    source:'online',source_ref:'RFC 4648 \u2014 verified against Buffer'});
}
/* CRC32 of strings (real; includes the classic check value) */
var CRCS=['123456789','hello','Hello, World!','test','JAH','password123','The quick brown fox jumps over the lazy dog',''];
for(i=0;i<100;i++){
  var ct=CRCS[i%CRCS.length]+(i>=CRCS.length?'#'+i:'');
  ONLINE.push({kind:'encoding-record',cat:'checksums',title:'CRC-32 of "'+ct.slice(0,24)+'"',
    concept:'CRC-32 (polynomial 0xEDB88320) of "'+ct+'" is '+crc32(ct)+'. The standard check value: CRC-32("123456789") = CBF43926.',
    method:'crc32',input:{text:ct},output:crc32(ct),
    spec:'CRC-32: init 0xFFFFFFFF, process each byte through the 256-entry table, xor out 0xFFFFFFFF.',
    source:'online',source_ref:'CRC-32 standard \u2014 check value CBF43926'});
}
/* Luhn check digits (real) */
for(i=0;i<60;i++){
  var dg=String(400000000000000+((i*7919)%89999999999999)).slice(0,12+ (i%4));
  ONLINE.push({kind:'encoding-record',cat:'checksums',title:'Luhn check digit for '+dg,
    concept:'Luhn algorithm: doubling every second digit from the right and summing gives check digit '+luhnCheckDigit(dg)+' for '+dg+'.',
    method:'luhn',input:{digits:dg},output:luhnCheckDigit(dg),
    spec:'Luhn: from the rightmost digit, double every second digit (subtract 9 if >9), sum; check digit makes the total a multiple of 10.',
    source:'online',source_ref:'Luhn algorithm \u2014 ISO/IEC 7812'});
}
/* parity bits over systematic bit strings (real) */
for(i=0;i<128;i++){
  var bits=i.toString(2).padStart(7,'0'),ty=i%2?'odd':'even';
  ONLINE.push({kind:'encoding-record',cat:'checksums',title:'Parity bit ('+ty+') for '+bits,
    concept:'The '+ty+' parity bit for '+bits+' is '+parity(bits,ty)+', making the total number of 1s '+(ty==='even'?'even':'odd')+'.',
    method:'parity',input:{bits:bits,type:ty},output:parity(bits,ty),
    spec:'Parity: one extra bit forces the count of 1s to the chosen parity; detects any single-bit error.',
    source:'online',source_ref:'Computed by parity definition'});
}
/* RLE examples (real) */
var RLES=['AAABBBCCDAA','WWWWBWWWWBBB','AAAABBBCCDAAA','1122334455','aabbbccccdddd','XXXXXXXXXX'];
for(i=0;i<60;i++){
  var rt=RLES[i%RLES.length]+(i>=RLES.length?'Z'.repeat(1+(i%3)):'');
  ONLINE.push({kind:'encoding-record',cat:'compression',title:'Run-length encoding of "'+rt.slice(0,20)+'"',
    concept:'RLE replaces each run with count+symbol: "'+rt+'" \u2192 "'+rleEnc(rt)+'", decoded back losslessly.',
    method:'rle-encode',input:{text:rt},output:rleEnc(rt),
    spec:'Run-length encoding: maximal runs become (count, symbol) pairs; lossless for repetitive data.',
    source:'online',source_ref:'Computed by RLE definition'});
}
/* Gray codes 0..127 (real) */
for(i=0;i<128;i++){
  ONLINE.push({kind:'encoding-record',cat:'number-systems',title:'Gray code of '+i,
    concept:'Gray code g = n XOR (n>>1): '+i+' \u2192 '+gray(i).toString(2)+'. Adjacent values differ in exactly one bit.',
    method:'gray-code',input:{n:i},output:gray(i).toString(2),
    spec:'Gray code: successive values differ by one bit; used in rotary encoders and Karnaugh maps.',
    source:'online',source_ref:'Computed by Gray code definition'});
}
/* Two's complement -128..127 at 8 bits (real) */
for(i=-128;i<128;i++){
  ONLINE.push({kind:'encoding-record',cat:'number-systems',title:"Two's complement of "+i+' (8-bit)',
    concept:'8-bit two\u2019s complement of '+i+' is '+twos(i,8)+'. Negative values are stored as 2^8 - |v|.',
    method:'twos-complement',input:{value:i,bits:8},output:twos(i,8),
    spec:"Two's complement: the standard signed-integer representation; negation is bitwise NOT plus one.",
    source:'online',source_ref:'Computed by two\u2019s complement definition'});
}
/* binary-op examples (real) */
var BOPS=[['and','1010','1100'],['or','1010','1100'],['xor','1010','1100'],['add','1010','0111'],['not','1010',null],['shl','0011','0010']];
for(i=0;i<72;i++){
  var bo=BOPS[i%BOPS.length];
  ONLINE.push({kind:'encoding-record',cat:'binary-ops',title:'Binary '+bo[0]+' '+(bo[1]+(bo[2]?' , '+bo[2]:'')),
    concept:'Bitwise '+bo[0]+' on '+bo[1]+(bo[2]?' and '+bo[2]:'')+' gives '+binop(bo[0],bo[1],bo[2])+'.',
    method:'binary-op',input:{op:bo[0],a:bo[1],b:bo[2]},output:binop(bo[0],bo[1],bo[2]),
    spec:'Binary operations act per bit (AND/OR/XOR/NOT) or on the whole value (ADD, shifts).',
    source:'online',source_ref:'Computed by bitwise definition'});
}
/* IEEE-754 examples (real, DataView-verified) */
var FLOATS=[0,1,-1,0.5,3.14159,100,-0.0,1.5,2.5,1000000,0.1,256,-273.15];
for(i=0;i<52;i++){
  var fv=FLOATS[i%FLOATS.length];
  ONLINE.push({kind:'encoding-record',cat:'number-systems',title:'IEEE-754 of '+fv,
    concept:'The 32-bit IEEE-754 encoding of '+fv+' is 0x'+ieee754hex(fv)+' (sign, 8-bit exponent, 23-bit mantissa).',
    method:'ieee754',input:{value:fv},output:ieee754hex(fv),
    spec:'IEEE-754 single: 1 sign bit, 8 exponent bits (bias 127), 23 mantissa bits.',
    source:'online',source_ref:'IEEE-754 \u2014 verified against DataView'});
}

/* ---------- generated records (source: signature) ---------- */
function genEx(rnd){
  var methods=Object.keys(EXEC),m=pick(methods,rnd),input;
  if(m==='base-convert'){var b=pick([2,8,16],rnd);input={value:String(ri(rnd,0,500)),from:10,to:b};}
  else if(m==='ascii-byte')input={code:ri(rnd,0,255)};
  else if(m==='utf8-encode')input={codepoint:ri(rnd,0x20,0x2FFF)};
  else if(m==='utf8-decode'){var c2=ri(rnd,0x20,0x2FFF);input={bytes:utf8enc(c2)};}
  else if(m==='base64-encode')input={text:'sig'+ri(rnd,1,9999)};
  else if(m==='base64-decode')input={text:b64enc('sig'+ri(rnd,1,9999))};
  else if(m==='hex-encode')input={text:'hx'+ri(rnd,1,9999)};
  else if(m==='hex-decode')input={text:hexEnc('hx'+ri(rnd,1,9999))};
  else if(m==='url-encode')input={text:'a b&c='+ri(rnd,1,999)};
  else if(m==='url-decode')input={text:urlEnc('a b&c='+ri(rnd,1,999))};
  else if(m==='binary-op'){var op=pick(['and','or','xor','add'],rnd),L=ri(rnd,4,8);input={op:op,a:ri(rnd,0,(1<<L)-1).toString(2).padStart(L,'0'),b:ri(rnd,0,(1<<L)-1).toString(2).padStart(L,'0')};}
  else if(m==='parity')input={bits:ri(rnd,0,255).toString(2).padStart(8,'0'),type:pick(['even','odd'],rnd)};
  else if(m==='luhn')input={digits:String(ri(rnd,100000,999999999999))};
  else if(m==='crc32')input={text:'sigcheck'+ri(rnd,1,99999)};
  else if(m==='rle-encode')input={text:'A'.repeat(ri(rnd,1,6))+'B'.repeat(ri(rnd,1,6))+'C'.repeat(ri(rnd,1,6))};
  else if(m==='rle-decode'){var rt2='X'.repeat(ri(rnd,1,5))+'Y'.repeat(ri(rnd,1,5));input={text:rleEnc(rt2)};}
  else if(m==='gray-code')input={n:ri(rnd,0,500)};
  else if(m==='twos-complement')input={value:ri(rnd,-128,127),bits:8};
  else input={value:ri(rnd,-100,100)+rnd()*0.5};
  return {kind:'exercise',cat:METHOD_CAT[m],title:'Generated exercise: '+METHOD_NAME[m],
    concept:'Convert or compute: apply '+METHOD_NAME[m]+' to the given input and check your answer against the recorded output.',
    method:m,input:input,output:EXEC[m](input),
    spec:'Drill generated by the Signature engine; the output is computed by the reference implementation.',
    source:'signature',creation_mode:'SIGNATURE-GENERATED'};
}

function baseRec(seed,cat,title){return {id:PREFIX+String(seed).padStart(7,'0'),category:cat,title:title,_seed:seed};}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var cat=opts.category;
  if(seed>=1&&seed<=ONLINE.length&&!cat){
    var e=ONLINE[seed-1],r=baseRec(seed,e.cat,e.title);
    Object.keys(e).forEach(function(k){if(k!=='cat'&&k!=='title')r[k]=e[k];});
    return r;
  }
  if(seed>=1&&seed<=ONLINE.length&&cat){
    var pool=ONLINE.filter(function(x){return x.cat===cat;});
    if(pool.length){var e2=pool[(rnd()*pool.length)|0],r2=baseRec(seed,cat,e2.title+' \u2014 archive pick');
      Object.keys(e2).forEach(function(k){if(k!=='cat'&&k!=='title')r2[k]=e2[k];});return r2;}
  }
  var g=genEx(rnd);cat=cat||g.cat;g.category=cat;
  var rec=baseRec(seed,cat,g.title);
  Object.keys(g).forEach(function(k){if(k!=='cat'&&k!=='title')rec[k]=g[k];});
  return rec;
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!/^JAH-BIN-\d{7}$/.test(r.id||''))e.push('id');
  if(CATS.indexOf(r.category)<0)e.push('category');
  if(typeof r.title!=='string'||!r.title.length)e.push('title');
  if(typeof r.concept!=='string'||r.concept.length<10)e.push('concept');
  if(r.source!=='online'&&r.source!=='signature')e.push('source');
  if(r.source==='online'&&typeof r.source_ref!=='string')e.push('source_ref');
  if(r.source==='signature'&&r.creation_mode!=='SIGNATURE-GENERATED')e.push('creation_mode');
  var m=r.method;
  if(!EXEC[m])e.push('method');
  else{
    var got;try{got=EXEC[m](r.input);}catch(x){e.push('exec threw');}
    if(sjson(got)!==sjson(r.output))e.push('output mismatch');
    /* independent oracle cross-checks */
    try{
      if(m==='utf8-encode'){var bb=Buffer.from(String.fromCodePoint(r.input.codepoint),'utf8');if(sjson(Array.from(bb))!==sjson(r.output))e.push('oracle utf8');}
      if(m==='base64-encode'){if(Buffer.from(r.input.text,'latin1').toString('base64')!==r.output)e.push('oracle b64');}
      if(m==='crc32'&&r.input.text==='123456789'){if(r.output!=='CBF43926')e.push('crc check value');}
      if(m==='ieee754'){var dv=new DataView(new ArrayBuffer(4));dv.setFloat32(0,r.input.value);var s='';for(var q=0;q<4;q++)s+=dv.getUint8(q).toString(16).padStart(2,'0');if(s.toUpperCase()!==r.output)e.push('oracle ieee');}
    }catch(x){e.push('oracle threw');}
  }
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  var seen={};(sample||[]).forEach(function(s){if(s&&s.t)seen[s.t]=1;});
  if(seen[rec.title])return {ok:false,errors:['duplicate title in archive sample']};
  return {ok:true,errors:[]};
}
var gen={version:'jahdb-binary-encoding-1.0',generate:generate,validate:validate,driftCheck:driftCheck};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('binary-encoding',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
