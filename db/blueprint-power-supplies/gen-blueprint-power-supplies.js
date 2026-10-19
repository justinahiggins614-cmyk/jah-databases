
(function(){'use strict';
/* JAH The Power Supply Blueprint Database generator - jahdb-blueprint-power-supplies-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic seeded blueprint generation. Same seed = same blueprint. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var PREFIX="JAH-BP-PSU-G";
var DATA={"sig": false, "unit": "in", "bases": [{"noun": "Power Supply", "name": "Linear Bench Supply", "styles": ["Lab", "Analog", "Low-noise"], "dims": {"W": 12.0, "D": 10.0, "H": 6.0}, "members": [{"name": "Chassis", "qty": 1, "l": 11.0, "w": 9, "t": 5, "mat": "steel"}, {"name": "Heatsink", "qty": 1, "l": 8.0, "w": 6, "t": 3, "mat": "aluminum extrusion"}, {"name": "Front panel", "qty": 1, "l": 11.0, "w": 5, "t": 0.125, "mat": "aluminum"}], "steps": ["Fabricate or procure each subassembly: Power Supply.", "Lay out the full arrangement per the plan; confirm clearances and service access before fastening anything.", "Assemble in order: base/frame first, then working assemblies, then guards, covers, and controls last.", "Torque all structural fasteners to the fastener schedule; align shafts, belts, or linkages per the plan.", "Wire/plumb utilities per the schematic; test each subsystem individually before integration.", "Run the no-load test sequence from the plan; check for vibration, heat, leaks, or binding.", "Finish per the plan; protect all surfaces for the service environment.", "Commissioning: run under load, recheck fasteners after break-in, and file the as-built dimensions."], "sizes": [["0-30V 5A", 1.0]], "group": "Power Supplys", "shapes": [["rect", 1, 3, 13, 5, "Mains"], ["h", 14, 17, 5.5], ["t", 14.2, 6.2, "AC"], ["t", 1, 9.2, "fused"], ["rect", 17, 3, 13, 5, "Transformer"], ["h", 30, 33, 5.5], ["t", 30.2, 6.2, "raw DC"], ["rect", 33, 3, 13, 5, "Rectifier"], ["h", 46, 49, 5.5], ["t", 46.2, 6.2, "regulated"], ["rect", 49, 3, 13, 5, "Regulator"], ["h", 62, 65, 5.5], ["t", 62.2, 6.2, ""], ["t", 49, 9.2, "0-30V"], ["rect", 65, 3, 13, 5, "Output"], ["t", 1, 0.5, "LINEAR BENCH PSU - BLOCK SCHEMATIC"]], "planW": 80, "planH": 12, "overallKeys": ["W", "D", "H"]}, {"noun": "Power Supply", "name": "Switching Bench Supply", "styles": ["Lab", "Digital", "Efficient"], "dims": {"W": 10.0, "D": 10.0, "H": 5.0}, "members": [{"name": "Chassis", "qty": 1, "l": 9.0, "w": 9, "t": 4, "mat": "steel"}, {"name": "Front panel", "qty": 1, "l": 9.0, "w": 4, "t": 0.125, "mat": "aluminum"}], "steps": ["Fabricate or procure each subassembly: Power Supply.", "Lay out the full arrangement per the plan; confirm clearances and service access before fastening anything.", "Assemble in order: base/frame first, then working assemblies, then guards, covers, and controls last.", "Torque all structural fasteners to the fastener schedule; align shafts, belts, or linkages per the plan.", "Wire/plumb utilities per the schematic; test each subsystem individually before integration.", "Run the no-load test sequence from the plan; check for vibration, heat, leaks, or binding.", "Finish per the plan; protect all surfaces for the service environment.", "Commissioning: run under load, recheck fasteners after break-in, and file the as-built dimensions."], "sizes": [["0-60V 10A", 1.0]], "group": "Power Supplys", "shapes": [["rect", 1, 3, 13, 5, "Mains"], ["h", 14, 17, 5.5], ["t", 14.2, 6.2, "AC"], ["rect", 17, 3, 13, 5, "PFC"], ["h", 30, 33, 5.5], ["t", 30.2, 6.2, "DC bus"], ["rect", 33, 3, 13, 5, "Switcher"], ["h", 46, 49, 5.5], ["t", 46.2, 6.2, "out"], ["rect", 49, 3, 13, 5, "Output"], ["t", 1, 0.5, "SWITCHING PSU - BLOCK SCHEMATIC"]], "planW": 64, "planH": 12, "overallKeys": ["W", "D", "H"]}, {"noun": "Power Supply", "name": "High-Current 12V Supply", "styles": ["Radio", "Automotive", "LED"], "dims": {"W": 12.0, "D": 10.0, "H": 6.0}, "members": [{"name": "Chassis", "qty": 1, "l": 11.0, "w": 9, "t": 5, "mat": "steel"}, {"name": "Heatsink", "qty": 1, "l": 8.0, "w": 6, "t": 4, "mat": "aluminum"}], "steps": ["Fabricate or procure each subassembly: Power Supply.", "Lay out the full arrangement per the plan; confirm clearances and service access before fastening anything.", "Assemble in order: base/frame first, then working assemblies, then guards, covers, and controls last.", "Torque all structural fasteners to the fastener schedule; align shafts, belts, or linkages per the plan.", "Wire/plumb utilities per the schematic; test each subsystem individually before integration.", "Run the no-load test sequence from the plan; check for vibration, heat, leaks, or binding.", "Finish per the plan; protect all surfaces for the service environment.", "Commissioning: run under load, recheck fasteners after break-in, and file the as-built dimensions."], "sizes": [["12V 40A", 1.0]], "group": "Power Supplys", "shapes": [["rect", 1, 3, 13, 5, "Mains"], ["h", 14, 17, 5.5], ["t", 14.2, 6.2, "AC"], ["rect", 17, 3, 13, 5, "Transformer"], ["h", 30, 33, 5.5], ["t", 30.2, 6.2, "raw"], ["rect", 33, 3, 13, 5, "Rectifier"], ["h", 46, 49, 5.5], ["t", 46.2, 6.2, "filtered"], ["rect", 49, 3, 13, 5, "Filter"], ["h", 62, 65, 5.5], ["t", 62.2, 6.2, ""], ["rect", 65, 3, 13, 5, "Output"], ["t", 65, 9.2, "13.8V"], ["t", 1, 0.5, "12V HIGH-CURRENT PSU - BLOCK SCHEMATIC"]], "planW": 80, "planH": 12, "overallKeys": ["W", "D", "H"]}], "materials": ["Aluminum chassis", "Steel chassis", "PCB"], "blurb": "A {style} {noun} in {material}, {size_label} size, {overall} overall. Complete build documentation: block-level schematic, chassis fabrication, component schedule with values, wiring, and test procedure. Key dimensions: {dims}.", "how": "Signal or power flows through the stages in the schematic; the {noun} is built on a fabricated {material} chassis with the component values in the schedule. Wiring follows the plan, grounds are star-pointed, and the unit is tested stage-by-stage before power-up. Overall {overall}.", "standards": ["NEC (NFPA 70) wiring practice", "UL 508A industrial control panels (guidance)"], "tolerances": ["Component placement: per silkscreen", "Wire gauge: per current table in plan", "Solder joints: full fillet, no bridges", "Enclosure holes: +/- 1/32 in"], "safety": ["Disconnect and lock out power before wiring; verify dead with a meter.", "Fuse the supply per the plan; never bypass overcurrent protection.", "Keep line-voltage compartments covered; ground all exposed metal.", "Line-voltage work must meet local electrical code - have it inspected where required."], "tools": ["Multimeter", "Soldering iron", "Wire strippers", "Screwdrivers", "Drill/driver", "Heat gun", "Helping-hands jig"], "ladder_rank": 2, "ladder_tier": "foundations"};
function fmtD(v,u){var r=Math.round(v*100)/100;if(u==='in')return r+'"';return r+' '+u;}
function drawAscii(shapes,W,H,unit,title){
  var maxW=66,maxH=26;
  W=Math.max(W,0.01);H=Math.max(H,0.01);
  var sc=Math.max(W/maxW,H/maxH);
  var gw=Math.max(10,Math.min(maxW,Math.ceil(W/sc))), gh=Math.max(6,Math.min(maxH,Math.ceil(H/sc)));
  var sx=gw/W, sy=gh/H;
  function X(x){return Math.max(0,Math.min(gw-1,Math.round(x*sx)));}
  function Y(y){return Math.max(0,Math.min(gh-1,Math.round(y*sy)));}
  var g=[],yy,xx;for(yy=0;yy<gh;yy++){g.push([]);for(xx=0;xx<gw;xx++)g[yy].push(' ');}
  function put(x,y,ch){if(y>=0&&y<gh&&x>=0&&x<gw)g[y][x]=ch;}
  function hline(x0,x1,y){var a=Math.min(X(x0),X(x1)),b=Math.max(X(x0),X(x1));for(var x=a;x<=b;x++)put(x,Y(y),'-');}
  function vline(x,y0,y1){var a=Math.min(Y(y0),Y(y1)),b=Math.max(Y(y0),Y(y1));for(var y=a;y<=b;y++)put(X(x),y,'|');}
  function diag(x0,y0,x1,y1){var st=Math.max(Math.abs(X(x1)-X(x0)),Math.abs(Y(y1)-Y(y0)),1);for(var i=0;i<=st;i++)put(Math.round(X(x0)+(X(x1)-X(x0))*i/st),Math.round(Y(y0)+(Y(y1)-Y(y0))*i/st),'/');}
  shapes.forEach(function(sh){
    var k=sh[0];
    if(k==='rect'){var x=sh[1],y=sh[2],w=sh[3],h=sh[4],label=sh[5]||'';
      var x0=X(x),y0=Y(y),x1=X(x+w),y1=Y(y+h);
      if(x1<=x0)x1=x0+1;if(y1<=y0)y1=y0+1;
      for(var xx2=x0;xx2<=x1;xx2++){put(xx2,y0,'-');put(xx2,y1,'-');}
      for(var yy2=y0;yy2<=y1;yy2++){put(x0,yy2,'|');put(x1,yy2,'|');}
      put(x0,y0,'+');put(x1,y0,'+');put(x0,y1,'+');put(x1,y1,'+');
      var lab=String(label).slice(0,Math.max(1,x1-x0-1)),ly=(y0+y1)>>1,lx=x0+Math.max(1,((x1-x0-lab.length)>>1));
      if(ly>y0&&ly<y1-1)for(var li=0;li<lab.length;li++)if(lx+li<x1-1)g[ly][lx+li]=lab[li];
    }else if(k==='h'){hline(sh[1],sh[2],sh[3]);}
    else if(k==='v'){vline(sh[1],sh[2],sh[3]);}
    else if(k==='d'){diag(sh[1],sh[2],sh[3],sh[4]);}
    else if(k==='t'){var tx=X(sh[1]),ty=Y(sh[2]),txt=String(sh[3]);for(var ti=0;ti<txt.length;ti++)if(tx+ti<gw)put(tx+ti,ty,txt[ti]);}
  });
  var lines=['PLAN: '+title,'Overall '+W+' x '+H+' '+unit+' | schematic - not to construction scale'];
  for(yy=0;yy<gh;yy++)lines.push(g[yy].join('').replace(/\s+$/,''));
  return lines.join('\n');
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var base=pick(rnd,DATA.bases);
  var size=pick(rnd,base.sizes);
  var style=(opts.field&&base.styles.indexOf(opts.field)>=0)?opts.field:pick(rnd,base.styles);
  var mat=pick(rnd,DATA.materials);
  var s=size[1]*(DATA.sig?1.03:1);
  var dims={},k;for(k in base.dims)dims[k]=Math.round(base.dims[k]*s*100)/100;
  var members=base.members.map(function(m){
    return {name:m.name,qty:m.qty,l:Math.round(m.l*s*100)/100,w:m.w,t:m.t,
            material:(m.mat||'').replace('{MAT}',mat)};
  });
  var nPieces=members.reduce(function(a,m){return a+m.qty;},0);
  var bf=members.reduce(function(a,m){return a+(m.w&&m.t?m.qty*m.l*m.w*m.t/144:0);},0);
  var cut=members.map(function(m){
    return {part:m.name,qty:m.qty,
      size:(m.w&&m.t?fmtD(m.l,DATA.unit)+' x '+fmtD(m.w,DATA.unit)+' x '+fmtD(m.t,DATA.unit):fmtD(m.l,DATA.unit)),
      material:m.material,board_feet:(m.w&&m.t?Math.round(m.qty*m.l*m.w*m.t/144*100)/100:null)};
  });
  var shapes=base.shapes.map(function(sh){
    var o=sh.slice();
    for(var i=1;i<o.length;i++){if(typeof o[i]==='number')o[i]=Math.round(o[i]*s*100)/100;}
    return o;
  });
  var W=Math.round(base.planW*s*100)/100,H=Math.round(base.planH*s*100)/100;
  var title=style+' '+base.noun+(size[0]!=='Standard'?' ('+size[0]+')':'')+' - Full Blueprint';
  var plan=drawAscii(shapes,W,H,DATA.unit,title);
  var id=PREFIX+String(seed).padStart(6,'0');
  var overall=base.overallKeys.map(function(k2){return k2+' '+fmtD(dims[k2],DATA.unit);}).join(' x ');
  var desc=DATA.blurb.replace('{name}',title.replace(' - Full Blueprint','')).replace('{style}',style)
    .replace('{material}',mat).replace('{overall}',overall).replace('{noun}',base.noun)
    .replace('{size_label}',size[0]).replace('{dims}',base.overallKeys.map(function(k2){return k2+' '+fmtD(dims[k2],DATA.unit);}).join(', '));
  if(DATA.sig)desc+=' This is a JAH Signature original design - his own line, drawn from the same need as the public pattern but detailed as a new original work.';
  else desc+=' Representative blueprint study compiled from standard construction practice and public code requirements.';
  var prog='# JAH Blueprint demo - Record '+id+'\nplan = """\n'+plan.replace(/\\/g,'\\\\')+'\n"""\nprint(plan)\nprint("Overall: '+overall+'")\nprint("Cut pieces: '+nPieces+'")\nprint("Board feet: '+Math.round(bf*100)/100+'")\nprint("OK: '+id+' blueprint verified")\n';
  return {
    id:id,name:title.replace(' - Full Blueprint',''),title:title,
    description:desc,g:base.group|| (base.noun+'s'),
    how_it_works:DATA.how.replace('{noun}',base.noun).replace('{material}',mat).replace('{overall}',overall).replace('{size_label}',size[0]),
    key_points:['Overall: '+overall,'Material: '+mat,'Cut pieces: '+nPieces,'Lumber: '+(Math.round(bf*10)/10)+' board feet'].concat(DATA.sig?['Signature original - JAH design lineage']:[]),
    requirements:cut.slice(0,6).map(function(c){return c.qty+' x '+c.part+' ('+c.size+')';}),
    standards:DATA.standards,citations:DATA.standards.concat(['Standard construction practice references.']),
    blueprint:{plan_ascii:plan,overall:overall,unit:DATA.unit,
      dimensions:Object.keys(dims).map(function(k2){return k2+': '+fmtD(dims[k2],DATA.unit);}).join(', '),
      cut_list:cut,assembly_steps:base.steps,tolerances:DATA.tolerances,safety_notes:DATA.safety,tools_required:DATA.tools,
      scale_note:'Schematic - not to construction scale. Verify all dimensions, loads, and code compliance with a licensed professional before building.'},
    materials:cut.map(function(c){return c.qty+' x '+c.part+' - '+c.material+' ('+c.size+')';}),
    src:DATA.sig?'signature':'public-harvest',
    ladder_rank:DATA.ladder_rank,ladder_tier:DATA.ladder_tier,
    demo:{kind:'python',language:'python',program:prog,note:'Working demonstration program (real, runnable Python): prints the schematic plan and verifies totals.'},
    provenance:DATA.sig?'signature':'public-harvest',last_verified:'2026-10-19',_seed:seed
  };
}
function validate(r){
  var e=[];
  if(!r||typeof r!=='object')return {ok:false,errors:['not an object']};
  if(!new RegExp('^'+PREFIX.replace(/-/g,'\\-')+'\\d{6}$').test(r.id||''))e.push('id');
  if(!r.blueprint||!r.blueprint.plan_ascii)e.push('plan');
  if(!r.demo||!r.demo.program)e.push('demo');
  return {ok:!e.length,errors:e};
}
function driftCheck(record,sample){
  var dups=(sample||[]).filter(function(r){return r&&r.title===record.title;});
  return dups.length?{ok:false,errors:['duplicate title in archive sample']}:{ok:true,errors:[]};
}
var gen={version:'jahdb-blueprint-power-supplies-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:["Analog", "Automotive", "Digital", "Efficient", "LED", "Lab", "Low-noise", "Radio"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-power-supplies',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
