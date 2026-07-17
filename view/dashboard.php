<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../assets/css/dashboard.css">
    <title>Dashboard</title>
</head>
<body>
    <aside class="sidebar">
        <h1 class="logo">Monitor PMPP</h1>
        <nav class="menu">
            <ul class="menu-lista">
                <li class="ativo">Dashboard</li>
                <li>Pontos Wi-Fi</li>
                <li>Manutenções</li>
                <li>Usuários</li>
                <li>Relatórios</li>
                <li>Configurações</li>
                <li>Sair</li>
            </ul>
        </nav>
    </aside>
    <section class="conteudo">
        <header class="topbar">
            <h1>Dashboard</h1>
            <p>Seja bem-vindo ao Monitor PMPP</p>
        </header>
        <main class="dashboard">
            <section class="cards">
                <article class="card">
                    <h2>Pontos Online</h2>
                    <p class="valor">58</p>
                </article>
                <article class="card">
                    <h2>Pontos Offline</h2>
                    <p class="valor">4</p>
                </article>
                <article class="card">
                    <h2>Em Manutenção</h2>
                    <p class="valor">7</p>
                </article>
                <article class="card">
                    <h2>Total de Pontos</h2>
                    <p class="valor">69</p>
                </article>
            </section>
            <section class="graficos">
                <article class="grafico">
                    <h2>Status dos Pontos</h2>
                    <canvas id="grafico-status"></canvas>
                </article>
                <article class="grafico">
                    <h2>Manutenções por Mês</h2>
                    <canvas id="grafico-manutencao"></canvas>
                </article>
            </section>
            <section class="atividades">
                <h2>Últimas Atividades</h2>
                <table>
                    <thead>
                        <tr>
                            <th>Data</th>
                            <th>Usuário</th>
                            <th>Ação</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>13/07/2026</td>
                            <td>Lucas</td>
                            <td>Cadastrou um novo ponto Wi-Fi</td>
                        </tr>
                        <tr>
                            <td>12/07/2026</td>
                            <td>João</td>
                            <td>Atualizou manutenção</td>
                        </tr>
                        <tr>
                            <td>11/07/2026</td>
                            <td>Maria</td>
                            <td>Criou um novo usuário</td>
                        </tr>
                    </tbody>
                </table>
            </section>
        </main>
    </section>
    <footer>
        <p>&copy; 2026 - Gov18 | Monitor PMPP</p>
    </footer>
</body>
</html>