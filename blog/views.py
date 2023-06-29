from ast import keyword
from unicodedata import category, name
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from .models import Post,Category,PostView
from django.urls import path
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    title='FIRST BLOG(検証)!!'
    # all_articles = Post.objects.all()
    # paginator = Paginator(all_articles, 2) # 1ページに10件表示
    # p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    # articles = paginator.get_page(p) # 指定のページのArticleを取得
    # post_list = Post.objects.all()
    # page_obj = paginate_queryset(request, post_list, 3)
    # category_data = Category.objects.all()
    # post_list = Post.objects.order_by('created_date').reverse()
    
    # 記事用のViewを検索
    postview_data = PostView.objects.all()
    # ページング
    page_obj = paginate_queryset(request, postview_data, 3)
    # htmlにレスポンスを返す変数
    params={
        'title':title,
        # 'post_list': page_obj.object_list,
        'page_obj': page_obj
    }
    return render(request,'blog/index.html',params)


def paginate_queryset(request, queryset, count):
    """Pageオブジェクトを返す。

    ページングしたい場合に利用してください。

    countは、1ページに表示する件数です。
    返却するPgaeオブジェクトは、以下のような感じで使えます。

        {% if page_obj.has_previous %}
          <a href="?page={{ page_obj.previous_page_number }}">Prev</a>
        {% endif %}

    また、page_obj.object_list で、count件数分の絞り込まれたquerysetが取得できます。

    """
    paginator = Paginator(queryset, count)
    page = request.GET.get('page')
    try:
        page_obj = paginator.page(page)
    # 整数でない値がリクエストされた際
    except PageNotAnInteger: 
        page_obj = paginator.page(1)
    # 有効な値がリクエストされているが、そのページが存在していない
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    return page_obj





# class IndexView(TemplateView):
#     template_name = 'blog/index.html'

class PostListView(ListView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し
    # model=PostView
    paginate_by = 1
    

class PostListDetailView(DetailView): # generic の ListViewクラスを継承
    model = Post # 一覧表示させたいモデルを呼び出し
    #レコード情報をテンプレートに渡すオブジェクト
    context_object_name = "post_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'FIRST BLOG(検証)!!'
        return context

class CategoryView(View):
    def get(self,request,*args,**kwards):
        # aiu=request.Get['category']
        # category_data=Category.objects.get(name=aiu)
        category_data=Category.objects.get(category=self.kwargs['category'])
        # print(category_data)
        # post_data=Post.objects.order_by('-id').filter(category=category_data)
        post_data=PostView.objects.order_by('-id').filter(category=category_data)
        # title=post_data + 'FIRST BLOG(検証)！！ '
        title='FIRST BLOG(検証)!!'

        # 記事用のViewを検索
        # postview_data = PostView.objects.all()

        # all_articles = Post.objects.all()
        # paginator = Paginator(all_articles, 2) # 1ページに10件表示
        # p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
        # articles = paginator.get_page(p) # 指定のページのArticleを取得
        # page_obj = paginate_queryset(request, post_data, 1)
        page_obj = paginate_queryset(request, post_data, 3)
    
        return render(request,'blog/post_category.html',
        {   
            'title':title,
            'post_data':page_obj.object_list,
            'category_data':category_data,
            # 'postview_data':postview_data,
            'page_obj': page_obj
        }
        )


class SearchView(View):
    def get(self,request,*args,**kwards):
        title='FIRST BLOG(検証)!!'
        keyword=request.GET.get('keyword')
        if keyword:
            # search_data = Post.objects.filter(Q(title__icontains=keyword)|Q(text__icontains=keyword))
            search_data = PostView.objects.filter(Q(title__icontains=keyword)|Q(text__icontains=keyword))
            page_obj = paginate_queryset(request, search_data, 1)
            return render(request,'blog/post_search.html',
            {
                'title':title,
                'search_data':page_obj.object_list,
                'keyword':keyword,
                'page_obj': page_obj
            })
        else:
            # search_data = Post.objects.order_by('-id').all()
            search_data = PostView.objects.order_by('-id').all()
            
            page_obj = paginate_queryset(request, search_data, 3)
            return render(request,'blog/index.html',
            {
                'title':title,
                'articles':page_obj.object_list,
                'keyword':keyword,
                'page_obj': page_obj
            })





# class CategoryView(ListView):
#     model = Post
#     template_name = 'blog/index.html'

#     def get_queryset(self):
#         category = Category.objects.get(name=self.kwargs['category'])
#         print (category)
#         queryset = Post.objects.order_by('-id').filter(category=category)
#         return queryset

#     """ アクセスされた値を取得し辞書に格納 """
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['category_key'] = self.kwargs['category']
#         return context



# def category(request, category):
#     sql="select * from blog_post where category_id in (select id from blog_category where category= '%s') "
#     print (sql)
#     # params = {"category": category, }
#     category = Category.objects.raw('select * from blog_post where category_id in (select id from blog_category where category="旅行")')
#     # category = Category.objects.get(category=category)
#     blog = Post.objects.filter(category=category)
#     return render(request, 'blog/post_category.html',
#                 #    {'blog': blog,'category': category })
#                     {'category': category })