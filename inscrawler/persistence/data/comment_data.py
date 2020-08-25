from typing import Optional, List

from inscrawler.model.comment import Comment
from inscrawler.persistence.entity import CommentEntity


def get_by_id(comment_id: int):
    return from_entity(CommentEntity.get_by_id(comment_id))


def get_by_author_and_date(author_id: int, comment_date: int) -> Optional[Comment]:
    try:
        comment_entity: CommentEntity = CommentEntity.get(CommentEntity.author == author_id,
                                                          CommentEntity.comment_date == comment_date)
    except CommentEntity.DoesNotExist:
        return None

    return from_entity(comment_entity)


def update(comment: Comment):
    comment_entity: CommentEntity = to_entity(comment)
    comment_entity.save()


def get_comments_by_post(post_id: int) -> List[Comment]:
    comment_entity_list: List[CommentEntity] = CommentEntity.select().where(CommentEntity.post == post_id)
    return_list = []
    for comment_entity in comment_entity_list:
        return_list.append(from_entity(comment_entity))

    return return_list


def create(comment: Comment):
    CommentEntity.insert(to_entity(comment))


def to_entity(comment: Comment) -> CommentEntity:
    return CommentEntity(id=comment.id_,
                         post=comment.post,
                         author=comment.author,
                         comment=comment.comment,
                         last_visit=comment.last_visit,
                         comment_date=comment.comment_date,
                         deleted=comment.deleted
                         )


def from_entity(comment_entity: CommentEntity) -> Comment:
    return Comment(id_=comment_entity.id,
                   post=comment_entity.post,
                   author=comment_entity.author,
                   comment=comment_entity.comment,
                   last_visit=comment_entity.last_visit,
                   comment_date=comment_entity.comment_date,
                   deleted=comment_entity.deleted
                   )
