from django.shortcuts import render
from django.shortcuts import resolve_url
from django.urls import reverse_lazy
from django.urls import reverse

from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from django.db.models import Prefetch

from .models import Category
from .models import Item
from .models import ShoppingList
from .models import ShoppingItem

from .forms import CategoryForm
from .forms import ItemForm
from .forms import ShoppingListForm
from .forms import ShoppingItemForm


# Create your views here.
class IndexView(TemplateView):
    template_name = 'shoppinglist/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '買い物リストくん'
        return context


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'shoppinglist/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '買い物リストくん'
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'shoppinglist/category/list.html'
    paginate_by = 3
    
    def get_queryset(self):
        object_list = Category.objects.all().order_by('id')
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ一覧'
        return context


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('shoppinglist:category_list')
    template_name = 'shoppinglist/category/create.html'
    success_message = 'カテゴリ新規登録が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ新規登録'
        return context


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('shoppinglist:category_list')
    template_name = 'shoppinglist/category/update.html'
    success_message = 'カテゴリ更新が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'カテゴリ更新'
        return context


class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'shoppinglist/item/list.html'
    paginate_by = 3
    
    def get_queryset(self):
        object_list = Item.objects.select_related('category').all().order_by('id')
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '商品一覧'
        return context


class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('shoppinglist:item_list')
    template_name = 'shoppinglist/item/create.html'
    success_message = '商品新規登録が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '商品新規登録'
        return context


class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('shoppinglist:item_list')
    template_name = 'shoppinglist/item/update.html'
    success_message = '商品更新が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '商品更新'
        return context


class ShoppingListListView(LoginRequiredMixin, ListView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist/list.html'
    paginate_by = 3
    
    def get_queryset(self):
        object_list = ShoppingList.objects.select_related('user').all().order_by('id')
        return object_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピングリスト一覧'
        return context


class ShoppingListCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ShoppingList
    form_class = ShoppingListForm
    success_url = reverse_lazy('shoppinglist:shoppinglist_list')
    template_name = 'shoppinglist/shoppinglist/create.html'
    success_message = 'ショッピングリスト新規登録が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピングリスト新規登録'
        return context


class ShoppingListUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ShoppingList
    form_class = ShoppingListForm
    success_url = reverse_lazy('shoppinglist:shoppinglist_list')
    template_name = 'shoppinglist/shoppinglist/update.html'
    success_message = 'ショッピングリスト更新が完了しました'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピングリスト更新'
        return context


class ShoppingListDetailView(LoginRequiredMixin, DetailView):
    model = ShoppingList
    template_name = 'shoppinglist/shoppinglist/detail.html'
    
    def get_object(self):
        shoppinglist_id = self.kwargs.get('pk')
        object = ShoppingList.objects \
            .filter(id=shoppinglist_id) \
            .select_related('user') \
            .prefetch_related(
                Prefetch(
                    'shoppingitem_set',
                    queryset=ShoppingItem.objects.select_related('item', 'item__category'),
                    to_attr='shoppingitems'
            )) \
            .first()
        return object
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピングリスト詳細'
        return context


class ShoppingItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = 'shoppinglist/shoppingitem/create.html'
    success_message = 'ショッピング商品新規登録が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピング商品新規登録'
        
        # ショッピングリストのモデル取得
        shoppinglist_id = self.kwargs.get('shoppinglist_id')
        shoppinglist = ShoppingList.objects.get(id=shoppinglist_id)
        context['shoppinglist'] = shoppinglist
        return context

    def get_form(self):
        # ショッピングリストのセレクトボックスの初期値設定
        form = super().get_form()
        shoppinglist_id = self.kwargs.get('shoppinglist_id')
        form.fields['shoppinglist'].initial = shoppinglist_id
        return form
    
    def get_success_url(self):
        # 新規登録処理完了後のリダイレクト先の指定
        # ショッピングリストの詳細画面へリダイレクト
        shoppinglist_id = self.object.shoppinglist.id
        return reverse('shoppinglist:shoppinglist_detail', kwargs={'pk': shoppinglist_id})


class ShoppingItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ShoppingItem
    form_class = ShoppingItemForm
    template_name = 'shoppinglist/shoppingitem/update.html'
    success_message = 'ショッピング商品更新が完了しました'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ショッピング商品更新'
        return context
    
    def get_success_url(self):
        # 更新処理完了後のリダイレクト先の指定
        # ショッピングリストの詳細画面へリダイレクト
        shoppinglist_id = self.object.shoppinglist.id
        return reverse('shoppinglist:shoppinglist_detail', kwargs={'pk': shoppinglist_id})

