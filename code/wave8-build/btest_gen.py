#!/usr/bin/env python3
import sys
sys.path.insert(0, '.')
from engine_gen import BUILDERS
src = ("function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;"
       "var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;"
       "return((t^(t>>>14))>>>0)/4294967296;};}\n"
       "function pick(r,s){return r[(s()*r.length)|0];}\n"
       "function shuffle(a,r){a=a.slice();for(var i=a.length-1;i>0;i--){var j=(r()*(i+1))|0;"
       "var t=a[i];a[i]=a[j];a[j]=t;}return a;}\n")
order = ['routine', 'room-theme', 'challenge-calendar', 'celebration', 'tradition',
         'adventure-plan', 'random-fun', 'bucket-list', 'daily-skill', 'brand-studio',
         'poll-gen', 'emote-studio', 'mascot', 'content-calendar', 'badge-gen',
         'theory', 'project-factory', 'podcast-segments']
for bid in order:
    src += BUILDERS[bid] + "\n"
calls = {
 'routine': 'BUILD_ROUTINE({wake:"07:00",sleep:"23:00",focus:"2",seed:"7"})',
 'room-theme': 'BUILD_ROOM_THEME({size:"medium",budget:"300",style:"calm minimal",seed:"7"})',
 'challenge-calendar': 'BUILD_CHALLENGE_CALENDAR({theme:"fitness",days:"14",difficulty:"easy",seed:"5"})',
 'celebration': 'BUILD_CELEBRATION({occasion:"just because",people:"6",budget:"50",seed:"9"})',
 'tradition': 'BUILD_TRADITION({who:"friends",freq:"monthly",values:"laughter",seed:"13"})',
 'adventure-plan': 'BUILD_ADVENTURE_PLAN({time:"a free afternoon",budget:"30",interests:"food",seed:"17"})',
 'random-fun': 'BUILD_RANDOM_FUN({time:"an hour",budget:"low",seed:"3"})',
 'bucket-list': 'BUILD_BUCKET_LIST({interests:"Create,Learn",timeframe:"the next year",budget:"flexible",seed:"11"})',
 'daily-skill': 'BUILD_DAILY_SKILL({interest:"",seed:"20261017"})',
 'brand-studio': 'BUILD_BRAND_STUDIO({niche:"gaming",tone:"playful",seed:"21"})',
 'poll-gen': 'BUILD_POLL_GEN({topic:"stream",platform:"stream chat",seed:"23"})',
 'emote-studio': 'BUILD_EMOTE_STUDIO({vibe:"cozy",prefix:"chan",count:"6",seed:"27"})',
 'mascot': 'BUILD_MASCOT({theme:"variety",species:"",seed:"29"})',
 'content-calendar': 'BUILD_CONTENT_CALENDAR({platforms:"video,shorts",perweek:"4",pillars:"Teach,Fun",seed:"3"})',
 'badge-gen': 'BUILD_BADGE_GEN({milestones:"A,B,C",seed:"31"})',
 'theory': 'BUILD_THEORY({universe:"test show",seed:"7"})',
 'project-factory': 'BUILD_PROJECT_FACTORY({interest:"art",size:"10",seed:"37"})',
 'podcast-segments': 'BUILD_PODCAST_SEGMENTS({theme:"tech",length:"45",seed:"41"})',
}
src += "var tests={\n" + ",\n".join(" %r:%s" % (k, v) for k, v in calls.items()) + "\n};\n"
src += ("var bad=[];\n"
        "Object.keys(tests).forEach(function(k){var r=tests[k];"
        "if(!r||!r.title||!r.sections||!r.sections.length)bad.push(k);});\n"
        "if(bad.length){console.log('FAIL: '+bad.join(','));process.exit(1);}\n"
        "console.log('ALL '+Object.keys(tests).length+' BUILDERS OK');\n")
open('/tmp/btest.js', 'w').write(src)
print('wrote /tmp/btest.js', len(src))
