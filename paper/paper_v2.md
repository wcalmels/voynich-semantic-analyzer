# Computational Semantic Analysis of the Voynich Manuscript
## A Contextual EVA-Based Experimental Framework Using NLP and Medieval Medical Corpora

### Walter Calmels Von dem Knesebeck

---

# Abstract

This work presents an experimental computational framework for semantic exploration of the Voynich Manuscript using EVA transcription analysis, visual glyph extraction, semantic clustering, transformer embeddings, and contextual comparison against medieval Anatolian-Seljuk medical corpora.

The framework integrates computer vision, lexical analysis, semantic embeddings, clustering algorithms, and historical contextual restriction focused on botanical medicine, hydrotherapy, gynecology, and medieval astrological medicine.

Results obtained through transformer-based semantic embeddings and automatic clustering indicate non-random contextual convergence between experimentally modeled EVA semantic families and medieval medical-botanical corpora associated with Anatolian-Seljuk traditions (13th century onward).

This work does not claim definitive decipherment of the Voynich Manuscript. Instead, it proposes a reproducible computational methodology for semantic-contextual exploration of Voynichese structures.

---

# 1. Introduction

The Voynich Manuscript (VMS) remains one of the most enigmatic undeciphered codices in history. Since its modern rediscovery, numerous cryptographic, linguistic, statistical, and speculative hypotheses have attempted to explain its origin and meaning.

Despite decades of research, no universally accepted decipherment has emerged.

However, prior research by:

- Prescott Currier
- William Friedman
- Gabriel Landini
- Takeshi Takahashi
- Jorge Stolfi
- Mary D’Imperio

demonstrated that Voynichese exhibits strong statistical regularities compatible with structured language-like systems rather than random noise.

This work proposes an alternative computational framework centered on:

- semantic-contextual exploration
- transformer embeddings
- visual glyph processing
- lexical family detection
- medieval medical contextualization
- restricted-domain corpus comparison

rather than direct symbol-to-symbol decipherment.

---

# 2. Hypothesis

The central hypothesis is that:

1. Voynichese may encode structured semantic domains rather than arbitrary random sequences.
2. Semantic regularities may emerge through contextual clustering.
3. A restricted medieval medical-botanical corpus provides a more coherent comparison framework than unrestricted multilingual comparison.
4. Transformer embeddings can reveal contextual convergence between EVA-derived semantic structures and medieval medical corpora.

---

# 3. Methodology

## 3.1 Glyph Extraction

Glyphs were extracted from manuscript folios using OpenCV-based image segmentation techniques:

- thresholding
- contour extraction
- bounding-box isolation
- PNG glyph export

This produced reusable glyph datasets for clustering and visual analysis.

---

## 3.2 EVA Processing

EVA transcriptions were processed through:

- tokenization
- frequency analysis
- bigram extraction
- lexical family grouping
- semantic mapping

Experimental semantic families included:

| EVA Family | Proposed Semantic Domain |
|---|---|
| qok-* | liquids / medicine |
| yka-* | preparation / boiling |
| sho-* | heat / pain / sun |
| pch-* | roots / cutting / mixture |
| dai-* | cycles / repetition |
| ata-* | tincture / preparation |
| qot-* | opening / channels |

These interpretations remain exploratory and computationally inferred.

---

# 4. Medieval Corpus Construction

A contextual medieval corpus was constructed experimentally using:

- Anatolian-Seljuk medical fragments
- Persian medical terminology
- hydrotherapy references
- herbal preparation texts
- medieval gynecological fragments
- astrological medicine contexts

The corpus structure included:

- title
- date
- region
- language
- transliteration
- thematic keywords
- medical context

---

# 5. Embedding-Based Semantic Analysis

## 5.1 TF-IDF Embeddings

Initial TF-IDF similarity analysis suggested contextual convergence between EVA semantic families and medical-botanical corpora.

Highest similarity scores appeared in:

- Persian medical fragments
- herbal preparation texts
- hydrotherapy contexts
- women's medicine
- astrological medicine

---

## 5.2 Transformer Embeddings

Advanced semantic embeddings were generated using:

```text
sentence-transformers/all-MiniLM-L6-v2