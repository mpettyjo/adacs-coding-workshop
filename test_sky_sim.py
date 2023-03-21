import numpy.testing as testing

def test_module_import():
    try:
        import mymodule.sky_sim
    except Exception as e:
        raise AssertionError("Failed to import module")
    return

def test_get_radec_return():
    import mymodule.sky_sim as sky_sim
    ra, dec = sky_sim.get_radec()
    if testing.assert_allclose((ra, dec), (14.215420962967535, 41.26916666666667)):
        raise AssertionError("get_radec returns wrong (ra,dec)=({ra},{dec}), expected (14.215420962967535, 41.26916666666667)") 
    return

def test_check_ra_dec_floats():
    import mymodule.sky_sim as sky_sim
    ra, dec = sky_sim.get_radec()
    if  (not isinstance(ra, float)) & (not isinstance(dec, float)):
        raise AssertionError("(ra,dec)=({ra},{dec}) are not floats")
    elif not isinstance(ra, float):
        raise AssertionError("ra={ra} is not a float")
    elif not isinstance(dec, float):
        raise AssertionError("dec={dec} is not a float")
    return

def test_ras_decs_length_equal_to_NUM_STARS():
    import mymodule.sky_sim as sky_sim
    ra, dec = sky_sim.get_radec()
    NUM_STARS = 1_000_000
    ras, decs = sky_sim.make_stars(ra, dec, NUM_STARS)

    if (len(ras) != NUM_STARS) & (len(decs) != NUM_STARS):
        raise AssertionError("Output length not equal to {NUM_STARS}")
    return