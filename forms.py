from wtforms import SubmitField, FileField


class FileForm():
    
    file = FileField(
        "PDF File"
        )