#Delete Data
#The code example will remove the “John Smith” record from the “actor” table.

import sqlalchemy as db
def main():
    # get engine object using pymysql driver for mysql
    engine = db.create_engine("mysql+pymysql://root:168098205@localhost:3306/movie")
    meta_data = db.MetaData()
    # get connection object
    connection = engine.connect()
    # get actor table definition
    actor_table = db.Table("actor", meta_data, autoload=True,autoload_with=engine)
    # set delete sql statement. delete the record where id is equal to 1
    sql_query = db.delete(actor_table).where(actor_table.columns.id == 2)
    results = connection.execute(sql_query)
if __name__ == '__main__':
   main()