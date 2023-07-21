#!/bin/bash


python -m venv venv-medprocner

PIP=venv-medprocner/bin/pip

$PIP install --upgrade pip
$PIP install -r requirements.txt