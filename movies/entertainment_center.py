"""@package docstring
Documentation for the entertainment_center module
"""

import fresh_tomatoes
import media


# Create a Movie class with a movie title,
# description, poster link, youtube trailer link
toy_story = media.Movie("Toy Story",
                        "A story and his living toys.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Sherlock Holmes",
                     "The detective Sherlock Holmes and Dr.Watson try to foil a mysticist's plot.",
                     "https://upload.wikimedia.org/wikipedia/en/e/e0/Sherlock_holmes_ver5.jpg",
                     "https://www.youtube.com/watch?v=ZSUiBVfvqhc")

inception = media.Movie("Inception",
                        "A thief who steals secrets through dreams",
                        "https://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

transformers = media.Movie("Transformers",
                           "A teenager who gets caught up in a war between two factions of alien robots who can disguise themselves by transforming into everyday machinery.",
                           "https://upload.wikimedia.org/wikipedia/en/6/66/Transformers07.jpg",
                           "https://www.youtube.com/watch?v=zX81c2vycKo")

flashpoint = media.Movie("Flashpoint",
                         "A police sergeant who plants his partner as a mole in a pursuit against a triad.",
                         "https://upload.wikimedia.org/wikipedia/en/b/be/Flash_Point_poster.jpg",
                         "https://www.youtube.com/watch?v=NyOQw6YL93E")

ipman = media.Movie("Ip Man",
                    "A biographical martial arts film based on the life of Ip Man, Bruce Lee's master.",
                    "https://upload.wikimedia.org/wikipedia/en/2/2f/Ipmanposter02.jpg",
                    "https://www.youtube.com/watch?v=j77XMwc5bqg")

movies = [toy_story, avatar, inception, transformers, flashpoint, ipman]
fresh_tomatoes.open_movies_page(movies)  # Creates and loads the html page from the fresh_tomatoes module
