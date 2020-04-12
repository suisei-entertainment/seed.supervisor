## ============================================================================
##                   **** SEED Virtual Reality Platform ****
##                Copyright (C) 2019-2020, Suisei Entertainment
## ============================================================================
##
##  This program is free software: you can redistribute it and/or modify
##  it under the terms of the GNU General Public License as published by
##  the Free Software Foundation, either version 3 of the License, or
##  (at your option) any later version.
##
##  This program is distributed in the hope that it will be useful,
##  but WITHOUT ANY WARRANTY; without even the implied warranty of
##  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##  GNU General Public License for more details.
##
##  You should have received a copy of the GNU General Public License
##  along with this program.  If not, see <http://www.gnu.org/licenses/>.
##
## ============================================================================

"""
Contains the implementation of the Supervisor class.
"""

# SEED Imports
from suisei.seed.application import BusinessLogic, ApplicationReturnCodes

class Supervisor(BusinessLogic):

    """
    Contains the top level business logic of the SEED supervisor daemon.

    Authors:
        Attila Kovacs
    """

    def __init__(self) -> None:

        """
        Creates a new Supervisor instance.

        Authors:
            Attila Kovacs
        """

        self._running = True

    def main_loop(self) -> 'ApplicationReturnCodes':

        """
        Contains the main loop (or the main business execution logic of
        the application.

        Returns:
            The overall return code of the application.
            ApplicationReturnCodes.SUCCESS for successful execution, or an
            integer value to indicate issues.

        Authors:
            Attila Kovacs
        """

        #pylint: disable=no-self-use

        while self._running:
            time.sleep(1)

        return ApplicationReturnCodes.SUCCESS

    def before_main_loop(self) -> None:

        """
        Function that is called before the application enters its main loop.

        Authors:
            Attila Kovacs
        """

        #pylint: disable=no-self-use

        return

    def after_main_loop(self) -> None:

        """
        Function that is called after the application exited the main loop in
        a normal way.

        Authors:
            Attila Kovacs
        """

        #pylint: disable=no-self-use

        return

    def initialize_services(self) -> None:

        """
        Initializes the services used by the application. It is called by the
        application upon initialization.

        Authors:
            Attila Kovacs
        """

        return

    @staticmethod
    def cb_process_command_line(arguments: 'argparse.Namespace') -> None:

        """
        Callback function that is called when the CLI processor processed the
        command line options provided.

        Args:
            arguments:      The argparse namespace object containing the
                            processed command line parameters.

        Authors:
            Attila Kovacs
        """

        pass