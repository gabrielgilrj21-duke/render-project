def get_age_group(age):
    """
    Retorna a faixa etária com base na idade em anos dentro do intervalo 0..150,
    caso contrário, retorna 'desconhecido'.
    """

    if age < 0 or age > 150:
        return 'desconhecido'
    elif age <= 14:
        return 'crianças'
    elif age <= 24:
        return 'jovens'
    elif age <= 64:
        return 'adultos'
    elif age <= 80:
        return 'idosos'
    else:
        return 'desconhecido'


def test_get_age_group():
    """teste de unidade para get_age_group"""

    assert get_age_group(-1) == 'desconhecido'
    assert get_age_group(0) == 'crianças'
    assert get_age_group(14) == 'crianças'
    assert get_age_group(15) == 'jovens'
    assert get_age_group(24) == 'jovens'
    assert get_age_group(25) == 'adultos'
    assert get_age_group(64) == 'adultos'
    assert get_age_group(65) == 'idosos'
    assert get_age_group(80) == 'idosos'
    assert get_age_group(150) == 'desconhecido'
