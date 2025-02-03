from account import Account

class AccountAngel(Account):

    USER_TYPE = "Angel"
    NOTIFICATION_PERCENT = 0.9
    LOCKED_OUT_PERCENT = 1000000000
    LOCKED_OUT_CATEGORY_NUM = 100000000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def user_type(self):
        return AccountAngel.USER_TYPE

    @property
    def notification_percent(self):
        return AccountAngel.NOTIFICATION_PERCENT

    @property
    def locked_out_percent(self):
        return AccountAngel.LOCKED_OUT_PERCENT

    @property
    def locked_out_category_num(self):
        return AccountAngel.LOCKED_OUT_CATEGORY_NUM

    def send_close_limit_message(self, selection):
        print(f"Polite reminder: You have spent more than {format(self.notification_percent, '.2%')} "
              f"of your {self._budgets.get_budget_name(selection)} budget. Keep up the good work!")

class AccountTroublemaker(Account):

    USER_TYPE = "Troublemaker"
    NOTIFICATION_PERCENT = 0.75
    LOCKED_OUT_PERCENT = 1.2
    LOCKED_OUT_CATEGORY_NUM = 100000000

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def user_type(self):
        return AccountTroublemaker.USER_TYPE

    @property
    def notification_percent(self):
        return AccountTroublemaker.NOTIFICATION_PERCENT

    @property
    def locked_out_percent(self):
        return AccountTroublemaker.LOCKED_OUT_PERCENT

    @property
    def locked_out_category_num(self):
        return AccountTroublemaker.LOCKED_OUT_CATEGORY_NUM

    def send_close_limit_message(self, selection):
        print(f"Hey, just a heads up: You've exceeded "
              f"{format(self.notification_percent, '.2%')} of your {self._budgets.get_budget_name(selection)} budget. "
              f"Please be mindful of your spending.")


class AccountRebel(Account):

    USER_TYPE = "Rebel"
    NOTIFICATION_PERCENT = 0.5
    LOCKED_OUT_PERCENT = 1.0
    LOCKED_OUT_CATEGORY_NUM = 2

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @property
    def user_type(self):
        return AccountRebel.USER_TYPE

    @property
    def notification_percent(self):
        return AccountRebel.NOTIFICATION_PERCENT

    @property
    def locked_out_percent(self):
        return AccountRebel.LOCKED_OUT_PERCENT

    @property
    def locked_out_category_num(self):
        return AccountRebel.LOCKED_OUT_CATEGORY_NUM

    def send_close_limit_message(self, selection):
        print(f"Warning: You've spent over {format(self.notification_percent, '.2%')} "
              f"of your {self._budgets.get_budget_name(selection)} budget. Please be careful with your choices.")
