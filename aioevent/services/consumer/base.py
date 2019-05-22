#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019


from typing import List, Dict


__all__ = [
    'BaseConsumer',
]


class BaseConsumer:
    def __init__(self) -> None:
        pass

    async def start_consumer(self) -> None:
        raise NotImplementedError

    async def stop_consumer(self) -> None:
        raise NotImplementedError

    def is_running(self) -> bool:
        raise NotImplementedError

    async def listen_event(self, mod: str = 'latest') -> None:
        raise NotImplementedError

    async def listen_state_builder(self, rebuild: bool = False) -> None:
        raise NotImplementedError

    async def get_many(self, partitions: List[int] = None, max_records: int = None):
        raise NotImplementedError

    async def get_one(self, partitions: List[int] = None):
        raise NotImplementedError
