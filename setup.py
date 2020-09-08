from setuptools import setup

setup(
	name = "mat.py",
	version = "0.0.1",
	py_modules = ["mat"],
	install_requires = [
		"Click"
	],
	entry_points = """
		[console_scripts]
		mat=mat:mat
	"""
)

