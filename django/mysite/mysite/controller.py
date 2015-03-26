# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from config import FB_APP_ID, FB_APP_SECRET, FORWARDING_URL
from config import TEMBOO_ACCOUNT_NAME, TEMBOO_APP_NAME, TEMBOO_APP_KEY
from temboo.Library.Facebook.OAuth import InitializeOAuth
from temboo.Library.Facebook.OAuth import FinalizeOAuth
from temboo.Library.Facebook.Reading import User
from temboo.core.session import TembooSession
import uuid
from django.template import RequestContext, loader
from facebookUtils import *

#### Statics #####
# Create a Temboo session object
SESSION = TembooSession(TEMBOO_ACCOUNT_NAME, TEMBOO_APP_NAME,
                        TEMBOO_APP_KEY)
CUSTOMCALLBACKID = None
STATIC_WORDS_TO_SERACH=[]
GROUPS=""
utils = facebookUtils()

def home(request):
        template = loader.get_template('templates/main.html')
        context = RequestContext(request, {
        'latest_question_list': '1',
        })
        return HttpResponse(template.render(context))


def get_login_url_to_serach_with_and(request):
    global STATIC_WORDS_TO_SERACH
    STATIC_WORDS_TO_SERACH =[]
    print 'get_login_url_to_serach_with_and'
    # Generate a random state token which is used as the CustomCallbackID and in the ForwardingURL
    customCallbackId = str(uuid.uuid4())

    # Instantiate the InitializeOAuth choreo to begin the OAuth process.
    initializeOAuthChoreo = InitializeOAuth(SESSION)
    print "initializeOAuthChoreo: ",initializeOAuthChoreo
    # Get an InputSet object for the InitializeOAuth choreo
    initializeOAuthInputs = initializeOAuthChoreo.new_input_set()

    groups = request.GET.get(u'groups', '')
    GROUPS= groups.encode('utf8')
    useAnd = request.GET.get('and', '')
    # Set inputs for InitializeOAuth
    # Append the state token to the Forwarding URL
    initializeOAuthInputs.set_AppID(FB_APP_ID)
    initializeOAuthInputs.set_Scope("user_groups")
    #initializeOAuthInputs.set_Scope("user_friends")
    CUSTOMCALLBACKID = customCallbackId
    initializeOAuthInputs.set_CustomCallbackID(customCallbackId)
    words = u"&groups=%s" % (groups)
    groups = groups.split(",")
    for word in groups:
        STATIC_WORDS_TO_SERACH.append(word)
    # STATIC_WORDS_TO_SERACH.append(groups)
    print STATIC_WORDS_TO_SERACH[0].encode('utf8')
    print FORWARDING_URL + "?state=" + TEMBOO_ACCOUNT_NAME + "/" + customCallbackId + unicode(words).encode('utf8')+"&and="+useAnd
    initializeOAuthInputs.set_ForwardingURL(FORWARDING_URL + "?state=" + TEMBOO_ACCOUNT_NAME + "/" + customCallbackId + words+"&and="+useAnd)

    # Execute InitializeOAuth choreo
    print "initializeOAuthChoreo: ",initializeOAuthChoreo
    initializeOAuthResults = initializeOAuthChoreo.execute_with_results(initializeOAuthInputs)
    print initializeOAuthResults
    print "~~~~The Authorization URL is: " + initializeOAuthResults.get_AuthorizationURL()

    # Redirect user to the AuthorizationURL so that they can login and grant the application access

    return HttpResponseRedirect(initializeOAuthResults.get_AuthorizationURL())

def get_user_info(request):
    print 'get_user_info'
     # Instantiate the FinalizeOAuth choreo
    finalizeOAuthChoreo = FinalizeOAuth(SESSION)

    # Get an InputSet object for the FinalizeOAuth choreo
    finalizeOAuthInputs = finalizeOAuthChoreo.new_input_set()

    # Set inputs for FinalizeOAuth
    # Get the state token parameter after the redirect to use as the CallbackID
    finalizeOAuthInputs.set_AppID(FB_APP_ID)
    finalizeOAuthInputs.set_AppSecret(FB_APP_SECRET)
    # import pdb;pdb.set_trace();
    print "~~~~The state token is: " + request.GET.get('state')
    finalizeOAuthInputs.set_CallbackID(request.GET.get('state'))

    # Execute FinalizeOAuth choreo to complete the OAuth process and retrieve an access token
    finalizeOAuthResults = finalizeOAuthChoreo.execute_with_results(finalizeOAuthInputs)

    # # Intiate the Facebook.Reading.User choreo to get the user's profile
    userChoreo = User(SESSION)

    # # Get an InputSet object for the Facebook.Reading.User choreo
    userInputs = userChoreo.new_input_set()

    # Initilize instance

    utils.setAccessToken(finalizeOAuthResults.get_AccessToken())
    listOfUserGroups = utils.getGroupsNames()


    listOfAllPosts=[]
    words_to_saerch=[]
    for word in STATIC_WORDS_TO_SERACH:
        words_to_saerch.append(word.encode('utf8'))
    #words_to_saerch.append(STATIC_WORDS_TO_SERACH[0].encode('utf8'))
    # print  STATIC_WORDS_TO_SERACH[0].encode('utf8')
    #words_to_saerch = STATIC_WORDS_TO_SERACH
    #words_to_saerch = words_to_saerch.split(',')

    searchWithAndBetweenWords = request.GET.get('and', '')
    allPosts = utils.getGroupPosts(listOfUserGroups)
    #allPosts = utils.getGroupPosts(['Twitter Bootstrap Developers','יד רוחצת יד'])
    template = loader.get_template('templates/posts.html')
    context = RequestContext(request, {
        'latest_question_list': utils.parse_posts(allPosts,searchWithAndBetweenWords,words_to_saerch),
        })
    return HttpResponse(template.render(context))

