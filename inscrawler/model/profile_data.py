from typing import Union


class ProfileData:
    username: str
    name: str
    description: str
    n_followers: int
    n_following: int
    n_posts: int
    photo_url: str
    last_visit: Union[int, None]
    created_at: Union[int, None]
    deleted: Union[bool, None]
    visited: Union[bool, None]

    def __init__(self, username: str,
                 name: str,
                 description: str,
                 n_followers: int,
                 n_following: int,
                 n_posts: int,
                 photo_url: str,
                 last_visit: Union[int, None],
                 created_at: Union[int, None],
                 deleted: Union[bool, None],
                 visited: Union[bool, None]) -> None:
        self.username = username
        self.name = name
        self.description = description
        self.n_followers = n_followers
        self.n_following = n_following
        self.n_posts = n_posts
        self.photo_url = photo_url
        self.last_visit = last_visit
        self.created_at = created_at
        self.deleted = deleted
        self.visited = visited
