from typing import Optional

from inscrawler.model.profile import Profile


class Post:
    id_: Optional[int]
    profile: Optional[Profile]
    url: Optional[str]
    url_imgs: Optional[str]
    post_date: Optional[int]
    caption: Optional[str]
    last_visit: Optional[int]
    created_at: Optional[int]
    deleted: Optional[bool]

    def __init__(self, id_: Optional[int],
                 profile: Optional[Profile],
                 url: Optional[str],
                 url_imgs: Optional[str],
                 post_date: Optional[int],
                 caption: Optional[str],
                 last_visit: Optional[int],
                 created_at: Optional[int],
                 deleted: Optional[bool]) -> None:
        self.id_ = id_
        self.profile = profile
        self.url = url
        self.url_imgs = url_imgs
        self.post_date = post_date
        self.caption = caption
        self.last_visit = last_visit
        self.created_at = created_at
        self.deleted = deleted
