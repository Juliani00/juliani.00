{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled15.ipynb",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "JuPTupxrl285"
      },
      "outputs": [],
      "source": [
        "#membuka file data.txt dengan mode append untuk menambah data\n",
        "data = open('data.txt','a')\n",
        "\n",
        "#menambah / append kalimat\n",
        "data.write(\"Yuk belajar di orbit\\n\")\n",
        "data.write(\"Jago python handling dalam sehari\\n\")\n",
        "data.write(\"Yuk rajin belajar di orbit\\n\")\n",
        "data.close() "
      ]
    }
  ]
}