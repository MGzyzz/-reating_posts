
from controllers.pages import PagesController
from src.router import Router
from src.server import runserver

config = {
    'host': 'localhost',
    'port': 1025,
    'static': 'static'
}

router = Router()
router.get('/', PagesController, 'home')
router.get('/page_image', PagesController, 'get_list')
router.get('/page_create', PagesController, 'new')
router.get('/find_image', PagesController, 'get_image')
router.get('/search_image', PagesController, 'search_image')
router.post('/page_image', PagesController, 'create')


runserver(router, config)