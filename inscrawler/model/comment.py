from typing import Optional

from inscrawler.model.post import Post
from inscrawler.model.profile import Profile


class Comment:
    id_: Optional[int]
    post: Optional[Post]
    author: Optional[Profile]
    comment: Optional[str]
    last_visit: Optional[int]
    comment_date: Optional[int]
    deleted: Optional[bool]

    def __init__(self, id_: Optional[int],
                 post: Optional[Post],
                 author: Optional[Profile],
                 comment: Optional[str],
                 last_visit: Optional[int],
                 comment_date: Optional[int],
                 deleted: Optional[bool]) -> None:
        self.id_ = id_
        self.post = post
        self.author = author
        self.comment = comment
        self.last_visit = last_visit
        self.comment_date = comment_date
        self.deleted = deleted
