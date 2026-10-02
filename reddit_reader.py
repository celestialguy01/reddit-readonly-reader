import os

import praw
from dotenv import load_dotenv


load_dotenv()


def create_reddit_client() -> praw.Reddit:
    return praw.Reddit(
        client_id=os.environ["REDDIT_CLIENT_ID"],
        client_secret=os.environ["REDDIT_CLIENT_SECRET"],
        user_agent=os.environ["REDDIT_USER_AGENT"],
    )


def read_recent_posts(reddit: praw.Reddit, subreddit_name: str, limit: int = 10):
    subreddit = reddit.subreddit(subreddit_name)

    for post in subreddit.new(limit=limit):
        print({
            "id": post.id,
            "title": post.title,
            "subreddit": subreddit_name,
            "score": post.score,
            "created_utc": post.created_utc,
            "url": post.url,
        })


if __name__ == "__main__":
    reddit = create_reddit_client()

    subreddit_name = input("Public subreddit name: ").strip()
    read_recent_posts(reddit, subreddit_name)
