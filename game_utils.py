def solve_riddle(riddle):
    print(f"Rätsel: {riddle['question']}")
    answer = input("Deine Antwort: ").strip().lower()
    if answer == riddle['answer'].strip().lower():
        print("Das ist korrekt!")
        return True
    else:
        print("Leider falsch. Versuch es nochmal!")
        return False
    
def end_game():
    print("Glückwunsch! Du hast den Schatz gefunden ")