from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('ChatBot')

def bot_trainning():
    print('[Training started]')
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
    print('[Training completed]')

def bot_answer(query: str):
    answer = bot.get_response(query)
    return f"🤖 {answer}"


if __name__ == '__main__':
    bot_trainning()
    exit_conditions = (":q", "quit", "exit")
    while True:
        query = input(">>> ")
        if query in exit_conditions:
            break
        else:
            print(bot_answer(query))