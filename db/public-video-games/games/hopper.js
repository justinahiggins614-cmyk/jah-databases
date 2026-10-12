/* Hopper — cross-the-road-and-river arcade. Openly licensed original (MIT) for the Public Video Games Database. */
PVG.register('hopper', {
  title:'Hopper', W:480, H:560,
  controls:{ dpad:true, buttons:[] },
  help:'Hop with arrows / WASD / numpad 2468 / pad. Cross the road, ride the logs, fill all 5 homes.',
  init:function(P){ this.reset(P); },
  reset:function(P){
    this.cs=40; this.cols=P.W/this.cs; this.rows=13;
    this.fx=6; this.fy=12; this.score=0; this.lives=4; this.over=false; this.t=0;
    this.homes=[false,false,false,false,false];
    this.lanes=[];
    // lanes 1..5 road (cars), 7..11 river (logs), 0 homes, 6 safe, 12 start
    var speeds=[0,90,-120,110,-95,130,0,-80,100,-70,90,-110,0];
    for(var r=0;r<this.rows;r++){
      var lane={r:r,items:[],speed:speeds[r]||0};
      if(r>=1&&r<=5){ for(var i=0;i<3;i++) lane.items.push({x:((i*170+r*90)%P.W),w:70}); }
      if(r>=7&&r<=11){ for(var j=0;j<3;j++) lane.items.push({x:((j*200+r*60)%P.W),w:110}); }
      this.lanes.push(lane);
    }
  },
  die:function(P){ this.lives--; P.beep(140,.3,'sawtooth'); this.fx=6; this.fy=12; if(this.lives<=0) this.over=true; },
  update:function(P,dt){
    if(this.over){ if(P.pressed.start||P.pressed.a) this.reset(P); return; }
    var k=P.keys;
    if(P.pressed.left){this.fx--;P.beep(400,.04);}
    if(P.pressed.right){this.fx++;P.beep(400,.04);}
    if(P.pressed.up){this.fy--;P.beep(460,.04);}
    if(P.pressed.down){this.fy++;P.beep(360,.04);}
    this.fx=Math.max(0,Math.min(this.cols-1,this.fx));
    this.fy=Math.max(0,Math.min(this.rows-1,this.fy));
    // move lanes
    for(var r=1;r<=11;r++){
      var lane=this.lanes[r];
      for(var i=0;i<lane.items.length;i++){
        lane.items[i].x+=lane.speed*dt;
        if(lane.speed>0&&lane.items[i].x>P.W+20) lane.items[i].x=-lane.items[i].w-20;
        if(lane.speed<0&&lane.items[i].x<-lane.items[i].w-20) lane.items[i].x=P.W+20;
      }
    }
    var px=this.fx*this.cs+this.cs/2;
    if(this.fy>=1&&this.fy<=5){
      var ln=this.lanes[this.fy];
      for(var c=0;c<ln.items.length;c++){
        var it=ln.items[c];
        if(px>it.x&&px<it.x+it.w){ this.die(P); return; }
      }
    }
    if(this.fy>=7&&this.fy<=11){
      var ln2=this.lanes[this.fy], on=false;
      for(var c2=0;c2<ln2.items.length;c2++){
        var it2=ln2.items[c2];
        if(px>it2.x&&px<it2.x+it2.w){ on=true; this.fx+=ln2.speed*dt/this.cs; break; }
      }
      if(!on){ this.die(P); return; }
      this.fx=Math.max(-1,Math.min(this.cols,this.fx));
      if(this.fx<0||this.fx>=this.cols){ this.die(P); return; }
    }
    if(this.fy===0){
      var home=Math.round((this.fx*this.cs)/(P.W/5)-0.5);
      home=Math.max(0,Math.min(4,home));
      if(this.homes[home]){ this.die(P); return; }
      this.homes[home]=true; this.score+=200; P.beep(880,.15);
      this.fx=6; this.fy=12;
      if(this.homes.every(function(h){return h;})){ this.score+=1000; this.over=true; P.beep(990,.4); }
    }
    this.t+=dt;
  },
  draw:function(P,ctx){
    ctx.fillStyle='#0d1526'; ctx.fillRect(0,0,P.W,P.H);
    for(var r=0;r<this.rows;r++){
      var y=r*this.cs;
      if(r===0){ ctx.fillStyle='#0f2f1d'; }
      else if(r>=1&&r<=5){ ctx.fillStyle='#141a26'; }
      else if(r===6||r===12){ ctx.fillStyle='#1d2c4d'; }
      else { ctx.fillStyle='#0b2a4a'; }
      ctx.fillRect(0,y,P.W,this.cs);
    }
    // homes
    for(var h=0;h<5;h++){
      var hx=h*(P.W/5)+P.W/10;
      ctx.fillStyle=this.homes[h]?'#00e5a0':'#000';
      ctx.strokeStyle='#00e5a0';
      ctx.beginPath(); ctx.arc(hx,this.cs/2,16,0,7); ctx.fill(); ctx.stroke();
    }
    // cars + logs
    for(var r2=1;r2<=11;r2++){
      var lane=this.lanes[r2];
      lane.items.forEach(function(it){
        if(r2<=5){ ctx.fillStyle='#e5484d'; ctx.fillRect(it.x,r2*this.cs+6,it.w,this.cs-12); }
        else { ctx.fillStyle='#8a5a2b'; ctx.fillRect(it.x,r2*this.cs+6,it.w,this.cs-12); }
      });
    }
    // frog
    ctx.fillStyle='#00e5a0';
    ctx.beginPath(); ctx.arc(this.fx*this.cs+this.cs/2,this.fy*this.cs+this.cs/2,13,0,7); ctx.fill();
    ctx.fillStyle='#070b16';
    ctx.beginPath(); ctx.arc(this.fx*this.cs+this.cs/2-5,this.fy*this.cs+this.cs/2-4,2.5,0,7); ctx.fill();
    ctx.beginPath(); ctx.arc(this.fx*this.cs+this.cs/2+5,this.fy*this.cs+this.cs/2-4,2.5,0,7); ctx.fill();
    P.text('SCORE '+this.score+'   LIVES '+this.lives, P.W/2, P.H-14, 14, '#9fb3d8');
    if(this.over&&this.homes.every(function(x){return x;})) P.text('ALL HOMES FILLED! — START for new game', P.W/2, P.H/2, 15, '#00e5a0');
    else if(this.over) P.text('GAME OVER — START to retry', P.W/2, P.H/2, 15, '#ff6b6b');
  }
});
