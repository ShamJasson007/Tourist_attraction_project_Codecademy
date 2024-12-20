from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class FieldsRequiredForm(FlaskForm):
  class Meta:
    def render_field(self, field, render_kw):
      if field.type == "_Option":
        render_kw.setdefault("required", True)
      return super().render_field(field, render_kw)

categories = [("recommended","Recommended"), ("tovisit", "Places To Go"), ("visited", "Visited!!!")]

class AddLocationForm(FieldsRequiredForm):
  name = StringField("Location Name", validators=[DataRequired()])
  description = TextAreaField("Location Description", validators=[DataRequired()])
  category = RadioField("Category", choices=categories)
  submit = SubmitField("Add Location")