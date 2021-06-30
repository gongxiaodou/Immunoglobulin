# Immunoglobulin
   To establish a benchmark dataset, the following steps will be taken. Protein sequences containing the nonstandard amino acid characters"B", "J", "O", "X", "Z" were first removed. Second to avoid overfitting caused by homology bias and to reduce redundancy, the CD-Hit program was chosen to set a 60% sequence identity cutoff to remove highly similar sequences. Finally, if a certain protein sequence was a subsequence of other proteins it was also removed. Considering that to avoid the influence of the expression of different protein sequences on the predicted effects, we selected only human, mouse, and rat samples.  For the benchmark dataset, the sequence information of 109 immunoglobulins was stored in the ip.fasta file. Meanwhile, the sequence information of 119 non-immunoglobulins is stored in the in.fasta file.  In order to study the generalization ability of the model, one hundred and eighty four samples were randomly selected from the benchmark data set for training. Forty-four sequences were used as an independent test set, including twenty two immunoglobulin sequences and twenty two non-immunoglobulin sequences.
# monoTrikGap
monoTriKGap Theoretical Description:
  When -kgap=n then the (20) × (20 × 20 × 20) × n features will exist for protein.
  When -kgap=1, feature structure will be X_XXX.
  When -kgap=2, feature structure will be X_XXX, and X_ _XXX.
  When -kgap=3, feature structure will be X_XXX, X_ _XXX, and X_ _ _XXX.
  X={A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y}.In this study, k=1.
Command for generate dataset only monoTriKGap method:
  Python main.py  -fa=/home/gongxiaodou/Datasets/Protein/7.fasta  -la=/home/gongxiaodou/Datasets/Protein/Lable.txt  -full=1  -optimum=1 -f13=1 -kgap=1
  Full = 1 where the parameters that do not want to save the complete set of data, optimum = 1 that do not want to save the best data set and the generated pseudo = 1 represents a feature.
# CC-PSSM
  This method first uses the pssm.py file to compare the input protein sequence with the blast to obtain the pssm matrix, then uses the cut-pssm.py file to intercept the first 20 columns of the matrix, and finally uses the test_calcCCPSSM.py file for profile-based Cross covariance (CC-PSSM) to calculate and extract the features of each protein sequence.
