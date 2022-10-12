{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPhtUTKWVMIMPLeGbvfqEFx",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/SebKrtys/solutions/blob/main/beolvasom.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K23p1W4pMHyz",
        "outputId": "0bf58ca5-f704-4199-db15-8b78f6087416"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Létem ha végleg lemerűlt\n",
            "\n"
          ]
        }
      ],
      "source": [
        "with open('source.txt') as f:\n",
        "  firstline = f.readline()\n",
        "  print(firstline)"
      ]
    }
  ]
}