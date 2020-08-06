from copy import deepcopy

def main():
	box = [
		['b','b','u','s','u','s','o','s'],
		['n','o','b','s','e','s','u','n'],
		['u','e','u','u','u','b','s','o'],
		['s','n','n','n','o','b','s','n'],
		['s','u','b','o','s','u','n','e'],
		['o','s','u','n','n','s','b','u'],
		['b','u','s','e','u','b','u','o'],
		['e','n','o','n','n','u','s','n']
	]
	words = ['sun', 'bus', 'none']
	colors = [31, 32, 33]
	for i, w in enumerate(words):
		find(w, box, colors[i])

def find(word, box, color):
	word = word.lower()
	wlen = len(word)

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

	box_copy = deepcopy(box)
	for c in coords:
		update_box(box_copy, c, color)

	print(f'== FIND A WORD ==')
	print(f'Find : "{word}"')
	print(f'Found: {len(coords)}')
	print()
	for row in box_copy:
		print(' '.join(row))
	print()

	return len(coords), coords, box
	
def update_box(box, xy, color):
	x1, y1 = xy[0]
	x2, y2 = xy[1]
	length = max(abs(x2 - x1), abs(y2 - y1)) + 1

	for i in range(length):
		x = x1 if x1 == x2 else x1+i if x2 > x1 else x1-i
		y = y1 if y1 == y2 else y1+i if y2 > y1 else y1-i
		letter = box[x][y]
		box[x][y] = f'\033[4;{color};40m'+letter.upper()+'\033[0;37;40m'

class Word():
	pass


class Search():
	results = [
		'word': {
			'coords': [(x, y),  ..]
			'grid': [],
			'color': '',
			'style': '',
			'bg': '',
		}
	]
	results = {}

	def __init__(grid, words):
		self.grid = grid
		self.words = words

	def __str__(self):
		return self.grid

	def find(self):
		pass




if __name__ == '__main__':
	main()
