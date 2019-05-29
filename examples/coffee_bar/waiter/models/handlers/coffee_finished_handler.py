#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019

import asyncio
from aiokafka import TopicPartition

from typing import Optional

# Import BaseEvent
from aioevent.models.events.event import BaseEvent
# Import BaseEventHandler
from aioevent.models.handler.event.event_handler import BaseEventHandler
# Import StoreBuilderBase
from aioevent.stores.store_builder.base import BaseStoreBuilder
# Import BaseProducer
from aioevent.services.producer.base import BaseProducer

# Import Coffee Model
from examples.coffee_bar.waiter.models.coffee import Coffee


class CoffeeFinishedHandler(BaseEventHandler):
    _store_builder: BaseStoreBuilder
    _transactional_producer: BaseProducer

    def __init__(self, store_builder: BaseStoreBuilder, transactional_producer: BaseProducer, **kwargs):
        super().__init__(**kwargs)
        self._store_builder = store_builder
        self._transactional_producer = transactional_producer

    async def handle(self, event: BaseEvent, tp: TopicPartition, group_id: str, offset: int) -> Optional[str]:
        if not self._transactional_producer.is_running():
            await self._transactional_producer.start_producer()

        async with self._transactional_producer.init_transaction():
            # Creates commit_offsets dict
            commit_offsets = {tp: offset + 1}

            # Gets coffee in local store
            coffee = Coffee.__from_dict_bytes__(await self._store_builder.get_from_local_store(event.uuid))

            # Updates coffee
            coffee.set_state('awaiting')
            coffee.set_context(event.context)

            # Sets coffee in local store
            await self._store_builder.set_from_local_store(event.uuid, coffee.__to_bytes_dict__())

            # End transaction
            await self._transactional_producer.end_transaction(commit_offsets, group_id)
        # TODO raise an exception
        return 'transaction'

    @classmethod
    def handler_name(cls) -> str:
        return 'aioevent.bartender.event.CoffeeFinished'
