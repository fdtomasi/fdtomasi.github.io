Title: ISMB/ECCB 2017 conference, Day 2
Slug: ismb-eccb-2017-day-2
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
Cancer genome graph. Weaver algorithm. Minimisation problem. Allele specific copy number. Integrated analysis with functional genomic data. Genome organisation has different resolutions. For example, there are methods developed to predict chromatine loops. Is this possible using only sequence data?
With machine learning methods it is possible to have:
1. motifs
2. word embedding model
Basically the task is to learn from a resolution and assess the impact on different resolutions of the genome.

#### Wei Wang (UCLA) - "Aztec: A machine learning empowered platform for FAIR biomedical software"
- autocomplete queries
- ontology highlights
- metadata extraction from PDF (authors, tool description)
Publication mining tool. They use [Latent Dirichlet Allocation](https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation) for topic extraction, which, as I have seen, is very common for text analysis.

#### Saurabh Sinha (UIUC) - "KnowEnG: Knowledge Network-guided analysis of genomics data on the Cloud"
This was the first of cloud-related talks, which was really interesting. One question that arises today was: why are we struggling to have the best hardware for data analysis when someone (*i.e.*, Amazon Web Services) could do that for us? The talk was about a pipeline for analysis of users spreadsheets, which are common and user-friendly. Starting from this, they incorporate prior knowledge building a knowledge network.
- (network-guided) gene set characterisation / discriminative random values
- (network-guided) sample clustering
- (network-guided) signature analysis - LogisticRegression + network-based penalisation
- multiomics analysis
- literature mining

[*break*]

## 2pm
Back to the [CAMDA track](https://www.iscb.org/cms_addon/conferences/ismbeccb2017/camda.php). This time was for the Cesare Furlanello's talk "Towards a scientific blockchain framework for reproducible data analysis". The reproducibility of the results in biomedical data analysis is a very fundamental issue (we tackled this problem as well, developing [PALLADIO](github.com/slipguru/palladio)) because, since the goal is to publish, some analysis may contain errors, or, worse, some results may be falsified. Cesare talked about an [horror story on a Duke University](http://www.foxnews.com/us/2017/07/04/epa-funded-lab-faked-research-results-on-respiratory-illnesses-whistleblower-lawsuit-claims.html), where *no results could be replicated*. There were some falsified or fabricated data, mixed labels, and int the end this resulted in 11 papers retracted, clinical trials interrupted. Clinical trials! These people were starting to experiment therapies clinically... Horror story is reductive.
I think (hope) this story was scaring for the audience.
Of course there must be a way to avoid these things. "Good" papers are also rewarded by citations. One solution may be record every pipeline, method, data, and put them open access (see how the BD2K track prepared me for this?). What about the money-back guarantee? So that there are positive and negative incentives. One can create machinery to remove lack of compliance. But the main problem still remains: institutions wants their people to publish.
Idea (not Cesare's): [blockchain, *a disruptive invention*](https://www.ted.com/talks/bettina_warburg_how_the_blockchain_will_radically_transform_the_economy). The blockchain avoids the necessity of authorities that regulates the exchange of money and any type of assets. As the internet is the medium for information, blockchain is the medium for value. There are lots of potential applications, even outside of the economy. One may be [PROBO blockchain for scientific reproducibility](https://mpbalab.fbk.eu/blog/the-probo-blockchain-for-scientific-reproducibility/). The idea is to rank people for adherence to the methodology. So, one can start to have a record to be able to replicate research. Following the blockchain idea, this record is unique and is distributed across the internet. For each "good transaction", *i.e.*, adherence to the methodology?, a new block may be created, and is put at the end of the chain. At this points one reputation score may be adopted, in which it is possible to compute how far from the methodology one is posed. All of this makes the PROBO approach transparent, trustless and accountable for. There is no effect on the reputation of institutions, and, also, the approach is integrable with standards like [MIAME](http://www.nature.com/news/robust-research-institutions-must-do-their-part-for-reproducibility-1.18259). Of course there could be the problem of the Matthew effect: rich get richer, to avoid.

## 4.45pm
I went back to the BD2K track, straight into the "Session 3: Data Science, Open Science, and the Commons" session. Angel Pizarro's "Accelerating Research on the Cloud" talk expressed a (certainly biased, but) interesting point of view. What about focusing on the research, and leave the hardware management to other people? In particular, of course, [AWS](https://aws.amazon.com/it/). The problem is that too much time of the same people that do research is spent on the management of the infrastructure, because who else better than themselves knows what they want? But this is not a one-timer. Managing infrastructures is an ongoing thing to do. Better to leave that all to companies like Amazon, and to pay when actually using the infrastructure, instead of paying for the services and using them only a fraction of time (of course, our computing machines are not always active!).

## 5.30pm, panel discussion
I was really glad to be able to attend this panel discussion. Actually I didn't plan for this, I was there and I remained seated. The topic of the discussion was: where do we stand as a single community? Is there something we can do together? Starting from data sharing, for example. Some problems arises for standards, privacy. It is really difficult to speak with each other, at the same time maintaining the privacy of the data which actually contains sensible information on patients. One comment was that the founding agency and academic people must be on the same page. Also, there is no single agency that can tackle the problems singularly, and this encourage the sharing of problems and solutions. But how to encourage open science in real time? Pizarro had the best solution, money: 10K for each preprint, so that people are encouraged to put online their work as soon as they are almost ready. The fact is that people do not do that because they fear someone can stole it. But maybe it is sufficient to give people publicity, honor. The big issue, however, is how to share data. It costs actually money to share data, for the privacy problems and everything.

## Photos, day 2.
And finally, another round of photos!
