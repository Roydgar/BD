from producer import Producer
from producers import Producers
from movie import Movie
from movies import Movies
import menu
import pickle

def main():
	producers = Producers()
	movies = Movies()

	try :
		with open('producers.pickle', 'rb') as f:
			producers = pickle.load(f)
		with open('movies.pickle', 'rb') as f:
			movies = pickle.load(f)
	except EOFError as e:
		pass

	pid = len(producers.producers)
	mid = len(movies.movies)
	print("%d producers"%(pid))
	print("%d movies"%(mid))
	try:
		while (True):
			select = menu.mainManu()
			if (select == 1):				#show database
				print("\nAll producers:")
				print(producers)
				print("\nAll movies:")
				print(movies)
			elif(select == 2):				#add an producer
				pname = input("Producer name: ")
				producers.add(Producer(pid, pname))	
				pid += 1

			elif(select == 3):				#add a new item
				pname = input("Producer name: ")
				mname = input("Movie name: ")
				country = input("Country : ")
				c = producers.add(Producer(pid, pname))		

				if c > -1:
					movies.add(Movie(c, mid, mname, country,  producers))
				else:
					movies.add(Movie(pid, mid, mname, country,  producers))

				pid += 1
				mid += 1
			elif (select == 4):							#delete producer
				id = int(input("Enter producer id:"))
				producers.delete(id, movies)
			elif (select == 5):							#delete book
				id = int(input("Enter movie id:"))
				movies.delete(id)
			elif (select == 6):							#find all the producers by country
				country = input("Enter country: ")
				producers.searchByCountry(country, movies)
			elif (select == 0):
				break
	
	except Exception as e:
		print(e)		
	finally:
		with open('producers.pickle', 'wb') as f:
			pickle.dump(producers, f)
		with open('movies.pickle', 'wb') as f:
			pickle.dump(movies, f)
		
  
		
main()



	

