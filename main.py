from game_events import intro, event1, event2, final_event, event_else_check_1, event_else_check_2, event_else_check_3, gameover_event1, gameover_event2, gameover_event3, gameover_event4, retry, final_retry


def main():
    while True:
        intro()

        choice = input(
            "Where do you want to go? 'Left' or 'Right'\n").lower()

        if choice == "right":
            gameover_event1()

            retry_choice = retry()

            if retry_choice == "Y":
                continue
            else:
                break

        elif choice == "left":
            event1()

            choice = input("What do you want to do?\n").lower()

            if choice == "run":
                gameover_event2()

                retry_choice = retry()

                if retry_choice == "Y":
                    continue
                else:
                    break

            elif choice == "sneak":
                event2()

                choice = input("Which door do you chose?\n").lower()

                if choice == "green":
                    gameover_event3()

                    retry_choice = retry()

                    if retry_choice == "Y":
                        continue
                    else:
                        break

                elif choice == "blue":
                    gameover_event4()

                    retry_choice = retry()

                    if retry_choice == "Y":
                        continue
                    else:
                        break

                elif choice == "red":
                    final_event()

                    retry_choice = final_retry()

                    if retry_choice == "Y":
                        continue
                    else:
                        break

                else:
                    event_else_check_1()

                    retry_choice = retry()

                    if retry_choice == "Y":
                        continue
                    elif retry_choice == "N":
                        break
                    else:
                        event_else_check_2()
                        retry_choice = retry()

                        if retry_choice == "Y":
                            continue
                        elif retry_choice == "N":
                            break
                        else:
                            event_else_check_3()
                            break

            else:
                event_else_check_1()

                retry_choice = retry()

                if retry_choice == "Y":
                    continue
                elif retry_choice == "N":
                    break
                else:
                    event_else_check_2()
                    retry_choice = retry()

                    if retry_choice == "Y":
                        continue
                    elif retry_choice == "N":
                        break
                    else:
                        event_else_check_3()
                        break

        else:
            event_else_check_1()

            retry_choice = retry()

            if retry_choice == "Y":
                continue
            elif retry_choice == "N":
                break
            else:
                event_else_check_2()
                retry_choice = retry()

                if retry_choice == "Y":
                    continue
                elif retry_choice == "N":
                    break
                else:
                    event_else_check_3()
                    break


main()
