import webbrowser

# Google style guide for python suggests to name classes with uppercase
class Movie():
    '''This class provides a way to store movie related information'''
    #Google style guide says to have constants be all uppercase
    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R']
    # considered the constructor of the class, creating an instance of self
    def __init__(self, movie_title, movie_storyline, poster_image,
    trailer_youtube, release_date, movie_budget, box_office):
        ''' Initilizes the class Movie to create an instance with functions
        below
        '''
        # below are considered instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.us_release_date = release_date
        self.budget = movie_budget
        self.box_office_earnings = box_office
    # considered an instance method
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
