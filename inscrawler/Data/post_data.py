from inscrawler.model.post import Post
from inscrawler.persistence.model.post_entity import PostEntity


def inset_profile(post: Post):
    post_entity = PostEntity(profile_id=post.profile_id,
                             url=post.url,
                             url_imgs=post.url_imgs,
                             post_date=post.post_date,
                             caption=post.caption,
                             last_visit=post.last_visit,
                             created_at=post.created_at,
                             deleted=post.deleted)

    PostEntity.insert(post_entity)
