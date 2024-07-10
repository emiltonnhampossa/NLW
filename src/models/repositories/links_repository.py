from typing import Dict, Tuple,List
from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def registry_link(self, trips_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO links
                    (id, trip_id,link,title)
                VALUES
                    (?, ?, ?,?)
            ''', (
                trips_infos["id"],
                trips_infos["trip_id"],
                trips_infos["link"],
                trips_infos["title"],
            )
        )
        self.__conn.commit()
    
    def find_link_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                SELECT * FROM links WHERE trip_id = ?
            ''',(trip_id,)
        )
        trip = cursor.fetchall()
        return trip


   