from django.db.models import Q
from django.views.generic import ListView
from .models import Package

class HomePageView(ListView):
    model = Package
    template_name = "home.html"
    context_object_name = "packages"

    def get_queryset(self):

        queryset = super().get_queryset()
        search_type = self.request.POST.get("search_type", "")
        search_query = self.request.POST.get("search_query", "")

        if search_query:
            if search_type == "author":
                queryset = queryset.filter(author__icontains=search_query)
            elif search_type == "email":
                queryset = queryset.filter(email__icontains=search_query)
            elif search_type == "description":
                queryset = queryset.filter(description__icontains=search_query)
            elif search_type == "keywords":
                queryset = queryset.filter(keywords__icontains=search_query)
            elif search_type == "version":
                queryset = queryset.filter(version__icontains=search_query)
            elif search_type == "maintainer":
                queryset = queryset.filter(maintainer__icontains=search_query)
            else:
                queryset = queryset.filter(
                    Q(author__icontains=search_query)
                    | Q(email__icontains=search_query)
                    | Q(description__icontains=search_query)
                    | Q(keywords__icontains=search_query)
                    | Q(version__icontains=search_query)
                    | Q(maintainer__icontains=search_query)
                )

        return queryset

    def get(self, request, *args, **kwargs):
        # Handle GET requests here
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # Handle POST requests here
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        return self.render_to_response(context)