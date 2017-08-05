
# 03 August 2017,,,Service Fee,,2.00,
# 03 August 2017,,,Transfer Home'Bank,,49.12,
# ,,,Beneficiary: RCS RDS S.A.,,,
# ,,,To account: RO51INGB0001000000018827,,,
# ,,,Bank: INGB CENTRALA,,,
# ,,,Details: 17376172,,,
# ,,, 33992682,,,
# ,,,Reference number: 180406724,,,

import datetime


class Transaction(object):

    def __init__(self, ordinal, dat, amount, details):

        assert isinstance(dat, datetime.datetime)
        self.ordinal = ordinal
        self.date = dat
        self.amount = amount
        self.details = details

        if self.amount < 0:
            self.date = self.date + datetime.timedelta(hours=12)

    def getDate(self):
        assert isinstance(self.date, datetime.datetime)
        return self.date
    
    def getAmount(self):
        assert  isinstance(self.amount, float)
        return self.amount

    def getDetails(self):
        assert isinstance(self.details, str)
        return self.details
