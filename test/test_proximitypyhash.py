import proximitypyhash


def test_in_circle_check_true():
    expected = True
    output = proximitypyhash.in_circle_check(12, 77, 12.1, 77, 100)
    assert output == expected


def test_in_circle_check_false():
    expected = True
    output = proximitypyhash.in_circle_check(12, 77, 23, 87, 100)
    assert output == expected


def test_get_centroid():
    expected = (15, 15)
    output = proximitypyhash.get_centroid(10, 10, 10, 10)
    assert output == expected


def test_convert_to_latlon():
    expected = (12.008993216059187, 77.0091941298557)
    output = proximitypyhash.convert_to_latlon(1000.0, 1000.0, 12.0, 77.0)
    assert output == expected


def test_create_geohash():
    expected = 'tdnu20t9,tdnu20t8,tdnu20t3,tdnu20t2,tdnu20mz,tdnu20mx,tdnu20tc,tdnu20tb,tdnu20td,tdnu20tf'
    expected = expected.split(',')
    output = proximitypyhash.get_geohash_radius_approximation(latitude=12.0,
                                                              longitude=77.0,
                                                              radius=20.0,
                                                              precision=8,
                                                              georaptor_flag=False,
                                                              minlevel=1,
                                                              maxlevel=12)

    assert set(output) == set(expected)
