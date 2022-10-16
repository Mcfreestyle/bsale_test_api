"""
  This module supplies the `MySQLQuery` class
"""

class MySQLQuery:
  """
    Queries to export and use in the engine
  """
  @staticmethod
  def select_all(table):
    """
      Query to select all records from given table
        Args:
          table(str): table name

        Return: Query(str)
    """
    return 'SELECT * FROM {}'.format(table)

  @staticmethod
  def select_by_id(table):
    """
      Query to select a record by id
      Args:
        table(str): table name
        id(int): record id

      Return: Query(str)
    """
    return 'SELECT * FROM {} WHERE id=%s'.format(table)

  @staticmethod
  def select_match(table, match):
    """
      Query to search a record according match
      Args:
        table(str): table name
        match(str): coincidence

      Return: Query(str)
    """
    return 'SELECT * FROM {} WHERE name LIKE "%{}%"'.format(table, match)
