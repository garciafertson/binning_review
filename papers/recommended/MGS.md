# Identification and assembly of genomes and genetic elements in complex metagenomic samples without using reference genomes
* binning (metagenomics) is the process of grouping reads or contigs and assigning them to individual genomes.
* CAG - Coabundant gene groups - like coevolution - present between organisms e.g. human and gut microbiome - usually a single species - wider than a gene, smaller than a full genome
* MGS - Metagenomic species - subset of CAG
* WGS - whole-genome shotgun - a method of microbiome sequencing - having reads of 500 bp is enough to determine species/strain of the organism where the DNA comes from using K-mer taxonomic classifier software.
* Contig - comes from the word contiguous which means next to each other (as opposed to continuous which means never ending) - a set of overlapping DNA segments that represent a consensus region of DNA

A method that accounts for the microbial diversity of environments without knowing all the reference genome databases (as the diversity of the gut is over 1000 different species and millions of genes plus even bacteria in the same species can show massive heterogeneity) and aids the assembly of microbial genomes without the need for reference sequences.
Allows the complete co-abundance clustering of microbiomes.
this is needed as we dont know all species, and inaccurate discrimination among closely related species can lead to false associations between clinical conditions and putative species.

It used to be that de novo assembly of genomes was difficult due to the large number of contigs that were not easily aggregated into species
Previous attempts at solutions included:
	Tetranucleotide distributions (how many times the contigs use a particular base) - this is only good for species that have extreme base compositions
	Abundance of sequence distributions - just assume that each genome has one copy of the gene and turn that into abundance
Structuring is important for making statistical associations between the metagenomic data and descriptors of the system
These descriptors can be clinical parameters (liver disease etc)
The paper assignes the genes from 396 samples (fastaq's) into 7381 CAGs, binning them into MGS and phage-like CAGs.
From the MGS, 238 unique genomes were assembled.
Comprehensive co-abundace gene segregation
	made a gene catalog of fastaq - picked a gene at random as a seed, looked for other genes with similar abundace profiles (called canopy) that had the pearsons CC of above 0.9 to the seed gene profile. Then the canopy profile was filetered for quality and identified as a CAG - removing it from the dataset. 32% of the genes were lost to the filtering.
	CAG's with 700+ genes were reffered to as MGS with several distinct MGS from the same species
	MGS and GAC show a detailed overview of the microbial community and makes good estimates of the species richness that are in strong agreement with the observed gene richness
Genome assembly
	By segregating the genes into species (binning) better, we are better able to assemble the genomes
	This process is called MGS-augmented assembly
	there is an issue of making chimeric assemblies of closely related strains - mitigated by only using sequence reads from a single sample.
Functional characterization of small CAGs
	Small CAGs were maily phage-like, those functions that were important for biotic interactions (CRISPR), and modificaiton of bacteiral cell surfaces
Dependency associations affiliate small CAGs to MGS
	The existance of phage small CAGs impolies other cellular organisms for proliferation
	There therefore was significant dependency between them (using Fishers exact test - https://www.youtube.com/watch?v=udyAvvaMjfM)
	the presence of one of the CRISPR and phage like CAGs were anticorrolated suggesting that the CRISPR prevents the phage from infrecting the bacterium
MGS persitence is influenced by associated CAGs
	looked at MGS longitudinal change
	found that there was a greater probability of B adeolescentis persisting at the second time poitn when CAG2298 was present proven by logistic regression and bayesian statistical methods - a posterior probailitity distribution over the possible annual persisence probabilities.
	the greater probability causing CAG contained CRISPR genes, collagen adhesion protein, and gram pos anchor proteins, and thioredoxin family proteins that might be important for the tolerance of reactive oxygen species - a must have for human gut microbiome proteins.
	also ten other CAGs had a negative effect on the persistance probability of their hosting MGS
	three phage like CAGs caused this
Discussion
	most genes involved in resistance to antibiotics (cept vancomycin) were not found as members of any CAG - due to the fact that most antibiotic genes, are known to act alone to provide antibiotic resistance)
	even small cags are important
