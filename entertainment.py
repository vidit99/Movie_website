import fresh_tomatoes
import media
'''9 instances of the Movie class to hold information of my favourite movies
 it has 5 arguments
1) has the movie name
2) has the director name of the movie
3) has the storyline of the movie
4) has the poster link of the movie
5) has the youtube trailer link of movie'''
toy_story = media.Movie("Toy Story 4", "John Lasseter",
                        "a story of boy and his toys come to life",
                        "https://upload.wikimedia.org/wikipedia/" +
                        "en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=Bj4gS1JQzjk")
aliens = media.Movie("Aliens", "James Cameron",
                     "Aliens is a 1986 American science-fiction action film",
                     "http://www.impawards.com/1986/posters/aliens_ver1.jpg",
                     "https://www.youtube.com/watch?v=bTCaVjQ8nU4")
avatar = media.Movie("Avatar", "James Cameron",
                     "a man with emotions",
                     "http://www.overthinkingit.com/wp-content/uploads" +
                     "/2009/12/avatar-poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY&t=10s")
raees = media.Movie("Raees", "Rahul Dholakia",
                    "It is the fictitious story of a man named Raees" +
                    ",set in 1980's in Gujarat",
                    "https://upload.wikimedia.org/wikipedia/en" +
                    "/2/2b/Raees_Poster.jpg",
                    "https://www.youtube.com/watch?v=J7_1MU3gDk0&t=23s")
pk = media.Movie("Pk", "Rajkumar Hirani",
                 "PK is a 2014 Indian satirical science fiction comedy film",
                 "http://ecx.images-amazon.com/images/I/81e" +
                 "fUbOf3%2BL._SY445_.jpg",
                 "https://www.youtube.com/watch?v=SOXWc32k4zA")
space_jam = media.Movie("Space Jam", "Joe Pytka",
                        "Fun Movie with Michael Jordan and Bugs Bunny",
                        "http://upload.wikimedia.org/wikipedia/" +
                        "en/1/14/Space_jam.jpg",
                        "https://www.youtube.com/watch?v=oKNy-MWjkcU")
kaabil = media.Movie("Kaabil", "Sanjay Gupta",
                     "It features a love affair between two blind people",
                     "https://i.ytimg.com/vi/O65JHeSDhuc/maxresdefault.jpg",
                     "https://www.youtube.com/watch?v=nubDFeiUAsI")
humari_adhuri_kahani = media.Movie("Humari Kahani", "Mohit Suri",
                                   "Hamari Adhuri Kahani is a  romantic" +
                                   "drama film directed by Mohit Suri ",
                                   "http://static.dnaindia.com/sites/def" +
                                   "ault/files/2015/05/04/333379-hak-1.jpg",
                                   "https://www.youtube.com/watch?v" +
                                   "=3EAr7FxgWps")
fight_club = media.Movie("Fight Club", "David Fincher",
                         "Fight Club is American film based on the n" +
                         "ovel of the same name",
                         "https://upload.wikimedia.org/wikipedia/en/f/fc" +
                         "/Fight_Club_poster.jpg",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
# variable which will contain instances of the movies
movies = [toy_story, aliens, avatar, raees, pk,
          space_jam, kaabil, humari_adhuri_kahani, fight_club]
fresh_tomatoes.open_movies_page(movies)
