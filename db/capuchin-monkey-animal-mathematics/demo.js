// Demo for capuchin-monkey-animal-mathematics — executed program. Prints the capuchin monkey's own measurements.
"use strict";
const LESSER_G = 100;
const MALE_KG = 3.5;
const FEMALE_KG = 2.5;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Capuchin Monkey mathematics");
console.log("Animal: capuchin monkey (Cebus capucinus and Sapajus apella)");
console.log("Court: the Chirp court");
console.log("Lesser unit: one pygmy marmoset = 100 g");
console.log("Adult male 3.5 kg = " + inUnits(MALE_KG) + " pygmy marmoset units");
console.log("Adult female 2.5 kg = " + inUnits(FEMALE_KG) + " pygmy marmoset units");
console.log("Human 70 kg = " + inUnits(70) + " pygmy marmoset units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
