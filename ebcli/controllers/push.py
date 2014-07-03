# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

from ebcli.core.abstractcontroller import AbstractBaseController
from ebcli.resources.strings import strings


class PushController(AbstractBaseController):
    class Meta:
        label = 'push'
        description = strings['push.info']
        arguments = [
            (['-f', '--foo'], dict(help='notorious foo option')),
        ]

    def do_command(self):

        # Check branch to see if its set up
           # ask to create branch stuff

        # do the push
            # wait for finish.. print status

        self.app.print_to_console('We are doing the push stuff!')