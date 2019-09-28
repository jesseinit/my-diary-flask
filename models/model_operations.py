from app import db


class Utility:
    def save(self):
        """Function for saving new objects"""
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, **kwargs):
        """Function for updating objects"""
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self.save()

    def delete(self):
        """Function for deleting objects"""
        self.update(deleted=True)
