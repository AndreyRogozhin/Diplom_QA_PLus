

headers = {
    "Content-Type": "application/json"
}



# данные заказа
order_body = {
    "firstName": "Иван",  # Имя пользователя
    "lastName": "Роднов", # Фамилия пользователя
    "address": "Улица Серова, д.18", # Адрес пользователя
    "metroStation": 25,   # Код станции метро
    "phone": "+79120001122",   # Телефон пользователя
    "rentTime": 5, # Срок аренды
    "deliveryDate": "2026-06-24",   # Дата доставки 
    "color": [       # Цвет
        "BLACK"
    ]
}

