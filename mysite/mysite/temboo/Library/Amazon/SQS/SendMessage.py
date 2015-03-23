# -*- coding: utf-8 -*-

###############################################################################
#
# SendMessage
# Sends a message to a specified queue.
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

class SendMessage(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the SendMessage Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(SendMessage, self).__init__(temboo_session, '/Library/Amazon/SQS/SendMessage')


    def new_input_set(self):
        return SendMessageInputSet()

    def _make_result_set(self, result, path):
        return SendMessageResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return SendMessageChoreographyExecution(session, exec_id, path)

class SendMessageInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the SendMessage
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_AWSAccessKeyId(self, value):
        """
        Set the value of the AWSAccessKeyId input for this Choreo. ((required, string) The Access Key ID provided by Amazon Web Services.)
        """
        super(SendMessageInputSet, self)._set_input('AWSAccessKeyId', value)
    def set_AWSAccountId(self, value):
        """
        Set the value of the AWSAccountId input for this Choreo. ((required, integer) The id for the AWS account associated with the queue you're sending a message to (remove all dashes in the account number).)
        """
        super(SendMessageInputSet, self)._set_input('AWSAccountId', value)
    def set_AWSSecretKeyId(self, value):
        """
        Set the value of the AWSSecretKeyId input for this Choreo. ((required, string) The Secret Key ID provided by Amazon Web Services.)
        """
        super(SendMessageInputSet, self)._set_input('AWSSecretKeyId', value)
    def set_MessageBody(self, value):
        """
        Set the value of the MessageBody input for this Choreo. ((required, string) The message to send. Maximum size is 64 KB.)
        """
        super(SendMessageInputSet, self)._set_input('MessageBody', value)
    def set_QueueName(self, value):
        """
        Set the value of the QueueName input for this Choreo. ((required, string) The name of the queue you want to send a message to.)
        """
        super(SendMessageInputSet, self)._set_input('QueueName', value)
    def set_ResponseFormat(self, value):
        """
        Set the value of the ResponseFormat input for this Choreo. ((optional, string) The format that the response should be in. Valid values are "xml" (the default) and "json".)
        """
        super(SendMessageInputSet, self)._set_input('ResponseFormat', value)
    def set_UserRegion(self, value):
        """
        Set the value of the UserRegion input for this Choreo. ((optional, string) The AWS region that corresponds to the SQS endpoint you wish to access. The default region is "us-east-1". See description below for valid values.)
        """
        super(SendMessageInputSet, self)._set_input('UserRegion', value)

class SendMessageResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the SendMessage Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Amazon.)
        """
        return self._output.get('Response', None)

class SendMessageChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return SendMessageResultSet(response, path)