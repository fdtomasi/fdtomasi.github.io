Title: ISMB/ECCB 2017 conference, Day 2
Slug: ismb-eccb-2017-day-1
Date: 2017-07-23 23:15
Category: posts
Tags: conference, life sciences, bioinformatics
Author: Federico Tomasi

## 10am, Sunday.
Organising a conference during a weekend is terrible. One loses his sense of time (and space?). It's Sunday, nonetheless I feel like it's only Tuesday, with the difference that I did not have time to rest this week. At least there is coffee, right?
(Yes there is! In early morning we need to take all we can, since there is not after lunch.)

Today it was time to explore different tracks. The choice was to attend the [BD2K track](https://www.iscb.org/ismbeccb2017-program/bd2k-special-track), which has a nice "Session 1: Machine Learning" as written in the program.
This track was about the data accessibility and reuse, basically. Again, this is a *huge* problem in data science. As yesterday (ADD LINK) the problem was how to integrate different types of data, today it can be summarised in: how *the heck* can I access data for my analyses? I did not known, until now, that "BD2K" actually stands for "Big Data to Knowledge". The speaker of the keynote talk was [Warren Kibbe (NIH NCI)](https://cbiit.nci.nih.gov/about/cbiit-director), and he talked about the "FAIR" principles for biomedical data, which stands for "Findable, Accessible, Interoperable, and Reusable" (I know, lots of acronyms in this track, right?). The keyword was "precision medicine". In fact, when data are FAIR, a lot of nice things may happen, such as
- matching therapies to patients
- avoiding therapies that will not work
He talked about the [Blue Ribbon Panel (BRP) Cancer Moonshot](https://www.cancer.gov/research/key-initiatives/moonshot-cancer-initiative/blue-ribbon-panel), which is basically a panel of experts established to talk about cancer-related problems (and, hopefully, proposed solutions). I don't think he entered into much details, but their website is full of useful info about it.

Then, the Machine Learning session started, with a Mark Craven's talk about "Learning to Uncover Host-Virus Interactions". (I almost forgot, today I was taking notes, finally. I managed to get a notebook and a pen!)
Finally the more technical talks started. This first and subsequent talks were about biological network inference and prediction. This is a task that I personally am interested in. However, they had only 15mins each, so they could not go into much details about their work. Craven had a subnetwork inference task. Basically what he did was to
1. assemble a background network, with ca. 40K interactions, and
2. given a background network and a phenotype label for genes infer the subnetwork for causal explanations for relevant genes.
Of course causal relationships are always difficult to infer. How can you infer the *directions* of relations between genes? This is an actual problem in biomedical data analysis.

Now it was time for Krishna Kalari (Mayo Clinic), "Genome-guided Framework for Personalized Cancer Treatment". Unfortunately I could not take lots of notes. They developed the [PANOPLY software](http://bioinformaticstools.mayo.edu/research/panoply/), which uses drug networks and [Random Forest](https://en.wikipedia.org/wiki/Random_forest) (yeah, not very informative summary).

Jiawei Han (UIUC)'s talk was in a slight different direction (clear from the title "Construction of Biological Networks from Massive Text Data: A Data-Driven Approach"). His networks were constructed starting from the text data. This is interesting; actually scientific community has tons of scientific articles which are not integrated and not used during new research. The question was: how to turn text data into knowledge? Data was the [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/) articles. What to use on them? [*keywords alert*] [Markov blanket](https://en.wikipedia.org/wiki/Markov_blanket) for feature selection, mutual enhancement of type propagation and clustering (*i.e.*, something to deal with text data).

#### Jian Ma (Carnegie Mellon University) - "Decoding genome structure"
Cancer genome graph. Weaver algorithm. Minimisation problem. Allele specific copy number. Integrated analysis with functional genomic data.
genome organisation has different resolutions. Chromatine loops -> methods developed to predict tys type of loops; possible using only sequence data? ML methods:
1. motifs
2. word embedding model
Basically the task is to learn from a resolution and assess the impact on different resolutions of the genome.

#### Wei Wang (UCLA) - "Aztec: A machine learning empowered platform for FAIR biomedical software"
- autocomplete queries
- ontology highlights
- metadata extraction from PDF (authors, tool description)
Publication mining tool. They use [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) for topic extraction, which, as I have seen, is very common for text analysis.

#### Saurabh Sinha (UIUC) - "KnowEnG: Knowledge Network-guided analysis of genomics data on the Cloud"
This was the first of cloud-related talks, which was really interesting. One question that arises today was: why are we struggling to have the best hardware for data analysis when someone (*i.e.*, Amazon) could do that for us? The talk was about a pipeline for analysis of users spreadsheets, which are common and user-friendly. Starting from this, they incorporate prior knowledge building a knowledge network.
- (network-guided) gene set characterisation / discriminative random values
- (network-guided) sample clustering
- (network-guided) signature analysis - LogisticRegression + network-based penalisation
- multiomics analysis
- literature mining

[*break*]
