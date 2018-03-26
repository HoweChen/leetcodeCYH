import string


class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..",
                      "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        alphabetical_dict = dict(zip(string.ascii_lowercase, morse_list))
        result = []
        for word in words:
            result_str = ""
            for character in word:
                result_str += alphabetical_dict.get(character)
            result.append(result_str)
        return len(set(result))
