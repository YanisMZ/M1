#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 22:42:27 2026

@author: yanis
"""
import re

import pandas as pd

def exercice1():
    
    
    tweets = [
    "I posted this 27 minutes ago and it's already trending!",
    "This happened 4 hours ago, can't believe it.",
    "What a day! 23rd june 2018 was unforgettable.",
    "Join us at the event on 1st september 2019 5:25 pm. It promises to be an insightful",
    ]
    
    MONTHS = (r"(?:january|february|march|april|may|june|july|august|"
             r"september|october|november|december)")

    #pour recuperer 27 minutes ago
    relative_time = re.compile(
       r"\b\d+\s+(?:second|minute|hour|day|week|month|year)s?\s+ago\b")

   #pour recuper 
    standard_date = re.compile(
       r"\b\d{1,2}(?:st|nd|rd|th)\s+" + MONTHS + r"\s+\d{4}\b")

  
    date_and_time = re.compile(
       r"\b\d{1,2}(?:st|nd|rd|th)\s+" + MONTHS + r"\s+\d{4}"
       r"\s+\d{1,2}:\d{2}\s*(?:am|pm)\b")

    for tweet in tweets:
       
       dt = date_and_time.findall(tweet)
       if dt:
           print("Date and Time:", dt)
           continue

       sd = standard_date.findall(tweet)
       if sd:
           print("Standard Date:", sd)
           continue

       rt = relative_time.findall(tweet)
       if rt:
           print("Relative Time:", rt)
           
           
def exercice2():
    
    
    
    clients = [
    "C801V", "C952S", "C503B", "C428F", "C851G", "C325H", "C542P", "C734M", "C987L", "C612K",
    "C443D", "C227J", "C745X", "C388T", "C159Y", "C629N", "C812R", "C473Q", "C293Z", "C911P"
    ]
    ratings = [
    4, 5, 3, 4, 3, 2, 3, 1, 5, 4, 2, 5, 3, 4, 1, 2, 4, 3, 5, 1
    ]
    categories = [
    "Electronics", "Home", "Electronics", "Home", "Sports", "Electronics", "Sports", "Home", "Electronics",
    "Sports", "Home", "Electronics", "Sports", "Home", "Sports", "Electronics", "Home", "Electronics",
    "Electronics", "Sports"
    ]
    
    # on recuper les categories et les notes dans un dictionnaire
    notes_par_categorie = {}
    for categorie, note in zip(categories, ratings):
        if categorie not in notes_par_categorie:
            notes_par_categorie[categorie] = []
        notes_par_categorie[categorie].append(note)
        
        
        
    print("Dictionnaire des notes par catégorie :")
    print(notes_par_categorie)
    print("\n")

    #affichage
    print(f"{'Category':<10}  {'Average Rating':<10}  {'Total Satisfied':<10}  {'Total Clients'}")

    for categorie, notes in notes_par_categorie.items():
        total_clients = len(notes)                          #  nb de clients
        moyenne = round(sum(notes) / total_clients, 2)      #  moyenne 
        satisfaits = sum(1 for n in notes if n >= 4)        #  satisfaits

        print(f"{categorie:<12} {moyenne:<17} {satisfaits:<17} {total_clients}")
    
    
    
    
def exercice3():
    matches = [
    {"team": "Lions", "opponent": "Tigers", "team_score": 3, "opponent_score": 1},
    {"team": "Lions", "opponent": "Bears", "team_score": 2, "opponent_score": 4},
    {"team": "Tigers", "opponent": "Bears", "team_score": 3, "opponent_score": 3},
    {"team": "Bears", "opponent": "Lions", "team_score": 5, "opponent_score": 3},
    {"team": "Tigers", "opponent": "Lions", "team_score": 2, "opponent_score": 1},
    {"team": "Bears", "opponent": "Tigers", "team_score": 3, "opponent_score": 2},
    {"team": "Sharks", "opponent": "Lions", "team_score": 4, "opponent_score": 2},
    {"team": "Sharks", "opponent": "Tigers", "team_score": 1, "opponent_score": 3},
    {"team": "Sharks", "opponent": "Bears", "team_score": 2, "opponent_score": 2},
    {"team": "Lions", "opponent": "Sharks", "team_score": 3, "opponent_score": 3},
    {"team": "Tigers", "opponent": "Sharks", "team_score": 2, "opponent_score": 1},
    {"team": "Bears", "opponent": "Sharks", "team_score": 4, "opponent_score": 3},
    {"team": "Owls", "opponent": "Lions", "team_score": 2, "opponent_score": 1},
    {"team": "Owls", "opponent": "Tigers", "team_score": 3, "opponent_score": 3},
    {"team": "Owls", "opponent": "Bears", "team_score": 1, "opponent_score": 4},
    {"team": "Lions", "opponent": "Owls", "team_score": 2, "opponent_score": 2},
    {"team": "Tigers", "opponent": "Owls", "team_score": 4, "opponent_score": 1},
    {"team": "Bears", "opponent": "Owls", "team_score": 3, "opponent_score": 2},
    {"team": "Owls", "opponent": "Sharks", "team_score": 0, "opponent_score": 0},
    {"team": "Sharks", "opponent": "Owls", "team_score": 0, "opponent_score": 0},
]

    # equipe
    teams = set()
    for m in matches:
        teams.add(m["team"])
        teams.add(m["opponent"])
    
    # 2
    stats = {
        t: {"wins": 0, "losses": 0, "draws": 0, "points": 0,
            "goals_for": 0, "goals_against": 0}
        for t in teams
    }
    
    for m in matches:
        a, b = m["team"], m["opponent"]
        sa, sb = m["team_score"], m["opponent_score"]
    
        stats[a]["goals_for"] += sa
        stats[a]["goals_against"] += sb
        stats[b]["goals_for"] += sb
        stats[b]["goals_against"] += sa
    
        if sa > sb:
            stats[a]["wins"] += 1
            stats[a]["points"] += 3
            stats[b]["losses"] += 1
        elif sa < sb:
            stats[b]["wins"] += 1
            stats[b]["points"] += 3
            stats[a]["losses"] += 1
        else:
            stats[a]["draws"] += 1
            stats[b]["draws"] += 1
            stats[a]["points"] += 1
            stats[b]["points"] += 1
    
    for s in stats.values():
        s["diff"] = s["goals_for"] - s["goals_against"]
    

    ranking = sorted(stats.items(), key=lambda item: (item[1]["points"], item[1]["wins"],
                          item[1]["draws"], item[1]["diff"]))
    
    print("Team Rankings:")
    print(f"{'Rank':<10}  {'Team':<10}  {'Points':>10}  {'Wins':>10}  {'Losses':>10}  {'Draws':>10}  {'+/-Goals':>10}")
    for rank, (team, s) in enumerate(ranking, start=1):
        print(f"{rank:<10} {team:<10} {s['points']:>10} {s['wins']:>10}"
              f"{s['losses']:>10} {s['draws']:>7}  {s['diff']:>10}")
    
  
    max_goals = max(s["goals_for"] for s in stats.values())
    
    
    best_attack = sorted(t for t, s in stats.items() if s["goals_for"] == max_goals)
    
    min_conceded = min(s["goals_against"] for s in stats.values())
    best_defense = sorted(t for t, s in stats.items() if s["goals_against"] == min_conceded)
    
    print()
    print(f"Best attac: {', '.join(best_attack)} with {max_goals} goal scored")
    print(f"Bestdefense : {', '.join(best_defense)} with {min_conceded} goalsconceded")
        
        
     
            
          
        
        
        
        

def main():
    
    exercice1()
    print()
    exercice2()
    print()
    exercice3()

    
    




if __name__ == "__main__":
    main()

