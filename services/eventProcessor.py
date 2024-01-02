from modules.rules.controller import (
    PushNotificationAction,
    AlertOperatorAction,
    AlertSellerAction,
)
from modules.rules.model import get_all_rules, get_conditions_for_rule


def load_rules():
    rules = get_all_rules()
    actions = {
        "push_notification": PushNotificationAction(),
        "alert_operator": AlertOperatorAction(),
        "alert_seller": AlertSellerAction(),
    }
    return [(rule, actions[rule.get("action_type")]) for rule in rules]


def check_condition(event, condition):
    # Implement the logic to check if the event satisfies the condition
    # Need to check the historical data
    # Returning True if verb is buy and noun is nft just to run the case
    return (
        True
        if condition.get("rule_id") == 1 and event.get("verb") == "buy"
        else False
    )


def process_event(event):
    rules = load_rules()
    for rule, action in rules:
        conditions = get_conditions_for_rule(rule.get("rule_id"))
        if all(check_condition(event, cond) for cond in conditions):
            action.execute(rule.get("message"))
