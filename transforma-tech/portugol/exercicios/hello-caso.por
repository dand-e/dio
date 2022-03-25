#Hello World
## Usando caso

programa {
    inclua biblioteca Util
    funcao inicio() {
        inteiro opcao
        
        escreva("Bem-vindes\n", "Agora escolha o idioma da clássica frase de tode programadore: \n")
        Util.aguarde(5000)
        limpa()
        escreva("1-Inglês, 2-Português, 3-Espanhol, 4-Francês, 5-Alemão, 6-Polonês\n")
        leia(opcao)
        escolha(opcao){
            caso 1:
                escreva("Hello world!")
                pare
            caso 2:
                escreva("Olá mundo!")
                pare
            caso 3:
                escreva("¡Hola Mundo!")
                pare
            caso 4:
                escreva("Bonjour le monde!")
                pare
            caso 5:
                escreva("Hallo weld!")
                pare
            caso 6:
                escreva("Witaj świecie!")
                pare
            caso contrario:
                escreva("Idioma não encontrado em nossa base\n","Tente novamente mais tarde")
        }
    }
}
