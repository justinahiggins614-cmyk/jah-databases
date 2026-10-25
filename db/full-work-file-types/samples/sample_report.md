# Completeness Audit of Full-Work File Types

## Executive summary

This report presents the findings of a completeness audit of one hundred full-work file types, covering documents, software, datasets, designs, media, and archival packages. The audit asked one question of every type: what must be present for a work of that type to count as complete and usable, rather than as a fragment, a summary, or a description of a work that does not yet exist. The answer, for every type, is a checklist, a validator, and a reconstruction method, recorded alongside a fifteen-field artifact record. The headline finding is reassuring and demanding in equal measure. Reassuring, because every type examined can be made complete with ordinary tools and ordinary care. Demanding, because completeness is a property of the whole work, and a single missing part, a single broken reference, or a single unchecked hash is enough to fail it.

## Findings

First, completeness is structural before it is stylistic. A beautifully written report with no methodology section is incomplete. A program that runs on its author's machine but has no entry point, no usage instructions, and no test is incomplete. A dataset with fifty rows and no units, no provenance, and no statement of how missing values are marked is incomplete, however clean the fifty rows may be. In each case the missing part is not a polish issue. It is the part that lets the next reader use the work without the author's help, and without that part the work cannot stand on its own.

Second, the fifteen-field artifact record is what turns a checklist into an auditable claim. The identifier, the format, the file location, the schema version, the generator, the dependencies, the source records, the creation date, the content hash, the validation status, the reconstruction instructions, and the rights statement together answer every question a future reader will ask first: what is this, where does it live, what does it need, what was it built from, when was it made, has it been checked, and how do I rebuild it. A record with any field empty is not a record of a complete work. It is a note that the work has not yet been finished.

Third, validators must be runnable, not merely described. This audit includes a runnable validator program, and the validator was executed against the sample works that accompany the audit. The program sample passed its five built-in tests. The dataset sample passed a check that every row has six fields, that every latitude lies between minus ninety and ninety, that every longitude lies between minus one hundred and eighty and one hundred and eighty, and that every population is a positive integer. The report sample passed a check that its findings, data, methodology, recommendations, appendices, and references sections are all present and non-empty. A validator that has never been run is a claim, not a check, and this audit treats the two differently.

Fourth, formats matter, and masters matter more than copies. Every type has a master format from which distribution copies are derived, and the audit records which format is the master. When a master and a copy disagree, the master governs, and the copy is rebuilt. When no master is recorded, disagreement cannot be resolved, and the work drifts. Recording the master is a small administrative act with large practical consequences, and it is required for every type in this reference.

## Data

The audit covers one hundred types, listed in order in the accompanying database. Three sample works accompany the audit and demonstrate the standard in practice: a runnable program with an entry point, usage instructions, and passing tests; a dataset of sixty cities with country, latitude in degrees, longitude in degrees, and population in persons, with a stated edition column and a missing-value convention of leaving a field empty only where a value is genuinely unknown and documenting that choice; and this report itself, which is the third sample. The dataset contains no missing values, because every city listed has a recorded country, coordinate pair, and population figure, and that fact is itself recorded so that a reader does not have to guess whether missing values were hidden or simply absent.

## Methodology

The method was the same for every type. First, the type was described in plain language, stating what a work of that type is for and who will use it. Second, the formats in which such a work can be stored were listed, with the master format identified. Third, a completeness checklist was written, stating every part a complete work of that type must contain. Fourth, a validator was described that checks each checklist item and reports pass or fail with a failure list. Fifth, a reconstruction method was written in plain steps. Sixth, the fifteen-field artifact standard was applied field by field to the type. A type was recorded as audited only when all six steps were complete and written in full prose.

## Recommendations

One, adopt the checklist, validator, and reconstruction method as a single unit. A checklist without a validator is a wish. A validator without reconstruction steps is a gate with no door. Two, keep the Markdown or plain-text source as the master for text works, and the source tree as the master for software works, and derive all other formats from the master. Three, record a content hash at the moment a work is declared complete, and re-check the hash whenever the work is copied. Four, never declare a work complete on the basis of its best parts. Declare it complete only when the validator passes on the whole work. Five, when a work fails validation, publish the failure list alongside the work, so that the next builder knows exactly what remains to be done.

## Appendices

### Appendix A: Checklist summary

The checklist for every type requires a title and purpose, the full content in reading order, front matter or header information, navigation aids, supporting material such as references or a data dictionary, and a closing statement of limits, sources, and future revision. The validator confirms the presence and non-emptiness of each required part, the resolution of internal references, and the match of recorded and recomputed hashes.

### Appendix B: Validation results for the sample works

The program sample passed all five built-in tests. The dataset sample passed all row, range, and field-count checks across sixty rows. This report sample passed the section-presence check for findings, data, methodology, recommendations, appendices, and references. All three sample artifact records carry a recorded SHA-256 hash computed from the stored file and a validation status of passed.

## References

Complete Works Reference, Full-Work File Types Database, 2026. Book Types Reference, 100 Book Types Database, 2026. Signature System Standards, completeness and reconstruction notes, 2026. Open archival practice for content hashes, manifests, and format masters, as applied in this audit.
