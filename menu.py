
from TT1 import fibonacci,list
from TT2 import factorial, factors
from TT3 import animation, matrix, swap, tree
main_menu = []

# Submenu list of [Prompt, Action]
# Works similarly to main_menu
week0_sub_menu = [
    ["Animation", animation.driver],
    ["Tree", tree.driver],
    ["Matrix", matrix.driver],
    ["Swap", swap.driver],
]

week1_sub_menu = [
    ["Fibonacci", fibonacci.driver],
    ["Lists", list.driver],
]

week2_sub_menu = [
    ["Factorials", factorial.driver],
    ["Factors", factors.driver],



]

border = "=" * 25
banner = f"\n{border}\nplease pick one\n{border}"


def menu():
    title = "function menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["TT0",TT0])
    menu_list.append(["TT1", TT1])
    menu_list.append(["TT2", TT2])
    buildMenu(title, menu_list)


def TT0():
    title = "function submenu" + banner
    buildMenu(title, week0_sub_menu)

def TT1():
    title = "Function Submenu" + banner
    buildMenu(title, week1_sub_menu)

def TT2():
    title = "Function Submenu" + banner
    buildMenu(title, week2_sub_menu)

def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("input:")

    try:
        choice = int(choice)



        if choice == 0:
            # stop
            print("you have left the program! thank you!")
            exit()
            return

        try:
            action = prompts.get(choice)[1]

            action()


        except TypeError:
            try:

                exec(open(action).read())


            except FileNotFoundError:
                print(f"File not found!: {action}")

    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)
if __name__ == "__main__":
    menu()
