import pygeohash as pgh
import georaptor
import math
import time
import argparse
from clint.textui import puts, indent, colored


def in_circle_check(latitude, longitude, centre_lat, centre_lon, radius):
    """
    Check if given latitude and longitude are within the circle
    :param latitude: to be checked latitude
    :param longitude: to be checked longitude
    :param centre_lat: The latitude of the centroid
    :param centre_lon: The longtiude of the centroid
    :param radius: Desired radius in meters
    :return:
    """
    x_diff = longitude - centre_lon
    y_diff = latitude - centre_lat

    if (math.pow(x_diff, 2) + math.pow(y_diff, 2) <= math.pow(radius, 2)):
        return True

    return False


def get_centroid(latitude, longitude, height, width):
    """
    Get the centroid of a bounding box
    :param latitude:
    :param longitude:
    :param height:
    :param width:
    :return: tuple containing the centroid
    """
    y_cen = latitude + (height / 2)
    x_cen = longitude + (width / 2)

    return (x_cen, y_cen)


def convert_to_latlon(y, x, latitude, longitude):
    """
    Convert the latitude and longitude relative to the centroid
    :param y: y of the centroid
    :param x: x of the centroid
    :param latitude:
    :param longitude:
    :return:
    """
    pi = math.pi

    r_earth = 6371000

    lat_diff = (y / r_earth) * (180 / pi)
    lon_diff = (x / r_earth) * (180 / pi) / math.cos(latitude * pi / 180)

    final_lat = latitude + lat_diff
    final_lon = longitude + lon_diff

    return (final_lat, final_lon)


def get_geohash_radius_approximation(latitude, longitude, radius, precision, georaptor_flag=False, minlevel=1, maxlevel=12):
    """
    Get the list of geohashed that approximate a circle
    :param latitude: Float the longitude to get the radius approximation for
    :param longitude: Float  the latitude to get the radius approximation for
    :param radius:  Integer Radius coverage in meters
    :param precision: Integer the geohash precision level
    :param georaptor_flag: Do you want to compress it with georaptor
    :param minlevel: minimal precision level possible
    :param maxlevel: maximal precision level possible
    :return: A list of geohashes
    """

    x = 0.0
    y = 0.0

    points = []
    geohashes = []

    grid_width = [5009400.0, 1252300.0, 156500.0, 39100.0, 4900.0, 1200.0, 152.9, 38.2, 4.8, 1.2, 0.149, 0.0370]
    grid_height = [4992600.0, 624100.0, 156000.0, 19500.0, 4900.0, 609.4, 152.4, 19.0, 4.8, 0.595, 0.149, 0.0199]

    height = (grid_height[precision - 1]) / 2
    width = (grid_width[precision - 1]) / 2

    lat_moves = int(math.ceil(radius / height))  # 4
    lon_moves = int(math.ceil(radius / width))  # 2

    for i in range(0, lat_moves):

        temp_lat = y + height * i

        for j in range(0, lon_moves):

            temp_lon = x + width * j

            if in_circle_check(temp_lat, temp_lon, y, x, radius):
                x_cen, y_cen = get_centroid(temp_lat, temp_lon, height, width)

                lat, lon = convert_to_latlon(y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]
                lat, lon = convert_to_latlon(-y_cen, -x_cen, latitude, longitude)
                points += [[lat, lon]]

    for point in points:
        geohashes += [pgh.encode(point[0], point[1], precision)]

    if georaptor_flag:
        georaptor_out = georaptor.compress(set(geohashes), int(minlevel), int(maxlevel))
        return list(georaptor_out)

    else:
        return list(set(geohashes))


def main():
    start_time = time.time()
    georaptor_flag = False
    minlevel = 1
    maxlevel = 12

    # Fetch input arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('latitude', help='latitude of the center point')
    parser.add_argument('longitude', help='longitude of the center point')
    parser.add_argument('radius', help='radius of coverage in metres')
    parser.add_argument('precision_level', help='geohash precision level')
    parser.add_argument('--georaptor', default=False,
                        help='georaptor flag to compress the output (default: false)')
    parser.add_argument('--minlevel', default=1,
                        help='minimum level of geohash if georaptor set to true(default: 1)')
    parser.add_argument('--maxlevel', default=12,
                        help='maximum level of geohash if georaptor set to true(default: 12)')

    args = parser.parse_args()

    latitude = args.latitude
    longitude = args.longitude
    radius = args.radius
    precision_level = args.precision_level

    if 'georaptor' in args:
        georaptor_flag = args.georaptor

    if 'minlevel' in args:
        minlevel = args.minlevel

    if 'maxlevel' in args:
        maxlevel = args.maxlevel

    puts(colored.green('\nGenerating geohashes for\n'))

    puts(colored.red('latitude: ' + latitude))
    puts(colored.red('longitude: ' + longitude))
    puts(colored.red('radius: ' + radius))
    puts(colored.red('precision_level: ' + precision_level))

    if georaptor_flag:
        puts(colored.red('georaptor: ' + str(georaptor_flag)))
        puts(colored.red('minlevel: ' + str(minlevel)))
        puts(colored.red('maxlevel: ' + str(maxlevel)))

    puts('\n')
    puts(colored.red('Output:'))

    print(get_geohash_radius_approximation(float(latitude), float(longitude), float(radius), int(precision_level), georaptor_flag,
                                           int(minlevel), int(maxlevel)))

    et = time.time() - start_time

    puts(colored.green('\nTotal execution time: ' + str(et) + ' seconds\n'))
