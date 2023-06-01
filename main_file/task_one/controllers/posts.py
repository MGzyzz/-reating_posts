import requests
import utils
from controllers.base import BaseController
from db.database import Database
from template_engine.jinja import env
from utils import id_gen


class PostsController(BaseController):
    def get_list(self):
        tmp = env.get_template('posts/list.html')
        body = tmp.render(posts=Database.all())

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def new(self):
        tmp = env.get_template('posts/create.html')
        body = tmp.render(id=int(next(utils.id_gen)))

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create(self):
        Database.add(self.request.body)

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_status(301)
        self.response.add_header('Location', '/posts')
        self.response.set_body('<a href="/posts"">Back to posts list</a>')


    def get_post(self):
        post_id = int(self.request.query['id'][0])
        if post_id is not None:
            post = Database.find_by_id(post_id)
            if post is not None:

                tmp = env.get_template('posts/find_post.html')
                body = tmp.render(post=post)

                self.response.add_header('Content-Type', 'text/html')
                self.response.set_body(body)
            else:
                self.response.set_status(404)
                self.response.set_body('Post not found')
        else:
            self.response.set_status(400)
            self.response.set_body('Bad Request: missing post id')
