def get_colab_metadata(file_name):
    meta_data = {
        "nbformat": 4,
        "nbformat_minor": 0,
        "metadata": {
            "colab": {
                "name": f"{file_name}",
                "provenance": [

                ],
                "collapsed_sections": [

                ]
            },
            "kernelspec": {
                "name": "python3",
                "display_name": "Python 3"
            }
        },
        "cells": [
            {
                "cell_type": "code",
                "metadata": {
                    "id": "XU0o_w7y2BQa",
                    "colab_type": "code",
                    "colab": {
                        "base_uri": "https://localhost:8080/",
                        "height": 51
                    },
                },
                "source": [
                    "print(\"hello world\")\n",
                    "print(\"made with 💖 by colab-cli\")"
                ],
                "execution_count": 1,
                "outputs": [
                ]
            }
        ]
    }
    return meta_data
