from django.contrib.auth import authenticate, login as auth_login, logout
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.views import generic
from django.contrib.auth.views import LogoutView
from django.views.generic import RedirectView
from home.models import Banner

from virgilbookstore.permissions import AdministratorPermission, LoginRequiredPermission
from .models import Profile, ProfileNewsletter, ProfileOffer
from .forms import LoginAuthenticationForm, LoginForm, SignUpForm


@login_required(login_url="/login")
def index(request):
    return render(request, "user/profile_page.html")


def signup_form(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            auth_login(request, user)

            data = Profile()
            data.save()
            messages.success(request, "Conta criada com sucesso!")
            return HttpResponseRedirect(reverse("user:profile"))
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect(reverse("user:signup"))

    context = {"form": SignUpForm()}
    return render(request, "user/signup_page.html", context)


def login(request):
    if request.method == "POST":
        form = LoginAuthenticationForm(request, data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())

            return HttpResponseRedirect(reverse("user:dashboard"))
        else:
            messages.warning(request, "Erro, usuário ou senha inválidos!")
            return HttpResponseRedirect(reverse("user:login"))

    context = {"form": LoginForm()}

    return render(request, "pages/login.html", context)


class AddProfileOffersView(views.APIView):
    queryset = ProfileOffer.objects.all()

    def post(self, request):
        if request.data.get("email"):
            self.queryset.get_or_create(email=request.data.get("email"))
            return Response(
                {"message": "E-mail adicionado para ofertas da Loja"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({"message": "Erro"}, status=status.HTTP_400_BAD_REQUEST)


class AddProfileNewsletterView(views.APIView):
    queryset = ProfileNewsletter.objects.all()

    def post(self, request):
        name = request.data.get("name")
        if name:
            self.queryset.get_or_create(email=request.data.get("email"), name=name)
            return Response(
                {"message": "E-mail adicionado na Newsletter"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response({"message": "Erro"}, status=status.HTTP_400_BAD_REQUEST)


class DashBoardProfile(LoginRequiredPermission, generic.TemplateView):
    template_name = "pages/dashboard.html"


class AccountsListView(AdministratorPermission, generic.ListView):
    queryset = Profile.objects.all()
    template_name = "user/accounts_table.html"

    def get(self, request):
        context = {"profiles": self.queryset.all()}
        return render(request, self.template_name, context)


class UpdatePasswordView(generic.TemplateView):
    template_name = "user/user_update_password.html"


class UpdatePasswordService(views.APIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        profile = request.user
        password = self.request.data["password"]

        if password:
            profile.set_password(password)
            profile.save()
            return Response(
                {"message": "Senha alterada com sucesso"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "Houve problema a salvar sua senha"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileUpdateView(generic.TemplateView):
    template_name = "user/user_update.html"

    def get(self, request):
        context = {}
        query = self.request.build_absolute_uri().split("id=")
        if len(query) > 1:
            context["profile"] = Profile.objects.get(id=query[1])
        else:
            context["profile"] = request.user

        return render(request, self.template_name, context)


class ProfileUpdateService(views.APIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk):
        data = request.data
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        phone = request.data.get("phone")
        is_active = False if not data.get("is_active") else True

        if data:
            Profile.objects.filter(id=pk).update(
                email=email,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                is_active=is_active,
            )
            return Response(
                {"message": "Profile updated successfully"}, status=status.HTTP_200_OK
            )
        return Response(
            {"message": "There were problems updating your profile"},
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProfileRemoveService(generics.DestroyAPIView):
    queryset = Profile.objects.all()
    permission_classes = (IsAuthenticated,)


class LogoutView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = "home:home"

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)


class ManagerBannersView(generic.TemplateView):
    template_name = "user/manager_banners.html"

    def get(self, request):
        context = {
            "banners": Banner.objects.all(),
        }

        return render(request, self.template_name, context)
