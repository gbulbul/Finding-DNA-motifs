class find_motif_in_DNA1:
    def search_over_DNA1(dna1,dna2):
        for i in range(len(dna1)-3):
                if dna1[i:i+4]==dna2:
                    print(i)
       
if __name__=="__main__":
    dna1='GATATATGCATATACTT'
    dna2='ATAT'
    find_motif_in_DNA1.search_over_DNA1(dna1,dna2)

