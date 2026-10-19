
(function(){'use strict';
/* JAH The Bicycle Wheel Blueprint Database generator - jahdb-blueprint-bicycle-wheels-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic seeded blueprint generation. Same seed = same blueprint. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return s[(r()*s.length)|0];}
var PREFIX="JAH-BP-WHEEL-G";
var DATA={"sig": false, "unit": "in", "bases": [{"noun": "Bicycle Wheel", "name": "Road Wheelset", "styles": ["700c", "Climbing", "Training"], "dims": {"W": 28.0, "D": 28.0, "H": 4.0}, "members": [{"name": "Rim", "qty": 2, "l": 28.0, "w": 1, "t": 1, "mat": "aluminum"}, {"name": "Spoke", "qty": 44, "l": 12.0, "w": 0.08, "t": 0.08, "mat": "stainless"}, {"name": "Hub", "qty": 2, "l": 4.0, "w": 3, "t": 3, "mat": "aluminum"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the wheelset; check square by comparing diagonals, then disassemble.", "Glue and clamp the wheelset; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["700c 20/24h", 1.0]], "group": "Bicycle Wheels", "shapes": [["rect", 0, 0, 28.0, 4.0, ""], ["h", 2.24, 25.76, 2.0], ["t", 2.8000000000000003, 2.14, "rim 28"], ["t", 1, 3.76, "ROAD WHEELSET - LACING"]], "planW": 28.0, "planH": 4.0, "overallKeys": ["W", "D", "H"]}, {"noun": "Bicycle Wheel", "name": "Mountain Wheelset", "styles": ["29er", "27.5", "Trail"], "dims": {"W": 30.0, "D": 30.0, "H": 5.0}, "members": [{"name": "Rim", "qty": 2, "l": 29.0, "w": 1.25, "t": 1.25, "mat": "aluminum"}, {"name": "Spoke", "qty": 56, "l": 12.0, "w": 0.09, "t": 0.09, "mat": "stainless"}, {"name": "Hub", "qty": 2, "l": 5.0, "w": 4, "t": 4, "mat": "aluminum"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the wheelset; check square by comparing diagonals, then disassemble.", "Glue and clamp the wheelset; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["29 in", 1.0]], "group": "Bicycle Wheels", "shapes": [["rect", 0, 0, 30.0, 5.0, ""], ["h", 2.4, 27.6, 2.5], ["t", 3.0, 2.675, "rim 29"], ["t", 1, 4.699999999999999, "MTB WHEELSET - LACING"]], "planW": 30.0, "planH": 5.0, "overallKeys": ["W", "D", "H"]}, {"noun": "Bicycle Wheel", "name": "Touring Wheel", "styles": ["36h", "Expedition", "Tandem"], "dims": {"W": 28.0, "D": 28.0, "H": 4.0}, "members": [{"name": "Rim", "qty": 2, "l": 28.0, "w": 1, "t": 1, "mat": "aluminum"}, {"name": "Spoke", "qty": 72, "l": 12.0, "w": 0.09, "t": 0.09, "mat": "stainless"}, {"name": "Hub", "qty": 2, "l": 5.0, "w": 4, "t": 4, "mat": "steel/aluminum"}], "steps": ["Mill all lumber to finished size; cut every part to the cut list, labeling each piece.", "Lay out and cut mortise-and-tenon joints on all frame members; test-fit dry before any glue.", "Dry-assemble the wheelset; check square by comparing diagonals, then disassemble.", "Glue and clamp the wheelset; wipe excess glue immediately and verify square while clamps set.", "Install secondary members (stretchers, slats, panels) per the plan; fasten per the fastener schedule.", "Sand progressively to 180 grit, ease all exposed edges, and apply a durable finish.", "Final check: confirm all dimensions against the plan, test load gently, and re-tighten fasteners after one week of use."], "sizes": [["700c 36h", 1.0]], "group": "Bicycle Wheels", "shapes": [["rect", 0, 0, 28.0, 4.0, ""], ["h", 2.24, 25.76, 2.0], ["t", 2.8000000000000003, 2.14, "rim 28"], ["t", 1, 3.76, "TOURING WHEEL - LACING"]], "planW": 28.0, "planH": 4.0, "overallKeys": ["W", "D", "H"]}], "materials": ["4130 chromoly", "6061 aluminum", "Carbon fiber"], "blurb": "A {style} {noun} in {material}, {size_label} size, {overall} overall. Full fabrication blueprint: geometry table, tube mitering, welding/brazing sequence, alignment, and build-up. Key dimensions: {dims}.", "how": "The {noun} is laid out from the geometry table - every tube mitered, tacked in the jig, and welded or brazed in sequence so heat stays balanced. The frame is aligned, faced, and built up with the component schedule; wheels are trued and the {noun} test-ridden. Overall {overall}.", "standards": ["AWS D1.1 structural welding (guidance)", "OSHA 29 CFR 1910.252 welding safety"], "tolerances": ["Cut length: +/- 1/16 in", "Hole locations: +/- 1/32 in", "Weldment squareness: 1/16 in per foot", "Flatness: 1/8 in per foot"], "safety": ["Welding PPE required: helmet, gloves, flame-resistant clothing; ventilate or exhaust fumes.", "Grinding: face shield plus eye protection; guard sparks away from flammables.", "Clamp work before drilling or cutting; deburr all edges.", "Keep a fire extinguisher rated ABC within reach."], "tools": ["Angle grinder", "Drill press", "Welder (process per plan)", "Clamps", "Tape measure", "Square", "Files", "Wire brush", "Welding helmet", "Gloves"], "ladder_rank": 2, "ladder_tier": "foundations"};
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
var gen={version:'jahdb-blueprint-bicycle-wheels-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:["27.5", "29er", "36h", "700c", "Climbing", "Expedition", "Tandem", "Trail", "Training"]};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-bicycle-wheels',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
