from random import randint

from faker import Faker


def rand_ratio():
    return randint(840, 900), randint(473, 573)


fake = Faker('pt_BR')
# print(signature(fake.random_number))


def make_command():
    return {
        'command_name': fake.sentence(nb_words=3),
        'description': fake.sentence(nb_words=20),
        'language': {
            fake.word(),
        },
        'sintaxe': fake.sentence(nb_words=20),
        'created_at': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
        },
        'cover': {
            'url': 'https://loremflickr.com/%s/%s/computing,program' % rand_ratio(),
        }
    }


if __name__ == '__main__':
    from pprint import pprint
    pprint(make_command())