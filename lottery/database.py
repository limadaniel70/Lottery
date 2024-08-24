import sqlite3
from multipledispatch import dispatch

class DataBase:

    def __init__(self, database_name: str) -> None:
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def add_player(self, player_name: str) -> None:
        pass

    def add_players(self, players: list[str]) -> None:
        pass

    def get_player(self) -> str:
        pass

    def get_all_players(self) -> list[str]:
        pass
        
    def remove_player(self, player_name: str) -> tuple[int, str]:
        pass

    @dispatch(list[str])
    def remove_players(self, players: list[str]) -> dict[int, str]:
        pass

    @dispatch(*str)
    def remove_players(self, *players: str) -> dict[int, str]:
        pass

    # def execute_custom_query(self, query: str) -> list[any]:
    #    result = self.cursor.execute(query)
    #    return result.fetchall()

    def commit_changes(self) -> None:
        self.connection.commit()

    def close_connection(self) -> None:
        self.connection.close
