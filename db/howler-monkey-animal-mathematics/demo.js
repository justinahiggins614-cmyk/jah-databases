// Demo for howler-monkey-animal-mathematics — executed program. Prints the howler monkey's own measurements.
"use strict";
const LESSER_G = 800;
const MALE_KG = 7;
const FEMALE_KG = 5.5;
function inUnits(kg) { return (kg * 1000 / LESSER_G).toFixed(0); }
console.log("DEMO: Howler Monkey mathematics");
console.log("Animal: howler monkey (Alouatta palliata and Alouatta seniculus)");
console.log("Court: the Howl court");
console.log("Lesser unit: one squirrel monkey = 800 g");
console.log("Adult male 7 kg = " + inUnits(MALE_KG) + " squirrel monkey units");
console.log("Adult female 5.5 kg = " + inUnits(FEMALE_KG) + " squirrel monkey units");
console.log("Human 70 kg = " + inUnits(70) + " squirrel monkey units");
console.log("Hierarchy: God supreme; humanity highest earthly authority under God; this animal supreme in its own system, subject to no other animal; Signature the shared foundation.");
console.log("Court recognition: NOT automatic; the local human court decides.");
console.log("DEMO OK");
