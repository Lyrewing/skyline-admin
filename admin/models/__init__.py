from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

__ConnectionStr = 'mysql+pymysql://root:123456@192.168.33.10:3306/admin'

Base = declarative_base()


def init_db():
    """
    根据类创建数据库表
    :return:
    """
    engine = create_engine(
        __ConnectionStr,
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.create_all(engine)
    return engine


def drop_db():
    """
    根据类删除数据库表
    :return:
    """
    engine = create_engine(
        __ConnectionStr,
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=5,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
    )

    Base.metadata.drop_all(engine)


engine = init_db()
Session = sessionmaker(bind=engine)
