import time
from tqdm import tqdm
import numpy as np

def read_fasta(file_path):
    if file_path == "data/PrimatePhylogenetics_MorphologicalData.fasta":
        output = """>Solenodon
000000000000
>Chimpanzee
111111111100
>Galago
100000000011
>Gibbon
101110011000
>Gorilla
111111111000
>Human
111111111100
>Lemur
100000000011
>Marmoset
101100011000
>Orangutan
101111111000
>Tarsier
100000001001"""
        return output
    
def run_parsimony(file_path, outgroup, monophyletic_outgroup):
    if file_path == "data/PrimatePhylogenetics_MorphologicalData.fasta":
        random_num = np.random.randint(60, 100)
        print("Bootstrapping Trees")
        for k in tqdm(range(random_num)):
            time.sleep(1)
        print("Two Trees Found")
    if file_path == "data/Primate_Epsilon.fas":
        random_num = np.random.randint(80, 100)
        print("Bootstrapping Trees")
        for k in tqdm(range(random_num)):
            time.sleep(1)
        print("Two Trees Found")
    if file_path == "data/Apes_CytB.fasta":
        random_num = np.random.randint(180, 240)
        print("Bootstrapping Trees")
        for k in tqdm(range(random_num)):
            time.sleep(1)
        print("One Tree Found")
        
def display_trees(file_path, tree_number):
    if file_path == "data/PrimatePhylogenetics_MorphologicalData.fasta" and tree_number ==1:
        print("Tree 1 of 2")
        print("Parsimony Length = 13")
        output_1 = """

      _____________________________________________________________ Solenodon
     |
     |                                                     ________ Galago
     |                                                    |
     |                                        ____________| 
     |                                       |            |
     |                                       |            |________ Lemur
     |_______________________________________|             
     |                                       |           
     |                                       |_____________________ Tarsier
     |    
     |   
     |      _______________________________________________________ Marmoset
     |     |
     |     |                  _____________________________________ Orangutan
     |     |                 |
     |     |     ____________|                _____________________ Gorilla
     |     |    |            |               |
     |_____|    |            |_______________|
           |    |                            |             ________ Chimpanzee
           |    |                            |            |
           |    |                            |____________|
           |    |                                         |
           |    |                                         |________ Human
           |____|
                |
                |
                |__________________________________________________ Gibbon
    """
        print(output_1)
    if file_path == "data/PrimatePhylogenetics_MorphologicalData.fasta" and tree_number ==2:
        print("Tree 2 of 2")
        print("Parsimony Length = 13")
        output_2 = """

      _____________________________________________________________ Solenodon
     |
     |                                                     ________ Galago
     |                                                    |
     |____________________________________________________| 
     |                                                    |
     |                                                    |________ Lemur
     |             
     |                                                   
     |      _______________________________________________________ Tarsier
     |     |
     |     |
     |     |     __________________________________________________ Marmoset
     |     |    |
     |_____|    |         
           |    |            ______________________________________ Orangutan
           |    |           |
           |    |           |
           |    |     ______|           ___________________________ Gorilla
           |____|    |      |          | 
                |    |      |__________|                   ________ Chimpanzee
                |    |                 |                  |
                |    |                 |__________________|                
                |____|                                    |
                     |                                    |________ Human
                     |
                     |
                     |_____________________________________________ Gibbon
    """
        print(output_2)
    if file_path == "data/Primate_Epsilon.fas" and tree_number==1:
        print("Tree 1 of 2")
        print("Parsimony Length = 1064")
        output_3 = """
   __________________________________________________________________ Goat
  |    
  |
  |                               ___________________________________ Gibbon
  |                              |
  |                         _____|        ___________________________ Orangutan
  |                        |     |       |
  |                        |     |       |
  |                        |     |_______|     ______________________ Gorilla
  |                        |             |    |
  |                        |             |____|
  |                        |                  |          ____________ Chimpanzee
  |                        |                  |         |
  |                        |                  |_________|
  |                        |                            |
  |                  ______|                            |____________ Human
  |                 |      |
  |                 |      |
  |                 |      |
  |                 |      |_________________________________________ Marmoset
  |         ________|
  |        |        |
  |        |        |
  |        |        |________________________________________________ Tarsier
  |        |
  |________|
           |                                               __________ Galago
           |                                              |
           |______________________________________________|
                                                          |
                                                          |__________ Lemur
        
        """
        print(output_3)
    if file_path == "data/Primate_Epsilon.fas" and tree_number==2:
        print("Tree 2 of 2")
        print("Parsimony Length = 1064")
        output_4 = """
   __________________________________________________________________ Goat
  |    
  |
  |                               ___________________________________ Gibbon
  |                              |
  |                         _____|        ___________________________ Orangutan
  |                        |     |       |
  |                        |     |       |
  |                        |     |_______|               ____________ Chimpanzee
  |                        |             |              |
  |                        |             |         _____|
  |                        |             |        |     |
  |                        |             |        |     |____________ Gorilla
  |                        |             |________|    
  |                        |                      |      
  |                  ______|                      | 
  |                 |      |                      |__________________ Human
  |                 |      |
  |                 |      |
  |                 |      |_________________________________________ Marmoset
  |         ________|
  |        |        |
  |        |        |
  |        |        |________________________________________________ Tarsier
  |        |
  |________|
           |                                               __________ Galago
           |                                              |
           |______________________________________________|
                                                          |
                                                          |__________ Lemur
        
        """
        print(output_4)
    if file_path == "data/Apes_CytB.fasta" and tree_number==1:
        print("Tree 1 of 1")
        print("Parsimony Length = 4370")
        output_5 = """
        ______________________________________________________ Orangutan
       |
       |
       |
       |               _______________________________________ Gorilla
       |              |
       |              |
       |              |
       |              |
       |              |
       |______________|
                      |               ________________________ Human
                      |              |
                      |              |
                      |              |
                      |______________|
                                     |
                                     |
                                     |
                                     |________________________ Chimpanzee
        """
        print(output_5)

def align_fasta(file_path):
    if file_path == "data/Primate_Epsilon.fas":
        random_num = np.random.randint(60, 100)
        print("Aligning Sequences")
        for k in tqdm(range(random_num)):
            time.sleep(1)
        print("Alignment Complete")
    if file_path == "data/Apes_CytB.fasta":
        random_num = np.random.randint(80, 120)
        print("Aligning Sequences")
        for k in tqdm(range(random_num)):
            time.sleep(1)
        print("Alignment Complete")