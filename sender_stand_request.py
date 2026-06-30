import configuration
import requests 
import data 

def post_create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH ,
                            json=data.order_body,
                            headers=data.headers)



def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "?t=" +str(track) ,
                            #headers=data.user_headers
                            )
