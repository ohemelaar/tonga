#!/usr/bin/env python
# coding: utf-8
# Copyright (c) Qotto, 2019

import os
import pytest
import uvloop
from kafka import KafkaAdminClient
from kafka.client import KafkaClient
from kafka.cluster import ClusterMetadata

# Serializer
from tonga.services.serializer.avro import AvroSerializer

# Stores import
from tonga.stores.local.memory import LocalStoreMemory
from tonga.stores.globall.memory import GlobalStoreMemory

# StoreBuilder import
from tonga.stores.store_builder.store_builder import StoreBuilder

# StoreRecord import
from tonga.models.store_record.store_record import StoreRecord
from tonga.models.store_record.store_record_handler import StoreRecordHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

t_loop = uvloop.new_event_loop()

# Store test
test_local_memory_store = LocalStoreMemory(name='local_store_memory_test')
test_global_memory_store = GlobalStoreMemory(name='global_store_memory_test')

# Avro Serializer test
test_serializer = AvroSerializer(BASE_DIR + '/misc/schemas')
test_serializer_local_memory_store = LocalStoreMemory(name='local_store_memory_serializer_test')
test_serializer_global_memory_store = GlobalStoreMemory(name='global_store_memory_serializer_test')

# StatefulsetPartitionAssignor test
assignor_kafka_client = KafkaClient(bootstrap_servers='localhost:9092', client_id='test_client')
assignor_cluster_metadata = ClusterMetadata(bootstrap_servers='localhost:9092')

# StoreBuilder test
store_builder_serializer = AvroSerializer(BASE_DIR + '/misc/schemas')

admin_client = KafkaAdminClient(bootstrap_servers='localhost:9092', client_id='test_store_builder')
cluster_metadata = ClusterMetadata(bootstrap_servers='localhost:9092')
test_store_builder_local_memory_store = LocalStoreMemory(name='test_store_builder_local_memory_store')
test_store_builder_global_memory_store = GlobalStoreMemory(name='test_store_builder_global_memory_store')
test_store_builder = StoreBuilder('test_store_builder', 0, 1, 'test-store', store_builder_serializer,
                                  test_store_builder_local_memory_store, test_store_builder_global_memory_store,
                                  'localhost:9092', cluster_metadata, admin_client, t_loop, False, False)
store_record_handler = StoreRecordHandler(test_store_builder)
store_builder_serializer.register_event_handler_store_record(StoreRecord, store_record_handler)


@pytest.yield_fixture()
def event_loop():
    loop = t_loop
    yield loop


@pytest.fixture
def get_local_memory_store_connection():
    return test_local_memory_store


@pytest.fixture
def get_global_memory_store_connection():
    return test_global_memory_store


@pytest.fixture
def get_avro_serializer():
    return test_serializer


@pytest.fixture
def get_avro_serializer_store():
    return test_serializer_local_memory_store, test_serializer_global_memory_store


@pytest.fixture
def get_assignor_kafka_client():
    return assignor_kafka_client


@pytest.fixture
def get_assignor_cluster_metadata():
    return assignor_cluster_metadata


@pytest.fixture
def get_store_builder():
    return test_store_builder
