import pytest

from ..address import Address
from ..user import User
from ..review import Review
from .Assert import Assert

class TestReviewFullyEnhancedTest(object):

    INVALID_TYPE = 0
    VALID_MOVIE_TYPE = 1
    VALID_BOOK_TYPE = 2
    VALID_ALBUM_TYPE = 3

    @classmethod
    def setup_class(cls):
        cls.default_address = Address("Konemiehentie 1", "Espoo")
        cls.basic_user = User(name="basic user", address=cls.default_address)


    def test_review_init_withValidBasicUser_andValidReviewInfo_returnsReviewWithGivenInfo_andReviewUserAsUserName(self):
        initialized_review = Review(review_type=self.VALID_MOVIE_TYPE,title="My first review",body="It sucked!",user=self.basic_user)

        Assert(initialized_review)\
            .has_user(self.basic_user.name)\
            .has_title("My first review")\
            .has_body("It sucked!")

    def test_review_init_withValidParameters_returnsReviewWithZeroCommentsAtStart(self):
        initialized_review = self.create_default_review_with_user(self.basic_user)

        Assert(initialized_review)\
            .has_empty_comments()

    def test_review_init_withEmptyReviewBody_returnsDefaultReviewBody(self):
        emptyBody = ""

        review_with_default_body = Review(review_type=self.VALID_MOVIE_TYPE,title="My second review",body=emptyBody,user=self.basic_user)

        Assert(review_with_default_body)\
            .has_body("Great movie!")

    def test_review_init_withUserWithoutAName_setsReviewUserAsAnonymous(self):
        user_without_name = User(name="", address=self.default_address)

        Assert(self.create_default_review_with_user(user_without_name))\
            .has_user("Anonymous user")

    def test_review_init_withValidReviewTypeCodeParams_transformsTheTypeCodeIntoValidType(self):
        Assert(self.create_default_review_with_type(self.VALID_MOVIE_TYPE))\
            .is_a_movie_review()

        Assert(self.create_default_review_with_type(self.VALID_BOOK_TYPE))\
            .is_a_book_review()

        Assert(self.create_default_review_with_type(self.VALID_ALBUM_TYPE))\
            .is_an_album_review()

    def test_review_init_withoutUser_raisesErrorNoUserGiven(self):
        with pytest.raises(ValueError) as error_info:
            self.create_default_review_with_user(None)

        self.assertErrorMessageIs("No user given for review!", error_info)

    def test_review_init_withInvalidReviewType_raisesErrorInvalidType(self):
        with pytest.raises(ValueError) as error_info:
            self.create_default_review_with_type(self.INVALID_TYPE)

        self.assertErrorMessageIs("Type of 0 is not allowed!", error_info)

    def test_review_init_withEmptyTitle_raisesErrorEmptyTitle(self):
        with pytest.raises(ValueError) as error_info:
            Review(review_type=self.VALID_MOVIE_TYPE, title="", body="It sucked!", user=self.basic_user)

        self.assertErrorMessageIs("Empty title is not allowed!", error_info)

    def test_review_init_withUserWithoutAnAddress_raisesErrorHomeless(self):
        user_without_address = User("basic user")
        with pytest.raises(ValueError) as error_info:
            self.create_default_review_with_user(user_without_address)

        self.assertErrorMessageIs("Homeless people are not allowed to review!", error_info)


    def create_default_review_with_type(self, review_type):
        return Review(review_type=review_type, title="Yess!! Another review!", body="It rocked big time!", user=self.basic_user)

    def create_default_review_with_user(self, user):
        return Review(review_type=self.VALID_MOVIE_TYPE, title="Yess!! Another review!", body="It rocked big time!",user=user)

    def assertErrorMessageIs(self, msg, error_info):
        assert msg in str(error_info.value)

