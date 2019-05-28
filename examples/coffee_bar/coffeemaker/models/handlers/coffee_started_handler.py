#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019

from aiokafka import TopicPartition

from typing import Optional

# Import BaseEvent
from aioevent.models.events.event import BaseEvent
# Import BaseEventHandler
from aioevent.models.handler.event.event_handler import BaseEventHandler


class CoffeeStartedHandler(BaseEventHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    async def handle(self, event: BaseEvent, tp: TopicPartition, group_id: str, offset: int) -> Optional[str]:
        pass

    @classmethod
    def handler_name(cls) -> str:
        return 'aioevent.coffeemaker.event.CoffeeStarted'
