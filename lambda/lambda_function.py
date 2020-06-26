# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils
import requests

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_core.utils import is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from ask_sdk_model.ui import StandardCard
from ask_sdk_model import ui

from decimal import *


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)





class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/"
        text = requests.get(url).text
        
        #<speak>............<audio src=\"https://sycl4.s3.eu-west-2.amazonaws.com/1min.mp3\"/></speak>
        
        speech = ("<speak>Welcome. This is the Alexa skill for voice controlling SEM. Please provide the passcode in order to fully enable the skill.<audio src=\"https://sycl4.s3.eu-west-2.amazonaws.com/1min.mp3\"/></speak>")
        reprompt = "Ask for help if you struggle. You have to provide passcode for some functions."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        #t1=time.time()
        #total=t1-t0
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class PasscodeIntentHandler(AbstractRequestHandler):
    """Handler for Passcode Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("PasscodeIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        passcode = slots["passcode"].value
        url = "https://sem-x395-a27c.try.yaler.io/pin/" + passcode
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class GetVariableIntentHandler(AbstractRequestHandler):
    """Handler for Get Main Variables Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetVariableIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/variables"
        text = requests.get(url).text
        speech = ("<speak>Variable list is shown on device.<audio src=\"https://sycl4.s3.eu-west-2.amazonaws.com/1min.mp3\"/></speak>")
        
        reprompt = "Ask me to wait for longer if you want me to stay. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class GetMagIntentHandler(AbstractRequestHandler):
    """Handler for Get Magnification Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetMagIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/getmag"
        text = requests.get(url).text
        speech = "Magnification is: " + text + " X."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", speech, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class SetMagIntentHandler(AbstractRequestHandler):
    """Handler for Set Magnification Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetMagIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["mag"].value
        decimal = slots["mag_decimal"].value
        change = slots["change"].value
        
        if data:
            if decimal:
                url = "https://sem-x395-a27c.try.yaler.io/setmag/" + str(data) + "." + str(decimal)
            else:
                url = "https://sem-x395-a27c.try.yaler.io/setmag/" + str(data) + ".0"
            
            text = requests.get(url).text    
        
        elif change:
            url_ori = "https://sem-x395-a27c.try.yaler.io/getmag"
            original = requests.get(url_ori).text
            
            if change == ("increase" or "raise" or "up"):
                url = "https://sem-x395-a27c.try.yaler.io/setmag/" + str(float(original)*1.25)
            elif change == ("decrease" or "reduce" or "down"):
                url = "https://sem-x395-a27c.try.yaler.io/setmag/" + str(float(original)*0.75)
        
            text = requests.get(url).text
        
        else:
            text = "Sorry, please tell me if you want to increase or decrease the magnification."
 
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"

        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class GetBriIntentHandler(AbstractRequestHandler):
    """Handler for Get Brightness Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetBriIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/getbri"
        text = requests.get(url).text
        speech = "Brightness is: " + text + "%."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", speech, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class SetBriIntentHandler(AbstractRequestHandler):
    """Handler for Set Brightness Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetBriIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["bri"].value
        decimal = slots["bri_decimal"].value
        change = slots["change"].value
        
        if data:
            if decimal:
                url = "https://sem-x395-a27c.try.yaler.io/setbri/" + str(data) + "." + str(decimal)
            else:
                url = "https://sem-x395-a27c.try.yaler.io/setbri/" + str(data) + ".0"
            
            text = requests.get(url).text
        
        elif change:
            url_ori = "https://sem-x395-a27c.try.yaler.io/getbri"
            original = requests.get(url_ori).text
            
            if change == ("increase" or "raise" or "up"):
                url = "https://sem-x395-a27c.try.yaler.io/setbri/" + str(float(original)+0.25)
            elif change == ("decrease" or "reduce" or "down"):
                url = "https://sem-x395-a27c.try.yaler.io/setbri/" + str(float(original)-0.25)
        
            text = requests.get(url).text
        
        else:
            text = "Sorry, please tell me if you want to increase or decrease the brightness."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response  
            
   
   
   

class GetConIntentHandler(AbstractRequestHandler):
    """Handler for Get Contrast Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetConIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/getcon"
        text = requests.get(url).text
        speech = "Contrast is: " + text + "%."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", speech, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class SetConIntentHandler(AbstractRequestHandler):
    """Handler for Set Contrast Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetConIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["con"].value
        decimal = slots["con_decimal"].value
        change = slots["change"].value
        
        if data:
            if decimal:
                url = "https://sem-x395-a27c.try.yaler.io/setcon/" + str(data) + "." + str(decimal)
            else:
                url = "https://sem-x395-a27c.try.yaler.io/setcon/" + str(data) + ".0"
            text = requests.get(url).text
        
        elif change:
            url_ori = "https://sem-x395-a27c.try.yaler.io/getcon"
            original = requests.get(url_ori).text
                
            if change == ("increase" or "raise" or "up"):
                url = "https://sem-x395-a27c.try.yaler.io/setcon/" + str(float(original)+0.25)
            elif change == ("decrease" or "reduce" or "down"):
                url = "https://sem-x395-a27c.try.yaler.io/setcon/" + str(float(original)-0.25)
                
            text = requests.get(url).text
            
        else:
            text = "Sorry, please tell me if you want to increase or decrease the contrast."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response  





class SetKVIntentHandler(AbstractRequestHandler):
    """Handler for Set KV Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetKVIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["kv"].value
        decimal = slots["kv_decimal"].value
        
        if data:
            if decimal:
                url = "https://sem-x395-a27c.try.yaler.io/setkv/" + str(data) + "." + str(decimal)
            else:
                url = "https://sem-x395-a27c.try.yaler.io/setkv/" + str(data) + ".0"
            text = requests.get(url).text
            
        else:
            text = "Sorry, please tell me if you want to increase or decrease the KV."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response  
  




class AutoFineAlignIntentHandler(AbstractRequestHandler):
    """Handler for Auto Fine Align Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AutoFineAlignIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/autofinealign"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class AutoFineFocusIntentHandler(AbstractRequestHandler):
    """Handler for Auto Fine Focus Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AutoFineFocusIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/autofinefocus"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class AutoStigIntentHandler(AbstractRequestHandler):
    """Handler for Auto Stig Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AutoStigIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/autostig"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class CaptureIntentHandler(AbstractRequestHandler):
    """Handler for Capture Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/capture"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class GrabIntentHandler(AbstractRequestHandler):
    """Handler for Grab Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GrabIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
    
        text = "Image updated."  
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
       
        return handler_input.response_builder.response





class MclAmazonIntentHandler(AbstractRequestHandler):
    """Handler for MCL Amazon Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MCLAmazonIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/amazon"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help." 
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(SimpleCard("The SEM Voice Assistance", text))
        
        return handler_input.response_builder.response





class NormalIntentHandler(AbstractRequestHandler):
    """Handler for MCL Normal Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("NormalIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/normal"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(SimpleCard("The SEM Voice Assistance", text))
        
        return handler_input.response_builder.response





class GetStagePositionIntentHandler(AbstractRequestHandler):
    """Handler for Get Stage Position Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("GetStagePositionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/getstage"
        text = requests.get(url).text
        speech = "Stage position is shown on device."
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class SetImagePositionIntentHandler(AbstractRequestHandler):
    """Handler for Set Image Position Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetImagePositionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["data"].value
        decimal = slots["data_decimal"].value
        direction = slots["dir"].value
        
        value=str(0)
        
        if data: 
            if decimal:
                value = str(data) + "." + str(decimal)
            else:
                value = str(data) + ".0"
            
            value = str(float(value)*0.001)
            
        else:
            url = "https://sem-x395-a27c.try.yaler.io/getmag"
            mag = requests.get(url).text
    
            value = str(Decimal(50*(1/float(mag))))
                
        if direction == "right":
            url = "https://sem-x395-a27c.try.yaler.io/setimageright/" + value
        elif direction == "left":
            url = "https://sem-x395-a27c.try.yaler.io/setimageleft/" + value
        elif direction == "up":
            url = "https://sem-x395-a27c.try.yaler.io/setimageup/" + value
        elif direction == "down":
            url = "https://sem-x395-a27c.try.yaler.io/setimagedown/" + value
                    
        text = requests.get(url).text

        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
                
        return handler_input.response_builder.response  


class SetStagePositionIntentHandler(AbstractRequestHandler):
    """Handler for Set Stage Position Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SetStagePositionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        data = slots["data"].value
        decimal = slots["data_decimal"].value
        direction = slots["dir"].value
        
        value=str(0)
        
        if data: 
            if decimal:
                value = str(data) + "." + str(decimal)
            else:
                value = str(data) + ".0"
            
            value = str(float(value)*0.001)
            
        else:
            url = "https://sem-x395-a27c.try.yaler.io/getmag"
            mag = requests.get(url).text
    
            value = str(Decimal(50*(1/float(mag))))
            
        if direction == "right":
            url = "https://sem-x395-a27c.try.yaler.io/setimageright/" + value
        elif direction == "left":
            url = "https://sem-x395-a27c.try.yaler.io/setimageleft/" + value
        elif direction == "up":
            url = "https://sem-x395-a27c.try.yaler.io/setstageup/" + value
        elif direction == "down":
            url = "https://sem-x395-a27c.try.yaler.io/setstagedown/" + value
                    
        text = requests.get(url).text

        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
                
        return handler_input.response_builder.response  


class SavePositionIntentHandler(AbstractRequestHandler):
    """Handler for Save Stage Position Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SavePositionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        preset = slots["int"].value
        
        url = "https://sem-x395-a27c.try.yaler.io/savestageposition/" + str(preset)
        text = requests.get(url).text    
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"

        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response    


class CallPositionIntentHandler(AbstractRequestHandler):
    """Handler for Call Stage Position Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CallPositionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        preset = slots["int"].value
        
        url = "https://sem-x395-a27c.try.yaler.io/callstageposition/" + str(preset)
        text = requests.get(url).text    
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"

        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response





class BeamOnIntentHandler(AbstractRequestHandler):
    """Handler for Run up/beam on Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("BeamOnIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/runup"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response
  

class ShutDownIntentHandler(AbstractRequestHandler):
    """Handler for shutdown/beam off Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ShutDownIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/shutdown"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response



  
  
class CloudIntentHandler(AbstractRequestHandler):
    """Handler for Cloud saving Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CloudIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/cloud"
        text = requests.get(url).text
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(text).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response 
  
  
  
  
  
class WaitForNextIntentHandler(AbstractRequestHandler):
    """Handler for Wait Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("WaitForNextIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        text = "Waiting for next command."
        speech = ("<speak>Of course. Please call me when you are ready. If I have exit the skill, please call the skill again.<audio src=\"https://sycl4.s3.eu-west-2.amazonaws.com/1min.mp3\"/></speak>")
        
        reprompt = "Ask me to wait for longer if you want me to stay. You can also ask me to show the variable list. To view the list of functions again, ask for help."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response  


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        url = "https://sem-x395-a27c.try.yaler.io/help"
        text = requests.get(url).text
        speech = "Please see the list of functions available on the screen."
        
        url_grab = "https://sem-x395-a27c.try.yaler.io/grab"
        filename = requests.get(url_grab).text
        
        url_img = "https://sem-x395-a27c.try.yaler.io/picture"
        send_img = requests.get(url_img)
        
        small_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename[:16]+"small_"+filename[16:]+".jpg"
        large_image_url = "https://sycl4.s3.eu-west-2.amazonaws.com/"+filename+".jpg"
        
        handler_input.response_builder.speak(speech).ask(reprompt)
        handler_input.response_builder.set_card(StandardCard("The SEM Voice Assistance", text, 
                image=ui.Image(small_image_url=small_image_url, large_image_url=large_image_url)))
        
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(PasscodeIntentHandler())
sb.add_request_handler(GetVariableIntentHandler())
sb.add_request_handler(GetMagIntentHandler())
sb.add_request_handler(SetMagIntentHandler())
sb.add_request_handler(GetBriIntentHandler())
sb.add_request_handler(SetBriIntentHandler())
sb.add_request_handler(GetConIntentHandler())
sb.add_request_handler(SetConIntentHandler())
sb.add_request_handler(SetKVIntentHandler())
sb.add_request_handler(AutoFineAlignIntentHandler())
sb.add_request_handler(AutoFineFocusIntentHandler())
sb.add_request_handler(AutoStigIntentHandler())
sb.add_request_handler(CaptureIntentHandler())
sb.add_request_handler(GrabIntentHandler())
sb.add_request_handler(MclAmazonIntentHandler())
sb.add_request_handler(NormalIntentHandler())
sb.add_request_handler(GetStagePositionIntentHandler())
sb.add_request_handler(SetImagePositionIntentHandler())
sb.add_request_handler(SetStagePositionIntentHandler())
sb.add_request_handler(SavePositionIntentHandler())
sb.add_request_handler(CallPositionIntentHandler())
sb.add_request_handler(ShutDownIntentHandler())
sb.add_request_handler(BeamOnIntentHandler())
sb.add_request_handler(CloudIntentHandler())
sb.add_request_handler(WaitForNextIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()