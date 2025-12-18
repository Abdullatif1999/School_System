from rest_framework.renderers import JSONRenderer
import json

class HappyJSONRenderer(JSONRenderer):


    def render(self, data, accepted_media_type=None, renderer_context=None):
        mydata = {}
        status = False
        message_name = "error_messages"
        if renderer_context and 'response' in renderer_context:
            response = renderer_context['response']
            status_code = response.status_code
            if status_code <400 and status_code>=200:
                status = True
                message_name = "data"
            mydata['status'] = status
            mydata['status_code'] = status_code
            if data is not None:
                mydata[f'{message_name}'] = data
            return super().render(mydata, accepted_media_type, renderer_context)            
        return super().render(data, accepted_media_type, renderer_context)