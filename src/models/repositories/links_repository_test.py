import pytest
import uuid

from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import LinksRepository

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
link_id = str(uuid.uuid4())

@pytest.mark.skip(reason="interacao com a base de dados")
def test_registry_link():
    conn= db_connection_handler.get_connection()
    linksRepository = LinksRepository(conn)

    link_trips_infos = {
        "id": link_id,
        "trip_id":trip_id,
        "link": "olaMundo@gmail.com",
        "title": "Mundo"
    }
    
    linksRepository.registry_link(link_trips_infos)

@pytest.mark.skip(reason="interacao com a base de dados")
def test_find_link_from_trip():
    conn= db_connection_handler.get_connection()
    linksRepository = LinksRepository(conn)

    response = linksRepository.find_link_from_trip(trip_id)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)