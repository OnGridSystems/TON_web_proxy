import os
import sys
import traceback


def print_error_and_exit(message):
    print(message)
    print('Exiting...')
    sys.exit(1)


def env_or_exit(env_name, cast=None):
    env = os.getenv(env_name)
    if env is None:
        print_error_and_exit(f'You should set \'{env_name}\' env')
    if cast is None:
        return env
    if cast is bool:
        mapping = {"true": True, "1": True, "false": False, "0": False}
        env = env.lower()
        if env not in mapping:
            print_error_and_exit(
                f'\'{env_name}\' value \'{env}\' is not a boolean'
            )
        return mapping[env]
    try:
        return cast(env)

    except Exception:
        traceback.print_exc()
        print_error_and_exit(
            f'Attempt to cast \'{env_name}\' value \'{env}\' '
            f'to \'{cast.__name__}\' failed'
        )
