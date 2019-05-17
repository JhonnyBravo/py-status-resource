# -*- coding: utf-8 -*-
"""
終了コードとメッセージを管理する。
"""


class StatusResource(object):
    """
    終了コードとメッセージを管理する。
    """

    def __init__(self):
        self.__code = 0
        self.__message = ""

    @property
    def code(self):
        """
        :return: 終了コードを返す。
        :rtype: int
        """
        return self.__code

    @code.setter
    def code(self, code):
        """
        :param int code: 終了コードとして設定する数値を指定する。
        """
        self.__code = code

    @property
    def message(self):
        """
        :return: メッセージを返す。
        :rtype: str
        """
        return self.__message

    @message.setter
    def message(self, message):
        """
        :param str message: メッセージとして設定する文字列を指定する。
        """
        self.__message = message

    def print_message(self, code, message):
        """
        終了コードの設定とメッセージの出力を実行する。

        :param int code: 終了コードとして設定する数値を指定する。
        :param str message: メッセージとして設定する文字列を指定する。
        """
        self.code = code
        self.message = message.decode("utf_8")
        print self.message
