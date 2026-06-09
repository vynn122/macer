

class Router_db:

    def db_for_write(self, model, **hint):
        if model._meta.app_label == "lessonApp":
            return "lessonAppDB"
        elif model._meta.app_label == "keyboardApp":
            return "keyboardAppDB"
        else:
            return None


    def db_for_read(self, model, **hint):
        if model._meta.app_label == "lessonApp":
            return "lessonAppDB"
        elif model._meta.app_label == "keyboardApp":
            return "keyboardAppDB"
        else:
            return None

    def allow_migrate(self, db, app_label, model_name=None, **hint):
        if app_label == "lessonApp" and db == "lessonAppDB":
            return True
        elif app_label == "keyboardApp" and db == "keyboardAppDB":
            return True
        else:
            return False

