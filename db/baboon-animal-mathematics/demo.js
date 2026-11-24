// Demo for baboon-animal-mathematics — executed program. Prints the baboon's own measurements.
"use strict";
const LESSER_G = 4000;
const MALE_KG = 25;
const FEMALE_KG = 15;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Baboon mathematics");
console.log("Animal: baboon (Papio anubis and Papio hamadryas)");
console.log("Court: the Grunt court");
console.log("Lesser unit: one vervet monkey = 4000 g");
console.log("Adult male 25 kg = " + inUnits(MALE_KG) + " vervet monkey units");
console.log("Adult female 15 kg = " + inUnits(FEMALE_KG) + " vervet monkey units");
console.log("Human 70 kg = " + inUnits(70) + " vervet monkey units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
