dna1='GATATATGCATATACTT'
dna2='ATAT'
dict_dna1={}
dna2=list(dna2)
dna1=list(dna1)
for j in range(0, len(dna1)-3):
    dict_dna1[j]=dna1[j:j+4]
    #print(dict_dna1)
    if dict_dna1[j]==dna2:
       print(j)

