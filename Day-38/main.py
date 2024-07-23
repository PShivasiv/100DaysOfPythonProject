import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

moviesWeb = response.text
soup = BeautifulSoup(moviesWeb,"html.parser")

movieName = soup.find_all(name="h3",class_ = "listicleItem_listicle-item__title__BfenH")
MovieNameList = [name.getText() for name in movieName]
Movies = MovieNameList[::-1]


with open("E:/Python Udemy/Day-41/Top100movie/movie.txt","w") as file:
    for movie in Movies:
        file.write(f"{movie}\n")
