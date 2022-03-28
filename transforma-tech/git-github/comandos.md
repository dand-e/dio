# Comandos Git/Github

## comandos gerais
- git config --list >> lista as configurações da conta
- git config --global --unset <o que será alterado> >> remove as configuração escolhida
- git remote -v >> lista os repositorios cadastrados
- git log >> mostra os commits 
- git status >> mostra qual o status do arquivo

- pwd >> mostra o diretorio em que está
- ls OU dir>> mostra todos os arquivos do diretorio
- Clear OU ctrl+l OU Esc >> limpa a tela
- ls -la OU ls -a>> mostra todos os diretorios, incluindo ocultos
- cd <nome> >> entra na pasta <nome>
- cd .. >> volta uma pasta

- git remote add origin <url-do-repositorio.git> >> vincula do repositorio remoto no github

- git add <file-name> >> add file to commit queue
- git add * >> add all files
- git add . >> add all files

- git commit -m "mensagem" >> add o commit ao repositório

- git branch -M main >> Selecionar o branch "main"
- git push -u origin main >> adiciona ao repositorio remoto main//
- git push -u origin master >> Enviar alterações para o repositório remoto: git push -u origin master
- git pull origin master//main >> adiciona ao repositorio local a partir do master//main
- git clone <url-do-repositorio.git> >> clona o reposítório

- mv <nome-do-diretorio-a-ser-movido> <nome-do-diretorio-para-onde-sera-movido>
- git rm --cached desafio_de_projeto-01 >> remove o file
- rm -rf <caminho-do-diretório> >> apaga o diretório

## create a new repository on the command line*
 
** forma 1 **
- echo "# repo-teste" >> README.md >> cria a adição do testo "# repo-teste" no README.md
- git init >> informa que o diretorio faz parte do git
- git add <file-name> >> add file to commit queue
            OU
- git add * >> add all files
            OU
- git add . >> add all files
- git commit -m "mensagem" >> add o commit ao repositório
- git branch -M main >> Selecionar o branch "main"
- git remote add origin <url-do-repositorio.git> >> vincula do repositorio remoto no github
- git push (-u) origin master >> Enviar alterações para o repositório remoto: git push (-u) origin master
            _() significam que item pode ser opcional_

** forma 1.2 **
- nano <nome.extensão> >> cria um arquivo de texto com o <nome>
            OU
- notepad <nome.extensão> >> abre o notepad para a criação do texto
- git init >> informa que o diretorio faz parte do git
- git add <file-name> >> add file to commit queue
            OU
- git add * >> add all files
            OU
- git add . >> add all files
- git commit -m "mensagem" >> add o commit ao repositório
- git branch -M main >> Selecionar o branch "main"
- git remote add origin <url-do-repositorio.git> >> vincula do repositorio remoto no github
- git push (-u) origin master >> Enviar alterações para o repositório remoto: git push (-u) origin master


## push an existing repository from the command line
- git remote add origin https://github.com/dand-e/repo-teste.git
- git branch -M main
- git push -u origin main


