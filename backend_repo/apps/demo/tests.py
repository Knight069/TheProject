from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from apps.demo.models import Post, Comment


class PostWithCommentsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.post = Post.objects.create(text="Sample Post", user=self.user)
        Comment.objects.create(text="Comment 1", post=self.post, user=self.user)
        Comment.objects.create(text="Comment 2", post=self.post, user=self.user)
        Comment.objects.create(text="Comment 3", post=self.post, user=self.user)
        Comment.objects.create(text="Comment 4", post=self.post, user=self.user)

    def test_post_with_comments(self):
        response = self.client.get("/api/posts/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["comment_count"], 4)
        self.assertEqual(
            len(response.data[0]["comments"]), 3
        )  # Should return only 3 comments
