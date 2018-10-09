import pytest

from ..address import Address
from ..user import User
from ..review import Review
from .review_assert import Assert

#pytest gathers test classses that starts with word Test
#the test file must end with test.py for pytest to gather it automatically, eg. -> review_fully_enhanced_test.py
class TestReviewFullyEnhancedTest(object):

    #set "magic constants" into well named variables
    INVALID_TYPE = 0
    VALID_MOVIE_TYPE = 1
    VALID_BOOK_TYPE = 2
    VALID_ALBUM_TYPE = 3

    #remove repetition by using fixture methods for creating common shared test data.
    #this is a method that is run at the start of test case once.
    @classmethod
    def setup_class(cls):
        cls.default_address = Address("Konemiehentie 1", "Espoo")
        cls.basic_user = User(name="basic user", address=cls.default_address)

    #if the common data must be freshly initialized for each test method, use per method fixture.
    #def setup_method(self, method):
    #    self.default_address = Address("Konemiehentie 1", "Espoo")
    #    self.basic_user = User(name="basic user", address=cls.default_address)


    #granular test methods + naming test methods properly
    def test_review_init_withValidBasicUser_andValidReviewInfo_returnsReviewWithGivenInfo_andReviewUserAsUserName(self):
        #1. detailed variable naming
        #2. use named method parametrs if the language supports it
        initialized_review = Review(review_type=self.VALID_MOVIE_TYPE,title="My first review",body="It sucked!",user=self.basic_user)

        #sometimes having a custom test dsl for doing assertions can bring readability & maintainaibility
        #for common occuring assertions.
        #dsl/fluent-apis can give chaining of methods for increased readability & natural language like 'feel'.
        Assert(initialized_review)\
            .has_user(self.basic_user.name)\
            .has_title("My first review")\
            .has_body("It sucked!")

    def test_review_init_withValidParameters_returnsReviewWithZeroCommentsAtStart(self):
        #                         use helper methods like this factory method to reduce repetition
        initialized_review = self.create_default_review_with_user(self.basic_user)

        Assert(initialized_review)\
            .has_empty_comments()

    def test_review_init_withEmptyReviewBody_returnsDefaultReviewBody(self):
        #sometimes its good to assing values into variable and name them properly
        emptyBody = ""

        review_with_default_body = Review(review_type=self.VALID_MOVIE_TYPE,title="My second review",body=emptyBody,user=self.basic_user)

        Assert(review_with_default_body)\
            .has_body("Great movie!")

    def test_review_init_withUserWithoutAName_setsReviewUserAsAnonymous(self):
        #think about variable naming, for example here user vs user_without_name
        user_without_name = User(name="", address=self.default_address)

        Assert(self.create_default_review_with_user(user_without_name))\
            .has_user("Anonymous user")

    def test_review_init_withValidReviewTypeCodeParams_transformsTheTypeCodeIntoValidType(self):
        #even though granular testing is the way to go, sometimes checked things are logical to group inside
        #one test method instead of duplicating almost the same muliple times
        Assert(self.create_default_review_with_type(self.VALID_MOVIE_TYPE))\
            .is_a_movie_review()

        Assert(self.create_default_review_with_type(self.VALID_BOOK_TYPE))\
            .is_a_book_review()

        Assert(self.create_default_review_with_type(self.VALID_ALBUM_TYPE))\
            .is_an_album_review()

    def test_review_init_withoutUser_raisesErrorNoUserGiven(self):
        with pytest.raises(ValueError) as error_info:
            self.create_default_review_with_user(None)

        #use helper methods when something is happening multiple times, if feasible
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
