class Base:
    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current url {get_url}')

    '''Method assert word'''

    def checking_word(self, checking_word, checking_result):
        value_word = checking_word.text
        assert value_word == checking_result
        print('The word is same')
