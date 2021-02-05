from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, and_, Boolean, null
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config_keys import owner_db, db_name, db_password

engine = create_engine(f"postgresql+psycopg2://{owner_db}:{db_password}@localhost:5432/{db_name}")

Session = sessionmaker(bind=engine)

BASE = declarative_base()


class Gender(BASE):
    __tablename__ = "user_gender"

    ID = Column(Integer, primary_key=True)
    title = Column(String(20))


class County(BASE):
    __tablename__ = "user_country"

    ID = Column(Integer, primary_key=True)
    name = Column(String(50))


class Town(BASE):
    __tablename__ = "user_town"

    ID = Column(Integer, primary_key=True)
    name = Column(String)


class Status(BASE):
    __tablename__ = "user_status"

    ID = Column(Integer, primary_key=True)
    name = Column(String)


class AllVkUsers(BASE):
    __tablename__ = "all_vk_users"

    vk_id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    gender_id = Column(Integer, ForeignKey("user_gender.ID"))
    country_id = Column(Integer, ForeignKey("user_country.ID"))
    town_id = Column(Integer, ForeignKey("user_country.ID"))
    status_id = Column(Integer, ForeignKey("user_status.ID"))
    is_bot_user = Column(Boolean, default=False)


class SearchParams(BASE):
    __tablename__ = "search_params"

    ID = Column(Integer, primary_key=True)
    search_owner_id = Column(Integer, ForeignKey("all_vk_users.vk_id"))
    age_from = Column(Integer)
    age_to = Column(Integer)
    status = Column(Integer, ForeignKey("user_status.ID"))
    town = Column(Integer, ForeignKey("user_town.ID"))
    country = Column(Integer, ForeignKey("user_country.ID"))
    gender = Column(Integer, ForeignKey("user_gender.ID"))


class SearchUsers(BASE):
    __tablename__ = "search_users"

    ID = Column(Integer, primary_key=True)
    search_params_id = Column(Integer, ForeignKey("search_params.ID"))
    found_result_vk_id = Column(Integer, ForeignKey("all_vk_users.vk_id"))
    is_shown = Column(Boolean, default=False)
    liked_status = Column(Boolean, default=null)


# def insert_into_gender():
#     gender_woman = Gender(ID=1, title="woman")
#     gender_man = Gender(ID=2, title="man")
#     gender_any = Gender(ID=3, title="any")
#     session.add_all([gender_woman, gender_man, gender_any])
#     session.commit()


# def insert_into_status():
#     status_1 = Status(ID=1, name="не женат(не за мужем)")
#     status_2 = Status(ID=2, name="встречается")
#     status_3 = Status(ID=3, name="помолвлен(-а)")
#     status_4 = Status(ID=4, name="женат(за мужем)")
#     status_5 = Status(ID=5, name="всё сложно")
#     status_6 = Status(ID=6, name="в активном поиске")
#     status_7 = Status(ID=7, name="влюблен(-а)")
#     status_8 = Status(ID=8, name="в гражданском браке")
#     session.add_all([status_1, status_2, status_3, status_4, status_5, status_6, status_7, status_8])
#     session.commit()


if __name__ == "__main__":
    session = Session()
    # BASE.metadata.create_all(engine)
    # insert_into_gender()
    # insert_into_status()