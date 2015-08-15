import media
import fresh_tomatoes

reload (fresh_tomatoes)

movies = [
            media.Movie ("Rainman",
                         "A playboy and his autistic brother roadtrip down the West Coast.",
                         "1988",
                         "Tom Cruise",
                         "http://ia.media-imdb.com/images/M/MV5BMTQ4NTA1NDU3NV5BMl5BanBnXkFtZTcwODUwMTU2NA@@._V1_SX640_SY720_.jpg",
                         "https://www.youtube.com/watch?v=KKC3W0awjm0"),
            media.Movie ("Platoon",
                         "A young soldier must choose between his two Platoon leaders.",
                         "1986",
                         "Charlie Sheen",
                         "http://www.gstatic.com/tv/thumb/movieposters/9665/p9665_p_v7_aa.jpg",
                         "https://www.youtube.com/watch?v=hGsyEkfjhQk"),
            media.Movie ("Apocalypse Now",
                         "In Vietnam in 1970, Captain Willard (Martin Sheen) takes a perilous and increasingly hallucinatory journey upriver to find and terminate Colonel Kurtz.",
                         "1979",
                         "Martin Sheen",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcT9GtFRvwy8cYE2gjMTzfR0MW_ubpZ_dcD0S2CkfTqBoiobgwFv",
                         "https://www.youtube.com/watch?v=IkrhkUeDCdQ")
        ]

# debugging
##for movie in movies:
##    print movie.lead_actor
##    print movie.release_date
    

fresh_tomatoes.open_movies_page (movies)
