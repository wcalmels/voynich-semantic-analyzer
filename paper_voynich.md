# Computational Semantic Analysis of the Voynich Manuscript:
## An Experimental EVA-Based Contextual Framework

### Walter Calmels Von dem Knesebeck

---

# Abstract

The Voynich Manuscript remains one of the most enigmatic undeciphered documents in history. This work presents an experimental computational framework for contextual semantic analysis of EVA-transcribed Voynich text using glyph extraction, clustering, lexical family detection, and domain-constrained semantic interpretation.

The proposed system integrates image-based glyph segmentation, EVA transcription processing, statistical frequency analysis, semantic family grouping, and contextual botanical-medical interpretation. The framework was implemented as an interactive web platform using Python, OpenCV, Pandas, Streamlit, and experimental semantic mapping techniques.

Preliminary findings suggest the existence of recurrent lexical structures compatible with procedural, botanical, hydrotherapeutic, and medical contexts. The work does not claim a definitive decipherment of the Voynich Manuscript, but rather proposes a reproducible computational methodology for structured semantic exploration.

---

# 1. Introduction

The Voynich Manuscript (VMS) is an illustrated codex written in an unknown script and language, generally dated to the early 15th century. Despite decades of cryptographic, linguistic, and statistical research, no universally accepted decipherment has emerged.

Previous work by Currier, Friedman, Landini, Takahashi, Stolfi, and others established the statistical regularity of Voynichese and demonstrated that the manuscript exhibits linguistic-like behavior rather than random noise.

This project proposes an experimental semantic-computational framework combining:

- EVA transcription analysis
- visual glyph extraction
- semantic family clustering
- contextual medical interpretation
- botanical correlation
- hydrotherapeutic contextualization
- exploratory medieval Turkic/Persian comparison

---

# 2. Objectives

The main objective is to develop a reproducible computational framework capable of:

1. Extracting glyph structures from Voynich folios.
2. Grouping glyphs through visual similarity clustering.
3. Processing EVA transcriptions computationally.
4. Detecting recurrent lexical families.
5. Building contextual semantic hypotheses.
6. Providing an interactive exploratory platform.

---

# 3. Methodology

## 3.1 Glyph Extraction

Glyphs were segmented from folio imagery using OpenCV image-processing techniques including:

- thresholding
- contour extraction
- bounding-box segmentation
- PNG glyph export

## 3.2 EVA Processing

Experimental EVA corpora were processed through:

- tokenization
- frequency analysis
- bigram analysis
- lexical clustering
- semantic family grouping

## 3.3 Semantic Families

Several recurrent lexical roots were detected experimentally:

| EVA Family | Proposed Contextual Interpretation |
|---|---|
| qok-* | liquids / medicinal preparation |
| yka-* | boiling / heating / preparation |
| sho-* | heat / sun / pain |
| pch-* | cutting / root / mixture |
| dai-* | cycles / repetition |
| ata-* | tincture / compound |
| qot-* | opening / channeling |

These interpretations remain hypothetical and exploratory.

---

# 4. Computational Platform

A local and web-based interactive platform was developed using:

- Python
- Pandas
- OpenCV
- PIL
- Streamlit
- Scikit-learn

The platform includes:

- glyph visualization
- semantic filtering
- EVA searching
- CSV export
- contextual reports
- lexical family exploration

---

# 5. Preliminary Findings

The experimental framework identified:

- recurrent lexical patterns
- stable prefix/suffix structures
- semantic clustering tendencies
- contextual association between botanical and medical domains

The data suggests that Voynichese may exhibit non-random semantic regularities.

---

# 6. Limitations

This work does not claim:

- definitive decipherment
- direct translation certainty
- linguistic proof of any specific historical language

The interpretations are experimental and intended for computational exploration.

---

# 7. Future Work

Future research directions include:

- transformer embeddings
- semantic vector spaces
- medieval corpus comparison
- Turkic/Persian lexical analysis
- astronomical symbol correlation
- AI-assisted semantic suggestion systems
- large-scale EVA datasets

---

# 8. Conclusion

This work presents an experimental computational framework for semantic exploration of the Voynich Manuscript through contextual EVA analysis, glyph extraction, and lexical family mapping.

While no definitive decipherment is claimed, the framework demonstrates that reproducible semantic-computational methodologies may provide useful structure for future Voynich research.

---

# References

1. Currier, Prescott. "Some Important New Statistical Findings."
2. Landini, Gabriel. EVA Transcription Files.
3. Takahashi, Takeshi. Complete EVA Voynich Transcription.
4. Stolfi, Jorge. Voynich Interlinear Archive.
5. Friedman, William. Voynich Studies.
6. D’Imperio, Mary. The Voynich Manuscript: An Elegant Enigma.