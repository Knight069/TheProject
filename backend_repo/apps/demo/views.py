# TODO There's certainly more than one way to do this task, so take your pick.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from apps.demo.models import Post, Comment


class PostWithComments(APIView):
    """
    API endpoint to retrieve a list of Posts with up to 3 latest Comments for each Post.

    Endpoint: /api/posts/
    Method: GET
    Response Format: JSON

    Each Post includes:
    - text: Post's text
    - timestamp: Post's timestamp
    - comment_count: Number of Comments associated with the Post
    - user: Post author's username
    - comments: Up to 3 latest Comments for the Post

    Each Comment includes:
    - text: Comment's text
    - timestamp: Comment's timestamp
    - user: Comment author's username
    """

    def get(self, request):
        posts = Post.objects.annotate(comment_count=Count("comments")).order_by(
            "-timestamp"
        )
        response_data = []

        for post in posts:
            comments = post.comments.all().order_by("-timestamp")[
                :3
            ]  # Fetch 3 latest comments
            response_data.append(
                {
                    "text": post.text,
                    "timestamp": post.timestamp,
                    "comment_count": post.comment_count,
                    "user": post.user.username,  # Extract username
                    "comments": [
                        {
                            "text": comment.text,
                            "timestamp": comment.timestamp,
                            "user": comment.user.username,  # Extract username
                        }
                        for comment in comments
                    ],
                }
            )

        return Response(response_data, status=status.HTTP_200_OK)


# Follow-Up Answer:
# To fetch 3 random comments instead of the latest ones, replace the query for comments with:
# comments = post.comments.order_by('?')[:3]  # Fetch 3 random comments
