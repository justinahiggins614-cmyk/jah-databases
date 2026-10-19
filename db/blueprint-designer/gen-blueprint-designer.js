(function(){'use strict';
/* JAH The Blueprint Designer Database generator — jahdb-blueprint-designer-1.0.
   Property of Justin Addam Higgins (JAH).
   The Blueprint Designer: deterministic need-driven blueprint generation.
   Same seed + same category = same blueprint. */
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX="JAH-BDGN-";
var FIELDS=["houses", "stores", "offices", "warehouses", "apartments", "barns", "schools", "factories", "machines", "tools", "devices", "vehicles", "infrastructure"];
var SIZES=["compact","standard","grand"];
var SCALE={compact:0.85,standard:1,grand:1.22};
var CONSTRAINTS=["tight budget","narrow lot","flood zone","high wind zone","steep slope","off-grid power","fast-track build","future expansion","historic district","noise ordinance"];
var PURPOSES={"houses": ["family living", "rental income", "retirement downsizing", "guest housing"], "stores": ["main-street retail", "grocery anchor", "specialty shop", "pop-up to permanent"], "offices": ["startup headquarters", "professional practice", "branch office", "remote hub"], "warehouses": ["regional distribution", "cold chain", "e-commerce fulfillment", "contractor storage"], "apartments": ["workforce housing", "senior living", "student housing", "luxury rental"], "barns": ["dairy operation", "horse boarding", "hay and feed", "equipment shelter"], "schools": ["elementary campus", "STEM wing", "community school", "rural school"], "factories": ["light assembly", "food processing", "craft manufacturing", "maker industrial"], "machines": ["farm power", "material handling", "shop production", "backup power"], "tools": ["carpentry kit", "mechanic kit", "workshop outfitting", "field repair"], "devices": ["kitchen suite", "climate control", "home office", "laundry"], "vehicles": ["family transport", "work truck", "water recreation", "last-mile delivery"], "infrastructure": ["river crossing", "flood defense", "rural power", "water supply"]};
var TYPES={"houses": [{"n": "Ranch House", "rooms": [["Living Room", 16, 14], ["Kitchen", 12, 10], ["Dining", 12, 10], ["Primary Bedroom", 14, 12], ["Bedroom 2", 12, 11], ["Bedroom 3", 11, 10], ["Bath", 8, 6], ["Hall Bath", 8, 6], ["Utility", 8, 8], ["Garage", 20, 20]]}, {"n": "Cape Cod Cottage", "rooms": [["Living Room", 15, 13], ["Kitchen", 11, 10], ["Dining Nook", 9, 8], ["Bedroom Down", 12, 10], ["Bedroom Up 1", 12, 10], ["Bedroom Up 2", 11, 9], ["Bath", 8, 6], ["Hall Bath", 7, 6], ["Entry", 6, 6]]}, {"n": "Colonial Two-Story", "rooms": [["Living Room", 15, 13], ["Dining Room", 14, 12], ["Kitchen", 13, 11], ["Family Room", 16, 13], ["Foyer", 8, 10], ["Primary Bedroom", 15, 13], ["Bedroom 2", 12, 11], ["Bedroom 3", 12, 10], ["Bedroom 4", 11, 10], ["Primary Bath", 10, 8], ["Hall Bath", 8, 6], ["Laundry", 8, 6]]}, {"n": "Craftsman Bungalow", "rooms": [["Front Porch", 20, 8], ["Living Room", 15, 13], ["Dining Room", 13, 11], ["Kitchen", 12, 10], ["Primary Bedroom", 13, 12], ["Bedroom 2", 11, 10], ["Bedroom 3", 10, 9], ["Bath", 8, 6], ["Hall Bath", 7, 5], ["Nook", 8, 8]]}], "stores": [{"n": "General Store", "rooms": [["Sales Floor", 40, 30], ["Checkout", 12, 8], ["Stockroom", 20, 15], ["Office", 10, 10], ["Restroom", 8, 6], ["Entry Vestibule", 8, 8], ["Loading", 12, 10]]}, {"n": "Supermarket", "rooms": [["Sales Floor", 120, 80], ["Produce", 30, 20], ["Meat Prep", 25, 20], ["Deli/Bakery", 25, 20], ["Dairy Cooler", 20, 15], ["Frozen Aisles", 40, 12], ["Checkout Lanes", 40, 15], ["Stockroom", 40, 25], ["Loading Dock", 30, 15], ["Office", 12, 10], ["Restrooms", 12, 10]]}, {"n": "Convenience Store", "rooms": [["Sales Floor", 40, 25], ["Cooler Line", 30, 8], ["Foodservice", 15, 12], ["Checkout", 10, 8], ["Restrooms", 10, 8], ["Office", 8, 8], ["Stockroom", 12, 10], ["Fuel Canopy", 80, 30]]}, {"n": "Clothing Boutique", "rooms": [["Entry Gallery", 15, 12], ["Main Salon", 30, 20], ["Fitting Suite", 15, 12], ["Cash Wrap", 8, 8], ["Stockroom", 15, 12], ["Office", 8, 8], ["Restroom", 7, 6]]}], "offices": [{"n": "Open-Plan Office", "rooms": [["Workstations", 60, 30], ["Meeting Room A", 16, 12], ["Meeting Room B", 12, 10], ["Phone Booths", 8, 8], ["Break Room", 16, 12], ["Copy/Print", 10, 8], ["Reception", 14, 10], ["Storage", 10, 8], ["Restrooms", 14, 10]]}, {"n": "Executive Suite", "rooms": [["Corner Office", 16, 14], ["Private Office A", 14, 12], ["Private Office B", 14, 12], ["Assistant Zone", 20, 12], ["Boardroom", 24, 16], ["Reception", 14, 12], ["Waiting", 12, 10], ["File Room", 10, 8], ["Pantry", 10, 8]]}, {"n": "Co-Working Hub", "rooms": [["Hot Desk Floor", 50, 30], ["Dedicated Desks", 30, 15], ["Private Offices", 20, 12], ["Phone Booths", 10, 8], ["Event Lounge", 25, 18], ["Kitchen", 14, 10], ["Print Bar", 8, 8], ["Lockers", 12, 6]]}, {"n": "Law Firm Office", "rooms": [["Partner Office", 12, 15], ["Partner Office B", 12, 15], ["Associate Office", 10, 12], ["Secretarial Bay", 24, 10], ["Conference Center", 30, 18], ["Law Library", 25, 18], ["File Room", 15, 12], ["Reception", 16, 12], ["Pantry", 10, 8]]}], "warehouses": [{"n": "Distribution Center", "rooms": [["Rack Storage", 300, 200], ["Staging", 100, 40], ["Shipping Office", 20, 15], ["Value-Added", 40, 30], ["Battery Charging", 20, 15], ["Offices", 30, 20], ["Break Room", 20, 15], ["Restrooms", 15, 12], ["Dock Court", 300, 120]]}, {"n": "Cold Storage Warehouse", "rooms": [["Freezer Storage", 150, 100], ["Blast Freeze", 40, 25], ["Tempering", 30, 20], ["Dock", 60, 20], ["Engine Room", 25, 20], ["Offices", 25, 15], ["Battery Charging", 15, 12], ["Restrooms", 12, 10]]}, {"n": "Fulfillment Warehouse", "rooms": [["Pick Modules", 200, 120], ["Decant", 60, 30], ["Pack Stations", 80, 30], ["Sortation", 60, 40], ["Robotics Zone", 80, 60], ["Outbound Staging", 60, 30], ["Offices", 30, 20], ["Break Room", 25, 18]]}, {"n": "Bulk Storage Shed", "rooms": [["Storage Volume", 120, 80], ["Push Walls", 120, 4], ["Office", 12, 10], ["Scale House", 10, 8], ["Equipment Bay", 20, 15]]}], "apartments": [{"n": "Studio Apartment", "rooms": [["Living/Sleeping", 18, 14], ["Kitchenette", 10, 8], ["Bath", 8, 6], ["Closet", 6, 4], ["Entry", 5, 5]]}, {"n": "One-Bedroom Apartment", "rooms": [["Living Room", 14, 12], ["Kitchen", 10, 9], ["Bedroom", 12, 11], ["Bath", 8, 6], ["Closet", 6, 5], ["Balcony", 10, 6], ["Entry", 5, 6]]}, {"n": "Two-Bedroom Apartment", "rooms": [["Living/Dining", 18, 14], ["Kitchen", 11, 10], ["Primary Bedroom", 13, 12], ["Primary Bath", 9, 7], ["Bedroom 2", 11, 10], ["Hall Bath", 8, 6], ["Laundry", 6, 6], ["Balcony", 12, 6]]}, {"n": "Three-Bedroom Apartment", "rooms": [["Living/Dining", 20, 15], ["Kitchen", 12, 10], ["Primary Bedroom", 14, 12], ["Primary Bath", 9, 7], ["Bedroom 2", 11, 10], ["Bedroom 3", 11, 10], ["Hall Bath", 8, 6], ["Laundry", 6, 6], ["Storage", 6, 8]]}], "barns": [{"n": "Dairy Barn", "rooms": [["Stanchion Rows", 80, 30], ["Feed Alley", 80, 10], ["Milk House", 20, 15], ["Haymow", 80, 30], ["Calf Pens", 25, 20], ["Maternity", 20, 15], ["Office", 10, 8]]}, {"n": "Horse Stable", "rooms": [["Center Aisle", 80, 14], ["Box Stalls", 80, 24], ["Tack Room", 12, 12], ["Wash Bay", 12, 10], ["Feed Room", 10, 10], ["Hay Storage", 25, 20], ["Office", 10, 10]]}, {"n": "Hay Barn", "rooms": [["Hay Storage", 60, 40], ["Equipment Corner", 20, 15], ["Drive Aisle", 60, 12]]}, {"n": "Tobacco Barn", "rooms": [["Curing Tiers", 40, 24], ["Drive Floor", 40, 12], ["Stripping Room", 20, 15]]}], "schools": [{"n": "One-Room Schoolhouse", "rooms": [["Classroom", 28, 22], ["Entry Vestibule", 10, 8], ["Cloakroom", 10, 6], ["Teacher Corner", 8, 8]]}, {"n": "Elementary School", "rooms": [["Classroom A", 30, 30], ["Classroom B", 30, 30], ["Classroom C", 30, 30], ["Classroom D", 30, 30], ["Admin Suite", 25, 18], ["Library", 40, 30], ["Cafeteria/Gym", 60, 40], ["Art Room", 30, 25], ["Music Room", 30, 25], ["Kitchen", 25, 20], ["Secure Vestibule", 12, 10]]}, {"n": "Middle School", "rooms": [["Team Wing A", 80, 40], ["Team Commons", 30, 25], ["Science Lab", 30, 25], ["Science Prep", 12, 10], ["Gymnasium", 84, 50], ["Locker Rooms", 30, 20], ["Cafeteria", 50, 35], ["Library", 40, 30], ["Art Room", 30, 25], ["Music Room", 35, 25], ["Admin Suite", 25, 18]]}, {"n": "High School", "rooms": [["Academic Wing", 120, 50], ["Science Wing", 80, 40], ["CTE Shops", 80, 50], ["Auditorium", 70, 50], ["Gymnasium", 94, 55], ["Cafeteria Commons", 70, 45], ["Library", 60, 40], ["Admin", 30, 20], ["Band/Choir", 40, 30], ["Kitchen", 30, 25]]}], "factories": [{"n": "Assembly Plant", "rooms": [["Assembly Line", 300, 60], ["Subassembly", 100, 40], ["Parts Supermarket", 80, 30], ["Receiving", 60, 30], ["Shipping", 60, 30], ["Offices", 40, 25], ["Cafeteria", 30, 20], ["Maintenance", 30, 20]]}, {"n": "Textile Mill", "rooms": [["Weaving Floor", 150, 100], ["Yarn Prep", 60, 30], ["Dye House", 60, 40], ["Finishing", 50, 30], ["Warehouse", 60, 40], ["Offices", 30, 20], ["Boiler Room", 25, 20]]}, {"n": "Food Processing Plant", "rooms": [["Processing Hall", 120, 80], ["Packaging Hall", 80, 40], ["Raw Storage", 40, 30], ["Cooler", 40, 30], ["Freezer", 40, 25], ["Dry Storage", 40, 25], ["Shipping", 40, 20], ["Locker Rooms", 25, 18], ["QA Lab", 15, 12]]}, {"n": "Steel Fabrication Shop", "rooms": [["Fab Bays", 200, 60], ["Cutting", 60, 30], ["Fitting Beds", 80, 30], ["Welding", 60, 30], ["Blast Booth", 30, 20], ["Paint Booth", 30, 20], ["Material Storage", 60, 30], ["Offices", 25, 15]]}], "machines": [{"n": "Steam Engine", "rooms": [["Boiler", 12, 8], ["Engine Bed", 16, 10], ["Flywheel", 10, 10], ["Line Shafting", 40, 4], ["Coal Bunker", 12, 10], ["Feedwater", 10, 8], ["Engineer Station", 8, 8]]}, {"n": "Wind Turbine", "rooms": [["Rotor Diameter", 400, 400], ["Nacelle", 30, 12], ["Tower", 300, 15], ["Foundation", 60, 60], ["Crane Pad", 60, 40], ["Substation", 40, 30]]}, {"n": "Industrial Press", "rooms": [["Press Cell", 16, 12], ["Die Storage", 12, 10], ["Infeed", 10, 8], ["Outfeed", 10, 8], ["Hydraulic Unit", 8, 6], ["Operator Station", 6, 4]]}, {"n": "Conveyor System", "rooms": [["Tail Section", 20, 8], ["Carry Run", 200, 6], ["Head Section", 20, 10], ["Drive House", 15, 12], ["Transfer Chute", 10, 8], ["Walkway", 220, 4]]}], "tools": [{"n": "Claw Hammer", "rooms": [["Head", 4.5, 1.2], ["Claw", 2.5, 1.0], ["Handle", 11, 1.1], ["Grip", 4.5, 1.3]]}, {"n": "Handsaw", "rooms": [["Blade", 26, 5], ["Tooth Line", 26, 0.5], ["Handle", 6, 4]]}, {"n": "Cordless Drill", "rooms": [["Barrel/Motor", 7, 3], ["Chuck", 2.5, 2], ["Grip", 4.5, 2.5], ["Battery", 4, 3.5]]}, {"n": "Table Saw", "rooms": [["Table", 27, 20], ["Blade Zone", 10, 0.13], ["Rip Fence", 30, 3], ["Outfeed", 27, 12], ["Motor Cabinet", 20, 18]]}], "devices": [{"n": "Refrigerator", "rooms": [["Fresh Food", 36, 28], ["Freezer Drawer", 36, 20], ["Doors Open Swing", 36, 30], ["Mechanical", 36, 10]]}, {"n": "Washing Machine", "rooms": [["Cabinet", 27, 27], ["Door Swing", 27, 24], ["Drum", 22, 20], ["Top Panel", 27, 6]]}, {"n": "Microwave Oven", "rooms": [["Cavity", 16, 14], ["Turntable", 13, 13], ["Control Panel", 4, 14], ["Magnetron Bay", 8, 10]]}, {"n": "Television", "rooms": [["Panel 55in", 48, 28], ["Wall Mount Zone", 16, 16], ["Stand Footprint", 36, 12]]}], "vehicles": [{"n": "Sedan", "rooms": [["Overall", 190, 72], ["Cabin", 100, 60], ["Trunk", 40, 50], ["Engine Bay", 40, 55]]}, {"n": "Pickup Truck", "rooms": [["Overall", 230, 80], ["Crew Cab", 70, 70], ["Bed 5.5ft", 67, 60], ["Frame Rails", 200, 36]]}, {"n": "Box Truck", "rooms": [["Overall", 260, 96], ["Box 16ft", 192, 96], ["Cab", 80, 90], ["Chassis", 240, 36]]}, {"n": "City Bus", "rooms": [["Overall", 480, 102], ["Cabin", 400, 96], ["Driver Station", 40, 40], ["Wheelchair Bays", 60, 50]]}], "infrastructure": [{"n": "Suspension Bridge", "rooms": [["Main Span", 4200, 90], ["Tower", 700, 60], ["Anchorage", 150, 120], ["Approach", 1500, 90]]}, {"n": "Concrete Dam", "rooms": [["Dam Axis", 1244, 45], ["Crest", 1244, 30], ["Spillway", 500, 80], ["Powerhouse", 400, 120]]}, {"n": "Highway Interchange", "rooms": [["Mainline A", 2000, 120], ["Mainline B", 2000, 120], ["Ramp Bridges", 800, 40], ["Footprint", 1400, 1400]]}, {"n": "Railway Tunnel", "rooms": [["Bore A", 20000, 30], ["Bore B", 20000, 30], ["Cross-Passages", 30, 15], ["Portal Works", 500, 200]]}]};
var UNIT={"houses": "ft", "stores": "ft", "offices": "ft", "warehouses": "ft", "apartments": "ft", "barns": "ft", "schools": "ft", "factories": "ft", "machines": "ft", "tools": "in", "devices": "in", "vehicles": "in", "infrastructure": "ft"};
function asciiPlan(title,rooms,unit){
  var items=rooms.slice().sort(function(a,b){return (b[1]*b[2])-(a[1]*a[2]);});
  var total=0,widest=0,i;
  for(i=0;i<items.length;i++){total+=items[i][1]*items[i][2];widest=Math.max(widest,items[i][1]);}
  var rowW=Math.max(widest,Math.sqrt(total*1.3));
  var rows=[],cur=[],curW=0;
  for(i=0;i<items.length;i++){var r=items[i];
    if(cur.length&&curW+r[1]>rowW*1.03){rows.push(cur);cur=[];curW=0;}
    cur.push(r);curW+=r[1];}
  if(cur.length)rows.push(cur);
  var W=0,D=0,placed=[],y=0;
  for(var ri=0;ri<rows.length;ri++){var rh=0,x=0;
    for(i=0;i<rows[ri].length;i++)rh=Math.max(rh,rows[ri][i][2]);
    for(i=0;i<rows[ri].length;i++){var q=rows[ri][i];placed.push({n:q[0],x:x,y:y,w:q[1],d:q[2]});x+=q[1];}
    W=Math.max(W,x);y+=rh;}
  D=y;
  var upc=2;while(Math.max(W,D)/upc>60)upc*=2;
  var gw=Math.max(8,Math.round(W/upc)),gh=Math.max(5,Math.round(D/upc));
  var g=[],yy,xx;
  for(yy=0;yy<gh;yy++){g.push([]);for(xx=0;xx<gw;xx++)g[yy].push(' ');}
  function hl(yy2,x0,x1){for(var x=Math.max(0,x0);x<Math.min(gw,x1);x++)if(g[yy2][x]===' ')g[yy2][x]='-';}
  function vl(xx2,y0,y1){for(var y=Math.max(0,y0);y<Math.min(gh,y1);y++)if(g[y][xx2]===' ')g[y][xx2]='|';}
  for(i=0;i<placed.length;i++){var p=placed[i];
    var x0=Math.floor(p.x/upc),y0=Math.floor(p.y/upc);
    var x1=Math.min(gw,Math.max(x0+2,Math.round((p.x+p.w)/upc)));
    var y1=Math.min(gh,Math.max(y0+2,Math.round((p.y+p.d)/upc)));
    hl(y0,x0,x1);hl(y1-1,x0,x1);vl(x0,y0,y1);vl(x1-1,y0,y1);
    var cps=[[x0,y0],[x1-1,y0],[x0,y1-1],[x1-1,y1-1]];
    for(var ci=0;ci<4;ci++)if(cps[ci][1]>=0&&cps[ci][1]<gh&&cps[ci][0]>=0&&cps[ci][0]<gw)g[cps[ci][1]][cps[ci][0]]='+';
    var label=String(p.n).slice(0,Math.max(1,x1-x0-2));
    var ly=y0+((y1-y0)>>1),lx=x0+Math.max(1,((x1-x0-label.length)>>1));
    if(ly>y0&&ly<y1-1)for(var li=0;li<label.length;li++)if(lx+li<x1-1)g[ly][lx+li]=label[li];
  }
  var lines=['PLAN: '+title,'Overall '+W+' x '+D+' '+unit+' | 1 char = '+upc+' '+unit+' | schematic - not to construction scale'];
  for(yy=0;yy<gh;yy++)lines.push(g[yy].join('').replace(/\s+$/,''));
  return {text:lines.join('\n'),W:W,D:D};
}
function pyEsc(s){return String(s).replace(/\\/g,'\\\\').replace(/"/g,'\\"');}
function pyDemo(rid,title,plan,stats){
  var L=['# JAH Blueprint Designer demo','# Record '+rid+' - '+String(title).replace(/"/g,"'"),'plan = "\\n".join(['];
  var plines=String(plan).split('\n');
  for(var i=0;i<plines.length;i++)L.push('"'+pyEsc(plines[i])+'"'+(i<plines.length-1?',':''));
  L.push('])','print(plan)');
  for(var j=0;j<stats.length;j++)L.push('print("'+String(stats[j][0]).replace(/"/g,"'")+': '+String(stats[j][1]).replace(/"/g,"'")+'")');
  L.push('print("OK: '+rid+' designer blueprint verified")');
  return L.join('\n')+'\n';
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var field=opts.field&&FIELDS.indexOf(opts.field)>=0?opts.field:pick(FIELDS,rnd);
  var type=pick(TYPES[field]||TYPES[FIELDS[0]],rnd);
  var size=pick(SIZES,rnd);
  var purpose=pick(PURPOSES[field]||PURPOSES['houses'],rnd);
  var c1=pick(CONSTRAINTS,rnd),c2=pick(CONSTRAINTS,rnd);
  if(c2===c1)c2='none';
  var sc=SCALE[size];
  var rooms=type.rooms.map(function(r){return [r[0],Math.round(r[1]*sc*2)/2,Math.round(r[2]*sc*2)/2];});
  var unit=UNIT[field]||'ft';
  var pl=asciiPlan(type.n+' ('+size+')',rooms,unit);
  var area=0,i;for(i=0;i<rooms.length;i++)area+=rooms[i][1]*rooms[i][2];
  area=Math.round(area);
  var id=PREFIX+String(seed).padStart(6,'0');
  var title='Designed '+type.n+' ('+size+', '+purpose+')';
  var roomList=rooms.map(function(r){return r[0]+': '+r[1]+' x '+r[2]+' '+unit;}).join('; ');
  var desc='SAMPLE RECORD (generated - structural sample). The Blueprint Designer composed this '+size+' '+type.n+
    ' for "'+purpose+'" under constraints ['+c1+(c2==='none'?'':', '+c2)+'], category '+field+
    '. Spaces: '+roomList+'. Estimated area '+area+' sq '+unit+'. Generated samples are clearly labeled and never presented as archive records.';
  return {
    id:id,
    name:type.n+' - designed '+size+' blueprint',
    title:title,
    description:desc,
    field:field,
    size:size, purpose:purpose, constraints:[c1,c2],
    src:"designer-generated-sample",
    sample:true,
    disclaimer:'Generated sample record - not an archive record. Seeded archive presets are the authoritative entries.',
    blueprint:{plan_ascii:pl.text, overall:pl.W+' x '+pl.D+' '+unit, area_estimate_sq:area, unit:unit},
    demo:{kind:'python',language:'python',program:pyDemo(id,title,pl.text,[['Overall',pl.W+' x '+pl.D+' '+unit],['Spaces',rooms.length],['Area (est.)',area+' sq '+unit],['Purpose',purpose]]),note:'Designer sample demo.'},
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
var gen={version:'jahdb-blueprint-designer-1.0',generate:generate,validate:validate,driftCheck:driftCheck,fields:FIELDS};
if(typeof JAHDB!=='undefined'&&JAHDB.registerGenerator)JAHDB.registerGenerator('blueprint-designer',gen);
if(typeof module!=='undefined'&&module.exports)module.exports=gen;
})();
