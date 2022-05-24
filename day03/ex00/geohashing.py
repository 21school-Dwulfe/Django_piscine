import sys
from antigravity import geohash

def main():
    if len(sys.argv) != 4:
        print("Please enter strictly longitude, latitude, YYYY-MM-DD-Dow Jones index daily price open")
        exit(1)
    longitude = float(sys.argv[1])
    latitude = float(sys.argv[2])
    date_dow_op = sys.argv[3]
    if latitude < -90.0 or latitude > 90.0 or longitude < -180.0 or longitude > 180.0:
        print("Are you realy form the Earth? 'Latitude range (-90.0, 90.0)' \
'Longitude range (-180, 180)'")
        exit(1)
    geohash(longitude, latitude, date_dow_op.encode())

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        with sys.stderr as cerr:
            print(e, file=cerr)



