#!/usr/bin/env bash
#There is an issue with nbextensions configurator
# https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator/issues/82
#manually turn on extensions that are needed after installing
#packages
jupyter nbextension enable freeze/main
jupyter nbextension enable hide_input/main
jupyter nbextension enable hide_input_all/main
jupyter nbextension enable varInspector/main
jupyter nbextension enable comment-uncomment/main
jupyter nbextension enable collapsible_headings/main
jupyter nbextension enable toc2/main
jupyter nbextension enable execute_time/ExecuteTime
jupyter nbextension enable nb_conda/main
jupyter nbextension enable spellchecker/main