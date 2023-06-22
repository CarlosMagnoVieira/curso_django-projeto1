from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_command_base import Commands, CommandTestBase


class TestCommandsModels(CommandTestBase):
    def setUp(self) -> None:
        self.command = self.make_command()
        return super().setUp()

    def make_command_in_defaults(self):
        comando = Commands(
            language=self.make_language(
                language_name='New language', language_version='version new language'),
            author=self.make_author(username='novo_usuario'),
            command_name='Algum Comando',
            description='Comando que faz alguma coisa bla blá blá',
            slag='algum-comando--',
            sintaxe='algum_comando(<blá blá blá>)',
            specifications='loren loren loren',
            fonte='as das das fifajie'
        )
        comando.full_clean()
        comando.save()
        return comando

    @parameterized.expand(
        [
            ('command_name', 30),
            ('description', 120),
            ('sintaxe', 80),
            ('fonte', 150)
        ]
    )
    def test_commands_fields_max_length(self, field, max_length):
        setattr(self.command, field, 'a' * (max_length+1))
        with self.assertRaises(ValidationError):
            self.command.full_clean()  # Aqui a validação ocorre

    @parameterized.expand(
        [
            ('language_name', 30),
            ('language_version', 15)
        ]
    )
    def test_language_fields_max_length(self, field, max_length):
        setattr(self.command.language, field, 'a' * (max_length+1))
        with self.assertRaises(ValidationError):
            self.command.language.full_clean()  # Aqui a validação ocorre

    def test_specifications_is_html_if_default_false(self):
        comando = self.make_command_in_defaults()
        self.assertFalse(comando.specifications_is_html,
                         msg='specifications_is_html is not default false')

    def test_is_published_if_default_false(self):
        comando = self.make_command_in_defaults()
        self.assertFalse(comando.is_published,
                         msg='is_published is not default false')

    def test_command_string_representation(self):
        self.command.command_name = 'comando1'
        self.command.language.language_name = 'linguagem de programação'
        needed = 'comando1'+'_'+'linguagem de programação'
        self.command.full_clean()
        self.command.save()
        self.assertEqual(str(self.command),
                         (needed),
                         msg=f'Commmand string representation "{str(self.command)}"not equal "{needed}"')

    def test_command_language_string_representation(self):
        self.command.language.language_name = 'linguagem de programação'
        self.command.language.language_version = 'versao da linguagem'
        needed = 'linguagem de programação'+'_'+'versao da linguagem'
        self.command.full_clean()
        self.command.save()
        self.assertEqual(str(self.command.language),
                         (needed),
                         msg=f'Language string representation "{str(self.command)}"not equal "{needed}"')
