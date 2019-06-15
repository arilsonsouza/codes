class Complement
  def self.of_dna(dna_strand)
    transcription = { G: 'C', C: 'G', T: 'A', A: 'U' }
    dna_strand.split('').map { |s| transcription[s.to_sym] }.join
  end
end