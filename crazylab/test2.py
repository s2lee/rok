class CrazyIdeaListView(ListView):
    model = Post
    template_name = 'crazylab/crazyidea_list.html'
    context_object_name = 'posts'
    paginate_by = 47

    def get_queryset(self):
        return Post.objects.filter(category__name='크레이지아이디어').select_related('author').prefetch_related(
            'author__profile').annotate(comment_count=Count('comments'))

    def get_context_data(self, **kwargs):
        context = super(CrazyIdeaListView, self).get_context_data(**kwargs)
        context['tops'] = Post.objects.filter(category__name='크레이지아이디어').annotate(comment_count=Count('comments')).order_by('-all_recommend','-date_posted')[:5]

        return context


def post_crazyidea(request):
    if request.method == "POST":
        form =  CrazyIdeaPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.category =  Category.objects.get(name='크레이지아이디어')
            post.save()
            coin = Coin.objects.only('blackcoin').get(user=request.user)
            coin.blackcoin += 1
            coin.save()
            return HttpResponseRedirect(reverse('crazylab:crazyidea_list'))
    else:
        form =  CrazyIdeaPostForm()

    context = {
        'form' : form,
    }
    return render(request, 'crazylab/crazyidea_post.html', context)
