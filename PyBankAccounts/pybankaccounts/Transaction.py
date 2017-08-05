


# 03 August 2017,,,Service Fee,,2.00,
# 03 August 2017,,,Transfer Home'Bank,,49.12,
# ,,,Beneficiary: RCS RDS S.A.,,,
# ,,,To account: RO51INGB0001000000018827,,,
# ,,,Bank: INGB CENTRALA,,,
# ,,,Details: 17376172,,,
# ,,, 33992682,,,
# ,,,Reference number: 180406724,,,

class Transaction(object):

    def __init__(self, lines):
        self.lines = lines
        
        self.date = Date()
        self.amount = 100
        
    def getDate(self):
        return self.date
    
    def getAmount(selfs):
        return self.amount
    
    @property
    def __str__(self):
        assert isinstance(self.lines, object)
        return self.lines
