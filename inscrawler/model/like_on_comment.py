from typing import Union


class LikeOnPost:
    profile_id: int
    comment_id: int
    created_at: Union[int, None]
    last_visit: Union[int, None]
    deleted: Union[bool, None]

    def __init__(self, profile_id: int,
                 post_id: int,
                 created_at: Union[int, None],
                 last_visit: Union[int, None],
                 deleted: Union[bool, None]) -> None:
        self.profile_id = profile_id
        self.comment_id = post_id
        self.created_at = created_at
        self.last_visit = last_visit
        self.deleted = deleted
