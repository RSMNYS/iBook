from constants import MISSED_PARAMS
def input_error(func):

    def inner(self, *args, **kwargs):
        try: 
            if len(args) < 2:
                print(MISSED_PARAMS)
                return
            return func(self, *args, **kwargs)
        except ValueError as error:
            print(error)
        except KeyError as error:
            print(error)


    return inner