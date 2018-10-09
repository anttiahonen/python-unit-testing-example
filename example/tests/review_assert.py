from ..review import Review
from ..user import User

#Test Domain specific language (DSL) class
class Assert:

    #insert the object to make assertions against in the init/constructor
    def __init__(self, review: Review):
        self.review = review


    #wrap assertions into readable methods that can be chained
    def has_user(self, user: User):
        assert self.review.user == user

        #key for chaining assertions is returning the DSL-class from method calls
        return self

    def has_title(self, title: str):
        assert self.review.title == title

        return self

    def has_body(self, body: str):
        assert self.review.body == body

        return self

    def has_empty_comments(self):
        assert len(self.review.comments) == 0

        return self

    def is_a_movie_review(self):
        assert self.review.type == "movie"

        return self

    def is_a_book_review(self):
        assert self.review.type == "book"

        return self

    def is_an_album_review(self):
        assert self.review.type == "album"

        return self
