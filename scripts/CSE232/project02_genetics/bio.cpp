#include "bio.h"
#include <algorithm>
#include <iostream>
#include <iterator>
#include <string>
#include <vector>

bool IsValidDNASequence(const std::string &input) {
  for (char c : input) {
    if ((c != 'A') && (c != 'T') && (c != 'G') && (c != 'C')) {
      return false;
    }
  }
  return true;
}

void GetReverseComplementSequence(const std::string &input,
                                  std::string *const output) {
  std::string new_input = input;
  std::reverse(new_input.begin(), new_input.end());
  std::string &compl_seq = *output;
  for (char &c : new_input) {
    if (c == 'A') {
      compl_seq += 'T';
    } else if (c == 'T') {
      compl_seq += 'A';
    } else if (c == 'C') {
      compl_seq += 'G';
    } else if (c == 'G') {
      compl_seq += 'C';
    }
  }
}

std::string GetRNATranscript(const std::string &input) {
  std::string new_input = input;
  std::reverse(new_input.begin(), new_input.end());
  std::string rna_seq;
  for (char &c : new_input) {
    if (c == 'A') {
      rna_seq += 'U';
    } else if (c == 'T') {
      rna_seq += 'A';
    } else if (c == 'C') {
      rna_seq += 'G';
    } else if (c == 'G') {
      rna_seq += 'C';
    }
  }
  return rna_seq;
}

std::vector<std::vector<std::string>>
GetReadingFramesAsCodons(const std::string &input) {
  std::string rna_seq = GetRNATranscript(input);
  std::string anti_rna_seq;
  for (char &c : rna_seq) {
    if (c == 'U') {
      anti_rna_seq += 'A';
    } else if (c == 'A') {
      anti_rna_seq += 'U';
    } else if (c == 'G') {
      anti_rna_seq += 'C';
    } else if (c == 'C') {
      anti_rna_seq += 'G';
    }
  }
  std::reverse(anti_rna_seq.begin(), anti_rna_seq.end());
  std::vector<std::vector<std::string>> codons_library;
  std::vector<std::string> codons_vecter_ori, codons_vecter_anti;
  std::string codons_ori, codons_anti;
  // Original
  // set the while loop to go through 3 bases at a time
  int count_set_ori = 0;
  while (count_set_ori < 3) {
    count_set_ori += 1;
    std::string copy_ori = rna_seq;
    // get codons corresponding to the original rna sequence
    while (static_cast<int>(size(copy_ori)) >= 3) {
      for (int i = 0; i < 3; i++) {
        codons_ori += copy_ori.at(i);
      }
      codons_vecter_ori.push_back(codons_ori);
      codons_ori = "";
      // remove the current first 3 bases to get the next 3 bases in
      // the next loop
      copy_ori.erase(0, 3);
    }
    // store codons in the codon library (a string vetor containing codons)
    codons_library.push_back(codons_vecter_ori);
    codons_vecter_ori.clear();
    // remove the first base to move to the next possible pattern we considered
    rna_seq.erase(0, 1);
  }
  // Antiparallel
  // set the while loop to go through 3 bases at a time
  int count_set_anti = 0;
  while (count_set_anti < 3) {
    count_set_anti += 1;
    std::string copy_anti = anti_rna_seq;
    // get codons corresponding to the antiparallel rna sequence
    while (static_cast<int>(size(copy_anti)) >= 3) {
      for (int i = 0; i < 3; i++) {
        codons_anti += copy_anti.at(i);
      }
      codons_vecter_anti.push_back(codons_anti);
      codons_anti = "";
      // remove the current first 3 bases to get the next 3 bases in
      // the next loop
      copy_anti.erase(0, 3);
    }
    // store codons in the codon library (a string vetor containing codons)
    codons_library.push_back(codons_vecter_anti);
    codons_vecter_anti.clear();
    // remove the first base to move to the next possible pattern we considered
    anti_rna_seq.erase(0, 1);
  }
  return codons_library;
}
// I learnt how to use range to find corresponding amino acids for each codons
// from https://piazza.com/class/k4wvjqt9b2x72k?cid=786
// This function was written to convert each codon into its corresponding
// amino acids
char find_cor_codons(std::string ccodon) {
  std::vector<std::string> codons_code = {
      "GCU", "GCC", "GCA", "GCG", "CGU", "CGC", "CGA", "CGG", "AGA", "AGG",
      "AAU", "AAC", "GAU", "GAC", "UGU", "UGC", "CAA", "CAG", "GAA", "GAG",
      "GGU", "GGC", "GGA", "GGG", "CAU", "CAC", "AUU", "AUC", "AUA", "UUA",
      "UUG", "CUU", "CUC", "CUA", "CUG", "AAA", "AAG", "AUG", "UUU", "UUC",
      "CCU", "CCC", "CCA", "CCG", "UCU", "UCC", "UCA", "UCG", "AGU", "AGC",
      "ACU", "ACC", "ACA", "ACG", "UGG", "UAU", "UAC", "GUU", "GUC", "GUA",
      "GUG", "UAG", "UGA", "UAA"};
  std::vector<char> amino_acids = {
      'A', 'A', 'A', 'A', 'R', 'R', 'R', 'R', 'R', 'R', 'N', 'N', 'D',
      'D', 'C', 'C', 'Q', 'Q', 'E', 'E', 'G', 'G', 'G', 'G', 'H', 'H',
      'I', 'I', 'I', 'L', 'L', 'L', 'L', 'L', 'L', 'K', 'K', 'M', 'F',
      'F', 'P', 'P', 'P', 'P', 'S', 'S', 'S', 'S', 'S', 'S', 'T', 'T',
      'T', 'T', 'W', 'Y', 'Y', 'V', 'V', 'V', 'V', '*', '*', '*'};
  // find the position of ccodon in amino_acids
  auto p = std::find(std::begin(codons_code), std::end(codons_code), ccodon);
  // find the distance from the beginning
  auto d = std::distance(std::begin(codons_code), p);
  // find the corresponding location in amino_acids
  return amino_acids[d];
}

std::string Translate(const std::vector<std::string> &codon_sequence) {
  std::string amio_seq;
  // use find_cor_codons(std::string ccodon) to convert codons to amino acids
  for (int index = 0; index < static_cast<int>(size(codon_sequence)); index++) {
    std::string ccodon = codon_sequence[index];
    amio_seq += find_cor_codons(ccodon);
  }
  return amio_seq;
}

std::string GetLongestOpenReadingFrame(const std::string &DNA_sequence) {
  std::vector<std::vector<std::string>> codons_library =
      GetReadingFramesAsCodons(DNA_sequence);
  int pos_m = 0, pos_ast = 0, len = 0, longest_len = 0;
  std::string strand, longest_strand;
  // loop through each amino acid sequence
  for (int row = 0; row < static_cast<int>(size(codons_library)); row++) {
    std::string amino_seq = Translate(codons_library[row]);
    // loop through each codons within a particular amino acid sequence
    for (int i = 0; i < static_cast<int>(size(amino_seq)); i++) {
      // seek for the position of 'M' (strat codons) to start the strand
      if (amino_seq[i] == 'M') {
        pos_m = i;
        len++;
        // loop through the characters next to 'M' until it hits '*'
        // keep track of the length of each strand by the variable named "len"
        // (stop codons) and save '*' 's position
        for (int n = 1; n < (static_cast<int>(size(amino_seq)) - pos_m - 1);
             n++) {
          len++;
          if (amino_seq[pos_m + n] == '*') {
            pos_ast = pos_m + n;
            // compare length to the longest strand we have before
            if (len > longest_len) {
              longest_len = len;
              strand = amino_seq.substr(pos_m, pos_ast - pos_m + 1);
              if (static_cast<int>(size(strand)) >
                  static_cast<int>(size(longest_strand))) {
                longest_strand = strand;
              }
            }
            break;
          }
        }
      }
    }
  }
  return longest_strand;
}
