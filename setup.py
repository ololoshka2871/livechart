"""
Set up the `livechart` tool.
"""

import setuptools

with open("README.rst") as file_:
	long_description = file_.read()

setuptools.setup(
	name="livechart",
	description="A CLI utility for charting data on the fly.",
	long_description=long_description,
	version="0.0.8",
	url="https://github.com/sevko/livechart",
	author="Severyn Kozak",
	author_email="severyn.kozak@gmail.com",
	entry_points={"console_scripts": ["livechart=livechart.script:run"]},
	packages=setuptools.find_packages(),
	# also works with 2.2.5 # 1.5.3
	install_requires=["matplotlib > 3.0.0"],
	license="MIT"
)
