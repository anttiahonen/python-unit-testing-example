from .user import User

class Review:

    allowed_types_dict = {
        1: "movie",
        2: "book",
        3: "album"
    }

    def __init__(self, review_type: int, title: str, body: str, user: User):
        self.type = review_type
        self.title = title
        self.body = body if body else "Great movie!"
        self.user = user
        self.comments = []
        self.__validate()

        self.type = self.allowed_types_dict[review_type]
        self.user = user.name if user.name else "Anonymous user"

    def __validate(self):
        if self.type not in self.allowed_types_dict.keys():
            raise ValueError("Type of {} is not allowed!".format(self.type))
        if self.user is None:
            raise ValueError("No user given for review!")
        if self.user and self.user.address is None:
            raise ValueError("Homeless people are not allowed to review!")
        if not self.title:
            raise ValueError("Empty title is not allowed!")
