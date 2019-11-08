from django.shortcuts import get_object_or_404, render
from wiki.models import Page
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class PageList(ListView):
    """
    CHALLENGES:
      1. On GET, display a homepage that shows all Pages in your wiki.
      2. Replace this CHALLENGE text with a descriptive docstring for PageList.
        - Pagelist is a ListView that get() the 5 most recent published wikis from Wiki model and renders it in wiki/list.html

      3. Replace pass below with the code to render a template named `list.html`.
    """
    model = Page
    # template_name = "wiki/list.html"
    # context_object_name = "pages" #specify or default will be object_list

    def get(self, request):
        """ Returns a list of wiki pages. """
        # latest_wiki_list = Page.objects.order_by('-pub_date')[:5] #grab 5 most recent wikis 
        # context = { 'latest_wiki_list': latest_wiki_list, }
        all_pages = Page.objects.all()
        context = { 'all_pages': all_pages }
        return render(request, 'wiki/list.html', context) #shortcut render


class PageDetailView(DetailView):
    """
    CHALLENGES:
      1. On GET, render a template named `page.html`.
      2. Replace this docstring with a description of what thos accomplishes.
        - PageDetailView's DetailView takes a wiki_id that was passed and get the detail of the wiki and display in detail.html,
          if wiki does not exist, then it will raise an Http404

    STRETCH CHALLENGES:
      1. Import the PageForm class from forms.py.
          - This ModelForm enables editing of an existing Page object in the database.
      2. On GET, render an edit form below the page details.
      3. On POST, check if the data in the form is valid.
        - If True, save the data, and redirect back to the DetailsView.
        - If False, display all the errors in the template, above the form fields.
      4. Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
      5. After successfully editing a Page, use Django Messages to "flash" the user a success message
           - Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
    """
    model = Page

    def get(self, request, slug):
        """ Returns a specific of wiki page by slug. """
        # page = Page.objects.get(slug = slug) #meredith's approach
        page = get_object_or_404(Page, slug=slug) #django.shortcut to get if the wiki exist or not
        context = {
          'page': page
        }
        return render(request, 'wiki/detail.html', context)

    def post(self, request, slug):
        pass
