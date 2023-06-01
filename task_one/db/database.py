from utils import id_gen


class Database:
    posts = [
        {'id': next(id_gen), 'title': 'This is 1 post', 'description': 'example1'},
        {'id': next(id_gen), 'title': 'This is 2 post', 'description': 'example2'},
        {'id': next(id_gen), 'title': 'This is 3 post', 'description': 'example3'},
    ]

    @classmethod
    def all(cls):
        return cls.posts

    @classmethod
    def add(cls, post: dict[str, str]):
        post_id = int(post["id"])
        post["id"] = post_id
        cls.posts.append(post)


    @classmethod
    def find_by_id(cls, id):
        for post in cls.posts:
            if post.get('id') == id:
                return post

        else:
            return None

