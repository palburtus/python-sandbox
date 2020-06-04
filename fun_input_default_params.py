def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yeah', 'yes'):
            return True
        if ok in ('n', 'nop', 'no'):
            return False 
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Are you sure you want to quit?")
ask_ok("Reall?", 2)
ask_ok("Seriously!?", 1, "yes or no only")

