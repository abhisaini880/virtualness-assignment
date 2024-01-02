from abc import ABC, abstractmethod


class RuleAction(ABC):
    @abstractmethod
    def execute(self, event):
        pass


class PushNotificationAction(RuleAction):
    def execute(self, event):
        # Mock sending a push notification
        print(f"Sending push notification for event: {event}")


class AlertOperatorAction(RuleAction):
    def execute(self, event):
        # Mock alerting an operator
        print(f"Alerting operator for event: {event}")


class AlertSellerAction(RuleAction):
    def execute(self, event):
        # Mock alerting an seller
        print(f"Alerting seller for event: {event}")
