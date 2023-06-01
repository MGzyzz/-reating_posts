from controllers.pages import PagesController
from controllers.posts import PostsController
from src.router import Router
from src.server import runserver

config = {
    'host': 'localhost',
    'port': 1025,
    'static': 'static'
}

router = Router()
router.get('/posts', PostsController, 'get_list')
router.get('/post', PostsController, 'get_post')
router.get('/posts/new', PostsController, 'new')
router.post('/posts', PostsController, 'create')


runserver(router, config)