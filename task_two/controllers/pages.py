from controllers.base import BaseController
import requests
import utils
from controllers.base import BaseController
from db.database import Database
from template_engine.jinja import env
from utils import id_gen, random_img


class PagesController(BaseController):
    def home(self):
        tmp = env.get_template('pages/home.html')
        body = tmp.render()
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def get_list(self):
        tmp = env.get_template('pages/page_image.html')
        body = tmp.render(images=Database.all())

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)


    def new(self):
        tmp = env.get_template('pages/create_page.html')
        body = tmp.render(id=next(utils.id_gen), img=next(utils.random_img))

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create(self):
        Database.add(self.request.body)
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_status(301)
        self.response.add_header('Location', '/page_image')
        self.response.set_body('<a href="/page_image">Back to posts list</a>')

    def get_image(self):
        id_image = int(self.request.query['id'][0])
        if id_image is not None:
            post = Database.find_by_id(id_image)
            if post is not None:
                print(post)
                tmp = env.get_template('pages/find_image.html')
                body = tmp.render(image=post)

                self.response.add_header('Content-Type', 'text/html')
                self.response.set_body(body)
            else:
                self.response.set_status(404)
                self.response.set_body('Post not found')
        else:
            self.response.set_status(400)
            self.response.set_body('Bad Request: missing post id')

    def search_image(self):
        tmp = env.get_template('pages/search.html')
        body = tmp.render()
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)