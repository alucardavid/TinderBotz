'''
Created by Frederikme (TeetiFM)
'''

from dotenv import load_dotenv
load_dotenv()

from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *
from tinderbotz.models.my_profile import MyProfile
import os

if __name__ == "__main__":
    # creates instance of session
    session = Session()
    # Or if you want to use a proxy
    # AUTHORISED BY IP -> "HOST:PORT"
    # AUTHORISED BY USERNAME, PASSWORD -> "username:password@HOST:PORT"
    #session = Session(proxy="23.23.23.23:3128")

    # set location (Don't need to be logged in for this)
    session.set_custom_location(latitude=float(os.getenv('LATITUDE')), longitude=float(os.getenv('LONGITUDE')))
    
    # replace this with your own email and password!
    email = os.getenv('FACEBOOK_USER')
    password = os.getenv('FACEBOOK_PASSWORD')
    
    # login using your google account with a verified email!
    #session.login_using_google(email, password)

    # Alternatively you can login using facebook with a connected profile!
    session.login_using_facebook(email, password)

    # Alternatively, you can also use your phone number to login
    '''
    - country is needed to get the right prefix, in my case +32
    - phone_number is everything after the prefix (+32)
    NOTE: this is not my phone number :)
    '''
    #country = "Brazil"
    #phone_number = ""
    #session.login_using_sms(country, phone_number)
    
    
    ### adjust allowed distance for geomatches
    ### Note: PARAMETER IS IN KILOMETERS!
    # session.set_distance_range(km=50)

    ### Geting my profile information
    my_profile: MyProfile = session._get_my_profile_match()


    ### spam likes, dislikes and superlikes
    ### to avoid being banned:
    ### - it's best to apply a randomness in your liking by sometimes disliking.
    ### - some sleeping between two actions is recommended
    # by default the amount is 1, ratio 100% and sleep 1 second
    
    #session.like(amount=20, ratio="72.5%", sleep=1)
    #session.dislike(amount=1)
    #session.superlike(amount=0)
    

    # set range of prefered age
    #session.set_age_range(30, 40)

    # set interested in gender(s) -> options are: WOMEN, MEN, EVERYONE
    #session.set_sexuality(Sexuality.WOMEN)

    # Allow profiles from all over the world to appear
    #session.set_global(True)

    ## Getting matches takes a while, so recommended you load as much as possible from local storage
    ## get new matches, with whom you haven't interacted yet
    ## Let's load the first 10 new matches to interact with later on.
    ## quickload on false will make sure ALL images are stored, but this might take a lot more time
    #new_matches = session.get_new_matches(amount=4, quickload=False)
    #print(f'Quantidade de matches {new_matches}')

    ## get already interacted with matches (matches with whom you've chatted already)
    # messaged_matches = session.get_messaged_matches()
    
    ## you can store the data and images of these matches now locally in data/matches
    ## For now let's just store the messaged_matches
    #for match in messaged_matches:
    #    session.store_local(match)

    ## Pick up line with their personal name so it doesn't look spammy
    #pickup_line = "Eu aqui tentando parecer descolado, mas só pensando em como puxar assunto com você sem pagar mico. Então: oi! 😅"

    ## loop through my new matches and send them the first message of the conversation
    #for match in new_matches:
        ## store name and chatid in variables so we can use it more simply later on
        #name = match.get_name()
        #id = match.get_chat_id()

        #print(name, id)

        ## Format the match her/his name in your pickup line for a more personal approach.
        #message = pickup_line

        ## send pick up line with their name in it to all my matches
        #session.send_message(chatid=id, message=message)

        ## send a funny gif
        #session.send_gif(chatid=id, gifname="")

        ## send a funny song
        #session.send_song(chatid=id, songname="")

        ## send instagram or other socials like facebook, phonenumber and snapchat
        #session.send_socials(chatid=id, media=Socials.INSTAGRAM, value="david.aluc")

        ## you can also unmatch
        #session.unmatch(chatid=id)

    ## let's scrape some geomatches now
    #for _ in range(5):
        ## get profile data (name, age, bio, images, ...)
        #geomatch = session.get_geomatch(quickload=False)
        ## store this data locally as json with reference to their respective (locally stored) images
        #session.store_local(geomatch)
        ## dislike the profile, so it will show us the next geomatch (since we got infinite amount of dislikes anyway)
        #session.dislike()
