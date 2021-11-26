import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

AUTHENTICATOR = IAMAuthenticator(API_KEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def englishToFrench(english_text):
    # write the code here
    if english_text is None:
        return "null"
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation["translations"][0]['translation']

def frenchToEnglish(french_text):
    # write the code here
    if french_text is None:
        return "null"
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation["translations"][0]['translation']
