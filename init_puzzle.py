#!/usr/bin/env python3

import argparse
import configparser
import logging
from pathlib import Path

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_input_file(url, cookie):
    response = requests.get(url, cookies={"session": cookie})
    if not response.ok:
        raise Exception(response.text)

    return response.text


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("day", type=int)
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read("config.ini")

    year = config['general']['year']
    day = args.day

    prj_path = Path()

    # Download puzzle input to ./inputs/{id}
    input_url = config['general']['input_url'].format(year=year, day=day)
    inputs_dir = prj_path/"inputs/{id:02d}".format(id=day)
    inputs_dir.mkdir(parents=True, exist_ok=True)
    input_file = inputs_dir/"input.txt"
    if input_file.exists():
        logger.info("input file '{}' already exists. Skipping...".format(input_file.as_posix()))
    else:
        logger.info("downloading input file '{}' from {}...".format(input_file.as_posix(), input_url))
        input_data = get_input_file(input_url, config['general']['session_cookie'])
        input_file.write_text(input_data)

    # Generate solution template into ./solutions/{id}.py
    solution_file = prj_path/"solutions/{id:02d}.py".format(id=day)
    solution_file.parent.mkdir(parents=True, exist_ok=True)
    solution_template = Path("_template.py").read_text()

    if solution_file.exists():
        logger.info("solution file '{}' already exists. Skipping...".format(solution_file.as_posix()))
    else:
        logger.info("creating solution file '{}'...".format(solution_file.as_posix()))
        solution_file.write_text(solution_template.format(year=int(year), day=day))
        solution_file.chmod(0o775)

    logger.info("Done!")
