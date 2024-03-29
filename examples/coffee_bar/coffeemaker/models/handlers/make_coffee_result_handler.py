#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019

from aiokafka import TopicPartition

# Import BaseCommandHandler
from tonga.models.handlers.result.result_handler import BaseResultHandler
# Import BaseCommand
from tonga.models.events.result.result import BaseResult

from typing import Union


class MakeCoffeeResultHandler(BaseResultHandler):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    async def on_result(self, result: BaseResult, tp: TopicPartition, group_id: str, offset: int) -> Union[str, None]:
        pass

    @classmethod
    def handler_name(cls) -> str:
        return 'tonga.coffeemaker.result.MakeCoffeeResult'
