from commands.tests.test_command_base import (Commands, CommandTestBase,
                                              Language)
from django.urls import resolve, reverse

from commands import views


class CommandViewsTest(CommandTestBase):

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
        self.make_command(language_data={
            'language_name': 'nome da linguagem',
            'language_version': '3.0'},
            sintaxe='Comando que faz nada')

        response = self.client.get(reverse('commands:home'))
        response_content = response.content.decode('UTF-8')
        response_context_commands_registered = len(
            response.context['commands'])
        self.assertIn(
            'nome da linguagem', response_content)
        self.assertIn('Algum Comando', response_content)
        self.assertIn('Comando que faz nada', response_content)
        self.assertEqual(response_context_commands_registered, 1)

    def test_command_home_dont_show_command_not_published(self):
        texto_para_teste = 'Nome do Comando para teste'
        self.make_command(command_name=texto_para_teste,
                          is_published=False,
                          )
        response = self.client.get(reverse('commands:home'))
        response_content = response.content.decode('UTF-8')
        response_context_commands_registered = len(
            response.context['commands'])
        self.assertNotIn(
            texto_para_teste, response_content)
        self.assertEqual(response_context_commands_registered, 0)
        self.assertIn('<h2> Commands not found! </h2>',
                      response.content.decode('UTF-8'))


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

    def test_command_language_template_load_language(self):
        texto_teste = 'nome da linguagem para teste'
        self.make_command(language_data={
            'language_name': texto_teste,
            'language_version': '2.0'})
        response = self.client.get(
            reverse('commands:language', kwargs={'language_id': 1}))
        response_content = response.content.decode('UTF-8')
        self.assertIn(
            texto_teste, response_content)

    def test_command_language_dont_show_language_not_published(self):
        nome_comando_para_teste = 'nome do comando para teste'
        command = self.make_command(command_name=nome_comando_para_teste,
                                    is_published=False)

        response = self.client.get(
            reverse('commands:language',
                    kwargs={'language_id': command.language.id}
                    )
        )
        response_content = response.content.decode('UTF-8')
        response_context = response.context['language_name']
        self.assertNotIn(
            nome_comando_para_teste, response_content)
        self.assertEqual(response_context, 'Not found')
        self.assertIn('<h2> Programming language not found!!! </h2>',
                      response.content.decode('UTF-8'))
        self.assertEqual(response.status_code, 200)


# tests command detail----------------------------------------------------------------------------------------

    def test_command_detail_view_function_is_correct(self):
        view = resolve(reverse('commands:command', kwargs={'id': 1}))
        self.assertIs(view.func, views.command)

    def test_command_detail_view_return_status_cod_404_if_command_not_found(self):
        response = self.client.get(
            reverse('commands:command', kwargs={'id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_command_detail_dont_show_command_not_published(self):
        texto_para_teste = 'Nome do Comando para teste'
        commando = self.make_command(command_name=texto_para_teste,
                                     is_published=False,
                                     )
        response = self.client.get(
            reverse('commands:command',
                    kwargs={'id': commando.id}
                    )
        )
        response_content = response.content.decode('UTF-8')
        self.assertNotIn(
            texto_para_teste, response_content)
        self.assertIn('Not Found',
                      response.content.decode('UTF-8'))
        self.assertEqual(response.status_code, 404)

    def test_command_detail_show_command_page(self):
        texto_para_teste = 'Nome do Comando para teste'
        commando = self.make_command(command_name=texto_para_teste,
                                     is_published=True,
                                     )
        response = self.client.get(
            reverse('commands:command',
                    kwargs={'id': commando.id}
                    )
        )
        response_content = response.content.decode('UTF-8')
        self.assertIn(
            texto_para_teste, response_content)
        self.assertEqual(response.status_code, 200)

# tests command search----------------------------------------------------

    def test_command_search_view_function_is_correct(self):
        view = resolve(reverse('commands:search'))
        self.assertIs(view.func, views.search)

    def test_command_search_load_correct_template(self):
        response = self.client.get(reverse('commands:search')+'?q=teste')
        self.assertTemplateUsed(response, 'commands/pages/search.html')

    def test_command_search_view_return_status_cod_404_if_no_search_term(self):
        response = self.client.get(
            reverse('commands:search'))
        self.assertEqual(response.status_code, 404)
