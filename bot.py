from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatBot')

conversa = ['Oi',
            'Olá',
            'Tudo bem?',
            'Tudo ótimo',
            'Você gosta de programar?',
            'Sim, eu programo em Python',
            'Que tipos de programas você gosta de criar?',
            'Eu gosto de criar programas que ajudem as pessoas em suas tarefas diárias.',
            'Foi ótimo conversar com você.',
            'Foi ótimo conversar com você também. Tenha um ótimo dia!']

trainer = ListTrainer(bot)
trainer.train(conversa)

# while True:
#     pergunta = input("Usuário: ")
#     resposta = bot.get_response(pergunta)
#     if float(resposta.confidence) > 0.5:
#         print('TW Bot: ', resposta)
#     else:
#         print('TW Bot: Ainda não sei responder esta pergunta')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"🤖 {bot.get_response(query)}")