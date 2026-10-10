/* JAH Paleontology Database generator — jahdb-paleontology-1.0
   Deterministic (mulberry32). Seed -> full fossil entry.
   Sourced records draw every fact from the curated real-taxon dataset below
   (public paleontological knowledge; headline facts spot-checked against
   public science reporting 2026-10-09). Signature records are homegrown
   study material / boundless speculation, always labeled as such.
   Property of Justin Addam Higgins (JAH). */
(function(){'use strict';
function prng(seed){var a=(seed>>>0)||1;return function(){a|=0;a=(a+0x6D2B79F5)|0;var t=Math.imul(a^(a>>>15),1|a);t=(t+Math.imul(t^(t>>>7),61|t))^t;return((t^(t>>>14))>>>0)/4294967296;};}
function pick(r,s){return r[(s()*r.length)|0];}
var PREFIX='JAH-PAL-';
var KIND='fossil entry';
var CATS=['dinosaur','marine-reptile','flying-reptile','prehistoric-mammal','invertebrate','plant','ancient-reptile','dig-site','era','field-note','hypothetical'];
/* [scientific, common, group, period, mya, region, diet, size, fact, category] */
var TAXA=[
["Tyrannosaurus rex","Tyrannosaurus","theropod","Late Cretaceous","68-66 million years ago","North America","carnivore","about 12 meters long","One of the largest land predators ever known, with bone-crushing bite force.","dinosaur"],
["Triceratops horridus","Triceratops","ceratopsian","Late Cretaceous","68-66 million years ago","North America","herbivore","about 9 meters long","Famous for its three facial horns and large bony frill.","dinosaur"],
["Stegosaurus stenops","Stegosaurus","stegosaur","Late Jurassic","about 155-150 million years ago","North America","herbivore","about 9 meters long","Carried two rows of upright bony plates along its back and spikes on its tail.","dinosaur"],
["Brachiosaurus altithorax","Brachiosaurus","sauropod","Late Jurassic","about 154-150 million years ago","North America","herbivore","about 22 meters long","Its front legs were longer than its hind legs, giving it a giraffe-like stance.","dinosaur"],
["Velociraptor mongoliensis","Velociraptor","dromaeosaur","Late Cretaceous","about 75-71 million years ago","Mongolia","carnivore","about 2 meters long","A small feathered predator with a sickle-shaped claw on each foot.","dinosaur"],
["Allosaurus fragilis","Allosaurus","theropod","Late Jurassic","about 155-145 million years ago","North America","carnivore","about 8.5 meters long","The most common large predator of the Morrison Formation.","dinosaur"],
["Diplodocus longus","Diplodocus","sauropod","Late Jurassic","about 154-152 million years ago","North America","herbivore","about 26 meters long","Had an extremely long whip-like tail, possibly used for defense.","dinosaur"],
["Parasaurolophus walkeri","Parasaurolophus","hadrosaur","Late Cretaceous","about 76-73 million years ago","North America","herbivore","about 10 meters long","Its long backward-curving crest may have worked as a resonating chamber.","dinosaur"],
["Ankylosaurus magniventris","Ankylosaurus","ankylosaur","Late Cretaceous","68-66 million years ago","North America","herbivore","about 8 meters long","Covered in armor plates with a heavy club on its tail.","dinosaur"],
["Spinosaurus aegyptiacus","Spinosaurus","theropod","Late Cretaceous","about 99-93 million years ago","North Africa","carnivore","about 14 meters long","Had a large sail on its back and likely hunted fish in rivers.","dinosaur"],
["Carnotaurus sastrei","Carnotaurus","theropod","Late Cretaceous","about 72-69 million years ago","Argentina","carnivore","about 8 meters long","Had two short horns above its eyes and remarkably tiny arms.","dinosaur"],
["Giganotosaurus carolinii","Giganotosaurus","theropod","Late Cretaceous","about 99-97 million years ago","Argentina","carnivore","about 12.5 meters long","One of the largest meat-eating dinosaurs, longer than Tyrannosaurus.","dinosaur"],
["Deinonychus antirrhopus","Deinonychus","dromaeosaur","Early Cretaceous","about 115-108 million years ago","North America","carnivore","about 3.4 meters long","Its fossils helped spark the idea that dinosaurs were active, bird-like animals.","dinosaur"],
["Iguanodon bernissartensis","Iguanodon","ornithopod","Early Cretaceous","about 126-122 million years ago","Europe","herbivore","about 10 meters long","Had a spike on each thumb, once mistakenly placed on its nose.","dinosaur"],
["Maiasaura peeblesorum","Maiasaura","hadrosaur","Late Cretaceous","about 76 million years ago","Montana","herbivore","about 9 meters long","Nests with eggs and babies showed it cared for its young; its name means good mother lizard.","dinosaur"],
["Pachycephalosaurus wyomingensis","Pachycephalosaurus","pachycephalosaur","Late Cretaceous","68-66 million years ago","North America","herbivore","about 4.5 meters long","Had a thick domed skull, possibly used for head-butting.","dinosaur"],
["Gallimimus bullatus","Gallimimus","ornithomimid","Late Cretaceous","about 70 million years ago","Mongolia","omnivore","about 6 meters long","Built like an ostrich, it was one of the fastest dinosaurs.","dinosaur"],
["Therizinosaurus cheloniformis","Therizinosaurus","therizinosaur","Late Cretaceous","about 70 million years ago","Mongolia","herbivore","about 10 meters long","Had enormous hand claws nearly a meter long.","dinosaur"],
["Dilophosaurus wetherilli","Dilophosaurus","theropod","Early Jurassic","about 193 million years ago","Arizona","carnivore","about 7 meters long","Had a pair of thin crests on top of its skull.","dinosaur"],
["Baryonyx walkeri","Baryonyx","spinosaur","Early Cretaceous","about 130-125 million years ago","England","carnivore","about 8.5 meters long","Fish scales found in its stomach show it ate fish.","dinosaur"],
["Tarbosaurus bataar","Tarbosaurus","theropod","Late Cretaceous","about 70 million years ago","Mongolia","carnivore","about 10 meters long","Asia's close relative of Tyrannosaurus.","dinosaur"],
["Edmontosaurus annectens","Edmontosaurus","hadrosaur","Late Cretaceous","68-66 million years ago","North America","herbivore","about 12 meters long","Mummified fossils preserved impressions of its skin.","dinosaur"],
["Styracosaurus albertensis","Styracosaurus","ceratopsian","Late Cretaceous","about 75 million years ago","Canada","herbivore","about 5.5 meters long","Had six long spikes around the edge of its frill.","dinosaur"],
["Euoplocephalus tutus","Euoplocephalus","ankylosaur","Late Cretaceous","about 76-70 million years ago","Canada","herbivore","about 6 meters long","Even its eyelids were armored with bony plates.","dinosaur"],
["Argentinosaurus huinculensis","Argentinosaurus","sauropod","Late Cretaceous","about 96-94 million years ago","Argentina","herbivore","about 35 meters long","Among the largest land animals ever discovered.","dinosaur"],
["Patagotitan mayorum","Patagotitan","sauropod","Late Cretaceous","about 101 million years ago","Argentina","herbivore","about 37 meters long","Its thigh bone alone stands over 2 meters tall; among the largest animals ever to walk the Earth.","dinosaur"],
["Brontosaurus excelsus","Brontosaurus","sauropod","Late Jurassic","about 155-152 million years ago","North America","herbivore","about 22 meters long","Once thought the same as Apatosaurus, it was restored as its own genus in 2015.","dinosaur"],
["Mamenchisaurus hochuanensis","Mamenchisaurus","sauropod","Late Jurassic","about 160 million years ago","China","herbivore","about 22 meters long","Had one of the longest necks of any animal, about half its body length.","dinosaur"],
["Psittacosaurus mongoliensis","Psittacosaurus","ceratopsian","Early Cretaceous","about 126-101 million years ago","Mongolia and China","herbivore","about 2 meters long","A small early horned dinosaur with a parrot-like beak.","dinosaur"],
["Protoceratops andrewsi","Protoceratops","ceratopsian","Late Cretaceous","about 75-71 million years ago","Mongolia","herbivore","about 1.8 meters long","One specimen was fossilized locked in combat with a Velociraptor.","dinosaur"],
["Oviraptor philoceratops","Oviraptor","oviraptorid","Late Cretaceous","about 75 million years ago","Mongolia","omnivore","about 1.6 meters long","First thought an egg thief, it was later found brooding its own nest.","dinosaur"],
["Microraptor zhaoianus","Microraptor","dromaeosaur","Early Cretaceous","about 125-113 million years ago","China","carnivore","about 0.8 meters long","A four-winged dinosaur with feathers on both its arms and legs.","dinosaur"],
["Compsognathus longipes","Compsognathus","theropod","Late Jurassic","about 150 million years ago","Germany","carnivore","about 1 meter long","Once thought to be the smallest dinosaur, about the size of a chicken.","dinosaur"],
["Coelophysis bauri","Coelophysis","theropod","Late Triassic","about 215-208 million years ago","New Mexico","carnivore","about 3 meters long","Thousands of skeletons were found together at Ghost Ranch.","dinosaur"],
["Herrerasaurus ischigualastensis","Herrerasaurus","theropod","Late Triassic","about 231 million years ago","Argentina","carnivore","about 6 meters long","One of the earliest known dinosaurs.","dinosaur"],
["Plateosaurus engelhardti","Plateosaurus","sauropodomorph","Late Triassic","about 214-204 million years ago","Germany","herbivore","about 8 meters long","One of the first giant herbivorous dinosaurs.","dinosaur"],
["Postosuchus kirkpatricki","Postosuchus","rauisuchian","Late Triassic","about 221-215 million years ago","North America","carnivore","about 4 meters long","A giant Triassic predator, but not a dinosaur; it was a crocodile relative.","dinosaur"],
["Mosasaurus hoffmannii","Mosasaurus","mosasaur","Late Cretaceous","70-66 million years ago","oceans worldwide","carnivore","about 15 meters long","A giant marine lizard, not a dinosaur; its discovery helped found paleontology.","marine-reptile"],
["Tylosaurus proriger","Tylosaurus","mosasaur","Late Cretaceous","about 88-78 million years ago","North America","carnivore","about 14 meters long","Had a battering-ram-like snout for ramming prey.","marine-reptile"],
["Elasmosaurus platyurus","Elasmosaurus","plesiosaur","Late Cretaceous","about 80 million years ago","North America","carnivore","about 14 meters long","Had an extremely long neck with more than 70 vertebrae.","marine-reptile"],
["Plesiosaurus dolichodeirus","Plesiosaurus","plesiosaur","Early Jurassic","about 199-192 million years ago","England","carnivore","about 3.5 meters long","One of the first plesiosaurs ever described by science.","marine-reptile"],
["Ichthyosaurus communis","Ichthyosaurus","ichthyosaur","Early Jurassic","about 201-194 million years ago","Europe","carnivore","about 3.3 meters long","A dolphin-shaped reptile; Mary Anning found famous specimens.","marine-reptile"],
["Liopleurodon ferox","Liopleurodon","pliosaur","Middle Jurassic","about 166-160 million years ago","Europe","carnivore","about 6.5 meters long","A short-necked plesiosaur with a massive head.","marine-reptile"],
["Kronosaurus queenslandicus","Kronosaurus","pliosaur","Early Cretaceous","about 120-100 million years ago","Australia","carnivore","about 10 meters long","Named after the Titan Kronos; one of the largest pliosaurs.","marine-reptile"],
["Xiphactinus audax","Xiphactinus","bony fish","Late Cretaceous","about 87-66 million years ago","North America","carnivore","about 5 meters long","One fossil was found with a whole fish preserved inside it.","marine-reptile"],
["Dunkleosteus terrelli","Dunkleosteus","placoderm","Late Devonian","about 382-358 million years ago","Ohio","carnivore","about 6 meters long","An armored fish with bladed jaw plates instead of teeth.","marine-reptile"],
["Helicoprion bessonowi","Helicoprion","shark relative","Permian","about 290-270 million years ago","oceans worldwide","carnivore","about 7 meters long","Had a spiral tooth whorl in its lower jaw.","marine-reptile"],
["Leedsichthys problematicus","Leedsichthys","bony fish","Middle Jurassic","about 165 million years ago","England","filter feeder","about 16 meters long","The largest known bony fish ever.","marine-reptile"],
["Shonisaurus popularis","Shonisaurus","ichthyosaur","Late Triassic","about 215 million years ago","Nevada","carnivore","about 15 meters long","Nevada's state fossil.","marine-reptile"],
["Mixosaurus cornalianus","Mixosaurus","ichthyosaur","Middle Triassic","about 247-242 million years ago","Europe and China","carnivore","about 1 meter long","One of the smallest ichthyosaurs.","marine-reptile"],
["Nothosaurus mirabilis","Nothosaurus","nothosaur","Middle Triassic","about 247-242 million years ago","Europe","carnivore","about 4 meters long","A long-necked swimmer, an early relative of the plesiosaurs.","marine-reptile"],
["Pteranodon longiceps","Pteranodon","pterosaur","Late Cretaceous","about 86-84 million years ago","North America","carnivore","wingspan about 7 meters","Had a long backward-pointing head crest.","flying-reptile"],
["Quetzalcoatlus northropi","Quetzalcoatlus","pterosaur","Late Cretaceous","68-66 million years ago","Texas","carnivore","wingspan about 10 meters","One of the largest flying animals ever, named for the Aztec god Quetzalcoatl.","flying-reptile"],
["Pterodactylus antiquus","Pterodactylus","pterosaur","Late Jurassic","about 150 million years ago","Germany","carnivore","wingspan about 1 meter","The first pterosaur ever named.","flying-reptile"],
["Rhamphorhynchus muensteri","Rhamphorhynchus","pterosaur","Late Jurassic","about 150 million years ago","Germany","carnivore","wingspan about 1.8 meters","Had a long tail with a diamond-shaped tip.","flying-reptile"],
["Dimorphodon macronyx","Dimorphodon","pterosaur","Early Jurassic","about 201-191 million years ago","England","carnivore","wingspan about 1.4 meters","Had a large head with two different kinds of teeth.","flying-reptile"],
["Mammuthus primigenius","Woolly mammoth","mammoth","Pleistocene","about 300,000-4,000 years ago","Northern Hemisphere","herbivore","about 3.4 meters at the shoulder","Covered in thick fur with curved tusks; frozen specimens preserve soft tissue.","prehistoric-mammal"],
["Mammuthus columbi","Columbian mammoth","mammoth","Pleistocene","about 1.5 million-11,000 years ago","North America","herbivore","about 4 meters at the shoulder","Larger than the woolly mammoth, with much less hair.","prehistoric-mammal"],
["Mammut americanum","American mastodon","mastodon","Pleistocene","about 3.7 million-11,000 years ago","North America","herbivore","about 3 meters at the shoulder","Browsed on trees and shrubs, unlike the grazing mammoths.","prehistoric-mammal"],
["Smilodon populator","Smilodon","saber-toothed cat","Pleistocene","about 1 million-10,000 years ago","South America","carnivore","about 2.6 meters long","Had canine teeth more than 28 centimeters long.","prehistoric-mammal"],
["Homotherium serum","Scimitar-toothed cat","machairodont","Pleistocene","about 1.8 million-12,000 years ago","North America","carnivore","about 1.1 meters at the shoulder","Had shorter, serrated saber teeth built for slashing.","prehistoric-mammal"],
["Aenocyon dirus","Dire wolf","canid","Pleistocene","about 250,000-10,000 years ago","the Americas","carnivore","about 1.5 meters long","Larger and stronger than modern gray wolves.","prehistoric-mammal"],
["Arctodus simus","Short-faced bear","bear","Pleistocene","about 800,000-11,000 years ago","North America","omnivore","about 3.4 meters standing","One of the largest land carnivores of the Ice Age.","prehistoric-mammal"],
["Megatherium americanum","Giant ground sloth","ground sloth","Pleistocene","about 1 million-10,000 years ago","South America","herbivore","about 6 meters long","An elephant-sized sloth that walked on the ground.","prehistoric-mammal"],
["Glyptodon clavipes","Glyptodon","glyptodont","Pleistocene","about 2.5 million-11,000 years ago","South America","herbivore","about 3.3 meters long","A giant armadillo relative with a domed shell.","prehistoric-mammal"],
["Doedicurus clavicaudatus","Doedicurus","glyptodont","Pleistocene","about 2 million-11,000 years ago","South America","herbivore","about 4 meters long","Had a spiked club on its tail.","prehistoric-mammal"],
["Megaloceros giganteus","Irish elk","deer","Pleistocene","about 400,000-7,700 years ago","Eurasia","herbivore","about 2.1 meters at the shoulder","Had the largest antlers of any deer, spanning 3.5 meters.","prehistoric-mammal"],
["Thylacoleo carnifex","Marsupial lion","marsupial","Pleistocene","about 1.6 million-46,000 years ago","Australia","carnivore","about 1.5 meters long","Australia's largest marsupial predator.","prehistoric-mammal"],
["Diprotodon optatum","Diprotodon","marsupial","Pleistocene","about 1.6 million-44,000 years ago","Australia","herbivore","about 3 meters long","The largest marsupial ever, the size of a rhinoceros.","prehistoric-mammal"],
["Paraceratherium transouralicum","Paraceratherium","rhino relative","Oligocene","about 34-23 million years ago","Eurasia","herbivore","about 4.8 meters at the shoulder","The largest land mammal ever known.","prehistoric-mammal"],
["Basilosaurus isis","Basilosaurus","early whale","Eocene","about 40-34 million years ago","Egypt","carnivore","about 18 meters long","A serpent-like early whale with tiny hind limbs.","prehistoric-mammal"],
["Pakicetus inachus","Pakicetus","early whale","Eocene","about 50 million years ago","Pakistan","carnivore","about 2 meters long","A land-dwelling ancestor of whales.","prehistoric-mammal"],
["Ambulocetus natans","Ambulocetus","early whale","Eocene","about 48 million years ago","Pakistan","carnivore","about 3 meters long","The walking whale that swam like an otter.","prehistoric-mammal"],
["Hyracotherium leporinum","Hyracotherium","early horse","Eocene","about 55-45 million years ago","North America and Europe","herbivore","about 0.4 meters at the shoulder","A dog-sized ancestor of the horse, once called Eohippus.","prehistoric-mammal"],
["Uintatherium anceps","Uintatherium","uintathere","Eocene","about 46-40 million years ago","North America","herbivore","about 1.6 meters at the shoulder","Had six bony knobs on its head and saber-like canine teeth.","prehistoric-mammal"],
["Megacerops coloradensis","Brontothere","brontothere","Eocene","about 38-33 million years ago","North America","herbivore","about 2.5 meters at the shoulder","A rhino-like giant with a forked horn on its nose.","prehistoric-mammal"],
["Hyaenodon horridus","Hyaenodon","hyaenodont","Eocene-Oligocene","about 42-34 million years ago","North America","carnivore","about 1.5 meters long","A bone-crushing predator, not related to modern hyenas.","prehistoric-mammal"],
["Entelodon magnus","Entelodon","entelodont","Oligocene","about 34-28 million years ago","Eurasia","omnivore","about 2 meters at the shoulder","A giant pig-like omnivore nicknamed the hell pig.","prehistoric-mammal"],
["Deinotherium giganteum","Deinotherium","deinothere","Miocene-Pleistocene","about 20 million-1 million years ago","Eurasia and Africa","herbivore","about 4 meters at the shoulder","Had downward-curving tusks on its lower jaw.","prehistoric-mammal"],
["Platybelodon grangeri","Platybelodon","gomphothere","Miocene","about 15-10 million years ago","Mongolia","herbivore","about 3 meters long","Had a shovel-like lower jaw for scooping plants.","prehistoric-mammal"],
["Sivatherium giganteum","Sivatherium","giraffid","Pliocene-Pleistocene","about 5 million-8,000 years ago","Africa and Asia","herbivore","about 2.2 meters at the shoulder","A giant short-necked relative of the giraffe.","prehistoric-mammal"],
["Gigantopithecus blacki","Gigantopithecus","ape","Pleistocene","about 2 million-300,000 years ago","China","herbivore","about 3 meters standing","The largest ape ever known.","prehistoric-mammal"],
["Australopithecus afarensis","Australopithecus afarensis","hominin","Pliocene","about 3.9-2.9 million years ago","Ethiopia","omnivore","about 1.1 meters tall","Lucy, the famous skeleton, belongs to this species.","prehistoric-mammal"],
["Homo neanderthalensis","Neanderthal","hominin","Pleistocene","about 400,000-40,000 years ago","Eurasia","omnivore","about 1.65 meters tall","Buried their dead and made complex tools.","prehistoric-mammal"],
["Homo erectus","Homo erectus","hominin","Pleistocene","about 1.9 million-110,000 years ago","Africa and Asia","omnivore","about 1.7 meters tall","The first hominin to control fire and leave Africa.","prehistoric-mammal"],
["Andrewsarchus mongoliensis","Andrewsarchus","mesonychid","Eocene","about 45-36 million years ago","Mongolia","carnivore","skull about 83 cm long","Known from a single giant skull; possibly the largest land carnivorous mammal.","prehistoric-mammal"],
["Elrathia kingi","Elrathia trilobite","trilobite","Cambrian","about 513-501 million years ago","Utah","detritivore","about 3 cm long","One of the most common trilobites in the Wheeler Shale.","invertebrate"],
["Anomalocaris canadensis","Anomalocaris","radiodont","Cambrian","about 508 million years ago","Canada","carnivore","about 1 meter long","The top predator of the Cambrian seas.","invertebrate"],
["Hallucigenia sparsa","Hallucigenia","lobopodian","Cambrian","about 508 million years ago","Canada","detritivore","about 3 cm long","Scientists once reconstructed it upside-down.","invertebrate"],
["Opabinia regalis","Opabinia","arthropod","Cambrian","about 508 million years ago","Canada","carnivore","about 7 cm long","Had five eyes and a nozzle-like snout.","invertebrate"],
["Wiwaxia corrugata","Wiwaxia","mollusc relative","Cambrian","about 508 million years ago","Canada","herbivore","about 5 cm long","Covered in overlapping scales and spines.","invertebrate"],
["Marrella splendens","Marrella","arthropod","Cambrian","about 508 million years ago","Canada","scavenger","about 2 cm long","The most common fossil of the Burgess Shale.","invertebrate"],
["Pikaia gracilens","Pikaia","chordate","Cambrian","about 508 million years ago","Canada","filter feeder","about 4 cm long","An early relative of all vertebrates, including humans.","invertebrate"],
["Eurypterus remipes","Sea scorpion","eurypterid","Silurian","about 422-419 million years ago","New York","carnivore","about 1.3 meters long","New York's state fossil.","invertebrate"],
["Jaekelopterus rhenaniae","Jaekelopterus","eurypterid","Devonian","about 390 million years ago","Germany","carnivore","about 2.5 meters long","The largest arthropod ever known.","invertebrate"],
["Placenticeras meeki","Ammonite","ammonite","Cretaceous","about 80-70 million years ago","North America","carnivore","shell up to 1 meter across","Its iridescent fossil shells are sold as the gemstone ammolite.","invertebrate"],
["Orthoceras regulare","Orthoceras","nautiloid","Ordovician","about 470 million years ago","oceans worldwide","carnivore","about 30 cm long","A straight-shelled relative of the nautilus.","invertebrate"],
["Lepidodendron aculeatum","Scale tree","lycopod","Carboniferous","about 359-299 million years ago","worldwide","photosynthesizer","up to 30 meters tall","A giant club moss; its remains formed much of the world's coal.","plant"],
["Calamites suckowii","Calamites","horsetail","Carboniferous","about 359-299 million years ago","worldwide","photosynthesizer","up to 10 meters tall","A tree-sized relative of modern horsetails.","plant"],
["Glossopteris browniana","Glossopteris","seed fern","Permian","about 299-252 million years ago","the Southern Hemisphere","photosynthesizer","tree-sized","Its fossils across southern continents helped prove continental drift.","plant"],
["Archaeopteris hibernica","Archaeopteris","progymnosperm","Devonian","about 383-359 million years ago","worldwide","photosynthesizer","up to 30 meters tall","One of the first true trees.","plant"],
["Williamsonia gigas","Williamsonia","bennettitale","Jurassic-Cretaceous","about 200-100 million years ago","worldwide","photosynthesizer","shrub-sized","A cycad-like plant with flower-like reproductive structures.","plant"],
["Ginkgoites huttonii","Fossil ginkgo","ginkgo","Jurassic","about 200-150 million years ago","worldwide","photosynthesizer","up to 30 meters tall","A near relative of the living ginkgo, a famous living fossil.","plant"],
["Dimetrodon limbatus","Dimetrodon","synapsid","Permian","about 295-272 million years ago","North America","carnivore","about 4.6 meters long","Its sail may have regulated body temperature; it lived before the dinosaurs.","ancient-reptile"],
["Eryops megacephalus","Eryops","temnospondyl","Permian","about 295 million years ago","North America","carnivore","about 2 meters long","A giant salamander-like amphibian.","ancient-reptile"],
["Tiktaalik roseae","Tiktaalik","tetrapodomorph","Devonian","about 375 million years ago","Canada","carnivore","about 2.75 meters long","A fish with wrist-like fins, a key step in the move onto land.","ancient-reptile"],
["Lystrosaurus murrayi","Lystrosaurus","dicynodont","Triassic","about 252-247 million years ago","South Africa","herbivore","about 1 meter long","Survived the great Permian extinction and spread worldwide.","ancient-reptile"],
["Cynognathus crateronotus","Cynognathus","cynodont","Triassic","about 247-237 million years ago","South Africa","carnivore","about 1.2 meters long","A mammal-like reptile close to the ancestry of mammals.","ancient-reptile"],
["Eusthenopteron foordi","Eusthenopteron","tetrapodomorph","Devonian","about 385 million years ago","Canada","carnivore","about 1.8 meters long","A lobe-finned fish closely related to land vertebrates.","ancient-reptile"]
];
/* [name, location, age, famous_for] */
var SITES=[
["Hell Creek Formation","Montana, USA","Late Cretaceous","Tyrannosaurus and Triceratops fossils."],
["Morrison Formation","Colorado and Utah, USA","Late Jurassic","Stegosaurus, Allosaurus, and giant sauropods."],
["La Brea Tar Pits","Los Angeles, California, USA","Pleistocene","Saber-toothed cats, mammoths, and dire wolves trapped in asphalt."],
["Burgess Shale","British Columbia, Canada","Cambrian","Exquisitely preserved soft-bodied Cambrian animals."],
["Solnhofen Limestone","Bavaria, Germany","Late Jurassic","Archaeopteryx and finely preserved Jurassic fossils."],
["Olduvai Gorge","Tanzania","Pleistocene","Early human ancestors and stone tools."],
["Ghost Ranch","New Mexico, USA","Late Triassic","Thousands of Coelophysis skeletons."],
["Cleveland-Lloyd Dinosaur Quarry","Utah, USA","Late Jurassic","A dense bonebed of Allosaurus and other predators."],
["Dinosaur National Monument","Utah and Colorado, USA","Late Jurassic","A wall of dinosaur bones left in place for visitors."],
["Liaoning fossil beds","Liaoning, China","Early Cretaceous","Feathered dinosaurs and early birds."],
["Messel Pit","Hesse, Germany","Eocene","Perfectly preserved Eocene mammals, birds, and insects."],
["Green River Formation","Wyoming and Utah, USA","Eocene","Millions of fossil fish in paper-thin limestone."],
["Mazon Creek","Illinois, USA","Carboniferous","Soft-bodied fossils in ironstone nodules, including the Tully monster."],
["Chengjiang","Yunnan, China","Cambrian","Older than the Burgess Shale, with early chordates."],
["Ediacara Hills","South Australia","Ediacaran","The first complex multicellular life."],
["Karoo Basin","South Africa","Permian-Triassic","Mammal-like reptiles across the great extinction."],
["Ischigualasto","Argentina","Late Triassic","Some of the oldest dinosaurs."],
["Santa Maria Formation","Brazil","Triassic","Early dinosaurs and their relatives."],
["John Day Fossil Beds","Oregon, USA","Eocene-Miocene","Forty million years of mammal evolution."],
["Ashfall Fossil Beds","Nebraska, USA","Miocene","Whole herds of rhinos and horses buried in volcanic ash."],
["Hagerman Fossil Beds","Idaho, USA","Pliocene","The Hagerman horse, an early one-toed horse."],
["Drumheller badlands","Alberta, Canada","Late Cretaceous","Rich dinosaur bonebeds of the Horseshoe Canyon."],
["Howe Quarry","Wyoming, USA","Late Jurassic","A sauropod bonebed excavated in the 1930s."],
["Mygatt-Moore Quarry","Colorado, USA","Late Jurassic","An active Jurassic dinosaur dig."]
];
/* [name, span, note] */
var ERAS=[
["Precambrian","4.6 billion-541 million years ago","From Earth's formation to the first complex animals."],
["Cambrian","541-485 million years ago","The Cambrian explosion of animal life."],
["Ordovician","485-444 million years ago","Seas full of trilobites, nautiloids, and early fish."],
["Silurian","444-419 million years ago","Plants and arthropods begin to colonize land."],
["Devonian","419-359 million years ago","The Age of Fishes; tetrapods evolve."],
["Carboniferous","359-299 million years ago","Giant insects and vast coal forests."],
["Permian","299-252 million years ago","Ends with the largest mass extinction ever."],
["Triassic","252-201 million years ago","Dinosaurs and mammals first appear."],
["Jurassic","201-145 million years ago","The golden age of giant dinosaurs."],
["Cretaceous","145-66 million years ago","Ends with the asteroid that wiped out the non-bird dinosaurs."],
["Paleogene","66-23 million years ago","Mammals diversify after the dinosaurs."],
["Neogene","23-2.6 million years ago","Grasslands spread; apes and early humans evolve."],
["Quaternary","2.6 million years ago to the present","Ice ages and the rise of Homo sapiens."]
];
var FOCUS=[
["anatomy",function(t){return "It grew to "+t[7]+", with a body built for its "+t[6]+" way of life.";}],
["diet",function(t){return "As a "+t[6]+", it played its part in the "+t[3]+" food web.";}],
["habitat",function(t){return "It lived in the region now known as "+t[5]+" during the "+t[3]+".";}],
["era",function(t){return "Its time was the "+t[3]+" ("+t[4]+").";}],
["relatives",function(t){return "It belongs to the "+t[2]+" group of prehistoric animals.";}],
["fossils",function(t){return "Fossil remains are the primary record of its existence.";}],
["extinction",function(t){return "Its world vanished long before humans appeared.";}],
["science",function(t){return "Paleontologists study its fossils to understand "+t[3]+" life.";}]
];
var ANGLES=[
["", "", ""],
["young readers"," \u2014 for young readers"," Imagine standing beside it: an unforgettable sight from deep time."],
["museum guide"," \u2014 museum guide"," Museum mounts let visitors stand beside its reconstructed skeleton."],
["research notes"," \u2014 research notes"," Each new fossil find sharpens what science knows about this animal."],
["a deep-time story"," \u2014 a deep-time story"," Picture it moving through its ancient world, ages before people."],
["quick facts"," \u2014 quick facts",""]
];
var SITE_ASPECTS=[
["overview","This dig site is one of the great fossil windows into deep time."],
["age and geology","Its rocks date to the "+""+""],
["famous finds","Its most celebrated fossils draw researchers from around the world."],
["research significance","Work here continues to reshape the scientific picture of ancient life."],
["preservation","Conditions here preserved details rarely seen elsewhere."],
["for students","Students can learn deep-time thinking from this site's story."],
["field methods","Excavation here follows careful layer-by-layer methods."],
["legacy","Generations of fossil hunters have walked these grounds."]
];
var ERA_ASPECTS=[
["overview","This span of deep time shaped the history of life."],
["life","The living world of this time would look alien to modern eyes."],
["geology","Its rocks record seas, deserts, and mountains long vanished."],
["climate","Climate shifts within this time redrew the map of life."],
["key events","Great events of this age still echo in the fossil record."],
["famous fossils","Its signature fossils are icons of paleontology."],
["for students","Students can trace cause and effect across this age."],
["deep time","Grasping this span trains the mind to think in millions of years."]
];
var NOTE_TYPES=[
"anatomy sketch notes","diet reconstruction","habitat reconstruction","era context",
"size comparison","behavior notes","classroom summary","research questions"
];
var SCEN=[
["surviving to the present","imagine it had survived the end-Cretaceous extinction and still walked the Earth today"],
["with feathers fully preserved","imagine a specimen preserved so perfectly that every feather and scale could be seen"],
["twice its known size","imagine it had grown to twice its known size"],
["in a colder climate","imagine it adapted to an ice-age climate"],
["with a different diet","imagine it had evolved a completely different diet"],
["discovered alive","imagine it was discovered alive in a remote valley"],
["with glowing display","imagine it carried bioluminescent display structures"],
["as a pack hunter","imagine it hunted in coordinated packs"],
["raised in a sanctuary","imagine a modern sanctuary built to house it"],
["as a deep-sea swimmer","imagine its lineage had returned to the sea"]
];
function identity(t){return t[1]+" ("+t[0]+") was a "+t[6]+" "+t[2]+" of the "+t[3]+" ("+t[4]+"), living in what is now "+t[5]+".";}
function taxonDetail(t){return {scientific_name:t[0],common_name:t[1],group:t[2],period:t[3],lived:t[4],region:t[5],diet:t[6],size:t[7],notable_fact:t[8]};}
var SRC="JAH Paleontology curated dataset v1 \u2014 taxa compiled from public paleontological knowledge; headline facts spot-checked against public science reporting 2026-10-09.";
var SIGSRC="JAH Signature generator \u2014 homegrown study material; underlying facts from the curated dataset, clearly labeled as generated.";
function mkRec(seed,cat,title,summary,details,prov,src){
  while(summary.length<80)summary+=" The full record below carries every known detail.";
  return {id:PREFIX+String(seed).padStart(6,"0"),title:title,category:cat,record_kind:KIND,
    summary:summary,details:details,provenance:prov,source:src,_seed:seed};
}
function genProfile(seed,j,rnd,wantCat){
  var pool=TAXA;
  if(wantCat)pool=TAXA.filter(function(t){return t[9]===wantCat;});
  if(!pool.length)pool=TAXA;
  var TL=pool.length;
  var t=pool[j%TL];
  var combo=Math.floor(j/TL)%48;
  var f=FOCUS[combo%8],a=ANGLES[Math.floor(combo/8)%6];
  var title=t[1]+(a[0]?a[1]:" \u2014 "+f[0]);
  var summary=identity(t)+" "+f[1](t)+" "+t[8]+a[2];
  var d=taxonDetail(t);d.focus=f[0];d.angle=a[0]||"standard";
  return mkRec(seed,t[9],title,summary,d,"sourced",SRC);
}
function genCompare(seed,s,rnd){
  var j=s,TL=TAXA.length;
  var ai=(j*13)%TL,bi=(j*29+7)%TL;
  if(bi===ai)bi=(bi+1)%TL;
  var a=TAXA[ai],b=TAXA[bi];
  var title=a[1]+" vs "+b[1];
  var sameP=a[3]===b[3],sameD=a[6]===b[6];
  var summary="Two prehistoric animals, side by side. "+identity(a)+" "+identity(b)+" "+
    (sameP?("Both lived during the "+a[3]+"."):("They lived in different times: the "+a[3]+" and the "+b[3]+"."))+" "+
    (sameD?("Both were "+a[6]+"s."):("One was a "+a[6]+" and the other a "+b[6]+"."));
  var details={subject_a:taxonDetail(a),subject_b:taxonDetail(b),shared_period:sameP,shared_diet:sameD,
    comparison:a[1]+" reached "+a[7]+"; "+b[1]+" reached "+b[7]+"."};
  return mkRec(seed,"dinosaur",title,summary,details,"sourced",SRC);
}
function genSite(seed,s,rnd){
  var j=s,SL=SITES.length;
  var st=SITES[j%SL];
  var asp=SITE_ASPECTS[Math.floor(j/SL)%8];
  var ang=ANGLES[Math.floor(j/(SL*8))%6];
  var title=st[0]+" \u2014 "+asp[0]+(ang[0]?" ("+ang[0]+")":"");
  var ageLine="Its rocks date to the "+st[2]+".";
  var summary=st[0]+" lies in "+st[1]+" and preserves fossils from "+st[2]+". "+st[3]+" "+
    (asp[0]==="age and geology"?ageLine:asp[1])+ang[2];
  var details={site_name:st[0],location:st[1],age:st[2],famous_for:st[3],aspect:asp[0]};
  return mkRec(seed,"dig-site",title,summary,details,"sourced",SRC);
}
function genEra(seed,s,rnd){
  var j=s;
  var e=ERAS[j%13];
  var asp=ERA_ASPECTS[Math.floor(j/13)%8];
  var ang=ANGLES[Math.floor(j/104)%6];
  var title="The "+e[0]+" \u2014 "+asp[0]+(ang[0]?" ("+ang[0]+")":"");
  var summary="The "+e[0]+" ("+e[1]+"). "+e[2]+" "+asp[1]+ang[2];
  var details={era:e[0],span:e[1],note:e[2],aspect:asp[0]};
  return mkRec(seed,"era",title,summary,details,"sourced",SRC);
}
function genFieldNote(seed,s,rnd){
  var j=s,TL=TAXA.length;
  var t=TAXA[(j*17)%TL];
  var nt=NOTE_TYPES[j%8];
  var v=Math.floor(j/(TL*8))%2;
  var title="Field note: "+t[1]+(v?" (II)":"");
  var summary="Signature-generated study note \u2014 homegrown material whose facts come from the curated dataset. "+
    "Subject: "+t[1]+" ("+t[0]+"), a "+t[6]+" "+t[2]+" of the "+t[3]+" ("+t[4]+") from "+t[5]+", reaching "+t[7]+". "+
    "Note type: "+nt+". "+t[8]+(v?" A second look at the same animal, for comparison across notes.":"");
  var details={subject:t[1],scientific_name:t[0],note_type:nt,pass:v+1,
    observations:[identity(t),t[8],"Recorded as Signature study material, not a new fossil claim."]};
  return mkRec(seed,"field-note",title,summary,details,"signature",SIGSRC);
}
function genHypo(seed,s,rnd){
  var j=s,TL=TAXA.length;
  var t=TAXA[(j*31)%TL];
  var sc=SCEN[j%10];
  var title="What if: "+t[1]+" \u2014 "+sc[0];
  var summary="A Signature boundless speculation \u2014 not a real fossil claim. The real animal: "+identity(t)+" "+
    "Now "+sc[1]+". This is an imagination exercise in the archive's style; every real fact above stays as science knows it.";
  var details={subject:t[1],scientific_name:t[0],real_facts:taxonDetail(t),scenario:sc[0],speculation:sc[1]};
  return mkRec(seed,"hypothetical",title,summary,details,"signature",SIGSRC);
}
function generate(seed,opts,rnd){
  opts=opts||{};rnd=rnd||prng(seed);
  var s=((seed-1)%10000)+1;
  var explicit=!!opts.category;
  var cat=opts.category;
  if(!cat){
    if(s<=5200)cat="taxon-profile";
    else if(s<=6400)cat="comparison";
    else if(s<=7400)cat="dig-site";
    else if(s<=7900)cat="era";
    else if(s<=9000)cat="field-note";
    else cat="hypothetical";
  }
  /* explicit category from the Generator tab: index from s-1 so any seed works */
  function ord(base){return explicit?(s-1):(s-base);}
  var taxonCats=["dinosaur","marine-reptile","flying-reptile","prehistoric-mammal","invertebrate","plant","ancient-reptile"];
  if(cat==="taxon-profile")return genProfile(seed,ord(1),rnd,null);
  if(taxonCats.indexOf(cat)>=0)return genProfile(seed,ord(1),rnd,cat);
  if(cat==="comparison")return genCompare(seed,ord(5201),rnd);
  if(cat==="dig-site")return genSite(seed,ord(6401),rnd);
  if(cat==="era")return genEra(seed,ord(7401),rnd);
  if(cat==="field-note")return genFieldNote(seed,ord(7901),rnd);
  if(cat==="hypothetical")return genHypo(seed,ord(9001),rnd);
  return genProfile(seed,ord(1),rnd);
}
function validate(r){
  var e=[];
  if(!r||typeof r!=="object")return {ok:false,errors:["not an object"]};
  if(!/^JAH-PAL-\d{6,7}$/.test(r.id||""))e.push("id");
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
var gen={version:"jahdb-paleontology-1.0",generate:generate,validate:validate,driftCheck:driftCheck,categories:CATS};
if(typeof JAHDB!=="undefined"&&JAHDB.registerGenerator)JAHDB.registerGenerator("paleontology",gen);
if(typeof module!=="undefined"&&module.exports)module.exports=gen;
})();
