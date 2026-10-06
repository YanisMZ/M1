import math
import pandas as pd



wlist = [
    ['Python', 'creativity', 'universel'],
    ['linterview', 'study', 'job', 'university', 'lecture'],
    ['task', 'objective', 'aim', 'subject', 'programming', 'test', 'research']
]


def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def exo1():

    lengths = [len(words) for words in wlist]

    words = [longest_word(words) for words in wlist]

    result = zip(wlist, lengths, words)

    for element in result:
        print(element)




def exo2():

    result = [
        (len(words), longest_word(words))
        for words in wlist
    ]

    print("Liste de tuples :")
    print(result)

    lengths, words = zip(*result)

    print("lengths :", lengths)
    print("words :", words)



def exo3():

   
    word_lengths = [
        (word, len(word))
        for words in wlist
        for word in words
    ]


    words, lengths = zip(*word_lengths)

  
    data = {
        'words': words,
        'lengths': lengths
    }


    df = pd.DataFrame(data)

    print("DataFrame de l'exercice 3 :")
    print(df)

    return df




def exo4():

    temperature = [22, 27, 21, 30, 25, 23, 29, 24, 28, 26]
    humidity = [45, 50, 55, None, 60, 52, None, 48, 54, 57]
    pressure = [1012, 998, 1005, 1008, 995, 1003, 999, 1006, 1001, 1009]

    result = []

    for temp, hum, press in zip(temperature, humidity, pressure):

      
        if temp is None or hum is None or press is None:
            continue


        if temp > 25:
            alert = "surchauffe"
        elif press < 1000:
            alert = "basse"
        else:
            alert = "aucune"

        result.append({
            'temperature': temp,
            'humidity': hum,
            'pressure': press,
            'alert': alert
        })

    print("Résultat de l'exercice 4 :")
    print(result)

    return result



def exo5():

    employee_name = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

    hours_worked = [
        [40, 38, 45],
        [50, 55, 60],
        [30, 25, 20],
        [60, 58, 55],
        [45, 50, 55]
    ]

    performance_scores = [
        [80, 85, 90],
        [60, 70, 75],
        [50, 40, 30],
        [90, 95, 92],
        [70, 75, 80]
    ]

    result = []

    for name, hours, scores in zip(
        employee_name,
        hours_worked,
        performance_scores
    ):


        average_score = sum(scores) / len(scores)


        if average_score > 75:
            appreciation = "satisfaisant"
        else:
            appreciation = "insatisfaisant"


        total_hours = sum(hours)


        result.append({
            'employee_name': name,
            'average_score': average_score,
            'appreciation': appreciation,
            'total_hours': total_hours
        })

    print("Résultat de l'exercice 5 :")
    print(result)

    return result




def main():

    exo1()

    print()

    exo2()

    print()

    exo3()

    print()

    exo4()

    print()

    exo5()


if __name__ == '__main__':
    main()
