class event_ids:
    """
    Calse con todos los Evnt IDs
    """
    def __init__(self):
        self.kerberos_authentication_ticket_was_requested_tgt = 4768
        self.kerberos_service_ticket_was_requested_tgs = 4769
        self.kerberos_service_ticket_was_renewed = 4770
        self.an_account_was_mapped_for_logon = 4774
        self.the_domain_controller_attempted_to_validate_the_credentials_for_an_account = 4776
        self.an_account_was_successfully_logged_on = 4624
        self.an_account_failed_to_logon_on = 4625
        self.an_account_was_logged_on = 4634
        self.user_initiated_logon = 4647
        self.a_logon_was_attempted_using_explicit_credentials = 4648
        self.special_privileges_assigned_to_a_new_logon = 4672
        self.the_workstation_was_locked = 4800
        self.the_workstation_was_unlocked = 4801
        self.the_screensaver_was_invoked = 4802
        self.the_screensaver_was_dismissed = 4803
        self.process_start = 4688
        self.process_end = 4689
        self.windows_is_starting_up = 4608
        self.windows_is_shutting_down = 4609
        self.event_logging_service_has_shut_down = 1100
