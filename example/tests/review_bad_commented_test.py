import pytest

from ..address import Address
from ..user import User
from ..review import Review

#pytest gathers test classses that starts with word Test
#the test file must end with test.py for pytest to gather it automatically, eg. -> review_bad_test.py
class TestReviewBad(object):

    #pytest gathers methods that start with test_ automatically
    #when using helper methods, don't start them with test_
    def test_review_init_valid(self):
        #what does basic user mean?
        user = User("basic user",Address("Konemiehentie 1", "Espoo"))

        #what is 1, how about 'My first review' & 'It sucked'?
        review = Review(1, "My first review", "It sucked!", user)

        #why the type is movie now?
        assert review.type == "movie"
        #why review.user is "basic user" instead of user?
        assert review.user == "basic user"
        assert review.title == "My first review"
        assert review.body == "It sucked!"
        #why zero comments?
        assert len(review.comments) == 0

        #what have we given as empty string here?
        review = Review(1, "My second review", "", user)
        #why is body "Great movie"?
        assert review.body == "Great movie!"

        #what is given as blank for user?
        user = User("", Address("Konemiehentie 2", "Espoo"))

        #2?
        review = Review(2, "Another review!", "It rocked!", user)
        #why type is book?
        assert review.type == "book"
        #why review.user is anonymous user?
        assert review.user == "Anonymous user"

        #3?
        review = Review(3, "Yess!! Another review!", "It rocked big time!", user)
        #how come review.type is album?
        assert review.type == "album"

    #pytest gathers methods that start with test_ automatically
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

        #why this is happening with the given user?
        assert "Homeless people are not allowed to review!" in str(error_info.value)
