<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../assets/css/relatorios.css">
    <title>Relatórios</title>
</head>
<body>
    <header>
    <h1>Relatórios</h1>
    <p>Visualize e exporte informações do sistema</p>
    </header>
    <main>
        <section class="filtros">
            <h2>Filtros</h2>
            <label for="inicio">Data Inicial</label>
            <input type="date" id="inicio">
            <label for="fim">Data Final</label>
            <input type="date" id="fim">
            <label for="">Tipo</label>
            <select name="" id="">
                <option value="">Todos</option>
                <option value="">Pontos Wi-Fi</option>
                <option value="">Manutenções</option>
                <option value="">Usuários</option>
            </select>    
        </section>
        <section class="botoes">
            <button class="pdf">Gerar PDF</button>
            <button class="excel">Gerar Excel</button>
            <button class="visualizar">Visualizar</button>
        </section>
        <section class="resumo">
            <h2>Resumo</h2>
            <article>
                <h3>Total de Pontos</h3>
                <p>58</p>
            </article>
            <article>
                <h3>Online</h3>
                <p>54</p>
            </article>
            <article>
                <h3>Offline</h3>
                <p>4</p>
            </article>
            <article>
                <h3>Em Manutenção</h3>
                <p>7</p>
            </article>
        </section>
    </main>
    <footer>

    </footer>
</body>
</html>