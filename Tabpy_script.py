import numpy as np
from sklearn.linear_model import LinearRegression


def predict_renewables(years, total_renewables):
    """
    This function executing Linear Regression to predict
    renewable energy trends
    """

    # Use reshaping to get the exact year value without aggregation bias
    x = np.array(years).astype(float).reshape(-1, 1)
    y = np.array(total_renewables).astype(float)

    # Mask only valid historical points (remove NaNs or Infs)
    mask = np.isfinite(y)

    # If data exists (at least 2 points), force the model to calculate
    if np.sum(mask) >= 2:
        model = LinearRegression().fit(x[mask], y[mask])
        return model.predict(x).tolist()
    else:
        # Return zeros if insufficient data points exist
        return [0.0] * len(y)


# Example usage for local testing
if __name__ == "__main__":
    # Mock data for testing
    test_years = [2010, 2011, 2012, 2013, 2014]
    test_data = [100, 120, 150, 170, 200]
    print(predict_renewables(test_years, test_data))