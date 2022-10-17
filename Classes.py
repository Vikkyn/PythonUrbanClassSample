class Coffee:
  def __init__(self, country: str, roast: str, taste: str, weight: int, cost: int):
    """
    Создание и подготовка к работе объекта "Кофе"
    
    :param country: Страна
    :param roast: Обжарка
    :param taste: Вкус
    :param weight: Вес
    :param cost: Стоимость
    """
    self.country = country
    self.roast = roast
    self.taste = taste
    weight = 100
    
  def get_info_coffee(self):
    """
    Функция которая выдает информацию о параметрах сорта кофе
    
    """
    ...
    
  def choose_a_coffee(self):
    """
    Функция которая помогает выбрать кофе из имеющихся в наличии  
    
    """
    #???????
    ...
    
  def calculate_price(self, weight * cost):
    """
    Функция которая рассчитывает стоимость кофе исходя из веса
    
    """
    ...
  
  if __name__ == "__main__":
    Arabica = Coffee('Kenya', 'light', 'soft', 100, 500) # инициализация экземпляра класса
 
