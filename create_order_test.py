# Андрей Рогожин, 44-я когорта — Финальный проект. Инженер по тестированию плюс
import sender_stand_request
import data 


def test_create_check_order_get_success_response():
    
    response = sender_stand_request.post_create_order()
    track = (response.json()["track"])
    response = sender_stand_request.get_order_by_track(track)
    assert response.status_code == 200

test_create_check_order_get_success_response()
