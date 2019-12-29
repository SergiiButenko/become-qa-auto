def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_dict():    
    f1 = dict(name='serbut', desc='desc')
    f2 = dict(name='sebut', desc='desc')
    assert f1 == f2