from django.contrib.auth import login, authenticate
def signin(request):
    if request.method == "GET":
        return render(request, 'customlogin/signin.html', {'f':SigninForm()} )
    elif request.method == "POST":
        form = SigninForm(request.POST)
        id = request.POST['username']
        pw = request.POST['password']
        u = authenticate(username=id, password=pw)
        if u:
            login(request, user=u)
            return HttpResponseRedirect(reverse('vote:index'))
        else:
            return render(request, 'customlogin/signin.html',{'f':form, 'error':'아이디나 비밀번호가 일치하지 않습니다.'})
from django.contrib.auth import logout
def signout(request):
    logout(request)
    return HttpResponseRedirect(reverse('vote:index'))
