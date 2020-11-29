import os
import json
from datetime import datetime,date
from dateutil import parser

def book_sorter():
	with open('../data/books.json','r', encoding='utf-8') as data:
		raw_data = data.read()
		x = []
		books = json.loads(raw_data)
		sorted_books = []
		read_index = []

		# Iterate All Books in isbn data from Books Key
		# Extract Books in Reading Phase
		# x -> List with all book completed Dates
		for idx, book in enumerate(books):
			if book['completed'].lower().strip() == 'reading':
				read_index.append(idx)
				continue
			x.append(book['completed'])

		# Sort the available dates using dateutil.parser
		non_sorted_dates = x
		x_timestamps = list(map(lambda datte: parser.parse(datte), x))

		# Sort using Sorted <Descending>
		# date.strftime() -> Reformatting as per previous String
		x_timestamps = sorted(x_timestamps, reverse=True)
		sorted_dates = list(map(lambda datte: datte.strftime("%b, %Y"), x_timestamps))
		#print(len(non_sorted_dates), len(sorted_dates))

		# Push the 'Books in Reading Phase'
		for idx,i in enumerate(read_index):
			sorted_dates.insert(idx, 'Reading')
			non_sorted_dates.insert(i, 'Reading')

		# Insert into a new list in a sorted Fashion
		# Unsorted List - Capture the value using the index from sorted List
		# Then mark 'XXX' for extracted dates
		for date in sorted_dates:
			idx = non_sorted_dates.index(date)
			non_sorted_dates[idx] = 'XXX'
			sorted_books.append(books[idx])

		data.close()

	with open('../data/books.json','w', encoding='utf-8') as data:
		data.write(json.dumps(sorted_books, indent=4, ensure_ascii=False))
		data.close()

if __name__ == '__main__':
	book_sorter()