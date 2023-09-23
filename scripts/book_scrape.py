import os
import json
import requests
from book_sorter import book_sorter

with open('isbns.json','r', encoding='utf-8') as data:
	raw_data = data.read()

	isbn_data = json.loads(raw_data)
	isbn_list = isbn_data["isbns"]
	done_list = isbn_data["done"]
	books_list = []

	search_url = r'https://openlibrary.org/api/books?bibkeys={}&jscmd=data&format=json'
	fina_list = list(set(isbn_list)-set(done_list))
	#print(fina_list)
	if len(fina_list) > 0:
		try:
			os.remove('../data/books.json')
		except Exception as e:
			pass
			#print('Books Deleted ' + e)
	else:
		with open('../data/books.json','w', encoding='utf-8') as edited_book_list:
			edited_book_list.write(json.dumps(isbn_data["books"], indent=4, ensure_ascii=False))
			edited_book_list.close()
			book_sorter()

	for isbn in fina_list:
		print(search_url.format(isbn) + "\n")
		try:
			r = requests.get(search_url.format(isbn))
			book = {}
			book_data = {}
			response = r.json()[isbn]
			book_data['title'] = response['title']
			book_data['isbn'] = isbn
			book_data['book_url'] = response['url']
			book_data['author_data'] = response['authors'][0]
			book_data['cover'] = response['cover']['medium']
			print(book_data['title'] + ": Enter Completed Date - (Ex. Jun, 2013) (Default - Reading)\n")
			print("Completed Date : " )
			completed = input()
			if completed == '':
				completed = 'Reading'
			print(book_data['title'] + ": Enter Rating on 5 - (Ex. 3) (Default - 0)\n")
			rating = input()
			if rating == '':
				rating = 0 
			book_data['completed'] = completed
			book_data['rating'] = float(rating)

			book[isbn] = book_data
			#print(book_data)
			books_list.append(book_data)
		except requests.exceptions.Timeout as etime:
			pass #Increase ISBN index
		except requests.exceptions.RequestException as ereq:
			pass #Increase ISBN index
		except KeyError as e:
			print(e)

	if (len(fina_list) > 0):
		isbn_data["done"].extend(fina_list)
		isbn_data["books"].extend(books_list)
	data.close()

if (len(fina_list) > 0):
	with open('isbns.json','w', encoding='utf-8') as data:
		data.write(json.dumps(isbn_data, indent=4, ensure_ascii=False))
		data.close()
	with open('../data/books.json','w', encoding='utf-8') as data:
		data.write(json.dumps(isbn_data["books"], indent=4, ensure_ascii=False))
		data.close()
		book_sorter()
