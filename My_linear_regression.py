{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMAAzUCJsajFnHyhxanm3Re",
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
        "<a href=\"https://colab.research.google.com/github/OneSll/ML_Algorithms/blob/main/My_linear_regression.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 49,
      "metadata": {
        "id": "9WIwRlemniqv"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "class MyLineReg:\n",
        "  def __init__(self, n_iter=100, learning_rate=0.1, weights = pd.DataFrame()):\n",
        "    self.n_iter = n_iter\n",
        "    self.learning_rate = learning_rate\n",
        "    self.weights = weights\n",
        "\n",
        "  def __str__(self):\n",
        "    oup_string = \"MyLineReg class: \"\n",
        "    d = vars(self)\n",
        "    for key, val in d.items():\n",
        "      oup_string += str(key) + \"=\" + str(val) + \", \"\n",
        "\n",
        "    return oup_string\n"
      ]
    }
  ]
}