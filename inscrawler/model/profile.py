from typing import Optional


class Profile:
    id_: Optional[int]
    username: Optional[str]
    name: Optional[str]
    description: Optional[str]
    n_followers: Optional[int]
    n_following: Optional[int]
    n_posts: Optional[int]
    photo_url: Optional[str]
    last_visit: Optional[int]
    created_at: Optional[int]
    deleted: Optional[bool]
    visited: Optional[bool]

    def __init__(self, id_: Optional[int],
                 username: Optional[str],
                 name: Optional[str],
                 description: Optional[str],
                 n_followers: Optional[int],
                 n_following: Optional[int],
                 n_posts: Optional[int],
                 photo_url: Optional[str],
                 last_visit: Optional[int],
                 created_at: Optional[int],
                 deleted: Optional[bool],
                 visited: Optional[bool]) -> None:
        self.id_ = id_
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
