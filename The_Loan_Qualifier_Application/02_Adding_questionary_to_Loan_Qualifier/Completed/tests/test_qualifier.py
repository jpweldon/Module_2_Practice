
# Import Calculators
from qualifier.utils import calculators

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

