
#http://alpopkes.com/posts/2018/07/coding-challenge-day-1/
class CastleKilmereMember:
    """
    Creates a member of the Castle Kilmere School of Magic
    """

    def __init__(self, name, birthyear, sex):
        self._name = name
        self.birthyear = birthyear
        self.sex = sex

    def says(self, words):
        return f"{self._name} says {words}"


bromley = CastleKilmereMember('Bromley Huckabee', '1959', 'male')
print(bromley.says("Hello!"))
