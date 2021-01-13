from django.views.generic import ListView, DetailView
from .models import Post

class Index(ListView):
    model = Post

class Detail(DetailView):
    model = Post
    
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class Create(CreateView):
    model = Post
    
    fields = ["title", "body", "category", "tags"]

class Update(UpdateView):
    model = Post
    
    fields = ["title", "body", "category", "tags"]

class Delete(DeleteView):
    model = Post
    
    success_url = "/blog"

from django.views.generic.edit import FormView

from . import forms

class ChangeText(FormView):
    form_class = forms.TextForm
    template_name = "change/change_text.html"
    
    # フォームの入力にエラーが無かった場合に呼ばれます
    def form_valid(self, form):
        # form.cleaned_dataにフォームの入力内容が入っています
        data = form.cleaned_data
        text = data["text"]
        search = data["search"]
        replace = data["replace"]
        
        #ここで変換
        new_text = text.replace(search, replace)
        
        # テンプレートに渡す
        ctxt = self.get_context_data(new_text=new_text, form=form)
        return self.render_to_response(ctxt)
    
