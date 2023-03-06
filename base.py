

class Game:
	def __init__(self, height, width):
		self.height = height
		self.width = width

	def board_matrix(self):
		self.matrix = [
			['+', '-', '-', '-', '+'],
			['|', None, None, None, '|'],
			['|', None, None, None, '|'],
			['|', None, None, None, '|'],
			['|', None, None, None, '|'],
			['+', '-', '-', '-', '+'],
		]
		return self.matrix     

	def render(self):
		matrix = self.board_matrix()
		for x in range(len(matrix)):
			for y in range(len(matrix[x])):
				mat = matrix[x][y]
				print(mat, end='')
		



game = Game(10, 20)
game.render()