// Generator + tools for space-camp-programs. Generated entries are labeled simulated; cap 10^15.
(function(){var titles=["Space Camp Core Program", "Space Academy", "Advanced Space Academy", "Aviation Challenge", "Cyber Camp", "Space Camp Robotics", "Simulated Space Missions", "The Multi-Axis Trainer", "The One-Sixth Gravity Chair", "Model Rocketry at Space Camp", "Shuttle-Era Simulators", "Teamwork and Crew Roles", "The Rocket Center Museum", "Educator Programs", "Space Camp Alumni Paths", "Planning a Space Camp Visit"];var count=0;var CAP=1e15;
window.SpaceCampProgramsTools={searchRecords:function(q){q=q.toLowerCase();return titles.filter(function(t){return t.toLowerCase().includes(q);});},
getRecord:function(i){return titles[i]||null;},
generateSimulated:function(){if(count>=CAP)return 'CAP REACHED';count++;var t=titles[count%titles.length];return 'Simulated variation of '+t+' (generated entry '+count+', labeled simulated)';},
validateRecord:function(t){return titles.includes(t);}};})();
