# паттерн Декоратор
from abc import ABC, abstractmethod
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


class SMSNotifier(Notifier):
    def __init__(self, phone: str):
        self.phone = phone

    def send(self, message: str):
        print(f"Отправлено SMS на номер {self.phone}, сообщение: {message}")


class NotifierDecorator(Notifier):
    def __init__(self, wrapper: Notifier):
        self._wrapper = wrapper

    def send(self, message: str):
        self._wrapper.send(message)

class WhatsappNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier, whatsapp_id: str):
        super().__init__(wrapper)
        self.whatsapp_id = whatsapp_id

    def send(self, message: str):
        super().send(message)
        print(f"Отправлено Whatsapp на номер: {self.whatsapp_id}, сообщение: {message}")


class TelegramNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier, telegram_id: str):
        super().__init__(wrapper)
        self.telegram_id = telegram_id

    def send(self, message: str):
        super().send(message)
        print(f"Отправлено Telegram на id: {self.telegram_id}, сообщение: {message}")


class PhotoNotifierDecorator(NotifierDecorator):
    def __init__(self, wrapper: Notifier):
        super().__init__(wrapper)
        self.photo = " sea1.jpg"

    def send(self, message: str):
        super().send(message)
        print(f"Сделан снимок")


notifier = SMSNotifier(phone="+7 902 138 76 31")
notifier = PhotoNotifierDecorator(notifier)
notifier = WhatsappNotifierDecorator(notifier, whatsapp_id="+7 902 138 76 31")
notifier = TelegramNotifierDecorator(notifier, telegram_id="@Paltus71")


notifier.send("Обнаружен подозрительный объект!")

