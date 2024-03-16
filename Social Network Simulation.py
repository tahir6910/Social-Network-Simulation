class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.friends = []
        self.posts = []

    def add_friend(self, friend_id):
        self.friends.append(friend_id)

    def add_post(self, post):
        self.posts.append(post)

# Example initialization
users = {
    1: User(1, "Alice"),
    2: User(2, "Bob"),
    3: User(3, "Charlie"),
    # Add more users as needed
}

# Establish connections (friendships)
users[1].add_friend(2)
users[1].add_friend(3)
users[2].add_friend(1)
users[3].add_friend(1)

import datetime

class Post:
    def __init__(self, post_id, content, author_id):
        self.post_id = post_id
        self.content = content
        self.author_id = author_id
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"Post {self.post_id} by User {self.author_id}: {self.content}"

def make_post(user_id, content):
    post_id = len(users[user_id].posts) + 1
    post = Post(post_id, content, user_id)
    users[user_id].add_post(post)

def view_news_feed(user_id):
    news_feed = []
    for friend_id in users[user_id].friends:
        news_feed.extend(users[friend_id].posts)
    news_feed.sort(key=lambda x: x.timestamp, reverse=True)
    
    print(f"News Feed for User {users[user_id].name}:")
    for post in news_feed:
        author_name = users[post.author_id].name
        print(f"Author: {author_name} (User ID: {post.author_id})")
        print(f"Post ID: {post.post_id}")
        print(f"Content: {post.content}")
        print(f"Timestamp: {post.timestamp}")
        print("-" * 30)

# Prompt user to make a post
user_id = int(input("Enter your user ID: "))
content = input("Enter the content of your post: ")
make_post(user_id, content)

# Prompt user to view their news feed
user_id = int(input("Enter your user ID to view news feed: "))
view_news_feed(user_id)
