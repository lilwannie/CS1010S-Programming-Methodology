# CS1010S --- Programming Methodology
# Mission 11 Template

# Note that written answers are stored in """multi-line strings"""
# to allow us to run your code easily when grading your problem set.

import csv

def read_csv(csvfilename):
    rows = ()
    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows += (tuple(row), )
    return rows


##########
# Task 1 #
##########

def replicate(dna_strand):
    dna_base_pairings = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    new_reversed = dna_strand[::-1]
    new_string = ""
    for letter in new_reversed:
        letter = dna_base_pairings[letter]
        new_string += letter
    return new_string     
        

print("## Q1 ##")
print(replicate("AAATGC"))     # 'GCATTT'
print(replicate("ATTGGGCCCC")) # 'GGGGCCCAAT'

with open("dna.txt") as f:
    dna = f.read()
print(replicate(dna )[:10])    #'AATAGTTTCT'


##########
# Task 2 #
##########

def transcribe(dna_strand):
    dna_base_pairings = {
        "A": "U",
        "T": "A",
        "G": "C",
        "C": "G"
    }
    new_reversed = dna_strand[::-1]
    new_string = ""
    for letter in new_reversed:
        letter = dna_base_pairings[letter]
        new_string += letter
    return new_string 

def reverse_transcribe(rna_strand):
    rna_base_pairings = {
        "U": "A",
        "A": "T",
        "C": "G",
        "G": "C"
    }
    new_reversed = rna_strand[::-1]
    new_string = ""
    for letter in new_reversed:
        letter = rna_base_pairings[letter]
        new_string += letter
    return new_string 
    
    

print("## Q2 ##")
print(transcribe("AAATGC"))     # 'GCAUUU'
print(transcribe("ATTGGGCCCC")) # 'GGGGCCCAAU'

print(reverse_transcribe(transcribe("AAATGC"))) # 'AAATGC'
print(reverse_transcribe("GGGGCCCAAU"))         # 'ATTGGGCCCC'

rna = transcribe(dna)
print(rna[-10:])                # 'GAAUAUGUGA'


##########
# Task 3 #
##########

def get_mapping(csvfilename):
    csv_tuple = read_csv(csvfilename)[1::]
    get_codon = list(map(lambda x: x[0], csv_tuple))
    get_value = list(map(lambda x: x[3], csv_tuple))
    d = dict(zip(get_codon, get_value))
    # d = {'AAA': 'K', 'AAC': 'N', 'AAG': 'K',......}
    return d 
    
    

print("## Q3 ##")
codon2amino = get_mapping("codon_mapping.csv")

print(codon2amino["ACA"]) # 'T'
print(codon2amino["AUU"]) # 'I'
print(codon2amino["CUC"]) # 'L'
print(codon2amino["ACU"]) # 'T'
print(codon2amino["UAG"]) # '_'
print(codon2amino["UGA"]) # '_'


##########
# Task 4 #
##########
'''
In order of priority :

- What if the length of the strand is < 3?

- What if the start codon never exists in the first place?

- From the start codon, slice each 3 the RNA strand and map the respective codons to the abbreviations using the mapping function you have defined earlier in task 3.

- What if there aren't any of the end codons?
'''


def translate(rna_strand):
    codon2amino = get_mapping("codon_mapping.csv")
    start = "AUG"
    end1 = "UAA"
    end2 = "UAG"
    end3 = "UGA"
    if len(rna_strand) < 3: #if the length of the strand is less than 3 
        return None
    elif start not in rna_strand: #if start codon is non-existent in the rna strand 
        return None
    else: 
        get_start_index = rna_strand.find("AUG") #get the starting index of the string 
        rna_strand_start = rna_strand[get_start_index:] #slice the strand from the start 
        new = "" #create a new string for the protein coding 
        if (end1 in rna_strand_start) or (end2 in rna_strand_start)or (end3 in rna_strand_start) :
            for i in range(0,len(rna_strand_start),3):
                codon = rna_strand_start[i] + rna_strand_start[i+1] + rna_strand_start[i+2]
        
                if codon == end1 or codon == end2 or codon == end3:
                    new += "_"
                    break
                else:
                    new += codon2amino[codon]
            return new
        
        else:
            return None 
    
        
        
                
            
            
            
        
    

print("## Q4 ##")
print(translate("AUGUAA"))           # 'M_'
print(translate("AGAGAUGCCCUGAGGG")) # 'MP_'

protein = translate(rna)
print(protein) # 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_'
print(protein == 'MANLTNFHLKIYIHTYIQLKHLSSGAFSLFSAHNSRSINYNYYFSFRDLNITYNHTHLTTY_') # True


##########
# Task 5 #
##########

'''
Answer here.
State which is the better implementation.
Show difference in the time and space complexities.
'''
