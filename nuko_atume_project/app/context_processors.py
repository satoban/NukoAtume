from .models import Category


def common(request):
    category_data = Category.objects.all()  # 全てのカテゴリーデータを取得する
    context = {
        'category_data': category_data
    }
    return context
