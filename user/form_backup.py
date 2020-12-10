
username = forms.CharField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Nome de usuário:'}))

email = forms.EmailField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'E-mail', 'id': 'input-email', 'name': 'email'}))

first_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Nome', 'id': 'input-firstname', 'name': 'firstname'}))

last_name = forms.CharField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Sobrenome', 'id': 'input-lastname', 'name': 'lastname'}))

phone = forms.CharField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Celular', 'id': 'input-telephone', 'name': 'telephone'}))

address = forms.CharField(max_length=30, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Endereço', 'id': 'input-address-1', 'name': 'address_1'}))

number_address = forms.IntegerField(label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Número da casa/AP', 'id': 'input-address-2', 'name': 'address_2'}))

zip_code = forms.CharField(max_length=50, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'CEP', 'id': 'input-postcode', 'name': 'postcode'}))

city = forms.CharField(max_length=50, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'Cidade'}))

state = forms.CharField(max_length=50, label='', widget=forms.TextInput(
    attrs={'class': 'form-control', 'placeholder': 'País'}))

password1 = forms.CharField(max_length=50, label='', widget=forms.PasswordInput(
    attrs={'class': 'form-control', 'placeholder': 'Senha'}))

password2 = forms.CharField(max_length=50, label='', widget=forms.PasswordInput(
    attrs={'class': 'form-control', 'placeholder': 'Confirme a senha'}))
