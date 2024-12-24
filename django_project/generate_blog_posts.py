import random
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.timezone import now

# List of random titles and content for the blog posts
titles = [
    "Adventures in Space", "The Secrets of the Ocean", 
    "A Day in the Life of a Cat", "Exploring Ancient Ruins", 
    "The Mystery of the Lost City", "10 Tips for Healthy Living",
    "Learning Django the Fun Way", "My Journey Across the Sahara",
    "The Art of Minimalism", "Top 5 Sci-Fi Books to Read",
    "Life Hacks for Busy People", "A Guide to Mindfulness",
    "The History of the Internet", "Understanding Quantum Physics",
    "Traveling on a Budget"
]

contents = [
    "This post dives deep into the topic of adventure and discovery.",
    "Learn about the fascinating underwater world and its secrets.",
    "A humorous look at life from a cat's perspective.",
    "Join us as we explore ancient ruins and uncover their mysteries.",
    "The lost city has always been a source of fascination for explorers.",
    "Here are some great tips to live a healthier life.",
    "A fun and engaging way to learn Django from scratch.",
    "My solo adventure across the Sahara desert taught me many lessons.",
    "Minimalism is not just a trend but a way of life.",
    "Explore some of the best sci-fi books that expand your imagination.",
    "Life hacks that save time and make everyday tasks easier.",
    "Discover the benefits of mindfulness and how to practice it.",
    "From its origins to today, explore the history of the internet.",
    "An introductory guide to the complex world of quantum physics.",
    "Practical tips and tricks for budget-friendly travel."
]

def create_random_posts():
    # Ensure there is at least one user in the database
    author = User.objects.first()
    
    if not author:
        print("No users found in the database. Please create at least one user.")
        return

    # Create 15 random posts
    for _ in range(15):
        title = random.choice(titles)
        content = random.choice(contents)
        
        Post.objects.create(
            title=title,
            content=content,
            date_posted=now(),
            author=author
        )

    print("15 random blog posts created successfully!")

# Run the function to generate blog posts
if __name__ == "__main__":
    create_random_posts()
