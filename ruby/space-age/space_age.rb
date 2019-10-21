class SpaceAge
 attr_reader :ageInSeconds, :planets

  def initialize(ageInSeconds)
    @ageInSeconds = ageInSeconds.to_f
    earthRevolution = 31557600

    @planets = { 
      earth: earthRevolution,
      mercury: earthRevolution * 0.2408467,
      venus: earthRevolution * 0.61519726,
      mars: earthRevolution * 1.8808158,
      jupiter: earthRevolution * 11.862615,
      saturn: earthRevolution * 29.447498,
      uranus: earthRevolution * 84.016846,
      neptune: earthRevolution * 164.79132,
    }

  end

  def on_earth
    puts calculateAge(planets[:earth]) 
    calculateAge(planets[:earth])
  end

  def on_mercury
    calculateAge(planets[:mercury])
  end

  def on_venus
    calculateAge(planets[:venus])
  end

  def on_mars
    calculateAge(planets[:mars])
  end
  
  def on_jupiter
    calculateAge(planets[:jupiter])
  end

  def on_saturn
    calculateAge(planets[:saturn])
  end

  def on_uranus
    calculateAge(planets[:uranus])
  end
  
  def on_neptune
    calculateAge(planets[:neptune])
  end

  private 
  def calculateAge(planetRevolution)
    ageInSeconds / planetRevolution
  end
  
end