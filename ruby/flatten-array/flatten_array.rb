class FlattenArray
  def self.flatten(array, result = [])
    array.each do |item|
      if item.class == Array
        flatten(item, result)
      elsif !item.nil?
        result << item
      end
    end
    result
  end
end