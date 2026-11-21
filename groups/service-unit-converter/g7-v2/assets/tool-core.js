
/* PURE TOOL FUNCTIONS — the page's own working tool, tested in Node. */
var UC_UNITS={
 length:{base:'m',label:'Length',units:{mm:0.001,cm:0.01,m:1,km:1000,'in':0.0254,ft:0.3048,yd:0.9144,mi:1609.344}},
 weight:{base:'kg',label:'Weight',units:{mg:0.000001,g:0.001,kg:1,t:1000,oz:0.028349523125,lb:0.45359237,st:6.35029318}},
 volume:{base:'l',label:'Volume',units:{ml:0.001,l:1,m3:1000,gal_us:3.785411784,gal_uk:4.54609,pt_us:0.473176473,pt_uk:0.56826125,cup_us:0.2365882365,tbsp:0.0147867648,tsp:0.00492892159}},
 speed:{base:'km/h',label:'Speed',units:{'m/s':3.6,'km/h':1,'mi/h':1.609344,kn:1.852}},
 area:{base:'m2',label:'Area',units:{m2:1,km2:1000000,ft2:0.09290304,mi2:2589988.110336,acre:4046.8564224,ha:10000}},
 time:{base:'s',label:'Time',units:{s:1,min:60,h:3600,day:86400,week:604800}},
 data:{base:'MB',label:'Data size',units:{B:0.000001,KB:0.001,MB:1,GB:1000,TB:1000000}},
 pressure:{base:'Pa',label:'Pressure',units:{Pa:1,kPa:1000,bar:100000,psi:6894.757293168}},
 energy:{base:'J',label:'Energy',units:{J:1,kJ:1000,cal:4.184,kcal:4184,'kWh':3600000}},
 power:{base:'W',label:'Power',units:{W:1,kW:1000,hp:745.699872,hp_metric:735.49875}},
 angle:{base:'deg',label:'Angle',units:{deg:1,rad:57.29577951308232}}
};
var UC_TEMP={c:{label:'Celsius'},f:{label:'Fahrenheit'},k:{label:'Kelvin'}};
function ucConvert(value, category, from, to){
  if(category==='temperature'){
    var c;
    if(from==='c') c=value;
    else if(from==='f') c=(value-32)*5/9;
    else if(from==='k') c=value-273.15;
    else throw new Error('Unknown temperature unit.');
    if(to==='c') return c;
    if(to==='f') return c*9/5+32;
    if(to==='k') return c+273.15;
    throw new Error('Unknown temperature unit.');
  }
  var t=UC_UNITS[category];
  if(!t) throw new Error('Unknown kind of unit.');
  if(!(from in t.units) || !(to in t.units)) throw new Error('Unknown unit for this kind.');
  return value*t.units[from]/t.units[to];
}
function ucFormat(v){
  if(v===0) return '0';
  var a=Math.abs(v);
  if(a>=1000000 || a<0.000001) return v.toExponential(6);
  var s=String(Math.round(v*1000000)/1000000);
  return s;
}


if(typeof module!=='undefined'){module.exports={UC_UNITS: UC_UNITS, ucConvert: ucConvert, ucFormat: ucFormat};}
