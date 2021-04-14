import geom_analysis as ga

def test_calculate_distance():
    coord1 = [0, 0, 0]
    coord2 = [1, 0, 0]
    expected = 1.0
    observed = ga.calculate_distance(coord1, coord2)
    assert observed == expected

def test_bond_check():
    atom_distance = 1.5
    expected = True
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test1_bond_check():
    atom_distance = 0
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test2_bond_check():
    atom_distance = 1.6 
    expected = False
    observed = ga.bond_check(atom_distance)
    assert observed == expected

def test_open_xyz():
    with pytest.raises(ValueError)
        ga.open_xyz(hello.txt)
