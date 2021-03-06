class Contact:
    """
    Class that generates new instances of contacts
    """
    contact_list = [] # Empty contact list
    def __init__(self,first_name,last_name,user_phone,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.user_phone = user_phone
        self.email = email



 # Init method up here

        def save_contact(self):

             '''
        save_contact method saves contact objects into contact_list
        '''
       

        Contact.contact_list.append(self)

    @classmethod
    def display_contacts(cls):
        '''
        method that returns the contact list
        '''
        return cls.contact_list

    @classmethod
    def copy_email(cls,number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
        
pass
