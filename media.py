''' Media file contains the "media" needed to 
	run the Entertainment Center web app. '''

###  Instances of the Movie class represent a movie 
###  and various attributes of that Movie.
class Movie:
    def __init__ (self, 
	    			title, 
	    			storyline, 
	    			release_date, 
	    			lead_actor, 
	    			poster_image_url, 
	    			trailer_youtube_url):
    	''' Initializes movie with the givien arguments. '''
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.release_date = release_date
        self.lead_actor = lead_actor
