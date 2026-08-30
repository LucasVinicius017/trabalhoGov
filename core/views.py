from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, PontoWifi, Manutencao
from django.db.models import Q
from django.contrib import messages

from django.http import HttpResponse
from io import BytesIO

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# Create your views here.
def index(request):
    return render(request, "index.html")
def login(request):

    if request.method == "POST":

        email = request.POST["email"]
        senha = request.POST["senha"]

        try:

            usuario = Usuario.objects.get(
                email=email,
                senha=senha
            )

            request.session["usuario_id"] = usuario.id
            request.session["usuario_nome"] = usuario.nome
            request.session["usuario_perfil"] = usuario.perfil

            return redirect("dashboard")

        except Usuario.DoesNotExist:

            messages.error(
                request,
                "E-mail ou senha inválidos."
            )

    return render(request, "login.html")
def usuarios(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    usuarios = Usuario.objects.all()

    pesquisa = ""

    if request.method == "POST":

        pesquisa = request.POST.get("pesquisa")

        if pesquisa:

            usuarios = Usuario.objects.filter(
                Q(nome__icontains=pesquisa) |
                Q(email__icontains=pesquisa)
            )

    return render(
        request,
        "usuarios.html",
        {
            "usuarios": usuarios,
            "pesquisa": pesquisa
        }
    )
def novo_usuario(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    if request.method == "POST":

        Usuario.objects.create(

            nome=request.POST["nome"],
            email=request.POST["email"],
            senha=request.POST["senha"],
            perfil=request.POST["perfil"],
            status=request.POST["status"]

        )

        return redirect("usuarios")

    return render(request, "cadastro_usuario.html")
from django.shortcuts import get_object_or_404

def editar_usuario(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    usuario = get_object_or_404(Usuario, id=id)

    if request.method == "POST":

        usuario.nome = request.POST.get("nome")
        usuario.email = request.POST.get("email")
        usuario.senha = request.POST.get("senha")
        usuario.perfil = request.POST.get("perfil")
        usuario.status = request.POST.get("status")

        usuario.save()

        return redirect("usuarios")

    return render(request, "editar_usuario.html", {"usuario": usuario})
def excluir_usuario(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    usuario = get_object_or_404(Usuario, id=id)

    usuario.delete()

    return redirect("usuarios")
def pontos(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    pesquisa = ""

    pontos = PontoWifi.objects.all()

    if request.method == "POST":

        pesquisa = request.POST.get("pesquisa")

        if pesquisa:

            pontos = PontoWifi.objects.filter(

                Q(codigo__icontains=pesquisa) |
                Q(nome__icontains=pesquisa) |
                Q(cidade__icontains=pesquisa) |
                Q(status__icontains=pesquisa)

            )

    return render(

        request,

        "pontos.html",

        {

            "pontos": pontos,
            "pesquisa": pesquisa

        }

    )
def novo_ponto(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    if request.method == "POST":

        PontoWifi.objects.create(

            codigo=request.POST.get("codigo"),
            nome=request.POST.get("nome"),
            endereco=request.POST.get("endereco"),
            bairro=request.POST.get("bairro"),
            cidade=request.POST.get("cidade"),
            ip=request.POST.get("ip"),
            status=request.POST.get("status"),
            observacao=request.POST.get("observacao")

        )

        return redirect("pontos")

    return render(request, "cadastro_ponto.html")
def editar_ponto(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    ponto = get_object_or_404(PontoWifi, id=id)

    if request.method == "POST":

        ponto.codigo = request.POST.get("codigo")
        ponto.nome = request.POST.get("nome")
        ponto.endereco = request.POST.get("endereco")
        ponto.bairro = request.POST.get("bairro")
        ponto.cidade = request.POST.get("cidade")
        ponto.ip = request.POST.get("ip")
        ponto.status = request.POST.get("status")
        ponto.observacao = request.POST.get("observacao")

        ponto.save()

        return redirect("pontos")

    return render(
        request,
        "editar_ponto.html",
        {"ponto": ponto}
    )
def excluir_ponto(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    ponto = get_object_or_404(PontoWifi, id=id)

    ponto.delete()

    return redirect("pontos")
def dashboard(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    total_pontos = PontoWifi.objects.count()

    pontos_online = PontoWifi.objects.filter(
        status="Online"
    ).count()

    pontos_offline = PontoWifi.objects.filter(
        status="Offline"
    ).count()

    pontos_manutencao = PontoWifi.objects.filter(
        status="Manutencao"
    ).count()

    total_usuarios = Usuario.objects.count()

    ultimos_pontos = PontoWifi.objects.order_by("-id")[:5]

    context = {

        "total_pontos": total_pontos,
        "pontos_online": pontos_online,
        "pontos_offline": pontos_offline,
        "pontos_manutencao": pontos_manutencao,
        "total_usuarios": total_usuarios,
        "ultimos_pontos": ultimos_pontos,

    }

    return render(
        request,
        "dashboard.html",
        context
    )
def relatorios(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    total_pontos = PontoWifi.objects.count()

    pontos_online = PontoWifi.objects.filter(
        status="Online"
    ).count()

    pontos_offline = PontoWifi.objects.filter(
        status="Offline"
    ).count()

    pontos_manutencao = PontoWifi.objects.filter(
        status="Manutencao"
    ).count()

    data_inicial = ""
    data_final = ""
    tipo = "todos"

    pontos = PontoWifi.objects.all()
    manutencoes = Manutencao.objects.all()
    usuarios = Usuario.objects.all()

    mostrar_resultado = False

    if request.method == "POST":

        data_inicial = request.POST.get(
            "data_inicial",
            ""
        )

        data_final = request.POST.get(
            "data_final",
            ""
        )

        tipo = request.POST.get(
            "tipo",
            "todos"
        )

        acao = request.POST.get(
            "acao"
        )

        # FILTRO DE DATA - MANUTENÇÕES

        if data_inicial:
            manutencoes = manutencoes.filter(
                data_abertura__gte=data_inicial
            )

        if data_final:
            manutencoes = manutencoes.filter(
                data_abertura__lte=data_final
            )

        # FILTRO DE DATA - USUÁRIOS

        if data_inicial:
            usuarios = usuarios.filter(
                data_cadastro__date__gte=data_inicial
            )

        if data_final:
            usuarios = usuarios.filter(
                data_cadastro__date__lte=data_final
            )

        # GERAR PDF

        if acao == "pdf":

            buffer = BytesIO()

            documento = SimpleDocTemplate(
                buffer,
                pagesize=A4,
                rightMargin=30,
                leftMargin=30,
                topMargin=30,
                bottomMargin=30
            )

            estilos = getSampleStyleSheet()

            titulo = estilos["Title"]
            titulo.alignment = TA_CENTER

            subtitulo = estilos["Heading2"]

            texto = estilos["Normal"]

            elementos = []

            elementos.append(
                Paragraph(
                    "Monitor PMPP",
                    titulo
                )
            )

            elementos.append(
                Paragraph(
                    "Relatório do Sistema",
                    subtitulo
                )
            )

            elementos.append(
                Spacer(1, 15)
            )

            # RESUMO

            resumo = [
                ["Resumo", "Quantidade"],
                ["Total de Pontos", str(total_pontos)],
                ["Pontos Online", str(pontos_online)],
                ["Pontos Offline", str(pontos_offline)],
                ["Pontos em Manutenção", str(pontos_manutencao)]
            ]

            tabela_resumo = Table(
                resumo,
                colWidths=[300, 150]
            )

            tabela_resumo.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#0F5FA8")
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "PADDING",
                        (0, 0),
                        (-1, -1),
                        8
                    )
                ])
            )

            elementos.append(
                tabela_resumo
            )

            elementos.append(
                Spacer(1, 20)
            )

            # PONTOS WI-FI

            if tipo in ["todos", "pontos"]:

                elementos.append(
                    Paragraph(
                        "Pontos Wi-Fi",
                        subtitulo
                    )
                )

                dados_pontos = [
                    [
                        "Código",
                        "Nome",
                        "Cidade",
                        "IP",
                        "Status"
                    ]
                ]

                for ponto in pontos:

                    dados_pontos.append([
                        str(ponto.codigo),
                        str(ponto.nome),
                        str(ponto.cidade),
                        str(ponto.ip),
                        str(ponto.status)
                    ])

                if len(dados_pontos) == 1:

                    dados_pontos.append([
                        "-",
                        "Nenhum ponto encontrado",
                        "-",
                        "-",
                        "-"
                    ])

                tabela_pontos = Table(
                    dados_pontos,
                    repeatRows=1
                )

                tabela_pontos.setStyle(
                    TableStyle([
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.HexColor("#0F5FA8")
                        ),
                        (
                            "TEXTCOLOR",
                            (0, 0),
                            (-1, 0),
                            colors.white
                        ),
                        (
                            "FONTNAME",
                            (0, 0),
                            (-1, 0),
                            "Helvetica-Bold"
                        ),
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey
                        ),
                        (
                            "PADDING",
                            (0, 0),
                            (-1, -1),
                            6
                        )
                    ])
                )

                elementos.append(
                    tabela_pontos
                )

                elementos.append(
                    Spacer(1, 20)
                )

            # MANUTENÇÕES

            if tipo in ["todos", "manutencoes"]:

                elementos.append(
                    Paragraph(
                        "Manutenções",
                        subtitulo
                    )
                )

                dados_manutencoes = [
                    [
                        "Ponto",
                        "Problema",
                        "Responsável",
                        "Status"
                    ]
                ]

                for manutencao in manutencoes:

                    dados_manutencoes.append([
                        str(manutencao.ponto.nome),
                        str(manutencao.problema),
                        str(manutencao.responsavel.nome),
                        str(manutencao.status)
                    ])

                if len(dados_manutencoes) == 1:

                    dados_manutencoes.append([
                        "-",
                        "Nenhuma manutenção encontrada",
                        "-",
                        "-"
                    ])

                tabela_manutencoes = Table(
                    dados_manutencoes,
                    repeatRows=1
                )

                tabela_manutencoes.setStyle(
                    TableStyle([
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.HexColor("#0F5FA8")
                        ),
                        (
                            "TEXTCOLOR",
                            (0, 0),
                            (-1, 0),
                            colors.white
                        ),
                        (
                            "FONTNAME",
                            (0, 0),
                            (-1, 0),
                            "Helvetica-Bold"
                        ),
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey
                        ),
                        (
                            "PADDING",
                            (0, 0),
                            (-1, -1),
                            6
                        )
                    ])
                )

                elementos.append(
                    tabela_manutencoes
                )

                elementos.append(
                    Spacer(1, 20)
                )

            # USUÁRIOS

            if tipo in ["todos", "usuarios"]:

                elementos.append(
                    Paragraph(
                        "Usuários",
                        subtitulo
                    )
                )

                dados_usuarios = [
                    [
                        "Nome",
                        "E-mail",
                        "Perfil",
                        "Status"
                    ]
                ]

                for usuario in usuarios:

                    dados_usuarios.append([
                        str(usuario.nome),
                        str(usuario.email),
                        str(usuario.perfil),
                        str(usuario.status)
                    ])

                if len(dados_usuarios) == 1:

                    dados_usuarios.append([
                        "-",
                        "Nenhum usuário encontrado",
                        "-",
                        "-"
                    ])

                tabela_usuarios = Table(
                    dados_usuarios,
                    repeatRows=1
                )

                tabela_usuarios.setStyle(
                    TableStyle([
                        (
                            "BACKGROUND",
                            (0, 0),
                            (-1, 0),
                            colors.HexColor("#0F5FA8")
                        ),
                        (
                            "TEXTCOLOR",
                            (0, 0),
                            (-1, 0),
                            colors.white
                        ),
                        (
                            "FONTNAME",
                            (0, 0),
                            (-1, 0),
                            "Helvetica-Bold"
                        ),
                        (
                            "GRID",
                            (0, 0),
                            (-1, -1),
                            0.5,
                            colors.grey
                        ),
                        (
                            "PADDING",
                            (0, 0),
                            (-1, -1),
                            6
                        )
                    ])
                )

                elementos.append(
                    tabela_usuarios
                )

            documento.build(
                elementos
            )

            buffer.seek(0)

            resposta = HttpResponse(
                buffer,
                content_type="application/pdf"
            )

            resposta["Content-Disposition"] = (
                'attachment; filename="relatorio_monitor_pmpp.pdf"'
            )

            return resposta

        # GERAR EXCEL
        
        if acao == "excel":

            workbook = Workbook()

            # Remove a planilha padrão
            planilha = workbook.active
            planilha.title = "Resumo"

            # TÍTULO

            planilha["A1"] = "Monitor PMPP"
            planilha["A1"].font = Font(
                bold=True,
                size=18
            )

            planilha["A2"] = "Relatório do Sistema"
            planilha["A2"].font = Font(
                bold=True,
                size=14
            )

            # RESUMO

            planilha["A4"] = "Resumo"
            planilha["A4"].font = Font(
                bold=True,
                size=14
            )

            planilha["A5"] = "Descrição"
            planilha["B5"] = "Quantidade"

            for celula in planilha[5]:
                celula.font = Font(
                    bold=True
                )

            planilha["A6"] = "Total de Pontos"
            planilha["B6"] = total_pontos

            planilha["A7"] = "Pontos Online"
            planilha["B7"] = pontos_online

            planilha["A8"] = "Pontos Offline"
            planilha["B8"] = pontos_offline

            planilha["A9"] = "Pontos em Manutenção"
            planilha["B9"] = pontos_manutencao

            # PONTOS WI-FI

            if tipo in ["todos", "pontos"]:

                planilha_pontos = workbook.create_sheet(
                    "Pontos Wi-Fi"
                )

                planilha_pontos.append([
                    "Código",
                    "Nome",
                    "Cidade",
                    "IP",
                    "Status"
                ])

                for celula in planilha_pontos[1]:
                    celula.font = Font(
                        bold=True
                    )

                for ponto in pontos:

                    planilha_pontos.append([
                        ponto.codigo,
                        ponto.nome,
                        ponto.cidade,
                        ponto.ip,
                        ponto.status
                    ])

            # MANUTENÇÕES

            if tipo in ["todos", "manutencoes"]:

                planilha_manutencoes = workbook.create_sheet(
                    "Manutenções"
                )

                planilha_manutencoes.append([
                    "Ponto Wi-Fi",
                    "Problema",
                    "Responsável",
                    "Status"
                ])

                for celula in planilha_manutencoes[1]:
                    celula.font = Font(
                        bold=True
                    )

                for manutencao in manutencoes:

                    planilha_manutencoes.append([
                        manutencao.ponto.nome,
                        manutencao.problema,
                        manutencao.responsavel.nome,
                        manutencao.status
                    ])

            # USUÁRIOS

            if tipo in ["todos", "usuarios"]:

                planilha_usuarios = workbook.create_sheet(
                    "Usuários"
                )

                planilha_usuarios.append([
                    "Nome",
                    "E-mail",
                    "Perfil",
                    "Status"
                ])

                for celula in planilha_usuarios[1]:
                    celula.font = Font(
                        bold=True
                    )

                for usuario in usuarios:

                    planilha_usuarios.append([
                        usuario.nome,
                        usuario.email,
                        usuario.perfil,
                        usuario.status
                    ])

            # AJUSTAR LARGURA DAS COLUNAS

            for planilha_atual in workbook.worksheets:

                for coluna in planilha_atual.columns:

                    maior_tamanho = 0

                    numero_coluna = coluna[0].column

                    letra_coluna = get_column_letter(
                        numero_coluna
                    )

                    for celula in coluna:

                        if celula.value is not None:

                            tamanho = len(
                                str(celula.value)
                            )

                            if tamanho > maior_tamanho:
                                maior_tamanho = tamanho

                    planilha_atual.column_dimensions[
                        letra_coluna
                    ].width = maior_tamanho + 3

            # GERAR ARQUIVO

            resposta = HttpResponse(
                content_type=(
                    "application/vnd.openxmlformats-officedocument."
                    "spreadsheetml.sheet"
                )
            )

            resposta["Content-Disposition"] = (
                'attachment; filename="relatorio_monitor_pmpp.xlsx"'
            )

            workbook.save(
                resposta
            )

            return resposta

        # VISUALIZAR

        if acao == "visualizar":

            mostrar_resultado = True

    context = {

        "total_pontos": total_pontos,

        "pontos_online": pontos_online,

        "pontos_offline": pontos_offline,

        "pontos_manutencao": pontos_manutencao,

        "pontos": pontos,

        "manutencoes": manutencoes,

        "usuarios": usuarios,

        "data_inicial": data_inicial,

        "data_final": data_final,

        "tipo": tipo,

        "mostrar_resultado": mostrar_resultado

    }

    return render(
        request,
        "relatorios.html",
        context
    )
def manutencoes(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    pesquisa = ""

    manutencoes = Manutencao.objects.all()

    if request.method == "POST":

        pesquisa = request.POST.get("pesquisa")

        if pesquisa:

            manutencoes = Manutencao.objects.filter(
                Q(problema__icontains=pesquisa) |
                Q(status__icontains=pesquisa) |
                Q(responsavel__nome__icontains=pesquisa) |
                Q(ponto__nome__icontains=pesquisa)
            )

    return render(
        request,
        "manutencoes.html",
        {
            "manutencoes": manutencoes,
            "pesquisa": pesquisa
        }
    )
def nova_manutencao(request):

    if "usuario_id" not in request.session:
        return redirect("login")

    pontos = PontoWifi.objects.all()
    usuarios = Usuario.objects.all()

    if request.method == "POST":

        ponto = PontoWifi.objects.get(
            id=request.POST["ponto"]
        )

        responsavel = Usuario.objects.get(
            id=request.POST["responsavel"]
        )

        Manutencao.objects.create(

            ponto=ponto,

            problema=request.POST["problema"],

            responsavel=responsavel,

            data_abertura=request.POST["data_abertura"],

            status=request.POST["status"],

            observacao=request.POST["observacao"]

        )

        return redirect("manutencoes")

    return render(

        request,

        "cadastro_manutencao.html",

        {

            "pontos": pontos,

            "usuarios": usuarios

        }

    )
def editar_manutencao(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    manutencao = Manutencao.objects.get(id=id)

    pontos = PontoWifi.objects.all()

    usuarios = Usuario.objects.all()

    if request.method == "POST":

        manutencao.ponto = PontoWifi.objects.get(
            id=request.POST["ponto"]
        )

        manutencao.problema = request.POST["problema"]

        manutencao.responsavel = Usuario.objects.get(
            id=request.POST["responsavel"]
        )

        manutencao.data_abertura = request.POST["data_abertura"]

        manutencao.status = request.POST["status"]

        manutencao.observacao = request.POST["observacao"]

        manutencao.save()

        return redirect("manutencoes")

    context = {

        "manutencao": manutencao,

        "pontos": pontos,

        "usuarios": usuarios

    }

    return render(
        request,
        "editar_manutencao.html",
        context
    )
def excluir_manutencao(request, id):

    if "usuario_id" not in request.session:
        return redirect("login")

    manutencao = get_object_or_404(
        Manutencao,
        id=id
    )

    if request.method == "POST":

        manutencao.delete()

        return redirect("manutencoes")

    return redirect("manutencoes")
def logout(request):

    request.session.flush()

    return redirect("login")