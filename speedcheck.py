from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import config
import models
import speedtest
import datetime
from icmplib import ping
import os

engine = create_engine(config.DATABASE_URI)
Session = sessionmaker(bind=engine)

def first_run():
    models.Base.metadata.create_all(engine)


def run_speedtest():
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    res = s.results.dict()
    return res["download"], res["upload"], res["ping"]

def run_pingtest():
    return ping(address='1.1.1.1', count=60, interval=1, timeout=2, privileged=False)


def record_data():
    r_speed = run_speedtest()
    r_ping = run_pingtest()

    r_ploss = False

    s = Session()

    if r_ping.packet_loss == 0.1:
        r_ploss = True

    q_speed = models.Speedtest(
        timestamp = datetime.datetime.now(),
        upload = r_speed[0],
        download = r_speed[1],
        ping = r_speed[2]
    )

    q_ping = models.Ping(
        timestamp = datetime.datetime.now(),
        ip = r_ping.address,
        rtt_min = r_ping.min_rtt,
        rtt_avg = r_ping.avg_rtt,
        rtt_max = r_ping.max_rtt,
        sent = r_ping.packets_sent,
        received = r_ping.packets_received,
        packet_loss = r_ploss
    )

    s.add(q_speed)
    s.add(q_ping)
    s.commit()
    s.close()

def main():
    if os.getenv('ST_DBCREATE') == "TRUE":
        first_run()
    else:
        record_data()
    
if __name__ == '__main__':
    main()