import bmi as bmi

# Test for Normal Weight
def test_bmi_normal_weight():
    # Test data with a BMI within the normal weight range
    bmi = 22.0  # Adjust as needed
    result = calculate_bmi(bmi)
    assert result == "Normal Weight"

# Test for Over Weight
def test_bmi_over_weight():
    # Test data with a BMI in the overweight range
    bmi = 27.5  # Adjust as needed
    result = calculate_bmi(bmi)
    assert result == "Over Weight"

# Test for Under Weight
def test_bmi_under_weight():
    # Test data with a BMI in the underweight range
    bmi = 16.0  # Adjust as needed
    result = calculate_bmi(bmi)
    assert result == "Under Weight"

