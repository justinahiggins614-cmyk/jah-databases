(function(){'use strict';
/* JAH The JAH Signature Binary System Signature Database generator — jahdb-jah-binary-system-signature-1.0.
   Property of Justin Addam Higgins (JAH).
   Deterministic: same seed, same record. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BINYS-";
var FIELDS=["Foundations","Compounded","Advanced"];
var TOPICS={
 "Foundations": [
  "What Is Binary (Signature Edition) - Foundations",
  "Counting in Binary (Signature Edition) - Foundations",
  "Bits, Nibbles, Bytes, and Words (Signature Edition) - Foundations",
  "Binary Addition and the Carry (Signature Edition) - Foundations",
  "Binary Subtraction and Borrowing (Signature Edition) - Foundations",
  "Powers of Two and Data Sizes (Signature Edition) - Foundations",
  "Converting Decimal to Binary (Signature Edition) - Foundations",
  "Converting Binary to Decimal (Signature Edition) - Foundations"
 ],
 "Compounded": [
  "Binary Multiplication by Shift and Add (Signature Edition) - Compounded",
  "Binary Division by Long Division (Signature Edition) - Compounded",
  "Ones Complement (Signature Edition) - Compounded",
  "Twos Complement and Negative Numbers (Signature Edition) - Compounded",
  "Signed Versus Unsigned Integers (Signature Edition) - Compounded",
  "Bitwise AND (Signature Edition) - Compounded",
  "Bitwise OR and XOR (Signature Edition) - Compounded",
  "Bitwise NOT and Bit Masks (Signature Edition) - Compounded",
  "Bit Shifts: Logical and Arithmetic (Signature Edition) - Compounded",
  "Hexadecimal Shorthand (Signature Edition) - Compounded",
  "Octal and Converting Between Bases (Signature Edition) - Compounded",
  "ASCII Text Encoding (Signature Edition) - Compounded",
  "Unicode and UTF-8 (Signature Edition) - Compounded",
  "Fixed-Point Binary Fractions (Signature Edition) - Compounded",
  "IEEE 754 Floating-Point Numbers (Signature Edition) - Compounded"
 ],
 "Advanced": [
  "Logic Gates: AND, OR, and NOT (Signature Edition) - Advanced",
  "XOR, NAND, NOR, and XNOR Gates (Signature Edition) - Advanced",
  "The Half Adder and Full Adder (Signature Edition) - Advanced",
  "Ripple-Carry and Carry-Lookahead Adders (Signature Edition) - Advanced",
  "Parity Bits and Error Detection (Signature Edition) - Advanced",
  "Hamming Error-Correcting Codes (Signature Edition) - Advanced",
  "Cyclic Redundancy Checks (CRC) (Signature Edition) - Advanced",
  "The Binary Reflected Gray Code (Signature Edition) - Advanced",
  "Binary-Coded Decimal (BCD) (Signature Edition) - Advanced",
  "Binary in Networking: Subnet Masks (Signature Edition) - Advanced",
  "Overflow, Carry, and CPU Status Flags (Signature Edition) - Advanced"
 ]
};
function demoProgram(topic,field){
  var safe=String(topic).replace(/\\/g,'\\\\').replace(/"/g,"'");
  return "# Binary System Study — "+safe+"\n"
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
    name:topic+' — binary system record',
    title:topic,
    description:'SAMPLE RECORD (generated — structural sample). A binary system record of "'+topic+'" in '+field+'. Generated samples are clearly labeled and never presented as archive records.',
    field:field,
    src:'signature-generated-sample',
    sample:true,
    disclaimer:'Generated sample record — not an archive record. Seeded archive records are the authoritative entries.',
    demo:{kind:"binary-system-demo",language:'python',program:demoProgram(topic,field),note:'Structural sample demo.'},
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
var gen={version:'jahdb-jah-binary-system-signature-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('jah-binary-system-signature',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
