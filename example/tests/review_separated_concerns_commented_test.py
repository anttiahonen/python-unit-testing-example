import pytest

from ..address import Address
from ..user import User
from ..review import Review

#pytest gathers test classses that starts with word Test
#the test file must end with test.py for pytest to gather it automatically, eg. -> review_separated_concerns_test.py
class TestReviewSeparatedConcerns(object):

    #more granularity for tests, behavior of method/class under test can be described better when having granular test
    #methods with good method naming

    # --> method name describes the behaviour and failing tests gives immediately some hint at what situation is failing

    #method naming pattern
    #   test | method under test | context   | more context  |  expected outcome        |  expected outcome
    def test_review_init_withValidBasicUser_andValidReviewInfo_returnsReviewWithGivenInfo_andReviewUserAsUserName(self):
        user = User("basic user",Address("Konemiehentie 1", "Espoo"))

        review = Review(1, "My first review", "It sucked!", user)

        assert review.user == "basic user"
        assert review.title == "My first review"
        assert review.body == "It sucked!"

    #method naming pattern
    #   test | method under test | context   |  expected outcome
    def test_review_init_withValidParameters_returnsReviewWithZeroCommentsAtStart(self):
        user = User("basic user",Address("Konemiehentie 1", "Espoo"))

        review = Review(1, "My first review", "It sucked!", user)

        assert len(review.comments) == 0

    def test_review_init_withEmptyReviewBody_returnsDefaultReviewBody(self):
        user = User("basic user", Address("Konemiehentie 1", "Espoo"))

        review = Review(1, "My second review", "", user)

        assert review.body == "Great movie!"

    def test_review_init_withUserWithoutAName_setsReviewUserAsAnonymous(self):
        user = User("", Address("Konemiehentie 2", "Espoo"))

        review = Review(2, "Another review!", "It rocked!", user)

        assert review.user == "Anonymous user"

    def test_review_init_withValidReviewTypeCodeParams_transformsTheTypeCodeIntoValidType(self):
        user = User("basic user", Address("Konemiehentie 1", "Espoo"))

        review = Review(1, "Yess!! Another review!", "It rocked big time!", user)
        assert review.type == "movie"

        review = Review(2, "Yess!! Another review!", "It rocked big time!", user)
        assert review.type == "book"

        review = Review(3, "Yess!! Another review!", "It rocked big time!", user)
        assert review.type == "album"


    def test_review_init_withoutUser_raisesError(self):
        with pytest.raises(ValueError) as error_info:
            Review(1, "My first review", "It sucked!", None)
        assert "No user given for review!" in str(error_info.value)

    def test_review_init_withInvalidReviewType_raisesError(self):
        user = User("basic user", Address("Konemiehentie 1", "Espoo"))

        with pytest.raises(ValueError) as error_info:
            Review(0, "My first review", "It sucked!", user)

        assert "Type of 0 is not allowed!" in str(error_info.value)

    def test_review_init_withEmptyTitle_raisesError(self):
        user = User("basic user", Address("Konemiehentie 1", "Espoo"))

        with pytest.raises(ValueError) as error_info:
            Review(1, "", "It sucked!", user)

        assert "Empty title is not allowed!" in str(error_info.value)

    def test_review_init_withUserWithoutAnAddress_raisesError(self):
        user = User("basic user")
        with pytest.raises(ValueError) as error_info:
            Review(1, "The review", "It sucked!", user)

        assert "Homeless people are not allowed to review!" in str(error_info.value)
