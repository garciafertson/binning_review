Improved metagenome binning and assembly using deep variational autoencoders
Nature biotechnology - 4th Jan 2021

It is still difficul to discern microbial species from metagenomics data.
The article discussed a program called variational autoencoders for metagenomic binning that uses deep variational autoencoders to encode sequence coabundance and k-mer distribution information BEFORE clustering. 

autoencoders
a kind of machine learning algorythm that encodes (compresses), decodes, then compares to the original to see if they are similar (with traditional neural network archetectures)

variational autoencoders
the same but use the mean and standard deviation in the middle nodes instead

disentangled variational autoencoders
google deepmind - tries to separate nodes - uses less variables - extracts causal features
in the future you could use this for reinforcement learning
