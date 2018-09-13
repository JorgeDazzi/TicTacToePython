#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Msgs:


    WARMING = {
        "playerSetWrong": {
            'EN': "Please, follow the rules!",
            'PT-BR': "Por favor, siga as regras!"
        },

        "wrongMove": {
            'EN': u"%s \u2190 this move command is not allowed!",
            'PT-BR': u"%s \u2190 Esse comando é ínvalido!"

        },

        "coordUsed": {
            'EN': u"%s \u2190 This coordinate has already been used",
            'PT-BR': u"%s \u2190 Essa coordenada já foi usada"
        }
    }

    ERROR = {
        "inputTypeIsWrong": {
            'EN' : "Make sure that you are using the right TYPE for this setting, anyway Default value will be used!",
            'PT-BR' : "Verifique o tipo usado na configuração, de qualquer forma a configuração será usada!"
        },

        "playerValue": {
            'EN': "Only 1 character is accepted and can not be empty",
            'PT-BR': "Apenas 1 caractere é aceito e não pode ser vazio"
        }
    }

    UI = {

        "welcome": {
            'EN': u"\u2716 \u25CF \u25BC Welcome to Tic Tac Toe 2.0  \u25BC \u25CF \u2716\n:....... Good lunk and Have Fun ......:\n\n",
            'PT-BR': u"\u2716 \u25CF \u25BC Bem vindo ao Tic Tac Toe 2.0  \u25BC \u25CF \u2716\n:....... Boa sorte e divirta-se  ......:\n\n"
        },

        "playerSizeChars": {
            'EN': "Min 2 characters",
            'PT-BR': "Min 2 caracteres"
        },

        "playerName": {
            'EN': "What is player name?",
            'PT-BR': "Qual é o nome do jogador?"
        },

        "playerSet": {
            'EN': "Player %s has been set",
            'PT-BR': "O nome do jogador %s foi definido"
        },

        "winnerAnnounce": {
            'EN': u"\n\n\uD83C\uDF81 \u01C3 %s - Player %s wins \u01C3 \uD83C\uDF81 \n\nThank you :)",
            'PT-BR': u"\n\n\uD83C\uDF81 \u01C3 %s - Jogador %s ganhou \u01C3 \uD83C\uDF81 \n\nObrigado :)"
        },

        "moveInstruction": {
            'EN': "(Move instruction: <Row,Column> (Nº between 0 and %s) ... ex 0,1)",
            'PT-BR': "(Instruções: <Linha,Coluna> (Nº entre 0 e %s) ... ex 0,1)"
        },

        "move": {
            'EN': "%s - Player Nº %s :: this is your turn, please make your move...",
            'PT-BR': "%s - Jogador Nº %s :: Esse é seu turno, faça sua jogada..."
        },

        "drawGame": {
            'EN': "There are no winners, the game ended in a draw. :/",
            'PT-BR': "Não há ganhador, o Jogo terminou empatado :/"
        },

        "announceTheWinner": {
            'EN': u"\n\n\U0001F389 \U0001F389 %s - Player %s wins \U0001F389 \U0001F389 \n\nObrigado :)",
            'PT-BR': u"\n\n\U0001F389 \U0001F389 %s - Jogador %s ganhou a partida \U0001F389 \U0001F389 \n\nObrigado :)"
        },



    }