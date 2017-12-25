'''
want to make a class called Movie:
-data: title, youtube_trailer, reviews, storyline, poster_image
title
storyline
'''

import media
import fresh_tomatoes

# media. = file; .Movie = class from file
fight_club = media.Movie('Fight Club',
                        """The narrator meets a mysterious man and begins a
                        Fight Club.""",
                        'https://images-na.ssl-images-amazon.com/images/I/5190cUTcbZL._SY445_.jpg',
                        'https://www.youtube.com/watch?v=BdJKm16Co6M',
                        'US Release Date: September 10, 1999',
                        'Budget: $63 million',
                        'Box Office: $100.9 million')

gny = media.Movie('Gangs of New York',
                """The film follows fictional gang leader Bill \'The Butcher\'
                Cutting in his roles as crime boss and political kingmaker.""",
                'https://images-na.ssl-images-amazon.com/images/I/51bTWMS2nNL._SY450_.jpg',
                'https://www.youtube.com/watch?v=qHVUPri5tjA',
                'US Release Date: December 20, 1999',
                'Budget: $100 million',
                'Box Office: $193.8 million')

tropic_thunder = media.Movie('Tropic Thunder',
                        """A group of prima donna actors make a fictional
                        Vietnam War film. When their frustrated director drops
                        them in the middle of the jungle, they are forced to
                        rely on their acting skills to survive the real action
                        and danger.""",
                        'https://images-na.ssl-images-amazon.com/images/M/MV5BNDE5NjQzMDkzOF5BMl5BanBnXkFtZTcwODI3ODI3MQ@@._V1_UY1200_CR112,0,630,1200_AL_.jpg',
                        'https://www.youtube.com/watch?v=T-6YhRZowgc',
                        'US Release Date: August 13, 2008',
                        'Budget: $92 million',
                        'Box Office: $188.1 million')

zoolander = media.Movie('Zoolander',
                """Zoolander features a dimwitted, narcissistic male model named
                Derek Zoolander who becomes the pawn of corrupt fashion
                executives who are plotting to assassinate the Prime Minister of
                Malaysia.""",
                'https://karlovicm.files.wordpress.com/2011/02/zoolander-poster.jpg',
                'https://www.youtube.com/watch?v=YtQq0T3ExLs',
                'US Release Date: September 28, 2001',
                'Budget: $28 million',
                'Box Office: $60.8 million')

monsters_inc = media.Movie('Monsters, Inc.',
                        """The film centers on two monsters employed at the
                        titular energy-producing factory Monsters, Inc.: top
                        scarer James P. "Sulley" Sullivan and his one-eyed
                        partner and best friend Mike Wazowski. In the film,
                        employees at Monsters, Inc. generate their city's power
                        by scaring children, but they themselves are afraid that
                         the children are toxic to them, and when one child
                         enters the factory, Sulley and Mike must return her
                         home before it is too late.""",
                        'https://i.pinimg.com/originals/bb/44/ae/bb44ae2a5a5003d0abd921f80541ff74.jpg',
                        'https://www.youtube.com/watch?annotation_id=annotation_24492&feature=iv&src_vid=cvOQeozL4S0&v=Ue_SfrHHBAc',
                        'US Release Date: November 2, 2001',
                        'Budget: $115 million',
                        'Box Office: $577.4 million')

finding_nemo = media.Movie('Finding Nemo',
                """The film tells the story of the overprotective ocellaris
                clownfish named Marline who, along with a regal blue tang named
                Dory, searches for his abducted son Nemo all the way to the
                Sydney Harbour.""",
                'http://www.wearemoviegeeks.com/wp-content/uploads/FindingNemo3DPoster.jpg',
                'https://www.youtube.com/watch?v=3JnKU9Stmyw',
                'US Release Date: May 30, 2003',
                'Budget: $94 million',
                'Box Office: $940.3 million')


movies = [fight_club, gny, tropic_thunder, zoolander, monsters_inc, finding_nemo,]

# This function call opens a page of movies generated from the input, a list of
# movie instances
fresh_tomatoes.open_movies_page(movies)

# print media.Movie.__doc__
# print media.Movie.__name__
# print media.Movie.__module__
# print media.Movie.__init__.__doc__
# print media.Movie.VALID_RATINGS
# print fight_club.title
# print fight_club.storyline
#
# print(gny.title)
# print(gny.storyline)
# print(gny.poster_image_url)
# print(gny.trailer_youtube_url)
#
# fight_club.show_trailer()
