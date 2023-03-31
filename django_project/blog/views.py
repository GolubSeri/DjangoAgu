from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Post, Comment
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, CommentForm


def CustomForm(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "custom_form.html", {"form": userform})


class PostListView(ListView):
    model = Post
    paginate_by = 2
    template_name = "home.html"


class PostDisplay(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class PostComment(SingleObjectMixin, FormView):
    model = Post
    form_class = CommentForm
    template_name = 'post_detail.html'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(PostComment, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.object
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        post = self.get_object()
        return reverse('post_detail', kwargs={'pk': post.pk}) + '#comments'


class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        view = PostDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PostComment.as_view()
        return view(request, *args, **kwargs)


class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


class CommentDelete(DeleteView):
    model = Comment
    template_name = "comment_delete.html"
    success_url = reverse_lazy("home")
