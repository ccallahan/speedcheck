from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, String, Float, Boolean
from sqlalchemy.dialects import postgresql

Base = declarative_base()

class Speedtest(Base):
    __tablename__ = 'speedtest'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    upload = Column(Float)
    download = Column(Float)
    ping = Column(Float)
    
    def __repr__(self):
        return "<Speedtest(timestamp={}, upload={}, download={}, ping={})>"\
                .format(self.timestamp, self.upload, self.download, self.ping)


class Ping(Base):
    __tablename__ = 'ping'
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    ip = Column(postgresql.INET)
    rtt_min = Column(Float)
    rtt_avg = Column(Float)
    rtt_max = Column(Float)
    sent = Column(Integer)
    received = Column(Integer)
    packet_loss = Column(Float)

    def __repr__(self):
        return "<Ping(timestamp={}, ip='{}', rtr_min={}, rtr_avg={}, rtr_max={}, sent={}, received={}, packet_loss={}>"\
            .format(self.timestamp, self.ip, self.rtr_min, self.rtr_avg, self.rtr_max, self.sent, self.received, self.packet_loss)
