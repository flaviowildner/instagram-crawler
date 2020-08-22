from typing import Union


class Post:
    profile_id: int
    url: str
    url_imgs: str
    post_date: int
    caption: Union[str, None]
    last_visit: Union[int, None]
    created_at: Union[int, None]
    deleted: Union[bool, None]

    def __init__(self, profile_id: int,
                 url: str,
                 url_imgs: str,
                 post_date: int,
                 caption: str,
                 last_visit: Union[int, None],
                 created_at: Union[int, None],
                 deleted: Union[bool, None]) -> None:
        self.profile_id = profile_id
        self.url = url
        self.url_imgs = url_imgs
        self.post_date = post_date
        self.caption = caption
        self.last_visit = last_visit
        self.created_at = created_at
        self.deleted = deleted
