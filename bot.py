from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatBot')

def bot_trainning():
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

def bot_answer(query: str):
    answer = bot.get_response(query)
    return f"🤖 {answer}"

# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     answer = bot.get_response(query)
#     if query in exit_conditions:
#         break
#     #elif float(answer.confidence) > 0.5:
#     else:
#         print(f"🤖 {answer}")
#     # else:
#     #     print("🤖 Ainda não sei como responder isso.")