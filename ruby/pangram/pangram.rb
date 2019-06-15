class Pangram
  def self.pangram?(sentence)
    sentence.downcase!
    ('a'..'z').all? { |char| sentence.include?(char) }
  end
end