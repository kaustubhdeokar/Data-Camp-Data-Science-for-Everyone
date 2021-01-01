def echo(word1):

    def inner_echo(word2):
        echo_word = word1*word2
        return echo_word

    return inner_echo

twice = echo(2)
print(twice("birthday!"))
