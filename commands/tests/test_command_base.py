from commands.models import Commands, Language, User
from django.test import TestCase


class CommandTestBase(TestCase):
    def setUp(self) -> None:
        #       language = self.make_language()
        #       author = self.make_author()
        #   self.make_command()

        return super().setUp()

    def make_language(self,
                      language_name='Java',
                      language_version='2.0'):
        return Language.objects.create(
            language_name=language_name,
            language_version=language_version,
        )

    def make_author(self,
                    username='username',
                    first_name='User',
                    last_name='Name',
                    password='123456',
                    email='sdjigsd@eiwek.com.br'
                    ):
        return User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email,
        )

    def make_command(self,
                     language_data=None,
                     author_data=None,
                     command_name='Algum Comando',
                     description='Comando que faz alguma coisa bla blá blá',
                     slag='algum-comando',
                     sintaxe='algum_comando(<blá blá blá>)',
                     specifications='loren loren loren',
                     specifications_is_html=False,
                     is_published=True,
                     fonte='as das das fifajie'
                     ):

        if language_data is None:
            language_data = {}
        if author_data is None:
            author_data = {}

        return Commands.objects.create(
            language=self.make_language(**language_data),
            author=self.make_author(**author_data),
            command_name=command_name,
            description=description,
            slag=slag,
            sintaxe=sintaxe,
            specifications=specifications,
            specifications_is_html=specifications_is_html,
            is_published=is_published,
            fonte=fonte,
        )
