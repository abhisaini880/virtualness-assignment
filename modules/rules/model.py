from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db_connector import Base


class Rule(Base):
    __tablename__ = "rules"
    rule_id = Column(Integer, primary_key=True)
    rule_name = Column(String)
    description = Column(String)
    message = Column(String)
    action_type = Column(String)
    conditions = relationship("Condition", back_populates="rule")


class Condition(Base):
    __tablename__ = "conditions"
    condition_id = Column(Integer, primary_key=True)
    rule_id = Column(Integer, ForeignKey("rules.rule_id"))
    field = Column(String)
    operator = Column(String)
    value = Column(String)
    rule = relationship("Rule", back_populates="conditions")


def get_all_rules():
    # uncomment this, if rules data is stored in db
    # return db_session.query(Rule).all()

    # using Sample data for project
    # Assuming data is fetched from database
    return [
        {
            "rule_id": 1,
            "rule_name": "First NFT Purchase Notification",
            "description": "Trigger a push notification on the very first NFT purchase for the user",
            "message": "Congrats! on your very first purchase.",
            "action_type": "push_notification",
        },
        {
            "rule_id": 2,
            "rule_name": "NFT Sale Alert",
            "description": "Alert NFT seller if their NFTs are not sold after 7 days of listing them for sale",
            "message": "NFT was viewed but not sold yet!",
            "action_type": "alert_seller",
        },
        {
            "rule_id": 3,
            "rule_name": "Bulk Purchase Alert",
            "description": "Alert operator if more than 100 NFTs are purchased by a user within an hour",
            "message": "Someone purchased more than 100 NFTs in an hour",
            "action_type": "alert_operator",
        },
    ]


def get_conditions_for_rule(rule_id):
    # uncomment this, if rules data is stored in db
    # return db_session.query(Condition).filter(Condition.rule_id == rule_id).all()

    # using Sample data for project
    # Assuming data is fetched from database
    conditions = {
        1: [
            {
                "condition_id": 1,
                "rule_id": 1,
                "field": "verb",
                "operator": "equals",
                "value": "purchase",
            },
            {
                "condition_id": 2,
                "rule_id": 1,
                "field": "noun",
                "operator": "equals",
                "value": "nft",
            },
            {
                "condition_id": 3,
                "rule_id": 1,
                "field": "purchase_count",
                "operator": "equals",
                "value": "1",
            },
        ],
        2: [
            {
                "condition_id": 4,
                "rule_id": 2,
                "field": "verb",
                "operator": "equals",
                "value": "list_for_sale",
            },
            {
                "condition_id": 5,
                "rule_id": 2,
                "field": "days_unsold",
                "operator": "greater_than_or_equal",
                "value": "7",
            },
        ],
        3: [
            {
                "condition_id": 6,
                "rule_id": 3,
                "field": "verb",
                "operator": "equals",
                "value": "purchase",
            },
            {
                "condition_id": 7,
                "rule_id": 3,
                "field": "noun",
                "operator": "equals",
                "value": "nft",
            },
            {
                "condition_id": 8,
                "rule_id": 3,
                "field": "quantity",
                "operator": "greater_than",
                "value": "100",
            },
            {
                "condition_id": 9,
                "rule_id": 3,
                "field": "time_frame",
                "operator": "less_than",
                "value": "3600",
            },
        ],
    }

    return conditions[rule_id]
