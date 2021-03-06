
__version__     = '2011.07.10-02'
__author__      = 'Scott Rogers, aka trash80'
__stability__   = 'alpha'
__copying__     = """Copyright (C) 2011 W. Scott Rogers \
                        This program is free software.
                        You can redistribute it and/or modify it under the terms of the
                        GNU General Public License as published by the Free Software Foundation;
                        version 2 of the License.
                    """
import sys

class Spinner(object):
    """
    Spinner Class used to show a busy spinner within a loop.
    [Usage:     spinner.render(counter) ]
    """

    def __init__(self, typeOfSpinner = [ ' [\\] ', ' [|] ', ' [/] ', ' [-] '], color = None):
        """
        typeOfSpinner:  A dictionary of characters to use as the spinner.
        color:          The color of the spinner. Supports ASCII colors. [Default: stdio default ]
        """
        self = self
        self.typeOfSpinner  = typeOfSpinner
        self.color          = color
        self.mod            = 0
    #end

    def render(self, count):
        """
        Displays a busy spinner.
        """
        spinner = self.typeOfSpinner
        counter = (((count - 1)/4)%4)

        if (counter == self.mod):
            self.mod = self.mod + 1
            if self.mod > 3:
                self.mod = 0
            print(spinner[self.mod]),
            sys.stdout.flush()
            sys.stdout.write('\r')

    #end

    def set_spinner_image(self, typeOfSpinner):
        """
        typeOfSpinner: A dictionary of characters to use as the spinner.
        """
        self.typeOfSpinner = typeOfSpinner
    #end

    def set_spinner_color(self, color):
        """
        color: The color of the spinner. Supports ASCII colors. [Default: stdio default ]
        """
        self.color = color
    #end

    def get_spinner_image(self):
        return self.typeOfSpinner
    #end

    def get_spinner_color(self):
        return self.color
    #end
#end