from django import forms
from .models import Category

class PostForm(forms.Form):
    category_data = Category.objects.all()
    category_choice = {}
    for category in category_data:
        category_choice[category] = category
        
    title = forms.CharField(max_length=30, label='タイトル')
    category = forms.ChoiceField(label='カテゴリ', widget=forms.Select,
                            choices=list(category_choice.items())) # ホームで登録されたカテゴリが選択できる
    
    content = forms.CharField(label='内容', widget=forms.Textarea())
    