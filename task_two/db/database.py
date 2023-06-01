from utils import id_gen, random_img


class Database:
    posts = [
        {'id': next(id_gen), 'img':  next(random_img), 'name': 'image_1', 'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repudiandae officiis voluptates doloremque laudantium quo. Laboriosam aliquam aliquid fugiat excepturi similique iure ratione accusamus a sapiente, iste, laudantium itaque, quo nulla.'},
        {'id': next(id_gen), 'img':  next(random_img), 'name': 'image_2', 'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repudiandae officiis voluptates doloremque laudantium quo. Laboriosam aliquam aliquid fugiat excepturi similique iure ratione accusamus a sapiente, iste, laudantium itaque, quo nulla.'},
        {'id': next(id_gen), 'img':  next(random_img), 'name': 'image_3', 'description': 'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Repudiandae officiis voluptates doloremque laudantium quo. Laboriosam aliquam aliquid fugiat excepturi similique iure ratione accusamus a sapiente, iste, laudantium itaque, quo nulla.'},
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

