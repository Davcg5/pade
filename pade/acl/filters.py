#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Framework para Desenvolvimento de Agentes Inteligentes PADE

# The MIT License (MIT)

# Copyright (c) 2015 Lucas S Melo

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from pade.acl.aid import AID
from pade.acl.messages import ACLMessage

class Filter():
    '''
        This class instantiates a filter object. The filter has the purpose of 
        selecting messages with pre established attributes in the filter object
    '''
    def __init__(self):
        self.conversationID = None
        self.sender = None
        self.performative = None
        self.protocol = None
        self.ontology = None
        self.language = None
        self.sender_local_name = None

    
    def set_sender(self, aid):
        self.sender = aid
        
    def set_performative(self, performative):
        self.performative = performative
    
    def setConversationID(self, conversationID):
        self.conversationID = conversationID
    
    def set_protocol(self, protocol):
        self.protocol = protocol

    def set_ontology(self, ontology):
        self.ontology = ontology

    def set_language(self, language):
        self.language = language

    def set_sender_local_name(self, local_name):
        if isinstance(local_name, AID):
            self.sender_local_name = local_name.getLocalName()
        else:
            self.sender_local_name = local_name
    
    def filter(self, message):
        state = True
        
        if self.conversationID != None and self.conversationID != message.conversationID:
            state = False
        
        if self.sender != None and self.sender != message.sender:
            state = False
        
        if self.performative != None and self.performative != message.performative:
            state = False
        
        if self.protocol != None and self.protocol != message.protocol:
            state = False

        if self.ontology != None and self.ontology != message.ontology:
            state = False

        if self.language != None and self.language != message.language:
            state = False

        if self.sender == None and self.sender_local_name != None and self.sender_local_name != message.sender.getLocalName():
            state = False

        return state

if __name__ == '__main__':
    message = ACLMessage(ACLMessage.REQUEST)
    message.set_sender(AID('lucas'))
    message.add_receiver('allana')
    message.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
    
    filtro = Filter()
    filtro.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
    
    if filtro.filter(message):
        print(message.as_xml())
    else:
        print('The message was blocked by the protocol.')
