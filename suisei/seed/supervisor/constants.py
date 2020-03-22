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
Contains common constants used by the SEED supervisor daemon.
"""

# Path to the default directory containing the configuration of the daemon.
DEFAULT_CONFIG_DIRECTORY = '/config'

# Path to the directory containing the service definitions used by the daemon.
DEFAULT_SERVICES_DIRECTORY = '/services'

# Path to the directory where the daemon will store its log files.
DEFAULT_LOG_DIRECTORY = '/logs'

# The default package name to use when loading supervisor services.
DEFAULT_SERVICE_PACKAGE = 'services'

# The default name of the supervisor's PID file.
DEFAULT_PID_FILE = 'seed_supervisor.pid'

# The description string to use in the CLI help.
CLI_DESCRIPTION_STRING = \
    'SEED supervior daemon. This process is responsible for managing the SEED '
    'node.'

# The usage string to use in the CLI help.
CLI_USAGE_STRING = \
    'seed.supervisor [start|stop|restart|status] [-h|--help] [--debug] '
    '[-c|--config-directory] [-s|--service-directory] [-l|--log-directory] '
    '[-p|--pid-file] [--service-package] [--key]'

# The epilogue string to use in the CLI help.
CLI_EPILOGUE_STRING = ''

# The CLI commands used by the application
CLI_COMMAND_MAP = \
[
    {
        'type': 'group',
        'name': 'Daemon Control',
        'description': 'Contains options to control the SEED supervisor daemon.',
        'commands':
        [
            {
                'type': 'switch',
                'shortkey': '',
                'command': 'start',
                'help': 'Starts the supervisor daemon.',
                'default': 'False'
            },
            {
                'type': 'switch',
                'shortkey': '',
                'command': 'stop',
                'help': 'Stops the supervisor daemon.',
                'default': 'False'
            },
            {
                'type': 'switch',
                'shortkey': '',
                'command': 'restart',
                'help': 'Restarts the supervisor daemon.',
                'default': 'False'
            },
            {
                'type': 'switch',
                'shortkey': '',
                'command': 'status',
                'help': 'Displays the current status of the supervisor daemon.',
                'default': 'False'
            }
        ]
    },
    {
        'type': 'group',
        'name': 'Daemon Configuration',
        'description': 'Contains options to customize the configuration of the SEED supervisor daemon.',
        'commands':
        [
            {
                'type': 'config',
                'shortkey': '-c',
                'command': '--config-directory',
                'help': 'Allows the specification of a custom configuration directory.',
                'metavar': 'PATH'
            },
            {
                'type': 'config',
                'shortkey': '-s',
                'command': '--service-directory',
                'help': 'Allows the specification of a custom service directory.',
                'metavar': 'PATH'
            },
            {
                'type': 'config',
                'shortkey': '',
                'command': '--service-package',
                'help': 'Allows the specification of a custom service package.',
                'metavar': 'PACKAGE NAME'
            },
            {
                'type': 'config',
                'shortkey': '-l',
                'command': '--log-directory',
                'help': 'Allows the specification of a custom log directory.',
                'metavar': 'PATH'
            },
            {
                'type': 'config',
                'shortkey': '-p',
                'command': '--pid-file',
                'help': 'Allows the specification of a custom PID file.',
                'metavar': 'PATH'
            },
            {
                'type': 'config',
                'shortkey': '',
                'command': '--key',
                'help': 'Allows the specification of the decryption key to use when loading the configuration',
                'metavar': 'KEY'
            }
        ]
    },
    {
        'type': 'group',
        'name': 'Miscellaneous Options',
        'description': 'Contains miscellaneous options for the SEED supervisor daemon.',
        'commands':
        [
            {
                'type': 'switch',
                'shortkey': '-d',
                'command': '--debug',
                'help': 'Starts the daemon in debug mode.',
                'default': 'False'
            }
        ]
    }
]