import time

import mysql.connector

start_time = time.time()
#清除租户id 106708,106703,106721,106772,106773
tenant_id = 106708
#清除共享库序号
share_db_seq = 13
#防止错误执行，真正执行需要删除
if (1 == 1):
    raise Exception('error')

# Establish database connection
conn = mysql.connector.connect(
    host='mysqlbfa17a0251a3.rds.ivolces.com',
    user='newlinkprod',
    password='jLXnbGMgQUrA$PVn',
    database='newlink_share' + str(share_db_seq)
)
cursor = conn.cursor()

# Get all tables containing 'tenant_id' column
cursor.execute("""
    SELECT table_name
    FROM information_schema.columns
    WHERE table_schema = DATABASE() AND column_name = 'tenant_id'
""")

# Fetch all table names
tables = cursor.fetchall()

# Loop through each table
for (table,) in tables:
    while True:
        # 判断当前表是否有id字段 没有就跳过
        cursor.execute(f"""
            SHOW COLUMNS FROM {table}
            WHERE Field = 'id'
        """)

        if not cursor.fetchone():
            #不存在id字段 通过tenant_id删除
            cursor.execute(f"""
                  delete FROM {table} where tenant_id = {tenant_id}
               """)
            print(f"Deleted {table} by tenant_id")
            break

        table_delete_start = time.time()
        # Select ids to delete where tenant_id != 106708 (batch of 10,000)
        cursor.execute(f"""
            SELECT id FROM {table}
            WHERE tenant_id = {tenant_id}
            LIMIT 50000
        """)
        ids_to_delete = cursor.fetchall()

        # If no rows to delete, break out of the loop
        if not ids_to_delete:
            print(f"No rows to delete in {table}")
            break

        # Prepare DELETE query for batch deletion
        ids = [str(row[0]) for row in ids_to_delete]
        ids_str = ",".join(ids)

        # Delete the selected rows in batches of 100,000
        delete_query = f"""
            DELETE FROM {table}
            WHERE id IN ({ids_str})
        """
        try:
            cursor.execute(delete_query)
            conn.commit()  # Commit the transaction

            print(f"Deleted {len(ids_to_delete)} rows from {table}")
            #打印时间取小数点后两位
            print(f"table delete Time taken: {time.time() - table_delete_start:.2f} seconds")
            #睡眠0.5s
            time.sleep(0.5)

        except Exception as e:
            print(f"Error in {table}: {e}")
            break

# Close the cursor and connection
cursor.close()
conn.close()
#输入完成，并打印时间
print(f"Time taken: {time.time() - start_time} seconds")