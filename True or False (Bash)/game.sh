#!/usr/bin/env bash

printf "Welcome to the True or False Game!\n"

login=$(curl -s http://0.0.0.0:8000/download/file.txt)
username=$(echo "$login" | awk -F'[:"]' '{print $5}')
password=$(echo "$login" | awk -F'[:"]' '{print $10}')
curl http://0.0.0.0:8000/login -u "$username:$password" -sc cookie.txt &> /dev/null

responses=("Perfect!" "Awesome!" "You are a genius!" "Wow!" "Wonderful!")

game() {
    task=$(curl http://0.0.0.0:8000/game -b cookie.txt)
    question=$(echo "$task" | awk -F'[:"]' '{print $5}') && printf '%s\n' "$question"
    answer=$(echo "$task" | awk -F'[:"]' '{print $10}') && printf 'True or False?\n'
    read -r user
}

while true; do
    printf "\n0. Exit"
    printf "\n1. Play a game"
    printf "\n2. Display scores"
    printf "\n3. Reset scores"
    printf "\nEnter an option:"
    read -r option

    case $option in
        0 | 'quit')
            printf "See you later!\n"
            break;;
        1)
            printf "What is your name?\n" && read -r player && correct=0
            game

            while [ "$answer" = "$user" ];
            do
                printf '%s\n' "${responses[$((RANDOM % 5))]}" && ((correct+=1))
                game

            done

            printf 'Wrong answer, sorry!\n'
            printf '%s you have %s correct answer(s).\n' "$player" "$correct"
            printf 'Your score is %s points.\n' "$((correct*10))"
            printf 'User: %s, Score: %s, Date: %s\n' "$player" "$((correct*10))" "$(date +'%Y-%m-%d')" >> scores.txt;;

        2)
            if [ -e scores.txt ]; then
              printf 'Player scores\n' && cat scores.txt
            else
              printf "File not found or no scores in it!\n"
            fi;;

        3)
            if [ -e scores.txt ]; then
                rm scores.txt
                printf "File deleted successfully!\n"
            else
                printf "File not found or no scores in it!\n"
            fi;;

        *)
            printf "Invalid option!";;
    esac
done
