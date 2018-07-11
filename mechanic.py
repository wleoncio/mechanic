# Dictionaries of problems and solutions
problems = {1:'instability',
            2:'long stopping distance',
            3:'low grip on curves',
            4:'low speed on straights',
            5:'general oversteer',
            5.1:'turn-in oversteer',
            5.2:'mid-corner oversteer',
            5.3:'corner exit oversteer',
            6:'general understeer',
            6.1:'turn-in understeer',
            6.2:'mid-corner understeer',
            6.3:'corner exit understeer',
            7:'poor turning response',
            8:'tyres lock up',
            9:'too much tyre wear',
            10:'traction loss'}
solutions = {'instability':['Stiffen suspension', 'Stiffen anti-roll',
                            'Reduce front toe out', 'Increase rear toe in',
                            'Increase front break bias'],
             'long stopping distance':['Increase break pressure'],
             'low grip on curves':['Increase wing', 'Reduce ride height',
                                   'Add negative camber'],
             'low speed on straights':['Decrease wing', 'Reduce ride height',
                                       'Increase tyre pressure'],
             'general oversteer':['Move ballast to the front',
                                  'Increase front break bias',
                                  'Increase front ride height',
                                  'Reduce rear ride height'],
             'turn-in oversteer':['Stiffen front anti-roll bar',
                                  'Stiffen the front springs',
                                  'Increase front damping'],
             'mid-corner oversteer':['Reduce rear ride height',
                                     'Increase rear camber'],
             'corner exit oversteer':['Soften the rear springs',
                                      'Decrease rear damping'],
             'general understeer':['Move ballast to the rear',
                                   'Reduce front toe out',
                                   'Decrease front break bias',
                                   'Decrease front ride height',
                                   'Increase rear ride height'],
             'turn-in understeer':['Soften front anti-roll bar',
                                   'Soften the front springs',
                                   'Decrease front damping'],
             'mid-corner understeer':['Lower front ride height',
                                      'Lift the throttle a bit'],
             'corner exit understeer':['Stiffen the rear springs',
                                       'Increase rear damping'],
             'poor turning response':['Stiffen anti-roll',
                                      'Increase front toe out',
                                      'Reduce rear toe in',
                                      'Increase tyre pressure',
                                      'Decrease front break bias',
                                      'Move ballast to the rear'],
             'tyres lock up':['Reduce break pressure'],
             'too much tyre wear':['Unlock differential', 'Soften suspension',
                                   'Soften anti-roll', 'Decrease tyre pressure',
                                   'Remove negative camber'],
             'traction loss':['Unlock differential', 'Decrease tyre pressure',
                              'Remove negative camber', 'Soften rear bumpers',
                              'Soften anti-roll']}

# Fixed text walls
problem_prompt = """
What is wrong with the car?
1. Instability
2. Long stopping distance
3. Low grip on curves
4. Low speed on straights
5. Oversteer
6. Understeer
7. Poor turning response
8. Tyres lock up
9. Too much tyre wear
10. Traction loss
"""

# Functions

def getProblemNumber():
    print(problem_prompt)
    while True:
        try:
            problem_number = int(input("Enter problem number: "))
        except ValueError:
            print("That is not a valid number.")
            continue
        if problem_number > 10:
            print("That is not a valid number.")
            continue
        else:
            break
    problem_subnumber = 0
    problem_name      = ""
    # Asking further questions about oversteer and understeer
    if problem_number == 5:
      problem_name = "oversteer"
    elif problem_number == 6:
      problem_name = "understeer"
    if problem_number == 5 or problem_number == 6:
      print("\nWhere are you getting ", problem_name, "?\n",
            "0. ", problem_name.capitalize(), " in general\n",
            "1. Turn-in  2. Mid-corner  3. Corner exit\n",
            sep = "")
      while True:
          try:
                problem_subnumber = int(input("Enter problem number: "))
          except ValueError:
                print("That is not a valid number.")
                continue
          if problem_subnumber not in (0, 1, 2, 3):
                print("That is not a valid number.")
                continue
          else:
                break
    # Final addition
    problem_number = problem_number + problem_subnumber / 10
    return problem_number

def getProblemName(problem_number):
    problem_name = problems[problem_number]
    return problem_name

def printFancy(text, num_hashes = 21, pad_with_hash = False):
    if pad_with_hash:
        if type(text) is not list:
            spaces = 2 * num_hashes - len(text) + 4
            print("#", text, " " * spaces, "#")
        else:
            for element in text:
                spaces = 2 * num_hashes - len(element) + 4
                print("#", element, " " * spaces, "#")
    else:
        hashes = "#" * num_hashes
        print(hashes, text, hashes)

def printSolution(problem_number):
    problem_name = getProblemName(problem_number)
    solution     = solutions[problem_name]
    print()
    printFancy("Problem")
    printFancy(problem_name.capitalize(), pad_with_hash = True)
    printFancy("Solutions", 20)
    printFancy(solution, pad_with_hash = True)
    print("#" * 51)

########
# Main #
########
done = False
while not done:
    problem_number = getProblemNumber()
    problem_name   = getProblemName(problem_number)
    printSolution(problem_number)
    try_again = input("\nPress <enter> to solve another issue or <q> to quit: ")
    if try_again == 'q':
        done = True
