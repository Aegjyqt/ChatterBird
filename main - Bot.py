from aiogram import Bot, Dispatcher, types, executor

import input

bot = Bot('5425262237:AAGOWteGA7ZHY4QprD0_SHYm9lzrtfld7is')
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start'])
async def greetings(message: types.Message):
    await message.answer('Привет! Я - Chatterbird, отличаюсь умом и сообразительностью. '
                         'Если введете комманду /about, можете '
                         'немного про меня почитать. А можем сразу начать работу, просто введите термин:')

@dp.message_handler(commands = ['about'])
async def about(message: types.Message):
    await message.answer('Я рожден из БОЛИ, причиненной Переводчиком ИСУ... Погодите, что-то слишком откровенно. '
                         'И совершенно не соответствует моей доброй природе.\n\n'
                         'Хм... \n\n'
                         'Я задуман как альтернатива поиску по Переводчику ИСУ, который:\n\n'
                         '1. чувствителен к регистру\n'
                         '2. не может искать сразу по всем категориям\n'
                         '3. не выдает перевод сразу же, а требует лишних кликов\n\n'
                         '(или мой автор совсем дурак и не понимает, как им пользоваться. '
                         'Если так - пожалуйста, скажите ему)\n\n'
                         'А еще я пытаюсь работать со склонениями, но пока это не всегда получается - мне нужен корм! '
                         'Например, доступ к данным Переводчика.\n\n'
                         'Давайте начнем?')

@dp.message_handler()
async def commence(message: types.Message):
    string = message.text
    temp = input.Input(string)
    output = temp.translate()
    if output == 'Простите, я только учусь! Но на всякий случай, попробуем ввести в именительном падеже?':
        await message.answer('Не знаю!')
    else:
        await message.answer('Знаю!')
    await message.answer(output)

executor.start_polling(dp)
