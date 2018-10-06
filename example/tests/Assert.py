from ..review import Review
from ..user import User

class Assert:

    def __init__(self, review: Review):
        self.review = review


    def has_user(self, user: User):
        assert self.review.user == user

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
