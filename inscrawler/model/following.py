from typing import Union


class Following:
    followed: int
    follower: int
    created_at: Union[int, None]
    last_visit: Union[int, None]
    deleted: Union[bool, None]

    def __init__(self, followed: int,
                 follower: int,
                 created_at: Union[int, None],
                 last_visit: Union[int, None],
                 deleted: Union[bool, None]) -> None:
        self.followed = followed
        self.follower = follower
        self.created_at = created_at
        self.last_visit = last_visit
        self.deleted = deleted
