import pytest

from ..address import Address
from ..user import User
from ..review import Review

class TestReviewBad(object):

    def test_review_init_valid(self):
        user = User("basic user",Address("Konemiehentie 1", "Espoo"))

        review = Review(1, "My first review", "It sucked!", user)

        assert review.type == "movie"
        assert review.user == "basic user"
        assert review.title == "My first review"
        assert review.body == "It sucked!"
        assert len(review.comments) == 0

        review = Review(1, "My second review", "", user)
        assert review.body == "Great movie!"

        user = User("", Address("Konemiehentie 2", "Espoo"))

        review = Review(2, "Another review!", "It rocked!", user)
        assert review.type == "book"
        assert review.user == "Anonymous user"

        review = Review(3, "Yess!! Another review!", "It rocked big time!", user)
        assert review.type == "album"

    def test_review_init_invalid(self):
        with pytest.raises(ValueError) as error_info:
            review = Review(1, "My first review", "It sucked!", None)
        assert "No user given for review!" in str(error_info.value)

        user = User("basic user", Address("Konemiehentie 1", "Espoo"))

        with pytest.raises(ValueError) as error_info:
            review = Review(0, "My first review", "It sucked!", user)

        assert "Type of 0 is not allowed!" in str(error_info.value)

        with pytest.raises(ValueError) as error_info:
            review = Review(1, "", "It sucked!", user)

        assert "Empty title is not allowed!" in str(error_info.value)

        user = User("basic user")
        with pytest.raises(ValueError) as error_info:
            review = Review(1, "The review", "It sucked!", user)

        assert "Homeless people are not allowed to review!" in str(error_info.value)
