"""
  This module supplies the `DBStorage` class
"""

import aiomysql
from engine.sql_queries import MySQLQuery

query = MySQLQuery()

class DBStorage:
  """
    Interacts with MySQL using aiomysql
  """
  async def connect(self):
    """
      Connect to database
    """
    credentials = {
      'host': 'mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com',
      'user': 'bsale_test',
      'password': 'bsale_test',
      'db': 'bsale_test',
      'port': 3306
    }
    self.__conn = await aiomysql.connect(**credentials)
    self.__cur = await self.__conn.cursor(aiomysql.DictCursor)

  async def all(self, table):
    """
      Get all records of specified table
        Args:
          table(str): table name
    
        Return: List of records(dicts) of specified table
    """
    await self.connect()

    await self.__cur.execute(query.select_all(table))
    result = await self.__cur.fetchall()
    await self.close()

    return result

  async def get(self, table, id):
    """
      Get a table record according its id
      Args:
        table(str): table name
        id(int): record id

      Return: record(dictionary)
    """
    await self.connect()

    await self.__cur.execute(query.select_by_id(table), (id,))
    result = await self.__cur.fetchone()
    await self.close()

    return result

  async def find(self, table, match):
    """
      Find a table match according match
      Args:
        table(str): table name
        match(str): coincidence

      Return: record(dictionary)
    """
    await self.connect()

    await self.__cur.execute(query.select_match(table, match))
    result = await self.__cur.fetchall()
    await self.close()

    return result

  async def close(self):
    """
      Close cursor and connection
    """
    await self.__cur.close()
    self.__conn.close()
  