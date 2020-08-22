from inscrawler.model.profile import Profile
from inscrawler.persistence.model.profile_entity import ProfileEntity


def insert_profile(profile: Profile):
    profile_entity = ProfileEntity(username=profile.username,
                                   name=profile.name,
                                   description=profile.description,
                                   n_followers=profile.n_followers,
                                   n_following=profile.n_following,
                                   n_posts=profile.n_posts,
                                   photo_url=profile.photo_url,
                                   last_visit=profile.last_visit,
                                   created_at=profile.created_at,
                                   deleted=profile.deleted,
                                   visited=profile.visited)

    ProfileEntity.insert(profile_entity)
