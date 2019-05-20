#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019

from aiokafka import TopicPartition

from typing import Dict

from aioevent.services.stores.base import BaseStores, BaseStoreMetaData

__all_ = [
    'BaseLocalStore',
]


class BaseLocalStore(BaseStores):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, key: str) -> bytes:
        raise NotImplementedError

    def set(self, key: str, value: bytes) -> None:
        raise NotImplementedError

    def delete(self, key: str) -> None:
        raise NotImplementedError

    def get_all(self) -> Dict[str, bytes]:
        raise NotImplementedError

    def set_metadata(self, metadata: BaseStoreMetaData) -> None:
        raise NotImplementedError

    def update_metadata_tp_offset(self, tp: TopicPartition, offset: int) -> None:
        raise NotImplementedError

    def get_metadata(self) -> BaseStoreMetaData:
        raise NotImplementedError

    def _update_metadata(self) -> None:
        raise NotImplementedError
