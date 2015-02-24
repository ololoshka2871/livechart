"""
Contains functions for parsing command-line arguments and initializing the
tool. Intended to serve as the command-line entry point.
"""

import argparse
import sys

from livechart import chart

def parse_args():
	"""
	Parse command-line arguments with `argparse`, and return the resulting
	dictionary.
	"""

	description = (
		"Plot a graph of STDIN data, live. Pipe in either rows of "
		"JSON-serialized dictionaries/objects or numbers. If objects are "
		"received, each top-level key is expected to be mapped to a number."
	)
	parser = argparse.ArgumentParser(description=description)
	parser.add_argument(
		"-s", "--subplots", default=False, const=True, nargs="?", type=str,
		help=(
			"Whether to plot each data point on a separate graph. "
			"`livechart` will intelligently format the subplots, but you can "
			"specify custom dimensions in the form of a 'XxY' string (eg '5x6')."
		)
	)
	parser.add_argument(
		"-n", "--normalize", action="store_true",
		help=(
			"Whether data points should be normalized. May be desirable when "
			"points with vastly different ranges are getting plotted on the "
			"same graph."
		)
	)

	args = vars(parser.parse_args())
	if not args["subplots"]:
		args["subplots"] = {
			"show": False
		}
	elif isinstance(args["subplots"], str):
		hor, ver = args["subplots"].split("x")
		args["subplots"] = {
			"show": True,
			"horizontal": int(hor),
			"vertical": int(ver)
		}
	else:
		args["subplots"] = {
			"show": True
		}

	return args

def run():
	"""
	Runs the tool.
	"""

	chart.configure_pyplot()
	try:
		sys.exit(chart.render_stdin(parse_args()))
	except KeyboardInterrupt:
		pass
