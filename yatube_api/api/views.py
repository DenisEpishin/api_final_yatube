from rest_framework import filters, mixins, pagination, permissions, viewsets
from posts.models import Post, Group, Comment, Follow

class PostViewSet(PermissionViewset):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = pagination.LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user
        )


class CommentViewSet(PermissionViewset):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user,
            post=self.get_post_obj()
        )

    def get_queryset(self):
        return self.get_post_obj().comments.all()

    def get_post_obj(self):
        return get_object_or_404(
            Post,
            pk=self.kwargs.get('post_pk')
        )
