class SecretListView(ListView):
    model = Post
    template_name = 'joseon/secret_list.html'
    context_object_name = 'posts'
    paginate_by = 15

    def get_queryset(self):
        return Post.objects.filter(category__name='비밀').annotate(comment_count=Count('comments'))


@login_required(login_url='login')
def secret(request):
    return render(request, 'joseon/secret_post.html')


def post_secret(request):
    title = request.POST['title']
    category = Category.objects.get(name='비밀')
    contents = request.POST['contents']
    name = make_nickname()
    jprofile = JProfile.objects.only('political_orientation').get(user=request.user)
    qs = Post(
            title=title,
            category=category,
            contents=contents,
            author=request.user,
            anonymous=name,
            political_orientation=jprofile.political_orientation
        )
    qs.save()    

    return HttpResponseRedirect(reverse('joseon:secret_list'))
