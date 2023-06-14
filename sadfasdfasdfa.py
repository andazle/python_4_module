def del_user_by_id(cursor, id):
    command = """
    DELETE FROM USERS WHERE id = 2 LIMIT 1;
    """
    result = cursor.exelute(command, (id,)).fetchall()
    print(result)