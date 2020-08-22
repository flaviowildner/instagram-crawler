from typing import Union


class Comment:
    post: int
    author: str
    comment: str
    last_visit: Union[int, None]
    comment_date: Union[int, None]
    deleted: Union[bool, None]

    def __init__(self, post: int,
                 author: str,
                 comment: str,
                 last_visit: Union[int, None],
                 comment_date: Union[int, None],
                 deleted: Union[bool, None]) -> None:
        self.post = post
        self.author = author
        self.comment = comment
        self.last_visit = last_visit
        self.comment_date = comment_date
        self.deleted = deleted
