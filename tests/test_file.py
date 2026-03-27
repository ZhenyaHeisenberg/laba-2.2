# tests/test_task.py
import pytest
from src.models.descriptors import (
    IdDescriptor,
    DescriptionDescriptor,
    PriorityDescriptor,
    StatusDescriptor,
    CreationTimeDescriptor
)
from src.models.task import Task
from datetime import datetime
from time import sleep



def test_IdDescriptor():
    class TestClass():
        id = IdDescriptor()
    obj = TestClass()
    obj.id = "test-123"
    assert obj.id == "test-123"
    with pytest.raises(ValueError):
        obj.id = "new-id"

def test_DescriptionDescriptor():
    class TestClass():
        description = DescriptionDescriptor()
    obj = TestClass()
    obj.description = "test-description"
    assert obj.description == "test-description"
    
    obj.description = "new-test-description"
    assert obj.description == "new-test-description"

def test_PriorityDescriptor():
    class TestClass():
        priority = PriorityDescriptor()
    obj = TestClass()
    obj.priority = 1
    assert obj.priority == 1
    
    obj.priority = 3
    assert obj.priority == 3
    
    with pytest.raises(TypeError):
        obj.priority = "string"
        assert obj.priority == 3
    
    with pytest.raises(ValueError):
        obj.priority = 7
        assert obj.priority == 3

def test_StatusDescriptor():
    class TestClass():
        status = StatusDescriptor()
    obj = TestClass()
    obj.status = "В процессе"
    assert obj.status == "В процессе"
    
    obj.status = "Готово"
    assert obj.status == "Готово"

def test_CreationTimeDescriptor():
    class TestClass():
        creationTime = CreationTimeDescriptor()
    obj = TestClass()
    time = datetime.now()
    assert (time - obj.creationTime).total_seconds() < 0.01


def test_Task():
    task = Task("123456", "Описание", 5, "В процессе")
    assert task.id == "123456"
    assert task.description == "Описание"
    assert task.priority == 5
    assert task.status == "В процессе"
    assert task.is_ready == 0.0
    
    assert task.is_ready == False
    
    task.status = "ready"
    time = datetime.now()
    assert ( (time - task.creationTime).total_seconds() / 60 - task.time_in_queue ) < 0.001