// Demo for mouse-lemur-animal-mathematics — executed program. Prints the mouse lemur's own measurements.
"use strict";
const LESSER_G = 30;
const MALE_KG = 0.06;
const FEMALE_KG = 0.06;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Mouse Lemur mathematics");
console.log("Animal: mouse lemur (Microcebus murinus)");
console.log("Court: the Squeak court");
console.log("Lesser unit: one pygmy mouse lemur = 30 g");
console.log("Adult male 0.06 kg = " + inUnits(MALE_KG) + " pygmy mouse lemur units");
console.log("Adult female 0.06 kg = " + inUnits(FEMALE_KG) + " pygmy mouse lemur units");
console.log("Human 70 kg = " + inUnits(70) + " pygmy mouse lemur units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
