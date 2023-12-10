from chess import Chess
import speech_recognition as sr

def get_input(prompt, is_voice):
    while True:
        if is_voice:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print(f'{prompt}: (Speak now)')
                try:
                    audio = r.listen(source, timeout=4, phrase_time_limit=4)
                    input_text = r.recognize_google(audio)
                    print(f'Recognized: {input_text}')
                    return input_text
                except sr.UnknownValueError:
                    print('Sorry, could not recognize your voice.')
                except sr.WaitTimeoutError:
                    print('Timeout. Please try again.')
        else:
            return input(f'{prompt}: ')

def get_input_method():
    while True:
        choice = input("Choose input method (voice/text): ").lower()
        if choice in ['voice', 'text']:
            return choice == 'voice'
        else:
            print("Invalid choice. Please enter 'voice' or 'text'.")

chess_game = Chess()
r = sr.Recognizer()

is_voice_input = get_input_method()

while True:
    chess_game.display()
    if chess_game.p_move == 1:
        print('\nWhites Turn (UPPER)\n')
    else:
        print('\nBlacks Turn (LOWER CASE)\n')

    cur_pos = get_input('What piece do you want to move?', is_voice_input)
    next_pos = get_input('Where do you want to move the piece to?', is_voice_input)

    if cur_pos is None or next_pos is None:
        continue  # If voice input failed or timed out, try again

    valid = False
    if chess_game.move(cur_pos, next_pos) == False:
        print('Invalid move')
    else:
        valid = True

    state = chess_game.is_end()
    if state == [0, 0, 0]:
        if chess_game.check_state(chess_game.EPD_hash()) == 'PP':
            print(chess_game.pawn_promotion())
    if sum(state) > 0:
        print('\n--------------------\n   GAME OVER\n----------------------\n')
        chess_game.display()
        print('\nGame Result:\n------------\n')
        if state == [0, 0, 1]:
            print('BLACK WINS')
        elif state == [1, 0, 0]:
            print('WHITE WINS')
        else:
            print('DRAW')
        break

    if valid:
        chess_game.p_move = chess_game.p_move * (-1)
