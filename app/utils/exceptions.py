class InvalidShopeeUrl(Exception):
    def __init__(self, message="Invalid Shopee URL"):
        self.message = message
        super().__init__(self.message)