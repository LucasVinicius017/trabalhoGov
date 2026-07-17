<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../assets/css/usuario.css">
    <title>Usuários</title>
</head>
<body>
    <header>
        <h1>Usuários</h1>
        <section class="acoes">
            <input type="search" placeholder="Pesquisar usuário">
            <button>Novo usuário</button>
        </section>
    </header>
    <main>
        <table>
            <caption>Lista de Usuários</caption>
            <thead>
                <tr>
                    <th>Nome</th>
                    <th>E-mail</th>
                    <th>Perfil</th>
                    <th>Status</th>
                    <th>Ações</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Lucas</td>
                    <td>lucas@gmail.com</td>
                    <td>Admin</td>
                    <td>Ativo</td>
                    <td>
                        <button class="editar">Editar</button>
                        <button class="excluir">Excluir</button>
                    </td>
                </tr>
                <tr>
                    <td>João</td>
                    <td>joao@gmail.com</td>
                    <td>Usuário</td>
                    <td>Ativo</td>
                    <td>
                        <button class="editar">Editar</button>
                        <button class="excluir">Excluir</button>
                    </td>
                </tr>
                <tr>
                    <td>Maria</td>
                    <td>maria@email.com</td>
                    <td>Usuário</td>
                    <td>Inativo</td>
                    <td>
                        <button class="editar">Editar</button>
                        <button class="excluir">Excluir</button>
                    </td>                   
                </tr>
            </tbody>
        </table>
    </main>
    <footer>

    </footer>
    </body>
</html>