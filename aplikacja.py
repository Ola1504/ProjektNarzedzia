import pytest

def powitanie(imie):
  return f"Czesc, {imie}!"

class TestPowitanie(pytest.TestCase):

  def test_powitanie(self):
    self.assertEqual(powitanie("Jan"), "Czesc, Jan!")
    self.assertEqual(powitanie("Amelia"), "Czesc, Amelia!")
    self.assertEqual(powitanie("Krzysiu"), "Czesc, Krzysiu!")

if __name__ == '__main__':
  pytest.main()
  
