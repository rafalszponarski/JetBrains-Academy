#!/usr/bin/env bash

filename=definitions.txt
reNum="^-?(0|[1-9][0-9]*)(\.[0-9]+)?$"

show_menu() {
  echo """
Select an option
0. Type '0' or 'quit' to end program
1. Convert units
2. Add a definition
3. Delete a definition"""
}

ask_line_number() {
  local nLines=$(wc -l < "$filename")
  if [[ ! -f "$filename" || $nLines = 0 ]]; then
    echo "Please add a definition first!" && return 1
  else
    echo "Type the line number to $2 or '0' to return"
    print_with_line_numbers "$filename"
    while true; do
      read -r "$1"
      [[ ${!1} = 0 ]] && return 1
      [[ "${!1}" =~ ^[0-9]+$ && ${!1} -ge 1 && ${!1} -le $nLines ]] && return 0
      echo "Enter a valid line number!"
    done
  fi
}

convert() {
  local line_number def ratio val
  if ask_line_number line_number "convert units"; then
    read -r def ratio <<< $(sed "$line_number!d" "$filename")
    enter_value val
    printf "Result: %s" $(bc -l <<< "scale=2; $ratio * $val")
  fi
}

enter_value() {
  echo "Enter a value to convert:"
  while true; do
    read -r "$1" && [[ "${!1}" =~ $reNum ]] && break
    echo "Enter a float or integer value!"
  done
}

add_def() {
  local reDef="^[a-z]+_to_[a-z]+$"
  local def ratio
  while true; do
    echo "Enter a definition:" && read -r def ratio
    if [[ "$def" =~ $reDef && "$ratio" =~ $reNum ]]; then
      echo "$def $ratio" >> $filename; break
    else
      echo "The definition is incorrect!"
    fi
  done
}

print_with_line_numbers() {
  local n
  while read -r line; do
    echo "$(( n += 1 )). $line"
  done < "$1"
}

del_def() {
  local line_number
  ask_line_number line_number "delete" && sed -i "${line_number}d" "$filename"
}

echo "Welcome to the Simple converter!"
while true; do
  show_menu && read -r option
  case $option in
    "0" | "quit" ) echo "Goodbye!"; break;;
    "1" ) convert;;
    "2" ) add_def;;
    "3" ) del_def;;
     *  ) echo "Invalid option!"
  esac
done

# I wrote very similar code, so to avoid being accused of plagiarism I put the author's code here which I used to improve my code
# However, I made corrections:
# - rewrite RegExp rule
# - read without -r will mangle backslashes
# - removed unnecessary variable in function
# This solution belongs to Oleksandr Butrym, His profile is available here: https://hyperskill.org/profile/6050949