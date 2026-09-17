import random
import time

answers = [
    "Zweifellos",
    "Ich denke, ja",
    "Es ist vorherbestimmt",
    "Höchstwahrscheinlich",
    "Keine Zweifel",
    "Gute Aussichten",
    "Du kannst sicher sein",
    "Ja",
    "Noch unklar, versuch es erneut",
    "Frag später",
    "Lieber nicht erzählen",
    "Konzentriere dich und frag noch mal",
    "Denk nicht mal dran",
    "Meine Antwort ist Nein",
    "Nach meinen Daten - Nein",
    "Sehr zweifelhaft"
]

greetings = [
    "Hallo Welt, ich bin eine magische Kugel und ich kenne die Antwort auf jede deiner Fragen.",
    "Tritt näher, Sterblicher... Ich bin die magische Kugel und sehe deine Zukunft.",
    "Willkommen! Die kosmischen Energien sind bereit. Ich kann dir jede Frage beantworten.",
    "Hallo! Du hast die magische Kugel geweckt. Frag mich, was immer du wissen willst."
]

name_prompts = [
    "Wie heißt du? ",
    "Wie ist dein Name? ",
    "Wer sucht nach Antworten? ",
    "Verrate mir deinen Namen... "
]

welcome_phrases = [
    "Hallo",
    "Guten Tag",
    "Willkommen",
    "Grüß dich"
]

question_prompts = [
    "Was möchtest du wissen? ",
    "Frag mich etwas... ",
    "Welches Geheimnis soll ich lüften? ",
    "Was bedrückt dein Herz? ",
    "Deine Frage an das Schicksal: "
]

continue_prompts = [
    "Möchtest du noch eine Frage stellen? ",
    "Hast du noch eine Frage an das Schicksal? ",
    "Soll ich dir noch ein Geheimnis verraten? ",
    "Brauchst du noch eine Antwort? "
]

farewells = [
    "Die Verbindung bricht ab... Möge das Schicksal dich leiten. ✨",
    "Die Magie verblasst. Gehe in Frieden, bis sich unsere Wege wieder kreuzen. 🔮",
    "Der Vorhang schließt sich. Deine Zukunft bleibt vorerst ein Geheimnis... 🌌",
    "Die Geister schweigen nun. Gehe, aber vergiss meine Warnungen nicht! 👁️"
]

def is_valid_answer(text):
    #Prüft, ob die Frage richtig beantwortet wurde.
    return text.strip().lower() in ["nein", "ja"]

def play_magic_8_ball():
    print(random.choice(greetings))
    name = input(random.choice(name_prompts))
    print(f"{random.choice(welcome_phrases)} {name}!")

    while True:
        input(random.choice(question_prompts))
        print("\n🔮 *Schütteln* ...")
        time.sleep(1)
        print(random.choice(answers))

        while True:
            next_step = input(random.choice(continue_prompts)).strip().lower()

            if not is_valid_answer(next_step):
                print("Ich habe dich nicht verstanden. Bitte gib deine Antwort noch einmal ein. (ja/nein)")
                continue
            break

        if next_step == 'nein':
            print(random.choice(farewells))
            break

if __name__ == '__main__':
    play_magic_8_ball()




