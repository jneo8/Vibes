from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from .views import home_page
from .models import Item


class HomePageTest(TestCase):

    # 測試url /superlist/ 是否有連接到 homepage 這個function
    def test_root_url_resolvers(self):
        found = resolve('/superlist/')
        self.assertEqual(found.func, home_page)

    def test_home_page_return_correct_html(self):
        # 建立HttpRequest物件
        request = HttpRequest()
        # 將request傳給home_page view, 會得到home_page回傳的response
        response = home_page(request)
        # 由於csrf token 所以會報錯
        expected_html = render_to_string('superlist/home.html')
        self.assertEqual(response.content.decode(), expected_html)
        # response.content是原始位元組，必須使用 b'' 語法來進行比較
        self.assertTrue(response.content.startswith(b'<!DOCTYPE html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.strip().endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_home_page_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = HttpRequest()
        response = home_page(request)

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())



    def test_home_page_redirects_after_POST(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/superlist/lists/the-only-list-in-the-world/')
        
    def test_home_page_only_saves_items_when_nessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):

    def test_saving_and_retriving_items(self):

        # 建立兩筆資料並儲存
        first_item = Item()
        first_item.text = 'The first(ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        # 撈出兩筆資料並比對text attrubite的值
        save_items = Item.objects.all()
        self.assertEqual(save_items.count(), 2)

        first_save_item = save_items[0]
        second_save_item = save_items[1]
        self.assertEqual(first_save_item.text, 'The first(ever) list item')
        self.assertEqual(second_save_item.text, 'Item the second')

class ListViewTest(TestCase):
    """docstring for ListViewTest"""
    def test_display_all_item(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/superlist/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')


        






























