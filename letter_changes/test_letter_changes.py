from letter_changes.letter_changes import LetterChanges


def test_letter_changes_nick():
    assert LetterChanges('nick*6') == 'Ojdl*6'


def test_letter_changes_arthur():
    assert LetterChanges('arthur lopes!') == 'bsUIvs mpqft!'
