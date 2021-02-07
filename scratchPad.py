import numpy as np
import xarray as xr
data = xr.DataArray(np.random.randn(2, 3), dims=("x", "y"), coords={"x": [10, 20]})
ds = xr.Dataset({"foo": data, "bar": ("x", [1, 2]), "baz": np.pi})