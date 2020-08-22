from inscrawler.model.comment import Comment
from inscrawler.persistence.model import CommentEntity


def get_by_id(comment_id: int):
    return from_entity(CommentEntity.get_by_id(comment_id))


# def get_by_post(post_id: int) -> list[Comment]:
#   CommentEntity.get(CommentEntity.post == post_id)


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
