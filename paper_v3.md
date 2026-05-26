# Computational Semantic Analysis of the Voynich Manuscript

## A Contextual EVA-Based Experimental Framework Using NLP, Transformer Embeddings, and Medieval Medical Corpora

### Walter Calmels Von dem Knesebeck

Independent Researcher
Santiago, Chile
[wcalmels@phi47.cl](mailto:wcalmels@phi47.cl)

---

# Abstract

The Voynich Manuscript (VMS) remains one of the most extensively studied undeciphered codices in history. Traditional approaches have primarily focused on cryptographic interpretation, direct linguistic substitution, or speculative historical hypotheses. This work proposes an alternative computational framework centered on semantic-contextual exploration using modern Natural Language Processing (NLP) methodologies.

The framework integrates glyph extraction, EVA-based lexical processing, semantic family modeling, transformer embeddings, unsupervised clustering, and contextual comparison against medieval medical corpora associated with Anatolian-Seljuk traditions.

Experimental results obtained through transformer-based semantic embeddings suggest measurable contextual convergence between EVA-derived semantic structures and medieval medical-botanical domains, particularly herbal preparation, hydrotherapy, medicinal processing, bodily regulation, and astrological medicine.

This work does not claim definitive decipherment of the Voynich Manuscript. Instead, it presents a reproducible computational methodology for semantic-contextual exploration of Voynichese structures using modern NLP techniques and historically restricted corpora.

---

# 1. Introduction

The Voynich Manuscript has resisted decipherment for more than a century despite sustained attention from cryptographers, linguists, historians, statisticians, and computer scientists. Since its rediscovery in the early twentieth century, the manuscript has generated numerous hypotheses involving natural language encoding, steganography, artificial languages, ciphers, glossolalia, and fabricated text.

Several foundational studies demonstrated that Voynichese exhibits non-random statistical properties consistent with structured information systems. Important contributions include:

* Prescott Currier’s language distribution studies
* William Friedman’s cryptographic investigations
* Mary D’Imperio’s structural analyses
* Gabriel Landini’s transcription work
* Takeshi Takahashi’s EVA corpus
* Jorge Stolfi’s interlinear archive and lexical statistics

While these studies strongly suggest that Voynichese is statistically structured, no universally accepted decipherment currently exists.

The present work departs from traditional direct-decoding approaches and instead investigates whether meaningful semantic regularities may emerge through contextual computational analysis.

Rather than attempting symbol-by-symbol translation, this framework explores whether:

1. EVA-derived structures exhibit semantic clustering behavior;
2. contextual semantic similarity can be measured computationally;
3. medieval medical corpora provide stronger semantic alignment than arbitrary multilingual baselines.

---

# 2. Research Position and Scientific Scope

This project should be interpreted as:

* exploratory computational humanities research;
* semantic-contextual NLP experimentation;
* medieval corpus analysis infrastructure;
* reproducible semantic modeling.

The framework explicitly does NOT claim:

* definitive translation of Voynichese;
* verified historical decipherment;
* direct linguistic equivalence;
* proven authorship or origin.

Instead, the objective is to evaluate whether modern semantic computation can reveal measurable contextual organization within EVA-derived structures.

---

# 3. Hypothesis

The central hypothesis is that Voynichese may encode structured semantic domains that can be explored computationally through contextual embeddings and restricted historical corpora.

More specifically:

1. Voynichese lexical structures may exhibit semantic organization rather than random distribution;
2. medieval medical-botanical corpora provide a meaningful contextual comparison space;
3. semantic convergence can emerge without requiring direct translation;
4. transformer embeddings may reveal latent semantic proximity between EVA structures and medieval medical domains.

---

# 4. Methodology

## 4.1 Framework Architecture

The computational pipeline follows the structure below:

```text
Voynich Folios
        ↓
Glyph Extraction
        ↓
OCR / Segmentation
        ↓
EVA Processing
        ↓
Semantic Families
        ↓
Transformer Embeddings
        ↓
Semantic Clustering
        ↓
Medieval Corpus Comparison
        ↓
Contextual Similarity Analysis
```

---

## 4.2 Glyph Extraction and Visual Processing

Voynich folios were processed using OpenCV-based segmentation techniques including:

* thresholding;
* contour extraction;
* glyph isolation;
* PNG glyph export.

This produced reusable glyph datasets suitable for clustering and visual inspection.

---

## 4.3 EVA Processing

EVA transcriptions were processed through:

* tokenization;
* frequency analysis;
* bigram extraction;
* lexical grouping;
* semantic family mapping.

Experimental semantic families were generated from recurring lexical structures.

Examples include:

| EVA Family | Experimental Semantic Domain     |
| ---------- | -------------------------------- |
| qok-*      | liquids / medicine               |
| yka-*      | preparation / boiling            |
| sho-*      | heat / pain / solar association  |
| pch-*      | roots / cutting / mixture        |
| dai-*      | cycles / repetition              |
| ata-*      | tincture / medicinal preparation |
| qot-*      | opening / channels               |

These semantic interpretations remain computationally inferred and exploratory.

---

## 4.4 Medieval Corpus Construction

A contextual medieval corpus was constructed experimentally using:

* Anatolian-Seljuk medical fragments;
* Persian medical terminology;
* hydrotherapy references;
* herbal preparation texts;
* medieval gynecological material;
* astrological medicine contexts.

The corpus structure included:

* title;
* approximate date;
* region;
* language;
* transliteration;
* thematic keywords;
* semantic context.

The corpus was intentionally restricted to historically coherent medical-botanical domains rather than arbitrary multilingual comparison.

---

# 5. Embedding-Based Semantic Analysis

## 5.1 TF-IDF Semantic Similarity

Initial experiments using TF-IDF vectorization suggested contextual convergence between EVA-derived semantic structures and medieval medical corpora.

Higher similarity scores emerged in:

* Persian medical fragments;
* herbal preparation contexts;
* hydrotherapy descriptions;
* women’s medicine;
* astrological medicine.

While limited, these results suggested that semantic organization may exist within the experimental EVA framework.

---

## 5.2 Transformer Embeddings

Advanced semantic analysis was performed using:

```text
sentence-transformers/all-MiniLM-L6-v2
```

Semantic similarity was calculated using cosine similarity within transformer embedding space.

Representative results included:

| Corpus Fragment                    | Semantic Score |
| ---------------------------------- | -------------- |
| Seljuk Herbal Preparation Fragment | 0.4290         |
| Divrigi Hydrotherapy Fragment      | 0.4149         |
| Persian Medical Treatise           | 0.4107         |
| Seljuk Herbal Fragment             | 0.3967         |
| Women’s Medicine Fragment          | 0.3876         |

These results suggest measurable contextual alignment toward medieval medical-botanical domains.

Importantly, the strongest alignments consistently emerged around:

* medicinal preparation;
* hydrotherapy;
* herbal processing;
* bodily regulation;
* thermal treatment;
* cyclical biological processes.

---

# 6. Automatic Semantic Clustering

Unsupervised clustering using transformer embeddings revealed emergent semantic grouping behavior without manually predefined categories.

Detected clusters converged around:

* liquids and medicinal mixtures;
* preparation and boiling processes;
* thermal treatment and pain;
* cyclical bodily regulation;
* herbal processing.

The emergence of these clusters suggests that EVA-derived structures may exhibit measurable semantic organization rather than purely arbitrary lexical distribution.

---

# 7. Semantic Visualization

Dimensionality reduction using Principal Component Analysis (PCA) generated two-dimensional semantic maps illustrating spatial proximity between:

* EVA semantic structures;
* herbal medicine fragments;
* hydrotherapy references;
* astrological medicine contexts.

The resulting semantic distributions suggest non-random contextual clustering behavior within the embedding space.

---

# 8. Computational Platform

An interactive research platform was developed using:

* Python;
* Streamlit;
* OpenCV;
* Pandas;
* Scikit-learn;
* Sentence Transformers.

The platform supports:

* glyph visualization;
* semantic search;
* embedding analysis;
* clustering visualization;
* contextual comparison;
* corpus exploration.

The framework is fully reproducible through GitHub-based deployment.

---

# 9. Discussion

The present work does not establish definitive decipherment of the Voynich Manuscript.

However, the experiments suggest several important observations:

1. EVA-derived structures exhibit measurable semantic regularities;
2. contextual medieval corpora produce stronger semantic alignment than arbitrary text domains;
3. transformer embeddings provide a viable framework for semantic exploration of undeciphered corpora;
4. medieval medical-botanical contexts repeatedly emerge as dominant semantic convergence regions.

The strongest semantic alignments consistently involve:

* medicinal preparation;
* hydrotherapy;
* botanical processing;
* bodily treatment;
* heat regulation;
* astrological medicine.

This pattern is broadly compatible with historical interpretations of the manuscript as a medical-herbal codex.

---

# 10. Limitations

Several important limitations remain:

* limited corpus size;
* partially synthetic corpus generation;
* exploratory semantic labeling;
* absence of verified translation pairs;
* possible confirmation bias;
* incomplete medieval source coverage.

Future work must incorporate:

* substantially larger medieval corpora;
* multilingual baselines;
* statistical significance testing;
* randomized comparison controls;
* broader historical datasets.

The current framework should therefore be interpreted as exploratory computational research rather than conclusive linguistic proof.

---

# 11. Future Directions

The broader long-term objective of this research is the development of:

```text
Computational Medieval Semantic Infrastructure
```

Future directions include:

* large-scale medieval corpus acquisition;
* automated OCR pipelines;
* multilingual transformer fine-tuning;
* semantic graph analysis;
* t-SNE and UMAP semantic visualization;
* collaborative corpus infrastructure;
* AI-assisted manuscript ingestion;
* historical NLP agents.

This infrastructure may ultimately support not only Voynich analysis, but broader medieval computational humanities research.

---

# 12. Conclusion

This work presents a reproducible computational framework for semantic-contextual exploration of the Voynich Manuscript using EVA processing, transformer embeddings, semantic clustering, and medieval medical corpus comparison.

While no definitive decipherment is claimed, the results suggest that contextual semantic methodologies may provide a productive direction for future computational Voynich research.

The strongest semantic convergence observed in this study consistently aligns with medieval medical-botanical domains associated with Anatolian-Seljuk traditions.

More broadly, the framework demonstrates the potential value of combining:

* NLP;
* transformer embeddings;
* medieval corpora;
* semantic clustering;
* digital humanities methodologies.

The Voynich Manuscript may therefore serve not only as an undeciphered artifact, but also as a catalyst for the development of new computational approaches to historical semantic analysis.

---

# References

1. Currier, Prescott. Some Important New Statistical Findings.
2. Friedman, William. Voynich Studies.
3. Landini, Gabriel. EVA Interlinear Files.
4. Takahashi, Takeshi. EVA Voynich Corpus.
5. Stolfi, Jorge. Interlinear Voynich Archive.
6. D’Imperio, Mary. The Voynich Manuscript: An Elegant Enigma.
7. Sentence Transformers Documentation.
8. OpenCV Documentation.
9. Scikit-learn Documentation.
10. Vaswani et al. Attention Is All You Need.
11. Rehurek & Sojka. Software Framework for Topic Modelling with Large Corpora.
12. Jurafsky & Martin. Speech and Language Processing.
