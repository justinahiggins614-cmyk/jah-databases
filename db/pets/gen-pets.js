/* JAH Pet Care Database generator — jahdb-pets-1.0
   Deterministic (mulberry32). Seed -> full pet care entry.
   Sourced records draw every fact from the curated dataset below
   (real breeds and species: origin, size, coat, temperament; headline
   facts spot-checked against public breed references 2026-10-09).
   Health notes always advise seeing a veterinarian. Signature records are
   homegrown checklists, always labeled as such.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
var PREFIX='JAH-PET-';
var KIND='pet care entry';
var CATS=['dog-breed','cat-breed','bird','fish','reptile','small-mammal','care-guide','health-note','training-tip','new-owner-checklist'];
/* [breed, origin, size, coat, temperament, note] */
var DOGS=[
["Labrador Retriever","Newfoundland, Canada","large","short double","friendly, outgoing, eager","Among the most popular breeds in the world for decades."],
["German Shepherd","Germany","large","medium double","confident, loyal, smart","Widely used in police, military, and service work."],
["Golden Retriever","Scotland","large","long","friendly, gentle, eager","Famous as a family dog and guide dog."],
["French Bulldog","France and England","small","short","playful, adaptable, affectionate","A city-friendly companion breed."],
["Bulldog","England","medium","short","calm, brave, friendly","Known for its wrinkled face and pushed-in nose."],
["Poodle","Germany and France","toy, miniature, or standard","curly","smart, active, proud","Comes in three sizes; famously trainable."],
["Beagle","England","small to medium","short","merry, curious, friendly","A scent hound with a famous baying bark."],
["Rottweiler","Germany","large","short","loyal, confident, calm","A strong working breed needing steady training."],
["German Shorthaired Pointer","Germany","large","short","energetic, smart, eager","A versatile hunting dog."],
["Dachshund","Germany","small","short, long, or wire","clever, brave, lively","Bred to hunt badgers; long body, short legs."],
["Siberian Husky","Siberia","medium to large","thick double","outgoing, mischievous, energetic","Bred for sled pulling; famously clever escape artists."],
["Boxer","Germany","large","short","playful, loyal, energetic","A bouncy, clownish family guardian."],
["Great Dane","Germany","giant","short","gentle, friendly, patient","The Apollo of dogs; one of the tallest breeds."],
["Doberman Pinscher","Germany","large","short","loyal, alert, smart","A sleek guardian breed."],
["Australian Shepherd","United States","medium","medium-long","smart, energetic, eager","A herding breed that thrives on having work to do."],
["Border Collie","Scotland and England","medium","medium","intense, smart, energetic","Often called the smartest of all dog breeds."],
["Shih Tzu","China and Tibet","small","long","affectionate, playful, gentle","Bred as a royal companion dog."],
["Chihuahua","Mexico","tiny","short or long","lively, loyal, bold","The smallest dog breed in the world."],
["Pomeranian","Germany and Poland","tiny","fluffy double","lively, bold, curious","A tiny spitz with a big personality."],
["Yorkshire Terrier","England","tiny","long silky","bold, affectionate, feisty","A tiny terrier with show-stopping hair."],
["Pembroke Welsh Corgi","Wales","small to medium","medium double","smart, cheerful, herding","A herding dog made famous by British royalty."],
["Shiba Inu","Japan","small to medium","thick double","alert, independent, bold","An ancient Japanese breed; a favorite online."],
["Akita","Japan","large","thick double","loyal, dignified, brave","A symbol of loyalty in Japan."],
["Saint Bernard","Switzerland and Italy","giant","long or short","gentle, patient, friendly","The Alpine rescue dog of legend."],
["Newfoundland","Canada","giant","thick","sweet, patient, gentle","A water rescue breed, famously gentle with children."],
["Bernese Mountain Dog","Switzerland","large","long tri-color","gentle, loyal, calm","A Swiss farm dog with striking markings."],
["English Mastiff","England","giant","short","gentle, dignified, calm","One of the heaviest of all dog breeds."],
["Greyhound","ancient Middle East","large","short","gentle, quiet, swift","The fastest dog breed; famously calm indoors."],
["Dalmatian","Croatia","medium to large","short spotted","energetic, playful, smart","The firehouse dog with iconic spots."],
["Cocker Spaniel","England and United States","small to medium","silky medium","merry, gentle, eager","A cheerful sporting breed."],
["Cavalier King Charles Spaniel","England","small","silky","affectionate, gentle, graceful","A lapdog named for royalty."],
["Havanese","Cuba","small","silky","cheerful, smart, social","The national dog of Cuba."],
["Maltese","Mediterranean region","tiny","long white silky","gentle, playful, affectionate","An ancient lapdog."],
["Boston Terrier","United States","small","short","friendly, smart, lively","The American Gentleman, with tuxedo markings."],
["Pug","China","small","short","charming, playful, even-tempered","An ancient Chinese companion with a wrinkled face."],
["Miniature Schnauzer","Germany","small","wiry","smart, spirited, obedient","A small ratter with a beard."],
["Bloodhound","France and Belgium","large","short","gentle, determined, tireless","The ultimate scent-tracking dog."],
["Basset Hound","France","medium","short","patient, low-key, charming","Long ears, short legs, and a big nose."],
["Vizsla","Hungary","medium to large","short","affectionate, energetic, gentle","The velcro dog that sticks close to its people."],
["Weimaraner","Germany","large","short","energetic, smart, loyal","The grey ghost of hunting dogs."],
["Rhodesian Ridgeback","South Africa","large","short","dignified, loyal, strong","Bred to hunt lions; named for its ridge of hair."],
["Alaskan Malamute","Alaska","large","thick double","strong, loyal, playful","A powerful freight-pulling sled dog."],
["Samoyed","Siberia","medium to large","fluffy white double","friendly, gentle, smiling","The smiling sled dog."],
["Chow Chow","China","medium to large","thick","dignified, aloof, loyal","Famous for its blue-black tongue."],
["Shar-Pei","China","medium","wrinkled short","calm, loyal, independent","Known for its deep wrinkles."],
["Lhasa Apso","Tibet","small","long","confident, smart, independent","A Tibetan watchdog."],
["Pekingese","China","small","long","regal, loyal, opinionated","A Chinese imperial lapdog."],
["Papillon","France and Belgium","tiny","silky","friendly, alert, happy","Butterfly ears give it its name."],
["Italian Greyhound","Italy","tiny","short","gentle, playful, sensitive","A miniature sighthound."],
["Whippet","England","small to medium","short","calm, gentle, swift","A smaller, quieter racing sighthound."],
["Afghan Hound","Afghanistan","large","long silky","dignified, aloof, elegant","An ancient sighthound with flowing hair."],
["Saluki","Middle East","large","short or feathered","gentle, dignified, swift","One of the oldest of all dog breeds."],
["Basenji","Central Africa","small to medium","short","independent, smart, quiet","The barkless dog that yodels instead."],
["Great Pyrenees","France and Spain","giant","thick white","calm, patient, protective","A livestock guardian of the mountains."],
["Standard Schnauzer","Germany","medium","wiry","smart, spirited, loyal","The original schnauzer."],
["Portuguese Water Dog","Portugal","medium","curly or wavy","smart, energetic, fun","Bred to help fishermen."],
["Australian Cattle Dog","Australia","medium","short double","smart, energetic, loyal","A tireless herding breed."],
["Belgian Malinois","Belgium","medium to large","short","smart, intense, driven","A top police and military working dog."],
["Shetland Sheepdog","Scotland","small to medium","long double","smart, gentle, vocal","A herding breed resembling a small collie."],
["Rough Collie","Scotland","large","long","gentle, loyal, smart","The breed of Lassie fame."]
];
/* [breed, origin, coat, temperament, note] */
var CATS_D=[
["Domestic Shorthair","worldwide","short","varied, adaptable","The everyday house cat; healthy and varied."],
["Maine Coon","Maine, USA","long shaggy","gentle, friendly, big","One of the largest domestic cat breeds."],
["Siamese","Thailand","short pointed","vocal, social, smart","Famous blue eyes and color points."],
["Persian","Iran","long","calm, sweet, quiet","The classic flat-faced longhair."],
["Ragdoll","USA","semi-long","docile, floppy, gentle","Goes limp when picked up."],
["Bengal","USA","short spotted","active, bold, athletic","A wild-looking spotted hybrid."],
["British Shorthair","United Kingdom","dense short","calm, sturdy, easygoing","The Cheshire Cat look."],
["Sphynx","Canada","hairless","warm, social, playful","The hairless cat."],
["Scottish Fold","Scotland","short or long","sweet, calm, owl-like","Folded ears."],
["Russian Blue","Russia","short blue-grey","shy, loyal, quiet","A silvery coat with green eyes."],
["Abyssinian","Ethiopia region","short ticked","active, curious, playful","One of the oldest cat breeds."],
["Birman","Burma and France","semi-long pointed","gentle, social, quiet","White gloves on every paw."],
["Oriental Shorthair","Thailand and UK","short","vocal, sleek, social","A Siamese-style cat in many colors."],
["Devon Rex","England","curly short","mischievous, social, warm","Pixie-like with huge ears."],
["Norwegian Forest Cat","Norway","long thick","sturdy, calm, climber","The legendary Viking ship cat."],
["Burmese","Burma and Thailand","short satin","social, playful, people-loving","Golden eyes and a muscular body."],
["Tonkinese","Canada and Thailand","short","social, chatty, playful","A Siamese-Burmese blend."],
["Himalayan","USA and UK","long pointed","calm, sweet, placid","A Persian in Siamese colors."],
["American Shorthair","USA","short dense","easygoing, sturdy, adaptable","The classic American mouser."],
["Exotic Shorthair","USA","short plush","calm, sweet, quiet","A short-haired Persian."],
["Savannah","USA","short spotted","tall, active, bold","A serval hybrid; tall and athletic."],
["Cornish Rex","England","wavy short","active, warm, clownish","A slender wave-coated cat."],
["Manx","Isle of Man","short or long","gentle, rounded, tailless","Born without a tail."],
["Japanese Bobtail","Japan","short or medium","social, active, lucky","A symbol of good fortune."],
["Turkish Angora","Turkey","silky medium","graceful, smart, playful","An ancient natural breed."],
["Turkish Van","Turkey","semi-long","energetic, loves water","Known as the swimming cat."],
["Chartreux","France","dense blue-grey","quiet, gentle, smiling","A historic French blue cat."],
["Egyptian Mau","Egypt","spotted short","athletic, loyal, fast","The only naturally spotted domestic breed."],
["Singapura","Singapore","short","tiny, curious, extroverted","One of the smallest cat breeds."],
["Ragamuffin","USA","thick medium","sweet, calm, cuddly","A gentle giant of a lap cat."]
];
/* [name, origin, note] */
var BIRDS=[
["Budgerigar","Australia","A small, social parakeet that can learn to mimic words."],
["Cockatiel","Australia","A crested parrot famous for whistling tunes."],
["African Grey Parrot","Central Africa","Among the most brilliant talking birds."],
["Blue-and-yellow Macaw","South America","A large, loud, long-lived macaw."],
["Sulphur-crested Cockatoo","Australia","A demanding, crested white cockatoo."],
["Canary","Atlantic islands","Bred for song; males are the singers."],
["Zebra Finch","Australia","A small, social finch; a beginner favorite."],
["Lovebird","Africa","A small parrot that bonds strongly in pairs."],
["Green-cheeked Conure","South America","A playful, quieter conure."],
["Cockatoo (Goffin's)","Indonesia","A small, clever, mischievous cockatoo."]
];
var FISH=[
["Betta","Thailand","A labyrinth fish; males must live alone."],
["Goldfish","China","A cold-water classic that can live decades."],
["Guppy","South America","A livebearer; a beginner favorite."],
["Neon Tetra","Amazon basin","A schooling fish with glowing stripes."],
["Angelfish","Amazon basin","An elegant cichlid for taller tanks."],
["Clownfish","Pacific reefs","Lives symbiotically with anemones."],
["Blue Tang","Indo-Pacific","A surgeonfish needing a large tank."],
["Corydoras Catfish","South America","A peaceful bottom cleaner."],
["Molly","the Americas","A hardy livebearer."],
["Discus","Amazon basin","A demanding but stunning cichlid."]
];
var REPTILES=[
["Bearded Dragon","Australia","A docile, hardy lizard; a beginner favorite."],
["Leopard Gecko","Middle East and South Asia","A gecko with eyelids; easy to handle."],
["Ball Python","West Africa","A calm constrictor; famous for curling into a ball."],
["Corn Snake","USA","A beginner snake; an escape artist."],
["Red-Eared Slider","USA","An aquatic turtle needing a large tank and basking spot."],
["Russian Tortoise","Central Asia","A small, hardy tortoise."],
["Crested Gecko","New Caledonia","A hardy gecko that eats fruit-based diet."],
["Blue-Tongue Skink","Australia","An omnivorous, handleable lizard."]
];
var MAMMALS=[
["Syrian Hamster","Syria","Solitary; must live alone."],
["Guinea Pig","Andes region","Social; needs herd companionship and vitamin C."],
["Rabbit","Europe","Can be litter-trained; needs hay always available."],
["Ferret","Europe","A playful mustelid; ferret-proof the home."],
["Fancy Rat","worldwide","Smart and social; best kept in pairs or groups."],
["Gerbil","Mongolia and desert regions","Social desert rodents; give deep bedding to burrow."],
["African Pygmy Hedgehog","Africa","An insectivore; needs warmth."],
["Chinchilla","Andes region","Takes dust baths; hates heat and humidity."]
];
var PET_TYPES=["dog","cat","bird","fish","reptile","small mammal"];
var PLURAL={dog:"dogs",cat:"cats",bird:"birds",fish:"fish",reptile:"reptiles","small mammal":"small mammals"};
var CARE_TOPICS=[
["feeding",{
 dog:"Feed a complete diet suited to age and size; measure meals to avoid obesity.",
 cat:"Feed a complete meat-based diet; cats are obligate carnivores.",
 bird:"Offer pellets plus vegetables; avoid avocado, chocolate, and caffeine.",
 fish:"Feed only what they eat in two minutes, once or twice a day.",
 reptile:"Match food to the species: insects, greens, or whole prey as appropriate.",
 "small mammal":"Hay always available for herbivores like rabbits and guinea pigs; species-appropriate pellets for others."}],
["housing",{
 dog:"A secure yard or daily walks plus a cozy indoor sleeping spot.",
 cat:"Indoor living is safest; provide vertical space and a clean litter box.",
 bird:"The largest cage you can fit, placed socially but away from drafts.",
 fish:"A cycled, filtered tank sized to the species; bigger is easier to keep stable.",
 reptile:"A secure terrarium with correct heat gradient and lighting for the species.",
 "small mammal":"A roomy, well-ventilated enclosure with hiding spots and bedding."}],
["grooming",{
 dog:"Brush regularly; bathe as needed; trim nails and clean ears.",
 cat:"Most cats self-groom; longhairs need daily brushing.",
 bird:"Provide baths or misting; trim nails as needed.",
 fish:"No grooming needed for fish; keeping the water pristine is the real grooming.",
 reptile:"Provide proper humidity for clean sheds; never pull shed skin.",
 "small mammal":"Brush long-haired species; trim nails regularly."}],
["exercise",{
 dog:"Daily walks plus play; match intensity to the breed's energy.",
 cat:"Interactive play sessions daily; climbing and scratching outlets.",
 bird:"Out-of-cage time in a safe room; flight or climbing exercise.",
 fish:"Adequate swimming space; avoid overcrowding.",
 reptile:"Enrichment and handling appropriate to the species' temperament.",
 "small mammal":"Daily supervised play outside the enclosure in a safe area."}],
["veterinary care",{
 dog:"Annual exams, vaccinations, parasite prevention, and dental checks.",
 cat:"Annual exams, vaccinations, parasite prevention, and dental checks.",
 bird:"Find an avian vet; annual exams catch problems early.",
 fish:"Quarantine new arrivals; watch water quality as the first medicine.",
 reptile:"Find a reptile vet; annual exams and fecal checks.",
 "small mammal":"Find an exotics vet; annual exams for rabbits, guinea pigs, and ferrets."}],
["enrichment",{
 dog:"Puzzle feeders, training games, and novel walks prevent boredom.",
 cat:"Window perches, puzzle feeders, and rotating toys.",
 bird:"Foraging toys, shreddables, and social interaction daily.",
 fish:"Plants, hides, and tank mates suited to the species.",
 reptile:"Climbing branches, hides, and varied terrain.",
 "small mammal":"Tunnels, chew toys, and foraging challenges."}]
];
var HEALTH_ISSUES=[
["appetite changes","A sudden change in eating or drinking warrants a prompt call to your veterinarian."],
["lethargy","Unusual tiredness or hiding can signal illness; call your veterinarian."],
["vomiting or diarrhea","Occasional upset passes, but repeated episodes need veterinary advice."],
["skin and coat changes","Itching, bald spots, or dull coat deserve a veterinary check."],
["limping","Do not wait on a persistent limp; have your veterinarian examine it."],
["breathing changes","Labored, noisy, or rapid breathing is urgent; seek veterinary care."],
["eye or nose discharge","Discharge can signal infection; call your veterinarian."],
["behavior changes","A sudden personality shift often means pain or illness underneath."]
];
var TRAINING_TIPS=[
["start early","Begin training the day your pet arrives; young animals learn fastest."],
["short sessions","Keep sessions to five or ten minutes; end on a success."],
["positive reinforcement","Reward what you like; ignore or redirect what you do not."],
["consistency","Everyone in the household should use the same cues and rules."],
["socialization","Gently expose young pets to people, sounds, and places."],
["crate training","Make the crate a cozy den, never a punishment."],
["litter training","Keep boxes clean and accessible; most cats train themselves."],
["recall","Practice come with high-value rewards in safe areas first."],
["leash manners","Reward loose-leash walking; stop when they pull."],
["trick training","Tricks build communication and burn mental energy."],
["clicker basics","Mark the exact right moment, then reward."],
["patience","Progress is not linear; celebrate small wins."]
];
var ANGLES=[
["","", ""],
["first-time owners"," \u2014 first-time owners"," If this is your first pet of this kind, take it slow and enjoy learning."],
["quick facts"," \u2014 quick facts",""],
["experienced keepers"," \u2014 experienced keepers"," Seasoned keepers will find the nuance here worth noting."],
["apartment living"," \u2014 apartment living"," Small spaces work fine with the right setup and routine."],
["budget notes"," \u2014 budget notes"," Plan for food, vet care, and supplies before you commit."]
];
function comboGen(j,nE,nA,nG){
  var per=nA*nG;
  var e=j%nE, c=Math.floor(j/nE)%per, part=Math.floor(j/(nE*per));
  return {e:e,a:Math.floor(c/nG),g:c%nG,part:part};
}
var SRC="JAH Pet Care curated dataset v1 \u2014 real breeds and species; origin, size, coat, and temperament from public breed knowledge; spot-checked 2026-10-09.";
var SIGSRC="JAH Signature generator \u2014 homegrown checklists and plans, clearly labeled as generated.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" Your veterinarian can tailor this guidance to your animal.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
var BREED_ASPECTS=[
["overview",function(x,cat){return breedLine(x,cat);}],
["temperament",function(x){return "Temperament: "+x[4]+". "+x[5];}],
["care needs",function(x){return "Plan for daily care, good food, fresh water, and regular veterinary visits.";}],
["exercise",function(x){return "Match activity to the animal's nature; a tired pet is a happy pet.";}],
["grooming",function(x,cat){return cat==="dog-breed"?("Coat: "+x[3]+"; brush on a schedule that suits the coat."):("Coat: "+x[2]+"; keep up the grooming routine for the coat type.");}],
["training",function(x){return "Start training early with patience and positive reinforcement.";}],
["health notes",function(x){return "Ask your veterinarian about screening and preventive care for this breed.";}],
["for families",function(x){return "Consider your household's time, space, and experience before committing.";}]
];
function breedLine(x,cat){
  if(cat==="dog-breed")return x[0]+" ("+x[1]+", "+x[2]+", "+x[3]+" coat): "+x[5];
  return x[0]+" ("+x[1]+", "+x[2]+" coat): "+x[4]+". "+x[5];
}
var BREEDS=[["dog-breed",DOGS],["cat-breed",CATS_D],["bird",BIRDS],["fish",FISH],["reptile",REPTILES],["small-mammal",MAMMALS]];
function breedRec(seed,j,wantCat){
  var pool=BREEDS;
  if(wantCat)pool=BREEDS.filter(function(b){return b[0]===wantCat;});
  var flat=[];
  pool.forEach(function(b){b[1].forEach(function(x){flat.push([b[0],x]);});});
  var cb=comboGen(j,flat.length,BREED_ASPECTS.length,ANGLES.length);
  var bc=flat[cb.e],cat=bc[0],x=bc[1];
  var a=BREED_ASPECTS[cb.a],g=ANGLES[cb.g];
  var title=x[0]+" \u2014 "+a[0]+(cb.part>0?" (Part "+(cb.part+1)+")":"")+g[1];
  var bl=breedLine(x,cat), ap=a[1](x,cat);
  var summary=(ap===bl?ap:bl+" "+ap)+g[2];
  var details={breed:x[0],origin:x[1],aspect:a[0]};
  if(cat==="dog-breed"){details.size=x[2];details.coat=x[3];details.temperament=x[4];details.note=x[5];}
  else if(cat==="cat-breed"){details.coat=x[2];details.temperament=x[3];details.note=x[4];}
  else{details.note=x[2];}
  return mkRec(seed,cat,title,summary,details,"sourced",SRC);
}
function careRec(seed,j){
  var per=CARE_TOPICS.length*PET_TYPES.length;
  var ti=Math.floor(j/PET_TYPES.length)%CARE_TOPICS.length;
  var pi=j%PET_TYPES.length;
  var part=Math.floor(j/(per*ANGLES.length));
  var t=CARE_TOPICS[ti],pt=PET_TYPES[pi];
  var g=ANGLES[Math.floor(j/per)%ANGLES.length];
  var title="Care guide: "+pt+" "+t[0]+(part>0?" (Part "+(part+1)+")":"")+g[1];
  var summary="Pet care guide for "+PLURAL[pt]+": "+t[0]+". "+t[1][pt]+g[2];
  return mkRec(seed,"care-guide",title,summary,{pet_type:PLURAL[pt],topic:t[0],guidance:t[1][pt],part:part+1},"sourced",SRC);
}
function healthRec(seed,j){
  var per=HEALTH_ISSUES.length*PET_TYPES.length;
  var ii=Math.floor(j/PET_TYPES.length)%HEALTH_ISSUES.length;
  var pi=j%PET_TYPES.length;
  var part=Math.floor(j/(per*ANGLES.length));
  var g=ANGLES[Math.floor(j/per)%ANGLES.length];
  var h=HEALTH_ISSUES[ii],pt=PET_TYPES[pi];
  var title="Health note: "+pt+" \u2014 "+h[0]+(part>0?" (Part "+(part+1)+")":"")+g[1];
  var summary="Pet health note for "+PLURAL[pt]+": "+h[0]+". "+h[1]+g[2]+" This is general information, not a diagnosis.";
  return mkRec(seed,"health-note",title,summary,{pet_type:PLURAL[pt],issue:h[0],guidance:h[1],disclaimer:"General information; see a veterinarian."},"sourced",SRC);
}
function trainRec(seed,j){
  var types=["dog","cat","bird","small mammal"];
  var per=TRAINING_TIPS.length*types.length;
  var ti=Math.floor(j/types.length)%TRAINING_TIPS.length;
  var pi=j%types.length;
  var part=Math.floor(j/(per*ANGLES.length));
  var g=ANGLES[Math.floor(j/per)%ANGLES.length];
  var t=TRAINING_TIPS[ti],pt=types[pi];
  var title="Training tip: "+pt+" \u2014 "+t[0]+(part>0?" (Part "+(part+1)+")":"")+g[1];
  var summary="Training tip for "+pt+"s: "+t[0]+". "+t[1]+g[2];
  return mkRec(seed,"training-tip",title,summary,{pet_type:pt,tip:t[0],guidance:t[1]},"sourced",SRC);
}
var CHECKLISTS={
 dog:["Choose a complete food, bowls, collar, leash, ID tag, crate, bed, toys, grooming tools, enzyme cleaner."],
 cat:["Choose a complete food, bowls, litter box and litter, scoop, scratching post, carrier, bed, toys, brush."],
 bird:["Choose pellets, cage, perches, toys, cuttlebone, carrier, cleaning supplies, and an avian vet contact."],
 fish:["Choose tank, filter, heater if needed, substrate, decor, water conditioner, test kit, and fishless-cycle the tank first."],
 reptile:["Choose terrarium, heat and UVB lighting, thermometers, substrate, hides, water dish, food, and a reptile vet contact."],
 "small mammal":["Choose enclosure, bedding, hideouts, food, hay where needed, water bottle, chew toys, and an exotics vet contact."]
};
function checkRec(seed,j){
  var pt=PET_TYPES[j%PET_TYPES.length];
  var v=Math.floor(j/PET_TYPES.length);
  var title="New-owner checklist: "+pt+(v>0?" (v"+(v+1)+")":"");
  var summary="Signature-generated new-owner checklist \u2014 homegrown planning material. Before bringing home a "+pt+": "+CHECKLISTS[pt][0]+" Research the species' full needs first.";
  return mkRec(seed,"new-owner-checklist",title,summary,{pet_type:pt,checklist:CHECKLISTS[pt][0],variant:v+1},"signature",SIGSRC);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=6000)cat="breed";
    else if(s<=7500)cat="care-guide";
    else if(s<=8500)cat="health-note";
    else if(s<=9500)cat="training-tip";
    else cat="new-owner-checklist";
  }
  function ord(base){return explicit?(s-1):(s-base);}
  var breedCats=["dog-breed","cat-breed","bird","fish","reptile","small-mammal"];
  if(cat==="breed")return breedRec(seed,ord(1),null);
  if(breedCats.indexOf(cat)>=0)return breedRec(seed,ord(1),cat);
  if(cat==="care-guide")return careRec(seed,ord(6001));
  if(cat==="health-note")return healthRec(seed,ord(7501));
  if(cat==="training-tip")return trainRec(seed,ord(8501));
  if(cat==="new-owner-checklist")return checkRec(seed,ord(9501));
  return breedRec(seed,ord(1),null);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-PET-\d{6,7}$/.test(r.id||""))e.push("id");
  if(typeof r.title!=="string"||!r.title.length)e.push("title");
  if(CATS.indexOf(r.category)<0)e.push("category");
  if(r.record_kind!==KIND)e.push("record_kind");
  if(typeof r.summary!=="string"||r.summary.length<80)e.push("summary");
  if(!r.details||typeof r.details!=="object")e.push("details");
  if(r.provenance!=="sourced"&&r.provenance!=="signature")e.push("provenance");
  if(typeof r.source!=="string"||!r.source.length)e.push("source");
  return {ok:!e.length,errors:e};
}
function driftCheck(rec,sample){
  sample=sample||[];
  for(var i=0;i<sample.length;i++)if(sample[i]&&sample[i].id===rec.id)return {ok:false,errors:["already in archive: "+rec.id]};
  return {ok:true,errors:[]};
}
var gen={version:"jahdb-pets-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("pets",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
