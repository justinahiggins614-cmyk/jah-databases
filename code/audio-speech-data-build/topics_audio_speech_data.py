#!/usr/bin/env python3
"""Topics + config for the audio-speech-data pair. Property of Justin Addam Higgins (JAH)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "audio-speech-data",
    "name_pub": "The Audio Speech Data Database",
    "name_sig": "Signature Audio Speech Data Database",
    "tagline_pub": ("Audio speech data from the ground up: how sound becomes data, speech corpora "
                    "with aligned transcripts, speaker diarization and separation, acoustic "
                    "analysis, feature extraction, and dataset stewardship - every record carrying "
                    "the full entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of audio speech data: the same "
                    "real speech-data knowledge carried forward, plus Signature-built corpus "
                    "pipelines, analysis frameworks, and dataset systems original to this system."),
    "record_kind": "audio speech data record",
    "record_kind_plural": "audio speech data records",
    "prefix_pub": "JAH-SPAU-", "prefix_sig": "JAH-SPAUS-",
    "ai_pub": "JAH Audio Speech Data Archivist",
    "ai_sig": "JAH Signature Audio Speech Data Creator",
    "role_pub": ("audio speech data archivist - teaching sound capture, corpora, transcripts, "
                 "diarization, acoustic analysis, and datasets; answers from many angles - "
                 "definition, example, process, analysis, stewardship - using only archive data "
                 "from this system"),
    "role_sig": ("Signature creator of audio speech data systems - designing corpus pipelines, "
                 "analysis frameworks, and dataset systems as original Signature works; answers "
                 "from many angles using only archive data from this system"),
    "search_ph": "Search corpora, transcripts, diarization, acoustics, features...",
    "chat_ph": "Ask about audio speech data...",
    "greet_pub": ("I am the JAH Audio Speech Data Archivist. Ask me about speech corpora, "
                  "transcripts, diarization, acoustic analysis, and datasets."),
    "greet_sig": ("I am the JAH Signature Audio Speech Data Creator. Ask me about "
                  "Signature-built speech data systems."),
    "gen_blurb": ("Generate clearly-labeled audio speech data studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded audio speech data records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced."),
    "demo_kind": "speech-data-demo",
    "demo_title": "Audio Speech Data Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Audio Speech Data Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "wave":
        return fill(
            "import math\n"
            "sr = @@SR@@\ndur = @@DUR@@\nfreq = @@FREQ@@\n"
            "n = int(sr * dur)\n"
            "sig = [math.sin(2 * math.pi * freq * i / sr) for i in range(n)]\n"
            "zc = sum(1 for i in range(1, n) if sig[i-1] * sig[i] < 0)\n"
            "peak = max(abs(s) for s in sig)\n"
            "print('Synthesized %.1fs tone at %d Hz, %d Hz sample rate' % (dur, freq, sr))\n"
            "print('Samples:', n, ' Peak amplitude: %.3f' % peak)\n"
            "print('Zero crossings:', zc, '(expected ~%d)' % int(2 * freq * dur))\n",
            {"SR": p["sr"], "DUR": p["dur"], "FREQ": p["freq"]})
    if v == "vad":
        return fill(
            "import math\n"
            "frames = @@FRAMES@@\n"
            "thresh = @@THRESH@@\n"
            "speech = [i for i, e in enumerate(frames) if e > thresh]\n"
            "print('Frames:', len(frames), ' Energy threshold:', thresh)\n"
            "print('Speech frames:', len(speech), 'of', len(frames))\n"
            "print('Speech ratio: %.2f' % (len(speech) / len(frames)))\n",
            {"FRAMES": p["frames"], "THRESH": p["thresh"]})
    if v == "diarize":
        return fill(
            "segs = @@SEGS@@\n"
            "merged = []\n"
            "for s in sorted(segs, key=lambda x: x['start']):\n"
            "    if merged and merged[-1]['speaker'] == s['speaker'] and s['start'] - merged[-1]['end'] < 0.5:\n"
            "        merged[-1]['end'] = max(merged[-1]['end'], s['end'])\n"
            "    else:\n"
            "        merged.append(dict(s))\n"
            "print('Raw segments:', len(segs), ' Merged turns:', len(merged))\n"
            "for m in merged:\n"
            "    print(' %s: %.1f-%.1fs' % (m['speaker'], m['start'], m['end']))\n",
            {"SEGS": p["segments"]})
    if v == "align":
        return fill(
            "words = @@WORDS@@\n"
            "offset = @@OFFSET@@\n"
            "print('Forced alignment with offset %.2fs:' % offset)\n"
            "for w in words:\n"
            "    print(' %-8s %.2f - %.2f' % (w['word'], w['start'] + offset, w['end'] + offset))\n"
            "dur = max(w['end'] for w in words) + offset\n"
            "print('Utterance duration: %.2fs' % dur)\n",
            {"WORDS": p["words"], "OFFSET": p["offset"]})
    if v == "features":
        return fill(
            "import math\n"
            "frames = @@FRAMES@@\n"
            "means = [sum(f) / len(f) for f in frames]\n"
            "overall = sum(means) / len(means)\n"
            "var = sum((m - overall) ** 2 for m in means) / len(means)\n"
            "print('Frames:', len(frames), ' Coeffs per frame:', len(frames[0]))\n"
            "print('Mean feature value: %.4f' % overall)\n"
            "print('Variance across frames: %.4f' % var)\n",
            {"FRAMES": p["frames"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta < 0 and 'gap' in label.lower() else ('improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged'))\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Audio Speech Data Is", tier=F,
 desc_pub=("Audio speech data is recorded human speech stored as digital data for analysis, "
  "training, and research: voice recordings paired with information about speakers, "
  "transcripts, and recording conditions. It powers speech recognition, voice assistants, "
  "captioning, speaker verification, and linguistic research.\n"
  "A speech dataset is more than audio files: it includes aligned transcripts, speaker "
  "labels, demographic metadata, and documentation of consent and licensing. Quality data - "
  "clean recordings, accurate transcripts - determines everything built on it."),
 desc_sig=("The Signature system treats speech data as a managed asset with lineage: every "
  "recording carries its provenance, processing history, and consent record - so datasets are "
  "auditable from collection to model."),
 how_pub=("Recordings are captured with suitable microphones in controlled conditions, "
  "transcribed (human or machine-verified), segmented by speaker, and annotated with metadata. "
  "Quality checks verify audio clarity and transcript accuracy before the data joins a "
  "corpus."),
 how_sig=("Signature lineage tracking attaches provenance and consent to every recording "
  "automatically."),
 keys=["Recorded speech as digital data",
  "Powers recognition, assistants, captioning, verification",
  "Dataset = audio + transcripts + speaker labels + metadata",
  "Consent and licensing documented",
  "Quality data determines everything built on it",
  "Clean recordings, accurate transcripts"],
 reqs=["Recording equipment and protocols",
  "Transcription workflow",
  "Metadata and consent documentation"],
 stds=["Speech data documentation standards (public literature)"],
 cites=["Linguistic Data Consortium — public resources (public)"],
 demo=("wave", {"sr": 16000, "dur": 0.5, "freq": 440})),

dict(title="How Sound Becomes Data", tier=F,
 desc_pub=("Sound becomes data through digitization: a microphone converts air pressure waves to "
  "electrical signals; an analog-to-digital converter samples the signal thousands of times per "
  "second, measuring amplitude at each sample. The sample rate (samples/second) and bit depth "
  "(measurement precision) define fidelity.\n"
  "The Nyquist rule: sample at least twice the highest frequency you want to capture. Human "
  "speech's key content sits below 8 kHz, so 16 kHz sampling is the speech-data standard."),
 desc_sig=("Signature capture standards specify sample rate, bit depth, and calibration per use "
  "case, so recordings are fit for purpose from the first sample."),
 how_pub=("Choose sample rate and bit depth for the task (16 kHz/16-bit for speech), calibrate "
  "levels to avoid clipping, record in quiet conditions, and store losslessly (WAV/FLAC) for "
  "archival masters. Verify with waveform and spectrum inspection."),
 how_sig=("Signature capture checklists enforce standards before recording begins."),
 keys=["Microphone: pressure to electrical signal",
  "ADC: samples amplitude thousands of times/second",
  "Sample rate and bit depth define fidelity",
  "Nyquist: sample 2x the highest frequency",
  "16 kHz standard for speech",
  "Store masters losslessly"],
 reqs=["Calibrated recording chain",
  "Standard sample rate/bit depth",
  "Lossless archival storage"],
 stds=["Audio engineering standards (AES, public)"],
 cites=["Audio Engineering Society — public resources (public)"],
 demo=("wave", {"sr": 16000, "dur": 1.0, "freq": 220})),

dict(title="Sampling and Bit Depth", tier=F,
 desc_pub=("Sampling rate sets the highest capturable frequency (half the rate); bit depth sets "
  "dynamic range - 16-bit gives ~96 dB, enough for speech with headroom. Higher rates (48 kHz) "
  "suit music and archival; higher depths (24-bit) ease level-setting.\n"
  "Trade-offs: higher rates/depths mean larger files. For speech recognition, 16 kHz/16-bit "
  "mono is the sweet spot - adequate fidelity, manageable size, universal tool support."),
 desc_sig=("Signature format policy matches rate and depth to each dataset's purpose, "
  "documenting the choice so future users understand the fidelity contract."),
 how_pub=("Select rate/depth per purpose, set levels peaking around -12 dBFS for headroom, and "
  "document the format in dataset metadata. Downsample only from higher-quality masters, never "
  "up-sample to fake quality."),
 how_sig=("Signature fidelity contracts document every dataset's rate/depth rationale."),
 keys=["Rate: max frequency = half the rate",
  "Depth: dynamic range (16-bit ~96 dB)",
  "16 kHz/16-bit mono: speech sweet spot",
  "Higher for music/archival",
  "Set levels with headroom (-12 dBFS)",
  "Document format in metadata"],
 reqs=["Format selection per purpose",
  "Level-setting discipline",
  "Metadata documentation"],
 stds=["Broadcast/archival audio standards (public)"],
 cites=["Audio Engineering Society — standards (public)"],
 demo=("wave", {"sr": 8000, "dur": 0.5, "freq": 880})),

dict(title="Audio File Formats", tier=F,
 desc_pub=("Audio formats serve different roles: WAV (uncompressed, universal), FLAC (lossless "
  "compressed, archival favorite), MP3/AAC (lossy, small - fine for distribution, never for "
  "masters), and Opus (modern low-bitrate speech codec).\n"
  "Rule: archive masters losslessly, distribute lossily. Transcoding lossy-to-lossy degrades; "
  "always derive distributions from the lossless master."),
 desc_sig=("Signature format pipelines enforce master-lossless policy with automated derivation "
  "of distribution formats, so quality discipline is built in."),
 how_pub=("Record and archive in WAV/FLAC; derive MP3/AAC/Opus copies for distribution or "
  "streaming. Document the format chain in metadata; never up-transcode lossy sources as if "
  "they were masters."),
 how_sig=("Signature automated derivation keeps masters pristine and distributions current."),
 keys=["WAV: uncompressed; FLAC: lossless compressed",
  "MP3/AAC: lossy distribution; Opus: modern speech",
  "Archive losslessly, distribute lossily",
  "Never derive masters from lossy sources",
  "Document the format chain",
  "Format affects file size hugely"],
 reqs=["Lossless archival storage",
  "Transcoding workflow",
  "Format documentation"],
 stds=["Archival audio format guidance (public, e.g., IASA)"],
 cites=["International Association of Sound Archives — guidance (public)"],
 demo=("features", {"frames": [
   [0.1, 0.2, 0.15], [0.3, 0.25, 0.2], [0.12, 0.18, 0.22], [0.28, 0.3, 0.26]]})),

dict(title="Speech vs Non-Speech Audio", tier=F,
 desc_pub=("Speech data work starts by separating speech from everything else: voice activity "
  "detection (VAD) classifies frames as speech or silence/noise using energy, zero-crossing "
  "rate, or learned models. Music, background chatter, and machinery each need different "
  "handling.\n"
  "Clean segmentation improves everything downstream: recognition accuracy, diarization, and "
  "transcript alignment all assume they are processing speech."),
 desc_sig=("Signature segmentation pipelines combine energy, spectral, and learned VAD with "
  "confidence scores, so downstream stages know each segment's reliability."),
 how_pub=("Apply VAD to recordings, tune thresholds on representative data, and verify on "
  "samples - especially noisy or overlapped regions. Segment boundaries feed transcription "
  "and diarization stages."),
 how_sig=("Signature confidence-scored segmentation lets downstream stages weight segments "
  "by reliability."),
 keys=["VAD classifies speech vs silence/noise",
  "Energy, zero-crossing, learned models",
  "Music and machinery need different handling",
  "Segmentation improves all downstream tasks",
  "Tune thresholds on representative data",
  "Verify on noisy samples"],
 reqs=["VAD tooling",
  "Representative tuning data",
  "Verification sampling"],
 stds=["VAD evaluation practices (public literature)"],
 cites=["International Speech Communication Association — public resources (public)"],
 demo=("vad", {"frames": [0.02, 0.03, 0.45, 0.62, 0.51, 0.04, 0.02, 0.38, 0.55, 0.03],
   "thresh": 0.1})),

dict(title="Transcripts and Alignment Basics", tier=F,
 desc_pub=("Transcripts are written records of speech; alignment maps each word to its time in "
  "the audio. Together they enable search ('find where she said...'), captioning, and training "
  "recognition systems.\n"
  "Alignment can be manual (precise, slow) or forced (automatic: given audio + transcript, find "
  "word times). Quality is measured in word error rate for transcripts and boundary accuracy "
  "for alignment."),
 desc_sig=("Signature transcript pipelines pair human and machine transcription with "
  "adjudication, producing aligned, verified transcripts at scale."),
 how_pub=("Transcribe per conventions (verbatim vs cleaned), then force-align with acoustic "
  "models; spot-check boundaries on samples. Store transcripts with word-level timestamps in "
  "standard formats (TextGrid, JSON, SRT/VTT for captions)."),
 how_sig=("Signature adjudication workflows combine human and machine strengths for "
  "verified alignment."),
 keys=["Transcripts: what was said; alignment: when",
  "Enable search, captioning, training",
  "Manual: precise; forced: automatic",
  "Word error rate measures transcripts",
  "Boundary accuracy measures alignment",
  "Store with word-level timestamps"],
 reqs=["Transcription conventions",
  "Forced-alignment tooling",
  "Quality spot-checking"],
 stds=["Transcription convention guidance (public literature)"],
 cites=["Linguistic Data Consortium — transcription (public)"],
 demo=("align", {"words": [
   {"word": "hello", "start": 0.0, "end": 0.4},
   {"word": "world", "start": 0.5, "end": 0.9},
   {"word": "today", "start": 1.0, "end": 1.5}], "offset": 2.0})),

dict(title="What a Speech Corpus Is", tier=F,
 desc_pub=("A speech corpus is a curated collection of speech data designed for a purpose: "
  "training recognizers (thousands of hours, diverse speakers), linguistic research (annotated "
  "phenomena), or benchmarking (fixed test sets). Famous examples: LibriSpeech (audiobooks), "
  "Common Voice (crowdsourced multilingual), TIMIT (phonetically balanced).\n"
  "Corpus design balances size, diversity (accents, ages, channels), annotation depth, and "
  "licensing. Documentation - the 'datasheet' - describes all of it."),
 desc_sig=("Signature corpus design starts from the datasheet: purpose, population, "
  "annotation, and licensing defined before the first recording."),
 how_pub=("Define the corpus purpose and target population, design collection protocols "
  "(prompts, conditions), recruit diverse speakers with consent, record and transcribe to "
  "standard, quality-check, and publish with documentation and license."),
 how_sig=("Signature datasheet-first design prevents the common failure of collecting data "
  "before knowing its purpose."),
 keys=["Curated collections designed for a purpose",
  "Training, research, benchmarking uses",
  "LibriSpeech, Common Voice, TIMIT examples",
  "Balance size, diversity, annotation, licensing",
  "Documentation via datasheets",
  "Design before collecting"],
 reqs=["Corpus design document",
  "Diverse speaker recruitment",
  "Datasheet publication"],
 stds=["Datasheets for Datasets framework (public)"],
 cites=["Mozilla Common Voice — public dataset (public)",
  "Linguistic Data Consortium (public)"],
 demo=("vad", {"frames": [0.5, 0.6, 0.02, 0.03, 0.55, 0.48, 0.02, 0.61, 0.02, 0.03, 0.52],
   "thresh": 0.1})),

dict(title="Recording Quality Basics", tier=F,
 desc_pub=("Recording quality determines data value: quiet environment (low background noise), "
  "appropriate microphone distance (consistent level), no clipping (peaks below 0 dBFS), and "
  "minimal reverberation (soft furnishings beat bare rooms).\n"
  "Checklist before recording: test levels with the actual speaker, listen on headphones, "
  "verify no hums or dropouts, and record a few seconds of room tone for noise profiling."),
 desc_sig=("Signature quality gates check recordings automatically on ingest - levels, noise "
  "floor, clipping - rejecting or flagging substandard takes immediately."),
 how_pub=("Set up in the quietest available space, position microphones consistently, test "
  "levels with the speaker's natural voice, record room tone, and monitor the first minutes. "
  "Log any issues per take."),
 how_sig=("Signature automated ingest checks catch quality problems at capture, not months "
  "later."),
 keys=["Quiet environment; consistent mic distance",
  "No clipping; minimal reverb",
  "Test levels with the actual speaker",
  "Record room tone",
  "Monitor first minutes",
  "Log issues per take"],
 reqs=["Suitable recording space",
  "Monitoring headphones",
  "Quality checklist"],
 stds=["Speech recording best practices (public literature)"],
 cites=["Audio Engineering Society — recording guidance (public)"],
 demo=("wave", {"sr": 16000, "dur": 0.25, "freq": 330})),

dict(title="Microphones for Speech Capture", tier=F,
 desc_pub=("Microphone choice shapes speech data: headset mics (consistent distance, great for "
  "recognition), lavalier/lapel mics (discreet, good for interviews), shotgun mics (distance "
  "with directionality), and USB condenser mics (convenient for crowdsourced collection).\n"
  "Polar patterns matter: cardioid rejects rear noise; omnidirectional captures rooms. Match "
  "mic to task, keep placement consistent, and document the chain."),
 desc_sig=("Signature capture specifications prescribe microphone type and placement per "
  "collection scenario, so datasets are comparable."),
 how_pub=("Select mics for the scenario, place consistently (headset: corner of mouth; lav: "
  "chest), test with the speaker, and document mic model and placement in metadata. Calibrate "
  "levels per session."),
 how_sig=("Signature scenario-specified capture keeps multi-site collections consistent."),
 keys=["Headset, lavalier, shotgun, USB condenser",
  "Cardioid rejects rear noise",
  "Match mic to task",
  "Consistent placement",
  "Document mic and placement",
  "Calibrate per session"],
 reqs=["Scenario-appropriate microphones",
  "Placement protocols",
  "Metadata documentation"],
 stds=["Microphone specification standards (public)"],
 cites=["Audio Engineering Society — microphones (public)"],
 demo=("features", {"frames": [
   [0.5, 0.4, 0.45], [0.52, 0.41, 0.44], [0.2, 0.15, 0.18], [0.51, 0.42, 0.46]]})),

dict(title="Noise and Room Acoustics", tier=F,
 desc_pub=("Rooms color recordings: reverberation smears speech, HVAC hums add noise, and "
  "outside sounds intrude. Treat the space (soft furnishings, closed doors), choose quiet "
  "times, and measure the noise floor before sessions.\n"
  "Noise profiling - capturing room tone - enables spectral subtraction in post. But no "
  "processing fully rescues bad acoustics: capture clean first."),
 desc_sig=("Signature acoustic standards set maximum noise floors and reverb times per "
  "collection type, verified before sessions."),
 how_pub=("Survey the room for noise sources, treat with available materials, record room tone, "
  "and monitor levels. Document acoustic conditions; apply noise reduction sparingly in post, "
  "preferring clean capture."),
 how_sig=("Signature pre-session acoustic verification prevents unusable recordings."),
 keys=["Reverb smears; hums and intrusions add noise",
  "Treat space; choose quiet times",
  "Measure noise floor first",
  "Room tone enables noise profiling",
  "Capture clean beats processing",
  "Document conditions"],
 reqs=["Acoustic survey",
  "Treatment materials",
  "Noise floor measurement"],
 stds=["Room acoustics guidance (public literature)"],
 cites=["Audio Engineering Society — acoustics (public)"],
 demo=("vad", {"frames": [0.15, 0.16, 0.5, 0.55, 0.14, 0.52, 0.15, 0.16],
   "thresh": 0.2})),

dict(title="Metadata for Speech Recordings", tier=F,
 desc_pub=("Metadata makes recordings usable: speaker ID (pseudonymized), demographics "
  "(age band, accent/region, gender as relevant), recording conditions (mic, room, date), "
  "transcript status, and consent/license identifiers.\n"
  "Privacy matters: strip direct identifiers, aggregate sensitive demographics, and store "
  "consent records securely. Good metadata is what separates a pile of audio from a "
  "research corpus."),
 desc_sig=("Signature metadata schemas enforce completeness at ingest - no recording enters "
  "the corpus without its metadata and consent record."),
 how_pub=("Define the schema before collection, capture metadata at recording time (not "
  "later), pseudonymize speaker IDs, and validate completeness on ingest. Publish a data "
  "dictionary with the corpus."),
 how_sig=("Signature ingest validation rejects metadata-incomplete recordings automatically."),
 keys=["Speaker, demographics, conditions, transcript status, consent",
  "Pseudonymize speaker IDs",
  "Capture at recording time",
  "Privacy: strip identifiers",
  "Data dictionary published",
  "Metadata separates corpus from pile"],
 reqs=["Metadata schema",
  "Pseudonymization process",
  "Ingest validation"],
 stds=["Metadata standards (public, e.g., Dublin Core extensions)"],
 cites=["Linguistic Data Consortium — metadata (public)"],
 demo=("diarize", {"segments": [
   {"speaker": "SPK1", "start": 0.0, "end": 2.1},
   {"speaker": "SPK1", "start": 2.3, "end": 4.0},
   {"speaker": "SPK2", "start": 4.5, "end": 6.2}]})),

# ---------------- Compounded (12) ----------------
dict(title="Building a Speech Corpus", tier=C,
 desc_pub=("Building a corpus is project management for data: define purpose and specs, design "
  "prompts (read sentences, spontaneous tasks), recruit diverse speakers with informed consent, "
  "record to standard, transcribe and annotate, quality-check, and publish with documentation "
  "and license.\n"
  "Budget realistically: transcription and annotation dominate costs, often exceeding "
  "recording. Pilot everything - prompts, workflow, tools - before scaling."),
 desc_sig=("Signature corpus builds run on staged pipelines with quality gates between "
  "stages, so problems surface early when they are cheap to fix."),
 how_pub=("Write the corpus specification, pilot collection with a small cohort, refine "
  "prompts and workflows, then scale recording. Transcribe with adjudication, annotate per "
  "guidelines, sample-check quality, and release with datasheet and license."),
 how_sig=("Signature stage-gated pipelines catch design flaws in the pilot, not at hour "
  "1,000."),
 keys=["Purpose and specs first",
  "Prompts: read + spontaneous",
  "Diverse speakers, informed consent",
  "Transcription dominates costs",
  "Pilot before scaling",
  "Publish with datasheet and license"],
 reqs=["Corpus specification",
  "Pilot cohort",
  "Annotation guidelines"],
 stds=["Datasheets for Datasets (public)"],
 cites=["Linguistic Data Consortium — corpus building (public)"],
 demo=("align", {"words": [
   {"word": "the", "start": 0.1, "end": 0.25},
   {"word": "quick", "start": 0.3, "end": 0.55},
   {"word": "brown", "start": 0.6, "end": 0.9},
   {"word": "fox", "start": 0.95, "end": 1.2}], "offset": 0.0})),

dict(title="Transcription Conventions", tier=C,
 desc_pub=("Transcription conventions decide what gets written: verbatim (every um, repetition, "
  "false start) vs cleaned (fluent text); how to mark pauses, laughter, overlapping speech, "
  "and unintelligible regions; spelling of numbers and abbreviations.\n"
  "Consistency is the product: transcribers train on the convention guide, adjudicate "
  "disagreements, and inter-transcriber agreement is measured. The convention serves the "
  "corpus purpose - training data wants verbatim; captions want cleaned."),
 desc_sig=("Signature transcription operations version convention guides with adjudication "
  "workflows, so large teams stay consistent."),
 how_pub=("Write the convention guide for the corpus purpose, train transcribers with examples, "
  "double-transcribe samples for agreement measurement, adjudicate differences, and update "
  "the guide for edge cases encountered."),
 how_sig=("Signature versioned guides with agreement tracking keep distributed teams "
  "aligned."),
 keys=["Verbatim vs cleaned",
  "Mark pauses, laughter, overlap, unintelligible",
  "Consistency is the product",
  "Train on the guide; adjudicate disagreements",
  "Measure inter-transcriber agreement",
  "Convention serves corpus purpose"],
 reqs=["Convention guide",
  "Transcriber training",
  "Agreement measurement"],
 stds=["Transcription best practices (public literature)"],
 cites=["Linguistic Data Consortium — conventions (public)"],
 demo=("align", {"words": [
   {"word": "[um]", "start": 0.0, "end": 0.2},
   {"word": "I", "start": 0.25, "end": 0.35},
   {"word": "think", "start": 0.4, "end": 0.7}], "offset": 5.0})),

dict(title="Forced Alignment", tier=C,
 desc_pub=("Forced alignment automatically maps transcript words to audio times using acoustic "
  "models: given the audio and the known text, find each word's boundaries. Tools like the "
  "Montreal Forced Aligner handle this at scale.\n"
  "Quality depends on transcript accuracy and acoustic match - mismatched transcripts produce "
  "garbage boundaries. Always spot-check: misalignments cluster at noisy or overlapped "
  "regions."),
 desc_sig=("Signature alignment pipelines pair forced alignment with confidence scoring and "
  "targeted human review of low-confidence regions."),
 how_pub=("Prepare audio and transcripts in the aligner's expected format, run alignment with "
  "appropriate acoustic models, and sample-check boundaries - especially at utterance edges "
  "and noisy regions. Correct systematic errors by fixing transcripts or models."),
 how_sig=("Signature confidence-guided review focuses human effort where alignment is "
  "uncertain."),
 keys=["Audio + known text -> word times",
  "Montreal Forced Aligner and similar tools",
  "Transcript accuracy determines quality",
  "Spot-check noisy regions",
  "Mismatches produce garbage boundaries",
  "Fix transcripts or models for systematic errors"],
 reqs=["Aligned-format inputs",
  "Acoustic models",
  "Spot-check protocol"],
 stds=["Forced alignment tool documentation (public)"],
 cites=["Montreal Forced Aligner — public tool (public)"],
 demo=("align", {"words": [
   {"word": "forced", "start": 1.0, "end": 1.4},
   {"word": "alignment", "start": 1.45, "end": 2.1},
   {"word": "works", "start": 2.15, "end": 2.5}], "offset": 0.5})),

dict(title="Phonetic Annotation", tier=C,
 desc_pub=("Phonetic annotation transcribes speech sounds (phones) rather than words, using "
  "alphabets like IPA or ARPAbet: capturing pronunciation variation, accents, and sound "
  "changes that orthography hides.\n"
  "It powers pronunciation modeling for recognition and linguistic research. Annotation is "
  "specialist work requiring phonetic training; forced aligners with phone models can "
  "bootstrap the process."),
 desc_sig=("Signature phonetic pipelines combine specialist annotation with phone-level "
  "forced alignment, scaling expert-quality annotation."),
 how_pub=("Define the phone set for the language/variety, train annotators with examples, "
  "annotate samples manually, bootstrap with phone aligners, and adjudicate disagreements. "
  "Document the phone set with the corpus."),
 how_sig=("Signature phone-set documentation keeps annotation interpretable."),
 keys=["Phones, not words: IPA/ARPAbet",
  "Captures pronunciation variation",
  "Powers pronunciation modeling",
  "Specialist work; phonetic training needed",
  "Bootstrap with phone aligners",
  "Document the phone set"],
 reqs=["Defined phone set",
  "Trained annotators",
  "Adjudication process"],
 stds=["IPA conventions (public)"],
 cites=["International Phonetic Association (public)"],
 demo=("features", {"frames": [
   [0.8, 0.2, 0.1], [0.75, 0.25, 0.12], [0.2, 0.8, 0.3], [0.15, 0.85, 0.28]]})),

dict(title="Speaker Diarization", tier=C,
 desc_pub=("Speaker diarization answers 'who spoke when': segmenting audio by speaker turns "
  "without knowing the speakers in advance. Pipeline: voice activity detection, speaker "
  "embeddings (x-vectors) per segment, clustering embeddings into speaker groups, and "
  "resegmentation.\n"
  "Errors come from overlap (two speaking at once), short turns, and similar voices. "
  "Diarization error rate (DER) measures performance. It enables meeting transcription and "
  "broadcast analysis."),
 desc_sig=("Signature diarization pipelines add overlap handling and confidence scores, so "
  "downstream users know which turns are certain."),
 how_pub=("Run VAD, extract embeddings per segment, cluster into speakers, and resegment "
  "boundaries. Evaluate DER on labeled data; tune for the domain (meetings vs broadcast). "
  "Combine with transcripts for 'who said what'."),
 how_sig=("Signature confidence-scored turns let applications trust or verify each "
  "attribution."),
 keys=["Who spoke when, speakers unknown",
  "VAD, embeddings, clustering, resegmentation",
  "Overlap is the hard case",
  "DER measures performance",
  "Enables meeting/broadcast transcription",
  "Combine with transcripts"],
 reqs=["Diarization system",
  "Labeled evaluation data",
  "Domain tuning"],
 stds=["Diarization evaluation protocols (public, e.g., NIST)"],
 cites=["National Institute of Standards and Technology — diarization evaluations (public)"],
 demo=("diarize", {"segments": [
   {"speaker": "SPK_A", "start": 0.0, "end": 3.2},
   {"speaker": "SPK_A", "start": 3.4, "end": 5.1},
   {"speaker": "SPK_B", "start": 5.5, "end": 8.0},
   {"speaker": "SPK_A", "start": 8.2, "end": 9.0},
   {"speaker": "SPK_B", "start": 9.1, "end": 11.5}]})),

dict(title="Speaker Separation", tier=C,
 desc_pub=("Speaker separation (source separation) unmixes overlapped speech into individual "
  "streams: given a cocktail-party recording, produce each voice separately. Modern neural "
  "approaches (like Conv-TasNet) dramatically outperform classic beamforming on single-"
  "channel mixtures.\n"
  "Separation enables transcription of overlapped meetings and hearing-assist devices. "
  "Evaluation uses SI-SDR (scale-invariant signal-to-distortion ratio). It is distinct from "
  "diarization: separation produces audio; diarization produces labels."),
 desc_sig=("Signature separation workflows benchmark models per domain with SI-SDR, deploying "
  "the right model for each acoustic condition."),
 how_pub=("Select separation models trained for the domain, evaluate SI-SDR on representative "
  "mixtures, and integrate separated streams into transcription pipelines. Multi-microphone "
  "setups add beamforming gains where available."),
 how_sig=("Signature domain-benchmarked deployment matches models to conditions."),
 keys=["Unmix overlapped speech into streams",
  "Neural models beat classic on single-channel",
  "SI-SDR measures quality",
  "Separation produces audio; diarization labels",
  "Enables overlapped transcription",
  "Multi-mic adds beamforming"],
 reqs=["Separation models",
  "Domain evaluation data",
  "Integration with transcription"],
 stds=["Source separation evaluation (public, e.g., SI-SDR)"],
 cites=["International Speech Communication Association — public resources (public)"],
 demo=("wave", {"sr": 16000, "dur": 0.5, "freq": 660})),

dict(title="Acoustic Feature Extraction: MFCCs", tier=C,
 desc_pub=("MFCCs (Mel-frequency cepstral coefficients) are the classic speech features: take "
  "short frames (~25ms), compute spectra, warp to the mel scale (mimicking human hearing), take "
  "logs, and apply the discrete cosine transform. The resulting dozen coefficients compactly "
  "describe each frame's sound.\n"
  "Modern systems often use learned features or filterbanks instead, but MFCCs remain the "
  "teaching standard and a strong baseline. Deltas (change over time) add dynamics."),
 desc_sig=("Signature feature pipelines standardize extraction parameters with versioned "
  "configs, so experiments are reproducible."),
 how_pub=("Choose frame length/shift, compute filterbank energies, take logs and DCT, and "
  "append deltas. Normalize per utterance (cepstral mean normalization). Document every "
  "parameter - features are meaningless without their recipe."),
 how_sig=("Signature versioned feature configs make every experiment reproducible."),
 keys=["Frames, mel warp, log, DCT",
  "Dozen coefficients per frame",
  "Mimics human hearing",
  "Deltas add dynamics",
  "Teaching standard; strong baseline",
  "Document the recipe"],
 reqs=["Feature extraction library",
  "Parameter documentation",
  "Normalization"],
 stds=["Speech feature literature (public)"],
 cites=["International Speech Communication Association (public)"],
 demo=("features", {"frames": [
   [0.31, -0.12, 0.05], [0.33, -0.10, 0.06], [0.29, -0.14, 0.04],
   [0.35, -0.08, 0.07], [0.30, -0.11, 0.05]]})),

dict(title="Spectrograms and Waveforms", tier=C,
 desc_pub=("Waveforms show amplitude over time - good for spotting clipping and silence. "
  "Spectrograms show frequency over time (brightness = energy) - revealing formants (vowel "
  "resonances), frication noise, and pitch contours. Together they are the speech analyst's "
  "eyes.\n"
  "Reading spectrograms is a learned skill: vowels show formant bands, stops show gaps then "
  "bursts, fricatives show high-frequency noise. Visualization choices (window size) trade "
  "time vs frequency resolution."),
 desc_sig=("Signature visualization standards fix spectrogram parameters per analysis type, so "
  "analysts compare like with like."),
 how_pub=("Plot waveforms for level/clipping checks; compute spectrograms (choose window: "
  "narrowband for harmonics, wideband for formants); annotate regions of interest. Use "
  "consistent parameters within a project."),
 how_sig=("Signature standardized visualization parameters keep analyses comparable."),
 keys=["Waveform: amplitude over time",
  "Spectrogram: frequency over time",
  "Formants, frication, pitch visible",
  "Window size trades time/frequency resolution",
  "Reading spectrograms is learned",
  "Consistent parameters within projects"],
 reqs=["Visualization tooling",
  "Parameter standards",
  "Analyst training"],
 stds=["Speech analysis literature (public)"],
 cites=["International Speech Communication Association (public)"],
 demo=("wave", {"sr": 16000, "dur": 1.0, "freq": 110})),

dict(title="Speech Datasets for Recognition", tier=C,
 desc_pub=("Recognition datasets train and test speech-to-text: training sets (thousands of "
  "hours, diverse), development sets (tuning), and test sets (final measurement, never trained "
  "on). Word error rate (WER) on held-out tests is the headline metric.\n"
  "Diversity decides real-world performance: accents, ages, channels, and noise conditions in "
  "training must match deployment. Benchmarks like LibriSpeech enable fair comparison."),
 desc_sig=("Signature dataset curation tracks diversity coverage explicitly - accents, ages, "
  "channels - so training data matches deployment reality."),
 how_pub=("Assemble train/dev/test splits with no speaker overlap between test and train, "
  "document diversity coverage, and benchmark WER. Refresh test sets periodically to prevent "
  "overfitting to the benchmark."),
 how_sig=("Signature diversity-coverage tracking prevents the train-on-one-population, "
  "deploy-everywhere failure."),
 keys=["Train, dev, test splits",
  "No speaker overlap test/train",
  "WER on held-out tests",
  "Diversity must match deployment",
  "Benchmarks enable fair comparison",
  "Refresh tests to prevent overfitting"],
 reqs=["Split discipline",
  "Diversity documentation",
  "Benchmark harness"],
 stds=["Recognition evaluation protocols (public)"],
 cites=["National Institute of Standards and Technology — evaluations (public)"],
 demo=("vad", {"frames": [0.4, 0.45, 0.03, 0.5, 0.02, 0.48, 0.03, 0.44, 0.02, 0.02],
   "thresh": 0.1})),

dict(title="Multilingual Speech Data", tier=C,
 desc_pub=("Multilingual speech data covers many languages: collection must handle diverse "
  "phonologies, scripts, and sociolinguistics. Crowdsourced projects (Common Voice) scaled "
  "collection to 100+ languages; low-resource languages need targeted fieldwork.\n"
  "Challenges: orthography variation, code-switching, dialect continua, and annotator "
  "scarcity. Multilingual models share representations across languages, helping low-resource "
  "ones."),
 desc_sig=("Signature multilingual collection uses language-specific protocols within a common "
  "framework, balancing consistency with linguistic reality."),
 how_pub=("Prioritize languages by need, recruit native speakers with linguistic guidance, "
  "adapt prompts culturally, and validate with native listeners. Document language variety "
  "precisely (which dialect, which script)."),
 how_sig=("Signature variety-precise documentation prevents the 'Spanish' that is actually "
  "one dialect."),
 keys=["Diverse phonologies, scripts, sociolinguistics",
  "Common Voice: 100+ languages crowdsourced",
  "Low-resource languages need fieldwork",
  "Code-switching and dialects complicate",
  "Multilingual models help low-resource",
  "Document variety precisely"],
 reqs=["Native speaker recruitment",
  "Linguistic guidance per language",
  "Cultural prompt adaptation"],
 stds=["Multilingual collection guidance (public literature)"],
 cites=["Mozilla Common Voice (public)",
  "Linguistic Data Consortium (public)"],
 demo=("align", {"words": [
   {"word": "hola", "start": 0.0, "end": 0.4},
   {"word": "mundo", "start": 0.45, "end": 0.9}], "offset": 1.0})),

dict(title="Children's Speech Data", tier=C,
 desc_pub=("Children's speech differs acoustically (higher pitch, developing articulation) and "
  "practically (attention spans, consent via guardians, school partnerships). It is essential "
  "for educational technology and developmental research - and scarce.\n"
  "Collection needs child-appropriate protocols: short sessions, engaging tasks, guardian "
  "consent plus child assent, and extra privacy care. Annotation must handle developmental "
  "pronunciation."),
 desc_sig=("Signature children's collection pairs engagement-designed protocols with "
  "heightened privacy safeguards, so data is both useful and protected."),
 how_pub=("Partner with schools/families, design short engaging sessions, obtain guardian "
  "consent and child assent, record with patient protocols, and annotate with developmental "
  "awareness. Store with strict access controls."),
 how_sig=("Signature heightened safeguards reflect children's special privacy needs."),
 keys=["Higher pitch; developing articulation",
  "Essential for ed-tech; scarce",
  "Short engaging sessions",
  "Guardian consent + child assent",
  "Extra privacy care",
  "Developmental annotation awareness"],
 reqs=["School/family partnerships",
  "Child-appropriate protocols",
  "Strict access controls"],
 stds=["Research ethics for children (public)",
  "COPPA considerations (public law)"],
 cites=["U.S. Federal Trade Commission — COPPA (public)"],
 demo=("wave", {"sr": 16000, "dur": 0.5, "freq": 520})),

dict(title="Disordered Speech Data", tier=C,
 desc_pub=("Disordered speech data - dysarthria, aphasia, stuttering, voice disorders - enables "
  "assistive technology for people whose speech differs from typical patterns. It is scarce "
  "because collection is harder and populations smaller.\n"
  "Ethical collection centers the speakers: accessible protocols, fair compensation, and "
  "technology that serves them first. Personalized models (trained on the individual's speech) "
  "often outperform generic ones."),
 desc_sig=("Signature disordered-speech collection is co-designed with speaker communities, "
  "ensuring technology serves the people whose data powers it."),
 how_pub=("Partner with clinical and community organizations, design accessible collection "
  "protocols, compensate fairly, and build personalized models where data is limited. "
  "Evaluate with the speakers, not just on metrics."),
 how_sig=("Signature co-designed collection keeps speaker communities in charge."),
 keys=["Dysarthria, aphasia, stuttering, voice disorders",
  "Scarce: harder collection, smaller populations",
  "Center the speakers ethically",
  "Personalized models often win",
  "Accessible protocols; fair compensation",
  "Evaluate with speakers"],
 reqs=["Clinical/community partnerships",
  "Accessible protocols",
  "Personalization capability"],
 stds=["Disability research ethics (public)"],
 cites=["American Speech-Language-Hearing Association — public resources (public)"],
 demo=("vad", {"frames": [0.3, 0.05, 0.35, 0.04, 0.28, 0.33, 0.05, 0.3],
   "thresh": 0.1})),

# ---------------- Advanced (11) ----------------
dict(title="Large-Scale Corpus Pipelines", tier=A,
 desc_pub=("Large-scale corpus pipelines automate collection at thousands of hours: crowdsourced "
  "recording apps, automated quality gates, machine transcription with human adjudication "
  "sampling, and continuous ingestion.\n"
  "Engineering concerns: data versioning, deduplication, bias monitoring across demographics, "
  "and cost control (transcription at scale is expensive). Pipelines make corpora living "
  "resources, not one-time dumps."),
 desc_sig=("Signature corpus pipelines run as versioned data factories with bias dashboards, so "
  "scale never sacrifices representativeness."),
 how_pub=("Build staged pipelines - collect, gate, transcribe, annotate, publish - with "
  "automation and sampling QC at each stage. Version datasets; monitor demographic coverage "
  "continuously; control costs with adjudication sampling."),
 how_sig=("Signature bias dashboards keep large-scale collection representative."),
 keys=["Crowdsourced apps + automated gates",
  "Machine transcription, human adjudication sampling",
  "Data versioning",
  "Bias monitoring across demographics",
  "Cost control at scale",
  "Living resources, not dumps"],
 reqs=["Pipeline infrastructure",
  "Versioning system",
  "Demographic monitoring"],
 stds=["MLOps data practices (public literature)"],
 cites=["Mozilla Common Voice — pipeline (public)"],
 demo=("features", {"frames": [
   [0.4, 0.3, 0.2], [0.42, 0.31, 0.21], [0.38, 0.29, 0.19],
   [0.41, 0.32, 0.22], [0.39, 0.3, 0.2], [0.43, 0.33, 0.23]]})),

dict(title="Synthetic Speech Data", tier=A,
 desc_pub=("Synthetic speech data - generated by text-to-speech systems - augments scarce real "
  "data: creating training examples for rare words, accents, or noisy conditions. It is "
  "cheap and controllable but mismatched to real speech in subtle ways.\n"
  "Best practice: augment, don't replace - mix synthetic with real, and validate on real-only "
  "tests. Disclosure matters: synthetic data must be labeled as such in datasets."),
 desc_sig=("Signature synthetic augmentation uses controlled generation with documented "
  "mixture ratios, so augmentation is principled."),
 how_pub=("Generate synthetic utterances for targeted gaps (rare words, conditions), mix with "
  "real data at documented ratios, label synthetic portions, and validate improvements on "
  "real-only test sets."),
 how_sig=("Signature documented mixture ratios keep synthetic augmentation honest."),
 keys=["TTS-generated training examples",
  "Augments scarce real data",
  "Cheap and controllable; subtly mismatched",
  "Augment, don't replace",
  "Label synthetic portions",
  "Validate on real-only tests"],
 reqs=["TTS generation capability",
  "Mixture documentation",
  "Real-only validation"],
 stds=["Synthetic data disclosure practices (public literature)"],
 cites=["International Speech Communication Association (public)"],
 demo=("wave", {"sr": 16000, "dur": 0.75, "freq": 392})),

dict(title="Privacy and Consent in Speech Data", tier=A,
 desc_pub=("Voice is biometric: speech data identifies speakers, so privacy and consent are "
  "foundational. Informed consent explains uses, sharing, and withdrawal rights in plain "
  "language; licenses (like CC0 or custom) define reuse.\n"
  "De-identification is hard - voices are fingerprints. Strategies: pseudonymization, access "
  "controls, and data-use agreements. Regulations (GDPR, BIPA) set legal baselines varying by "
  "jurisdiction."),
 desc_sig=("Signature consent management makes permissions machine-readable and revocable, so "
  "withdrawal actually removes data from future use."),
 how_pub=("Design consent flows before collection, document licenses per dataset, implement "
  "access controls matching sensitivity, and honor withdrawals by removing data from future "
  "releases. Audit compliance regularly."),
 how_sig=("Signature revocable consent makes withdrawal operational, not theoretical."),
 keys=["Voice is biometric",
  "Informed consent in plain language",
  "Licenses define reuse",
  "De-identification is hard",
  "Pseudonymization + access controls",
  "Honor withdrawals"],
 reqs=["Consent process design",
  "License selection",
  "Withdrawal mechanism"],
 stds=["GDPR, BIPA baselines (public law)",
  "Data-use agreement practices (public)"],
 cites=["Electronic Frontier Foundation — biometric privacy (public)"],
 demo=("diarize", {"segments": [
   {"speaker": "CONSENTED_A", "start": 0.0, "end": 5.0},
   {"speaker": "WITHDRAWN_B", "start": 5.5, "end": 8.0}]})),

dict(title="Bias in Speech Datasets", tier=A,
 desc_pub=("Speech datasets reflect their collection: over-representing some accents, ages, and "
  "genders while missing others. Models trained on biased data fail the underrepresented - a "
  "fairness problem with real consequences for voice interfaces.\n"
  "Mitigation: measure representation across demographics, target collection at gaps, evaluate "
  "WER by group (not just overall), and report disaggregated results. Datasheets document "
  "known limitations honestly."),
 desc_sig=("Signature fairness practice requires disaggregated evaluation and gap-targeted "
  "collection for every dataset release."),
 how_pub=("Audit dataset demographics against target populations, collect to fill gaps, "
  "evaluate models per group, and publish disaggregated metrics with limitations. Treat "
  "fairness as a release gate, not an afterthought."),
 how_sig=("Signature release-gated fairness checks block biased datasets from shipping."),
 keys=["Datasets reflect collection bias",
  "Underrepresented groups get worse models",
  "Measure representation vs targets",
  "Evaluate WER by group",
  "Target collection at gaps",
  "Document limitations honestly"],
 reqs=["Demographic auditing",
  "Gap-targeted collection",
  "Disaggregated evaluation"],
 stds=["AI fairness evaluation practices (public literature)"],
 cites=["Partnership on AI — fairness resources (public)"],
 demo=("outcome", {"label": "WER gap between best/worst groups (lower better)", "pre": 38, "post": 12})),

dict(title="Evaluation Sets and Benchmarks", tier=A,
 desc_pub=("Evaluation sets measure progress honestly: fixed test sets with hidden labels, "
  "diverse conditions, and regular refreshment to prevent overfitting. Benchmarks (like "
  "SUPERB for speech) standardize comparison across systems.\n"
  "Goodhart's law warns: when a measure becomes a target, it ceases to be good. Rotate "
  "benchmarks, test on real deployment data, and report multiple metrics."),
 desc_sig=("Signature evaluation maintains rotating benchmark suites with deployment-data "
  "validation, so progress is real, not benchmark-shaped."),
 how_pub=("Curate hidden test sets reflecting deployment, run standardized benchmarks, and "
  "validate on fresh real-world data. Report WER alongside latency, fairness gaps, and "
  "robustness metrics."),
 how_sig=("Signature rotating suites prevent benchmark overfitting."),
 keys=["Fixed tests, hidden labels",
  "Diverse conditions",
  "Refresh to prevent overfitting",
  "Benchmarks standardize comparison",
  "Goodhart's law: don't game the metric",
  "Validate on deployment data"],
 reqs=["Hidden test curation",
  "Benchmark harness",
  "Deployment validation"],
 stds=["ML evaluation best practices (public literature)"],
 cites=["National Institute of Standards and Technology — evaluations (public)"],
 demo=("vad", {"frames": [0.5, 0.02, 0.55, 0.03, 0.48, 0.52, 0.02, 0.5],
   "thresh": 0.1})),

dict(title="Streaming Audio Processing", tier=A,
 desc_pub=("Streaming processing handles audio as it arrives - for live captioning, voice "
  "assistants, and call analytics: low-latency VAD, incremental recognition, and online "
  "diarization that update as speech flows.\n"
  "Constraints: latency budgets (milliseconds), limited future context, and resource limits "
  "on devices. Architectures trade accuracy for speed explicitly."),
 desc_sig=("Signature streaming design budgets latency per stage with accuracy trade-offs "
  "documented, so real-time systems are engineered, not hoped."),
 how_pub=("Design pipelines with per-stage latency budgets, use streaming-capable models "
  "(causal architectures), and measure end-to-end delay plus accuracy. Test on realistic "
  "streaming conditions, not just files."),
 how_sig=("Signature latency budgeting makes real-time performance predictable."),
 keys=["Process audio as it arrives",
  "Live captioning, assistants, analytics",
  "Latency budgets in milliseconds",
  "Limited future context",
  "Accuracy-speed trade-offs explicit",
  "Test on streaming conditions"],
 reqs=["Streaming-capable models",
  "Latency measurement",
  "Realistic streaming tests"],
 stds=["Real-time system practices (public literature)"],
 cites=["International Speech Communication Association (public)"],
 demo=("vad", {"frames": [0.02, 0.4, 0.5, 0.03, 0.02, 0.45, 0.55, 0.02],
   "thresh": 0.1})),

dict(title="Far-Field and Noisy Speech", tier=A,
 desc_pub=("Far-field speech - recorded at distance, with reverb and noise - is the hard case for "
  "recognition: smart speakers, meeting rooms, factories. Techniques: microphone arrays with "
  "beamforming, dereverberation, noise-robust features, and training on matched noisy data.\n"
  "Data collection must match deployment: record in real rooms with real noise, not just "
  "simulate. The CHiME challenges benchmarked this frontier."),
 desc_sig=("Signature far-field programs collect in deployment-real conditions with array "
  "geometries documented, so models face reality in training."),
 how_pub=("Deploy microphone arrays, apply beamforming and enhancement, train on matched "
  "noisy/far-field data, and evaluate in real rooms. Document array geometry and room "
  "acoustics with the dataset."),
 how_sig=("Signature reality-matched collection prevents lab-only models."),
 keys=["Distance + reverb + noise = hard case",
  "Arrays + beamforming help",
  "Train on matched noisy data",
  "Collect in real rooms",
  "Document arrays and acoustics",
  "CHiME benchmarked the frontier"],
 reqs=["Microphone arrays",
  "Real-condition collection",
  "Matched training data"],
 stds=["CHiME challenge protocols (public)"],
 cites=["CHiME speech separation challenges (public)"],
 demo=("features", {"frames": [
   [0.25, 0.2, 0.3], [0.5, 0.35, 0.28], [0.22, 0.18, 0.31], [0.48, 0.33, 0.27]]})),

dict(title="Code-Switched Speech Data", tier=A,
 desc_pub=("Code-switching - mixing languages mid-conversation - is normal for billions of "
  "speakers and hard for monolingual systems. Data collection must capture natural switching, "
  "transcribed with language tags per segment.\n"
  "Modeling approaches: multilingual models, explicit language identification, and "
  "code-switched training data. Evaluation measures both languages' accuracy and switch-point "
  "handling."),
 desc_sig=("Signature code-switch collection uses natural conversation prompts with "
  "language-tagged transcription, capturing real switching patterns."),
 how_pub=("Recruit bilingual speakers, design prompts eliciting natural switching, transcribe "
  "with per-segment language tags, and train/evaluate multilingual models on the data. "
  "Document the language pair and switching patterns."),
 how_sig=("Signature pattern-documented collection captures how switching actually works."),
 keys=["Mixing languages mid-conversation",
  "Normal for billions; hard for monolingual systems",
  "Transcribe with language tags",
  "Multilingual models + LID",
  "Evaluate both languages + switch points",
  "Document pair and patterns"],
 reqs=["Bilingual speaker recruitment",
  "Language-tagged transcription",
  "Multilingual modeling"],
 stds=["Code-switching research literature (public)"],
 cites=["International Speech Communication Association (public)"],
 demo=("align", {"words": [
   {"word": "I", "start": 0.0, "end": 0.2},
   {"word": "quiero", "start": 0.25, "end": 0.6},
   {"word": "tacos", "start": 0.65, "end": 1.0}], "offset": 3.0})),

dict(title="Archival and Preservation Formats", tier=A,
 desc_pub=("Speech archives preserve for decades: preservation masters in open lossless formats "
  "(WAV/FLAC), checksums verifying integrity, redundant geographic storage, and format "
  "migration before obsolescence. Metadata following archival standards (OAIS) keeps future "
  "users oriented.\n"
  "The enemy is neglect: formats decay, media fails, documentation is lost. Active "
  "preservation - fixity checks, migration plans - beats benign storage."),
 desc_sig=("Signature preservation runs fixity checks and migration planning as scheduled "
  "operations, so archives survive organizational change."),
 how_pub=("Ingest masters with checksums, store redundantly across sites, document per OAIS, "
  "and run scheduled fixity checks with migration reviews. Treat preservation as operations, "
  "not archiving-and-forgetting."),
 how_sig=("Signature operations-scheduled preservation survives staff turnover."),
 keys=["Open lossless masters; checksums; redundancy",
  "OAIS metadata standard",
  "Format migration before obsolescence",
  "Enemy is neglect",
  "Fixity checks scheduled",
  "Preservation as operations"],
 reqs=["Checksum infrastructure",
  "Geographic redundancy",
  "Migration planning"],
 stds=["OAIS reference model (public)",
  "IASA preservation guidance (public)"],
 cites=["International Association of Sound Archives (public)"],
 demo=("wave", {"sr": 16000, "dur": 2.0, "freq": 261})),

dict(title="Licensing Speech Data", tier=A,
 desc_pub=("Licensing decides who can use speech data how: open licenses (CC0, CC-BY) maximize "
  "research use; custom licenses restrict commercial use or require approval; some data stays "
  "restricted to the collecting institution.\n"
  "License choice shapes impact: open data gets cited and built on; restricted data protects "
  "sensitive populations. Document licenses clearly - ambiguity chills reuse."),
 desc_sig=("Signature licensing pairs each dataset with a clear license and use registry, so "
  "permissions are never ambiguous."),
 how_pub=("Choose licenses matching the consent given and the data's sensitivity, document in "
  "the datasheet and at download, and track significant reuses. Revisit licenses if consent "
  "scopes change."),
 how_sig=("Signature consent-matched licensing keeps permissions aligned with promises."),
 keys=["Open vs custom vs restricted",
  "CC0/CC-BY maximize research",
  "Match license to consent given",
  "Ambiguity chills reuse",
  "Document at download",
  "Sensitive data stays restricted"],
 reqs=["License selection per dataset",
  "Consent-license alignment",
  "Documentation at distribution"],
 stds=["Creative Commons licenses (public)",
  "Data licensing practices (public literature)"],
 cites=["Creative Commons (public)"],
 demo=("outcome", {"label": "Datasets with clear documented licenses", "pre": 57, "post": 98})),

dict(title="The Future of Speech Data", tier=A,
 desc_pub=("Speech data's future: ever-larger multilingual corpora, self-supervised learning "
  "reducing labeled-data needs, personalized models from minutes of speech, and real-time "
  "systems everywhere. Synthetic data grows as a complement.\n"
  "The through-line is inclusion: technology understanding everyone, in every language and "
  "voice. Data stewardship - consent, fairness, preservation - grows more important as scale "
  "grows. This database's Signature edition prototypes the knowledge core such stewardship "
  "needs."),
 desc_sig=("The Signature future-state is a speech-data operating system: consented "
  "collection, fair representation, preserved archives, and auditable lineage - serving "
  "inclusive voice technology. This database is a prototype of that system's knowledge core."),
 how_pub=("The field invests in low-resource languages, fairness evaluation, privacy-"
  "preserving techniques (federated learning), and sustainable collection economics. "
  "Stewardship standards mature alongside scale."),
 how_sig=("Signature's operating-system vision makes stewardship the default at scale."),
 keys=["Multilingual scale; self-supervised learning",
  "Personalized models from minutes",
  "Synthetic as complement",
  "Through-line: inclusion",
  "Stewardship grows with scale",
  "Consent, fairness, preservation"],
 reqs=["Low-resource investment",
  "Fairness evaluation",
  "Privacy-preserving techniques"],
 stds=["Emerging responsible-AI data standards (public literature)"],
 cites=["Partnership on AI (public)",
  "International Speech Communication Association (public)"],
 demo=("wave", {"sr": 16000, "dur": 1.5, "freq": 330})),
]
