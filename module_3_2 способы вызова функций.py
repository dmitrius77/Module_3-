def send_email(message, recipient, sender="university.help@gmail.com"): #Создайте функцию send_email, которая принимает 2 обычных аргумента: message, recipient и 1 обязательно именованный аргумент со значением по умолчанию sender = "university.help@gmail.com".
    if "@" not in recipient or "@" not in sender or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")): #Если строки recipient и sender не содержит "@" или не оканчивается на ".com"/".ru"/".net"
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")# то вывести на экран(в консоль) строку: "Невозможно отправить письмо с адреса <sender> на адрес <recipient>".
    elif recipient == sender:  # Если же sender и recipient совпадают,
        print("Нельзя отправить письмо самому себе!")  # то вывести "Нельзя отправить письмо самому себе!"
    elif sender != "university.help@gmail.com": # если отправитель отличается от заданного по умолчанию
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>.")  # В противном случае вывести сообщение: "НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <sender> на адрес <recipient>."
    else: # в остальных случаях, вывести в консоль
        print("Письмо успешно отправлено с адреса sender на адрес recipient.")  # то вывести сообщение: "Письмо успешно отправлено с адреса <sender> на адрес <recipient>."


#send_email('Проверка связи', 'vasyok1337@gmail.com') # письмо успешно отправлено

#send_email('Если Вы видите это сообщение, значит справились с заданием!', 'urban.fan@mail.ru', sender='urban.info@mail.com') # нестандартный отправитель

#send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')  # невозможно отправить

#send_email('Напомнить о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')  # невозможно отправить себе
