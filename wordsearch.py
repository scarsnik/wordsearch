import os
import random

def main():
	file = os.path.join(os.getcwd(), 'grid2.txt')
	grid1 = WordSearch(file)
	print(grid1)


class WordSearch:
	colors = list(range(1, 256))
	random.shuffle(colors)

	def __init__(self, filename):
		self.gridfile = filename
		grid, words = self.parse_file()
		self.grid = grid
		self.words = words
		self.coords = {}
		self.solution = self.find_words()

	def __str__(self):
		s = ''
		for row in self.grid:
			s += f'{" ".join(row)}\n'
		s += '\n'
		for index, word in enumerate(self.words):
			s += u'\u001b[38;5;' + str(self.colors[index]) + 'm' + word.upper() + ' (' + str(len(self.coords[word])) + ')\u001b[0m\n'
		return s

	def parse_file(self):
		grid, words = [], []
		rows = 0
		with open(self.gridfile, 'r') as gridfile:
			for line, data in enumerate(gridfile):
				if line == 0:
					rows = int(data.strip())
				elif line <= rows:
					grid.append(list(data.strip()))
				else:
					words.append(data.strip())
		return grid, words
	
	def find_words(self):
		for word in self.words:
			self.coords[word] = self.get_cooords(word)

		for index, word in enumerate(self.words):
			for coord in self.coords[word]:
				self.update_grid(coord, self.colors[index])

	def get_cooords(self, word):
		word = word.lower()
		wlen = len(word)
		box = self.grid

		coords = []
		for i, r in  enumerate(box):
			for j, c in enumerate(r):
				right = j <= (len(r) - len(word))
				down = i <= (len(box) - len(word))
				up = i >= len(word) - 1
				left = j >= len(word) - 1
		
				if up and word == ''.join([box[i-x][j].lower() for x in range(wlen)]):
					xy = [(i, j), (i-wlen+1, j)]
					coords.append(xy)
				if up and right and word == ''.join([box[i-x][j+x] for x in range(wlen)]):
					xy = [(i, j), (i-wlen+1, j+wlen-1)]
					coords.append(xy)
				if right and word == ''.join([box[i][j+x] for x in range(wlen)]):
					xy = [(i, j), (i, j+wlen-1)]
					coords.append(xy)
				if right and down and word == ''.join([box[i+x][j+x] for x in range(wlen)]):
					xy = [(i, j), (i+wlen-1, j+wlen-1)]
					coords.append(xy)
				if down and word == ''.join([box[i+x][j] for x in range(wlen)]):
					xy = [(i, j), (i+wlen-1, j)]
					coords.append(xy)
				if down and left and word == ''.join([box[i+x][j-x] for x in range(wlen)]):
					xy = [(i, j), (i+wlen-1, j-wlen+1)]
					coords.append(xy)
				if left and word == ''.join([box[i][j-x] for x in range(wlen)]):
					xy = [(i, j), (i, j-wlen+1)]
					coords.append(xy)
				if left and up and word == ''.join([box[i-x][j-x] for x in range(wlen)]):
					xy = [(i, j), (i-wlen+1, j-wlen+1)]
					coords.append(xy)
		return coords

	def update_grid(self, coord, color):
		x1, y1 = coord[0]
		x2, y2 = coord[1]
		length = max(abs(x2 - x1), abs(y2 - y1)) + 1

		for i in range(length):
			x = x1 if x1 == x2 else x1+i if x2 > x1 else x1-i
			y = y1 if y1 == y2 else y1+i if y2 > y1 else y1-i
			letter = self.grid[x][y]
			if len(letter) == 1:
				self.grid[x][y] = u'\u001b[38;5;' + str(color) + 'm' + letter.upper() + '\u001b[0m'
			


if __name__ == '__main__':
	main()
