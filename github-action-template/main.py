# -*- coding: utf-8 -*-
"""This module contains the code that executes the github action."""
import os


def main():
    """Greet user using the supplied name."""
    my_input = os.getenv('INPUT_MYINPUT') or 'world'

    my_output = f"Hello {my_input}"

    print(f"::set-output name=MYOUTPUT::{my_output}")


if __name__ == "__main__":
    main()
