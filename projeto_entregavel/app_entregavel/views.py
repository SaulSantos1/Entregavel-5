from django.shortcuts import render

def home(request):
    if request.method == 'POST':
        # Obtém os valores dos campos de entrada
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')

        # Imprime os valores (você pode modificar esta parte conforme necessário)
        print(f'Nome: {nome}')
        print(f'Idade: {idade}')

    return render(request, 'usuarios/home.html')