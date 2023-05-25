from commands.tests.test_command_base import CommandTestBase
from django.urls import resolve, reverse

from commands import views


class CommandViewsTest(CommandTestBase):

    def tearDown(self) -> None:
        return super().tearDown()

    # tests command home --------------------------------------------------------------------------

    def test_command_home_view_function_is_correct(self):
        view = resolve(reverse('commands:home'))
        self.assertIs(view.func, views.home)

    def test_command_home_view_return_status_cod_200_ok(self):
        response = self.client.get(reverse('commands:home'))
        self.assertEqual(response.status_code, 200)

    def test_command_home_view_loads_correct_template(self):
        response = self.client.get(reverse('commands:home'))
        self.assertTemplateUsed(response, 'commands/pages/home.html')

    def test_command_home_template_show_commands_not_found_if_no_commands(self):
        response = self.client.get(reverse('commands:home'))
        self.assertIn('<h2> Commands not found! </h2>',
                      response.content.decode('UTF-8'))

    def test_command_home_template_load_commands(self):
        self.make_command(self.make_language(language_name='nome da linguagem'),
                          self.make_author(),
                          sintaxe='Comando que faz nada'
                          )
        response = self.client.get(reverse('commands:home'))
        response_content = response.content.decode('UTF-8')
        response_context_commands_registered = len(
            response.context['commands'])
        self.assertIn(
            'nome da linguagem', response_content)
        self.assertIn('Algum Comando', response_content)
        self.assertIn('Comando que faz nada', response_content)
        self.assertEqual(response_context_commands_registered, 1)


# tests command language------------------------------------------------------------------------------------------------

    def test_command_language_view_function_is_correct(self):
        view = resolve(reverse('commands:language', kwargs={'language_id': 1}))
        self.assertIs(view.func, views.language)

    def test_command_language_view_return_status_cod_200_ok(self):
        response = self.client.get(
            reverse('commands:language', kwargs={'language_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_command_language_view_return_status_cod_200_if_language_not_found(self):
        response = self.client.get(
            reverse('commands:language', kwargs={'language_id': 1000}))
        self.assertEqual(response.status_code, 200)

    def test_command_language_template_show_language_not_found_if_no_language(self):
        response = self.client.get(
            reverse('commands:language', kwargs={'language_id': 1}))
        self.assertIn('<h2> Programming language not found!!! </h2>',
                      response.content.decode('UTF-8'))

    def test_command_language_view_loads_correct_template(self):
        response = self.client.get(
            reverse('commands:language', kwargs={'language_id': 1}))
        self.assertTemplateUsed(response, 'commands/pages/language.html')


# tests command detail----------------------------------------------------------------------------------------

    def test_command_detail_view_function_is_correct(self):
        view = resolve(reverse('commands:command', kwargs={'id': 1}))
        self.assertIs(view.func, views.command)

    def test_command_detail_view_return_status_cod_404_if_command_not_found(self):
        response = self.client.get(
            reverse('commands:command', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)
