{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
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
      "execution_count": 16,
      "metadata": {
        "id": "nwZWcJOL0Vhu"
      },
      "outputs": [],
      "source": [
        "class Node:\n",
        "  def __init__(self,val=None):\n",
        "    self.val = val\n",
        "    self.next = None\n",
        "\n",
        "\n",
        "class LinkedList:\n",
        "  def __init__(self):\n",
        "    self.head = None\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def push(self,val):\n",
        "  new_node = Node(val)\n",
        "  # if there is no node\n",
        "  if self.head is None:\n",
        "    self.head = new_node\n",
        "    return\n",
        "  # otherwise reach the end and then insert\n",
        "  last = self.head\n",
        "  while last.next is not None:\n",
        "    last = last.next\n",
        "  last.next = new_node\n",
        "\n",
        "LinkedList.push = push"
      ],
      "metadata": {
        "id": "iKJ3cnlF0wRW"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def __str__(self):\n",
        "  temp = self.head\n",
        "  ret_str = \"[\"\n",
        "  while temp is not None:\n",
        "    ret_str += str(temp.val) + \", \"\n",
        "    temp = temp.next\n",
        "  ret_str = ret_str.strip(\", \")\n",
        "  ret_str += \"]\"\n",
        "  return ret_str\n",
        "\n",
        "LinkedList.__str__ = __str__"
      ],
      "metadata": {
        "id": "4-KxeP311w_t"
      },
      "execution_count": 18,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l = LinkedList()\n",
        "l.push(1)\n",
        "l.push(2)\n",
        "l.push(3)\n",
        "\n",
        "print(l)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BMbeiFFQ1zLR",
        "outputId": "c3fa49ae-60c0-472d-9ea3-a82140f21815"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def pop(self):\n",
        "  if self.head is None:\n",
        "    raise Exception(\"Cannot pop no value\")\n",
        "\n",
        "  if self.head.next is None:\n",
        "    val = self.head.val\n",
        "    self.head = None\n",
        "    return val\n",
        "\n",
        "  temp = self.head\n",
        "  while temp.next is not None:\n",
        "    prev = temp\n",
        "    temp = temp.next\n",
        "\n",
        "  prev.next = None\n",
        "  val = temp.val\n",
        "  return val\n",
        "\n",
        "LinkedList.pop = pop"
      ],
      "metadata": {
        "id": "y0C3N29b5cvK"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l.pop()\n",
        "print(l)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ME5SWqhR-K59",
        "outputId": "8c760981-9e56-44f3-d2f7-7e73dbcba9aa"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def insert(self,index,val):\n",
        "\n",
        "  new_node = Node(val)\n",
        "  if index == 0:\n",
        "    new_node.next = self.head\n",
        "    self.head = new_node\n",
        "    return\n",
        "\n",
        "  temp = self.head\n",
        "  counter = 0\n",
        "  while temp is not None and counter < index:\n",
        "    prev = temp\n",
        "    temp = temp.next\n",
        "    counter += 1\n",
        "  prev.next = new_node\n",
        "  new_node.next = temp\n",
        "\n",
        "LinkedList.insert = insert\n",
        "\n"
      ],
      "metadata": {
        "id": "MjrvJ7jS-ORD"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l = LinkedList()\n",
        "l.push(1)\n",
        "l.push(2)\n",
        "l.push(3)\n",
        "print(l)\n",
        "l.insert(0,10)\n",
        "l.insert(2,10)\n",
        "print(l)"
      ],
      "metadata": {
        "id": "IalW6bbPDnXQ",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d333581e-3212-49dc-9a1a-77a4b98043fc"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3]\n",
            "[10, 1, 10, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def remove(self, val):\n",
        "  temp = self.head\n",
        "\n",
        "\n",
        "  if temp is None:\n",
        "    return\n",
        "\n",
        "  if temp.val == val:\n",
        "    self.head = temp.next\n",
        "    return\n",
        "\n",
        "  prev = temp\n",
        "  temp = temp.next\n",
        "\n",
        "  while temp is not None:\n",
        "    if temp.val == val:\n",
        "\n",
        "      prev.next = temp.next\n",
        "      return\n",
        "\n",
        "\n",
        "    prev = temp\n",
        "    temp = temp.next\n",
        "\n",
        "\n",
        "  return\n",
        "\n",
        "LinkedList.remove = remove"
      ],
      "metadata": {
        "id": "Ftp6lYw2LlF6"
      },
      "execution_count": 39,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "l = LinkedList()\n",
        "l.push(1)\n",
        "l.push(2)\n",
        "l.push(3)\n",
        "print(l)\n",
        "l.insert(0,10)\n",
        "l.insert(2,10)\n",
        "print(l)\n",
        "l.remove(10)\n",
        "l.remove(3)\n",
        "print(l)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "W8D63DpOTb2_",
        "outputId": "3bf8120c-fc38-4a92-dbd3-70677a6953b5"
      },
      "execution_count": 41,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[1, 2, 3]\n",
            "[10, 1, 10, 2, 3]\n",
            "[1, 10, 2]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "MJCiSAq9T-51"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}