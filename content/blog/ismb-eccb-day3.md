Title: ISMB/ECCB 2017 conference, Day 3
Slug: ismb-eccb-2017-day-3
Date: 2017-07-24 23:15
Category: posts
Tags: conference, life sciences, bioinformatics
Author: Federico Tomasi
Headline: The third day at the conference.
Summary: The third day at the conference. BioVis and HiTSeq!

Another day, another round of fresh and exciting ideas.
Today it was a bit difficult to follow each talk (remember I did not have a weekend!). To take it easy, I attended the [BioVis](http://biovis.net/2017/index.html) track in the morning. I guessed that if they talked about data visualisation, my attention was not required to have high levels. Of course I was wrong.

## (Biological) data visualisation
They went into details a lot, but, as the name of the track suggests, they had nice figures.
First was time for the keynote by Boudewijn Lelieveld, "Visual analytics for spatial transcriptomics: from single cell to tissue and back". Main topic was: what if Netflix uses [PCA](https://en.wikipedia.org/wiki/Principal_component_analysis)? Well, they may suggest [the Jaws movie](https://en.wikipedia.org/wiki/Jaws_(film)) to a family. As for the biomedical data, PCA is not that great, ouside, for example, macroscopic differences. Interesting, instead, is that most of the talks were focused on using some variation of [t-SNE algorithm](https://distill.pub/2016/misread-tsne/). And actually it seems to work well in such use cases. In particolar for brain transcriptomics (as explained in this talk, with its hierarchical evolution H-SNE). The topic of brain transcriptomics was investigated also in the following talks, by Marwan Abdellah's "Reconstruction and visualization of large-scale volumetric models of neocortical circuits for physically-plausible in silico optical studies" and Sjoerd M. H. Huisman's "BrainScope: interactive visual exploration of the spatial and temporal human brain transcriptome". The goal is to reconstruct the brain network with watertight meshes to have realistic simulations of what happens inside the brain.

Here there is a collection of some photos of the BioVis track.
<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Here’s a great collection of photos from <a href="https://twitter.com/hashtag/biovis?src=hash">#biovis</a> at <a href="https://twitter.com/hashtag/ismbeccb?src=hash">#ismbeccb</a> 2017 in Prague by <a href="https://twitter.com/jandot">@jandot</a>: <a href="https://t.co/hcLJQNG6fc">https://t.co/hcLJQNG6fc</a>. Impressive attendance!</p>&mdash; Nils Gehlenborg (@nils_gehlenborg) <a href="https://twitter.com/nils_gehlenborg/status/895299653247303680">August 9, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

## Deep networks with string data
After that, the last talks of the morning were a bit difficult to follow, so let's get straight to the afternoon.
In the afternoon, I switched to the [HiTSeq](http://hitseq.org/). The website of course is not as nice as the BioVis' one, but the arguments were equally interesting, maybe a little bit more machine learning oriented. Interesting was Xu Min talk about "Chromatin accessibility prediction via convolutional long short-term memory networks with k-mer embedding". [Deep networks](https://en.wikipedia.org/wiki/Deep_learning)! I hadn't seen any up to now. Such networks were used with a string embedding, in particular after extracting $k$-mers from the words. This is similar to the string kernel methods, but with the difference that, well, this is not a kernel. And you can use it with [LSTM](http://colah.github.io/posts/2015-08-Understanding-LSTMs/) supervised learning. As for the implementations, it is possible to use it in [Keras](https://keras.io/), [Theano](http://deeplearning.net/software/theano/). So basically the learning is done in two steps.

1. unsupervised training of $k$-mer embedding;
2. supervised learning with LSTM.

During all the talk I had the suspect that he had been reading all the time. Nevertheless, it was a nice example of usage of deep networks with string data. [Read more here](https://academic.oup.com/bioinformatics/article/33/14/i92/3953949/Chromatin-accessibility-prediction-via).

Unfortunately, the weather was very bad, and I did not have time to take any photos anyway. Bad day.
