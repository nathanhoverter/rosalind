import pattern_to_number

def computing_frequencies(text, k):
	frequency_array = []
	for i in range(0, 4**k):
		frequency_array.append(0)
	#return frequency_array
	for i in range(0, len(text) - k + 1):
		pattern = text[i:k+i]
		j = pattern_to_number.pattern_to_number(pattern, k)	
		frequency_array[j] = frequency_array[j] + 1
	return frequency_array



#list = computing_frequencies('CCATGAGGCATTTTGCTGGGGTGGAGAACTGATACACAGTGCGGGGTCAGCACGGGGATCCAGAACATCTACGCACAACTAGATCAATTGAGGGCCTGGAAAAACACCTTGCCTGGACGTTCGTTCAGATGAATTTTAGAACCGCCAAAACGTGGATTAGGCCAATGCCATTCCAACGTAATCGAACATATTATTTTTTGGATTTGGAATACCGGGTAGGAGGTCAGGAGGTAGACTTTTGAACCAGGACCTAGAACGATCAATATGTCGATTTCCGGGCGTTCAACCCGCCGGCGGCAAGGGGTAACGCGTGCGCCGCGGTGGCGTCCGTTTTGTGCTACCATGTGTACCTGCCTGTTCAGTTGGACATCAGCTGTGTTCACCAACTTCTTGCGTCCCAACGGCAAACCGGGCGTAGCGTGTTGGTGCCGAGCTGAGATTCCGTAGTGTTCATTCTGTGCAGCACCGCGATCCTTATGGAGTCTGACATACCTCGCGCTGAACCTATAAGAAAGGCTTAATACAAAGGCTAACCGGGCCTCAGATCTTTGACGGGACTGCCGAGTATGACCAAATTGCGGTTTCGTCTGATGGAACGGCTTCCGCTAAGTACCACTCCCGCGTTAAGCGTCCGCGATAACAGATCTAGGGTTCAGCATAGAGGGTCAGAGTTGGGGGGAAAGCGCAGCGCTTGTTCGGTTACGCCGAGTCTGTGAGAGATGCTCATCAGCCGCGTTTAGCTAATTTTTCTACACTTCTAGCAGCTGGGGCCTTCACCTAGCAGCCCCCTAATTATTC', 6)
#formatted_list = ' '.join(str(i) for i in list)
#print formatted_list