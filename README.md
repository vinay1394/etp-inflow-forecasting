1. *Problem statement:* Forecast actual hourly wastewater inflow to Melbourne Water's Eastern Treatment Plant.

2. *Consumption forecasting:* Estimate historical ETP catchment consumption from Melbourne daily water use using provisional α = 0.402, then forecast consumption.

3. *Inflow forecasting:* Use historical ETP inflow, estimated/forecast consumption, rainfall and temperature to predict future hourly inflow.

4. *Engineering stack:* Python, uv, pytest, Ruff, MLflow, FastAPI, GitHub Actions and Docker.

5. *Data limitations:* Catchment consumption is estimated, not measured; actual dataset date overlap and allocation assumptions still require validation.