import webbrowser
'''This class has two methods and
stores info about movie like its
title, storyline, image and youtube url.'''


class Movie():
    def __init__(self, title, director, storyline,
                 poster_image_url, trailer_youtube_url):
        '''This docstring explains the constructor method,
        its inputs and outputs if any'''
        self.title = title
        self.director = director
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        '''this open a browser and plays the trailer
        This docstring explains what the show_trailer function does'''
        webbrowser.open(self.trailer_youtube_url)
