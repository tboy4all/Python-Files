# def shout():
#     return print("WHOA!")

# def whisper():
#     return print("Shhhh")

# def perform_action(func):
#     print("something is happening")
#     return func()

# perform_action(shout)
# perform_action(whisper)


# def new_decorator(func):
#     def wrap_func():
#         print("code before func!")
#         func()
#         print("code after func!")
#     return wrap_func

# @new_decorator
# def decorate_me():
#     print("decorate me!")

# # decorate_me = new_decorator(decorate_me)

# decorate_me() # What do you think this will print?


def perform_action(func):
    def wrap_func():
        print("something is happening")
        return func()
    return wrap_func

@perform_action
def whisper():
    return print("Shhhh")

@perform_action
def shout():
    return print("WHOA!")

whisper()
shout()