class Animal:
	noise = "Rrrr"
	def make_noise(self):
		print(f"{self.noise}")

	def set_noise(self, new_noise):
		self.noise = new_noise

	def get_noise(self):
		return self.noise


class Wolf(Animal):
	noise = 'grrrr'