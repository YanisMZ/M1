
def exo1(*arg):
    nums = []
    args = []
    for elem in arg:
        if isinstance(elem, (int, float)):
            nums.append(elem)
        else:
            args.append(elem)
    return nums, args


def exo2(**kargs):
    dic = {}
    for (cle, arg) in kargs.items():
        if type(arg) not in dic:
            dic[type(arg)] = []
        dic[type(arg)].append(cle)
    print(dic)
    return dic


def exo3(*args, **kargs):
    num1, string1 = exo1(*args)
    num2, string2 = exo1(*kargs.values())
    return (num1 + num2, string1 + string2)


def register_attendees(*participants, **details):
    print("Conference :", details["conference_name"])
    print("Date :", details["date"])
    print("Location :", details["location"])

    emails = []
    participants_uniques = []
    sessions = {}

    for nom, email, liste_sessions in participants:
        if email not in emails:
            if len(liste_sessions) > 0:
                emails.append(email)
                participants_uniques.append((nom, email, liste_sessions))
                print(nom, email, liste_sessions)
            else:
                print("Aucune session valide pour", nom)
        else:
            print("Inscription déjà existante :", email)

    if len(participants_uniques) == 0:
        print("Aucune inscription n'a été effectuée.")
        return

    for nom, email, liste_sessions in participants_uniques:
        for session in liste_sessions:
            if session not in sessions:
                sessions[session] = 0
            sessions[session] += 1

    print("Nombre de participants uniques :", len(participants_uniques))
    print("Répartition par session :")

    for session, nombre in sessions.items():
        print(session, ":", nombre)


def main():
    exo1(1, 2, "rtre", 5, 4, "er")

    exo2(kwar="1", kwar2=1, kwar3="a")

    res = exo3(1, 2, 4, "cat", kwar=2)
    print(res)

    register_attendees(
    ("Uma Johnson", " uma.johnson@example.com", ["Opening Ceremony", "Workshop A"]),
    ("Mel Smith", "mel.smith@example.com", ["Keynote", "Panel Discussion"]),
    ("Uma Johnson", " uma.johnson@example.com", ["Workshop B"]),  # Duplicate
    ("Mariana Rodriguez", "mariana.rodriguez@example.com", []),  # Invalid session
    ("Sofia Li", "sofia.li@example.com", ["Workshop C"]),
    ("Luis Gonzalez", "luis.gonzalez@example.com", ["Closing Ceremony"]),
    ("Nora Wilson", " nora.wilson@example.com", ["Closing Ceremony", "Networking Event"]),
    conference_name="Tech Innovators 2024",
    date="May 5, 2024",
    location="Downtown Convention Center"
)


if __name__ == '__main__':
    main()
