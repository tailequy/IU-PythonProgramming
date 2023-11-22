#create an “actor” table with the columns id, first_name,
#last_name, age, date_of_birth, and active
#conda install pymysql
#conda install sqlalchemy
#Create a schema movie in mySQL
import sqlalchemy
import pymysql
import sqlalchemy as db
def main():
    # get sqlalchemy and pymysql used libraries version
    print("sqlalchemy: {}".format(sqlalchemy.__version__))
    print("pymysql: {}".format(pymysql.__version__))
    # get engine object using pymysql driver for mysql
    engine = db.create_engine("mysql+pymysql://root:168098205@localhost:3306/movie")
    # get connection object
    connection = engine.connect()
    # get meta data object
    meta_data = db.MetaData()
    # set actor creation script table
    actor = db.Table(
        "actor", meta_data,
        db.Column("id", db.Integer, primary_key=True, autoincrement=True,nullable=False),
        db.Column("first_name", db.String(50), nullable=False),
        db.Column("last_name", db.String(50), nullable=False),
        db.Column("age", db.Integer, nullable=False),
        db.Column("date_of_birth", db.Date, nullable=False),
        db.Column("active", db.Boolean, nullable=False))
    # create actor table and stores the information in metadata
    meta_data.create_all(engine)
if __name__ == '__main__':
    main()