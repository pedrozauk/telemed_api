from sqlmodel import create_engine, Session, SQLModel



engine = create_engine('sqlite:///test.db')



def create_all_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_all_tables()
