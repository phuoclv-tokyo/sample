from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        ctxt["username"] = "phuoclv"
        return ctxt

class AboutView(TemplateView):
    template_name = "about.html"
    
    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data()
        ctxt["skills"] = [
                "Python",
                "Django",
                "Java"
            ]
        return ctxt