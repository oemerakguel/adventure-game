from game_utils import solve_riddle, end_game

def greeting():
    print("Willkommen zu die verlorene Schatzsuche!")
    print("Ziel des Spiels ist es den Schatz zu finden indem du die Rätsel löst.")
    print("Du kannst durch Eingabe von Befehlen wie 'norden', 'süden', 'osten', 'westen' navigieren.\n")

def enter_room(room):
    print(room['description'])

def main():
    rooms = {
        'raum1': {
            'name': 'Raum1',
            'description': 'Du betrittst den ersten Raum',
            'riddle': {'question': 'Welche Farbe erhälst du wenn du Gelb und Blau mischst?', 'answer': 'Grün'},
            'norden': 'raum2',
            'osten': 'schatz'
        },
        'raum2': {
            'name': 'Raum2',
            'description': 'Du betrittst den zweiten Raum',
            'riddle': {'question': 'Was ist das Ergebnis von 11 mal 11?', 'answer': '121'},
            'süden': 'raum1'
        },
        'schatz': {
            'name': 'Schatzkammer',
            'description': 'Du hast den verlorenen Schatz gefunden!',
            'riddle': {'question': 'Wie kann man 1 Liter Wasser in einem Sieb transponieren?', 'answer': 'gefroren'},
            'norden': None,
            'osten': None,
            'süden': None,
            'westen': 'raum1'
        }
    }

    current_room = 'raum1'
    solved_riddles = set()

    while True:
        room = rooms[current_room]
        enter_room(room)


        if current_room not in solved_riddles:
            solved = False
            while not solved:
                solved = solve_riddle(room['riddle'])
            solved_riddles.add(current_room)

        if current_room == 'schatz':
            end_game()
            exit()

        move = input("Wohin möchtest du gehen? (norden, süden, osten, westen): ").strip().lower()

        if move in ['norden', 'süden', 'osten', 'westen']:
            direction = {
                'norden': 'norden',
                'süden': 'süden',
                'osten': 'osten',
                'westen': 'westen'
            }

            if direction[move] in room and room[direction[move]] is not None:
                current_room = room[direction[move]]
            else:
                print("Falsche Richtung! Versuch es nochmal!")
        else:
            print("Ungültige Eingabe. Gib norden, süden, osten oder westen ein.")

if __name__ == "__main__":
    greeting()
    main()
