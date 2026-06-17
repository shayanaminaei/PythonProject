# Rock Paper Scissors Game

import random

choices = {
    "1": "rock",
    "2": "paper",
    "3": "scissors"
}

user_choice = input(
    "Please enter your choice by number_input {1) Rock 2) Paper 3) Scissors}: "
)

if user_choice not in choices:
    print("Invalid choice! Please enter 1, 2 or 3.")

else:
    computer_choice = random.choice(list(choices.values()))
    user_pick = choices[user_choice]


    # User chooses Rock
    if user_pick == "rock":

        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)


        if computer_choice == "rock":

            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

            print("Both players chose rock, try again...")


        elif computer_choice == "paper":

            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)

            print(
                f"You lose😭, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )


        elif computer_choice == "scissors":

            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

            print(
                f"You win😎, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )



    # User chooses Paper
    elif user_pick == "paper":

        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)


        if computer_choice == "rock":

            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

            print(
                f"You win😎, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )


        elif computer_choice == "paper":

            print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
            ---.__________)
            """)

            print("Both players chose paper, try again...")


        elif computer_choice == "scissors":

            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)

            print(
                f"You lose😭, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )



    # User chooses Scissors
    elif user_pick == "scissors":

        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)


        if computer_choice == "rock":

            print("""
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

            print(
                f"You lose😭, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )


        elif computer_choice == "paper":

            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)

            print(
                f"You win😎, you choose {user_pick} "
                f"and computer choose {computer_choice}."
            )


        elif computer_choice == "scissors":

            print("""
            _______
        ---'   ____)____
              _______)
             _______)
             _______)
        ---.__________)
            """)

            print("Both players chose scissors, try again...")