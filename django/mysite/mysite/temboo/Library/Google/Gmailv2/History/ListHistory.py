# -*- coding: utf-8 -*-

###############################################################################
#
# ListHistory
# Lists the history of all changes to the given mailbox.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class ListHistory(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the ListHistory Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(ListHistory, self).__init__(temboo_session, '/Library/Google/Gmailv2/History/ListHistory')


    def new_input_set(self):
        return ListHistoryInputSet()

    def _make_result_set(self, result, path):
        return ListHistoryResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return ListHistoryChoreographyExecution(session, exec_id, path)

class ListHistoryInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the ListHistory
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AccessToken(self, value):
        """
        Set the value of the AccessToken input for this Choreo. ((optional, string) A valid Access Token retrieved during the OAuth2 process. This is required unless you provide the ClientID, ClientSecret, and RefreshToken to generate a new Access Token.)
        """
        super(ListHistoryInputSet, self)._set_input('AccessToken', value)
    def set_ClientID(self, value):
        """
        Set the value of the ClientID input for this Choreo. ((conditional, string) The Client ID provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ListHistoryInputSet, self)._set_input('ClientID', value)
    def set_ClientSecret(self, value):
        """
        Set the value of the ClientSecret input for this Choreo. ((conditional, string) The Client Secret provided by Google. Required unless providing a valid AccessToken.)
        """
        super(ListHistoryInputSet, self)._set_input('ClientSecret', value)
    def set_Fields(self, value):
        """
        Set the value of the Fields input for this Choreo. ((optional, string) Used to specify fields to include in a partial response. This can be used to reduce the amount of data returned. See Choreo notes for syntax rules.)
        """
        super(ListHistoryInputSet, self)._set_input('Fields', value)
    def set_LabelID(self, value):
        """
        Set the value of the LabelID input for this Choreo. ((optional, string) Returns messages with a label matching this ID.)
        """
        super(ListHistoryInputSet, self)._set_input('LabelID', value)
    def set_MaxResults(self, value):
        """
        Set the value of the MaxResults input for this Choreo. ((optional, integer) The maximum number of results to return.)
        """
        super(ListHistoryInputSet, self)._set_input('MaxResults', value)
    def set_PageToken(self, value):
        """
        Set the value of the PageToken input for this Choreo. ((optional, string) The "nextPageToken" found in the response which is used to page through results.)
        """
        super(ListHistoryInputSet, self)._set_input('PageToken', value)
    def set_RefreshToken(self, value):
        """
        Set the value of the RefreshToken input for this Choreo. ((conditional, string) An OAuth Refresh Token used to generate a new Access Token when the original token is expired. Required unless providing a valid AccessToken.)
        """
        super(ListHistoryInputSet, self)._set_input('RefreshToken', value)
    def set_StartHistoryID(self, value):
        """
        Set the value of the StartHistoryID input for this Choreo. ((required, string) Returns history records after the specified marker. The history ID is returned by the Messages.GetMessage Choreo.)
        """
        super(ListHistoryInputSet, self)._set_input('StartHistoryID', value)
    def set_UserID(self, value):
        """
        Set the value of the UserID input for this Choreo. ((optional, string) The ID of the acting user. Defaults to "me" indicating the user associated with the Access Token or Refresh Token provided.)
        """
        super(ListHistoryInputSet, self)._set_input('UserID', value)

class ListHistoryResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the ListHistory Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. ((json) The response from Google.)
        """
        return self._output.get('Response', None)
    def get_NewAccessToken(self):
        """
        Retrieve the value for the "NewAccessToken" output from this Choreo execution. ((string) Contains a new AccessToken when the RefreshToken is provided.)
        """
        return self._output.get('NewAccessToken', None)

class ListHistoryChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return ListHistoryResultSet(response, path)
