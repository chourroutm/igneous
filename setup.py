#!/usr/bin/env python
import setuptools

MYSQL = [ "mysql-connector-python" ]

NII = [ "nibabel" ]
NRRD = [ "pynrrd" ]
BIOIO = [ "bioio",
          "bioio-ome-zarr",
          "bioio-bioformats",
        ]

setuptools.setup(
  setup_requires=['pbr', 'numpy'],
  entry_points={
    "console_scripts": [
      "igneous=igneous_cli:main"
    ],
  },
  extras_require={
    "bioio": BIOIO,
    "mysql": MYSQL,
    "nrrd": NRRD,
    "nii": NII,
    "all": BIOIO + MYSQL + NII + NRRD,
  },
  long_description_content_type="text/markdown",
  pbr=True,
)

