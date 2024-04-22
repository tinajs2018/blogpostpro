# from flask import Flask,render_template

# app=Flask(__name__)
# posts = {
#   1: {
#     "title": "First Blog Post",
#     "content": "This is the content of the first blog post."
#   },
#   2: {
#     "title": "Second Blog Post",
#     "content": "This is the content of the second blog post."
#   },
# }

# @app.route("/")
# def index():
#     #get all the post
#     all_post=posts.values()
#     return render_template("base.html",posts=all_post)

# @app.route("/post/<int:post_id>")
# def post(post_id):
#     try:
#         post = posts[post_id]

#     except KeyError:
#         return "post not found",
    
#     return render_template("post.html",post=post)

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts (replace with database integration later)
posts = [
    {"title": "Post One", "content": "This is the content of the first blog post."},
    {"title": "Post Two", "content": "This is the content of the second blog post."},
]

@app.route("/")
def home():
    return render_template("base.html", posts=posts)  # Assuming an index.html template

@app.route("/post/<int:post_id>")
def post(post_id):
    # Simulate fetching post by ID (replace with database logic)
    for post in posts:
        if post.get("id") == post_id:
            return render_template("post.html", post=post)
    return render_template("error.html", message="Post not found!")  # Error handling

if __name__ == "__main__":
    app.run(debug=True)

    
  