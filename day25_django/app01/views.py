from django.shortcuts import render
from app01 import models


# Create your views here.

def article(request, *args, **kwargs):
    # print(request.path_info) # 获取当前URL
    # from django.urls import reverse
    # # {'article_type_id': '0', 'category_id': '0'}
    # url = reverse('article', kwargs={'article_type_id': '1', 'category_id': '0'})
    # print(url)
    # print(kwargs)
    condition = {}
    for k, v in kwargs.items():
        kwargs[k] = int(v)
        if v == '0':
            pass
        else:
            condition[k] = v

    article_type_list = models.ArticleType.objects.all()
    category_list = models.Category.objects.all()
    result = models.Article.objects.filter(**condition)
    return render(
        request,
        'article.html_模板中实现',
        {
            'result': result,
            'article_type_list': article_type_list,
            'category_list': category_list,
            'arg_dict': kwargs
        }
    )
